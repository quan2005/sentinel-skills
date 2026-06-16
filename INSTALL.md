# 安装说明

> 本文件面向人类读者，不属于技能上下文（Claude 触发技能时只加载 SKILL.md 及其引用的 references/assets）。

## 设计原则

三道门禁共享同一套 hook 哲学：

- **hook 零逻辑，判断在 prompt**：所有"是否触发、该走哪条路径、是否跳过"的决策全在 SKILL.md 内由模型执行。hook 不含判断代码，逻辑迭代不必改 hook。
- **提醒不阻断**：hook 永远 exit 0（`|| true`），最终决定权在用户手上。`[skip-gate]` / `[跳过门禁]` 可跳过任何一道门。
- **注入文本是陈述句**：命令式越权指令可能触发 Claude 提示注入防御，因此统一写成"本项目约定：……"的事实陈述。

### 两种 hook 事件的差异

| 事件 | 用于 | stdout 行为 | 注入方式 |
|---|---|---|---|
| **UserPromptSubmit** | requirements-gate | 纯文本直接进入模型上下文 | `echo '…'` |
| **PreToolUse** | verification-gate、docs-maintenance | 纯 stdout 只进 debug log，不进模型上下文 | 必须输出 `hookSpecificOutput.additionalContext` 的 JSON |

PreToolUse 的 matcher 只能按工具名匹配（这里是 `Bash`），不能按命令内容过滤。多了一行 `grep -q 'git commit'` 做路由——避免对每条 shell 命令都注入提醒。这是路由不是判断。

## 安装步骤

### 1. 放置技能目录

个人级（所有项目生效）：

```
~/.claude/skills/
├── requirements-gate/
├── verification-gate/
└── docs-maintenance/
```

项目级（仅当前仓库生效）：

```
.claude/skills/
├── requirements-gate/
├── verification-gate/
└── docs-maintenance/
```

可按需只装其中一道或两道——技能彼此独立。

### 2. 合并 hook 到 settings.json

将以下内容合并进 `~/.claude/settings.json`（个人级）或 `.claude/settings.json`（项目级）：

```json
{
  "hooks": {
    "UserPromptSubmit": [
      {
        "hooks": [
          {
            "type": "command",
            "command": "echo '[需求门禁] 本项目约定：新的开发需求在进入编码前，须先经 requirements-gate 技能完成梳理，产出 story.md 并由用户确认为 status: approved。非开发消息、已批准任务的延续、或标注 [skip-gate] 的消息不受此约定影响。'"
          }
        ]
      }
    ],
    "PreToolUse": [
      {
        "matcher": "Bash",
        "hooks": [
          {
            "type": "command",
            "command": "grep -q 'git commit' && echo '{\"hookSpecificOutput\":{\"hookEventName\":\"PreToolUse\",\"additionalContext\":\"[验收门禁] 本项目约定：git commit 前，若存在与本次改动相关、status: approved 但尚未 verified 的 story.md，须先经 verification-gate 技能由独立 subAgent 完成验收并产出 verify-report.md，全部通过后将 story 翻为 verified。无相关 story、已验收、或用户标注 [skip-gate] 时不受此约定影响。\"}}' || true"
          }
        ]
      },
      {
        "matcher": "Bash",
        "hooks": [
          {
            "type": "command",
            "command": "grep -q 'git commit' && echo '{\"hookSpecificOutput\":{\"hookEventName\":\"PreToolUse\",\"additionalContext\":\"[文档维护] 本项目约定：git commit 前，若本次改动对应的 story 已 verified 且影响面涉及架构/设计/约定或用户可感知变化，须经 docs-maintenance 技能同步更新 AGENTS.md / ARCH.md / DESIGN.md，并按需维护 README、llms.txt 与使用、开发说明文档。无相关 story、文档已覆盖变更、或用户标注 [skip-gate] 时不受此约定影响。\"}}' || true"
          }
        ]
      }
    ]
  }
}
```

只装部分门禁时，删去对应条目即可。

### 3. 软链初始化（docs-maintenance 需要）

docs-maintenance 以 AGENTS.md 为唯一主源，CLAUDE.md 应为指向它的软链：

```bash
# 仓库根目录执行
ln -sf AGENTS.md CLAUDE.md
```

**已有实体 CLAUDE.md 的仓库**：先把内容并入 AGENTS.md，再删实体文件、建软链。此操作需人工执行——技能不会自动删除或转换已有文件。

不使用 docs-maintenance 时可跳过此步。

### 4. 验证

| 门禁 | 验证方法 |
|---|---|
| requirements-gate | 发一条含"新增/实现/开发"的消息 → Claude 应主动进入门禁流程；发纯提问 → 正常回答不受打扰 |
| verification-gate | 让 Claude 执行 `git commit` → 应可见放行判断；执行 `ls` 等普通命令 → 无注入 |
| docs-maintenance | 带 verified story 的 `git commit` → 触发五问判断；无相关 story → 静默放行 |

## 上下文成本

- requirements-gate：每条消息注入约 70 字（UserPromptSubmit 会留在会话历史累积）
- verification-gate / docs-maintenance：仅命令含 `git commit` 时各注入约 100 字，普通命令零注入

## 已知问题与兜底

- **PreToolUse 注入通道失效**：个别 Claude Code 版本曾报告 Bash matcher 的 PreToolUse 注入不生效（如 GitHub issue #55889）。兜底方案：各技能 description 中的触发条件仍可独立触发技能；亦可将约定写入 AGENTS.md。
- **grep 模式覆盖不全**：`grep -q 'git commit'` 不匹配 `git -C <dir> commit`、`git cz`、`npm run commit` 等变体。如需覆盖，可放宽为 `grep -qE 'git.*(commit|cz)'` 或按项目实际调整。
- **UserPromptSubmit 阻塞**：该事件会阻塞模型处理直至 hook 完成（默认超时 30s）。静态 echo 几乎零延迟，但若改为脚本需注意耗时。

## 跳过约定

单条消息或命令带 `[skip-gate]` / `[跳过门禁]` 即跳过对应门禁。该约定由注入文本与 SKILL.md 的 L0/放行规则共同保障——纯 prompt 实现，无脚本参与。

## 备选方案

- **最简方案（不装 hook）**：把注入文本写进 CLAUDE.md / AGENTS.md。代价是长会话中规则可能被压缩稀释。两者可并存。
- **硬门禁（按需升级）**：软门禁跑顺后若仍有"偷跑"，可增加 PreToolUse hook 在 Edit/Write 调用前检查是否存在 approved story（requirements-gate），或输出 `permissionDecision: "deny"` 阻断未验收的 commit（verification-gate）。硬门禁需要真正的判断逻辑，与"零逻辑"原则冲突，建议确有需要再做。
