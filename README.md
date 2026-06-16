# Sentinel

> 三个协同的 Claude Code 技能,在 AI 辅助开发的入口、出口、收尾各设一道哨卡:需求不再凭感觉开工,实现不再自说自话验收,文档不再事后失修。Sentinel——始终在岗的开发哨兵。

一套面向 AI 辅助开发的纪律框架。每道门禁是一个独立的 Claude Code skill,由一个零逻辑的 hook 在关键节点轻量提醒,真正的判断与执行全部由技能内的 prompt 驱动。三者串联成闭环,却互不耦合——单独安装任意一个都能工作,跳过任意一个不影响其余。

## 为什么需要它

AI 写代码很快,但快的代价常常是:需求一句"优化一下体验"就开工,做完才发现各方理解不同;实现者核对自己的代码,结论永远是"都做完了";代码改了文档没改,文档从资产变成误导源。这三个问题分别发生在开发的入口、出口和收尾,这套框架就在这三处各设一道门。

## 三道门禁

| 技能 | 触发时机 | 解决的问题 | 产物 |
|---|---|---|---|
| **requirements-gate**(需求门禁) | 提出新需求时 | 想清楚再做:消除模糊、定清用户意图 | `story.md` |
| **verification-gate**(验收门禁) | git commit 前 | 做得对:独立核对实现与需求是否相符 | `verify-report.md` |
| **docs-maintenance**(文档维护) | git commit 前 | 知识不丢失:同步七类项目文档 | 各类文档更新 |

### requirements-gate — 需求门禁

把模糊的开发需求变成一份无歧义、**纯用户视角**的 `story.md`(只讲"要什么",不碰"怎么做"),作为后续开发与验收的意图契约。实现方案由下游 brainstorming 产出 `design.md` 承接。

- **分级处理**:从琐碎修复(L1)到触碰数据契约/权限/计费的高风险变更(L3),按风险决定评审强度,不让简单需求陷入繁文缛节
- **模糊性清除**:扫描"体验好一点""支持更多场景"这类表达,逐条给出可直接替换进 story 的改写
- **缺口扫描**:NFR(回滚、降级、隐私、可观测性等最易漏项)+ 依赖与影响面分析
- **两层分工**:story.md 管"要什么"(背景/AC/非目标),实现层问题(NFR、回滚、依赖、架构)打包成交棒清单移交 design.md,各司其职
- **方案级未知交棒**:当需求方向本身不明确时,移交 superpowers 的 brainstorming 梳理,并把已收集的证据与交棒清单一并带过去
- **可机械核对的契约**:验收标准写成用户可观察行为、编号稳定、非目标明确,为下游验收提供基准

### verification-gate — 验收门禁

commit 前 spawn 一个**独立的** subAgent,在干净上下文中核对实现与双层契约(story.md 意图 + design.md 方案)的符合度。独立性是关键——实现者核对自己的代码会无意识地按写代码时的理解去解读需求,盲点随实现一起继承。

按六字标准逐项核对,每条结论必须附 `文件:行` 证据:

- **不漏**:每条验收标准都有对应实现(对 story)
- **不重**:没有重复实现同一标准的冗余(对 story)
- **不偏**:实现行为符合 AC,且方案落实 design(对 story+design)
- **不倚**:不偏向某些标准而敷衍其他(对 story)
- **不多**:没有超出非目标/方案范围的额外实现(对 story+design)
- **不少**:范围内功能完整覆盖(对 story)

全部通过才将 story 翻为 `verified`;存在偏差则留存报告、不翻状态,支持"修复 → 再验 → 新报告"的多轮验收。

### docs-maintenance — 文档维护

commit 前判断本次已验收的变更是否影响项目知识,按需同步七类文档。判断与跳过同样重要——目标是文档与代码一致,而非每次都改文档。

七类文档分读者维护:

- **仓库内工作上下文**(供在本仓库开发的 Agent):`AGENTS.md`(项目约定主源,语义化版本 + 同步影响报告)、`ARCH.md`(固定八章节架构文档)、`DESIGN.md`(交由 impeccable 维护)
- **对外文档**(读者可能是人,也可能是 Agent):`README.md`(门面)、`llms.txt`(遵循 [llmstxt.org](https://llmstxt.org/) 规范的机读导航)、用户使用说明、技术开发说明

`AGENTS.md` 的约定采用 MUST / SHOULD / MAY 三级措辞、清除不可检验的模糊词,确保约定真正能约束 Agent。

## 工作流

```
用户提出需求
  │
  ▼  requirements-gate ───────▶ story.md (用户意图,status: approved)
  │        │
  │        └──(方案级未知/需细化)──▶ brainstorming ──▶ design.md (实现方案)
  │
  ▼  开发  ──▶  writing-plans 或 spec-kit /plan (计划首行引用 story + design)
  │
  ▼  git commit
  ├─ verification-gate ──▶ 独立 subAgent
  │     │   核对实现 vs story(要什么) + design(怎么做)
  │     ▼ 通过                          ▼ 偏差
  │  story → verified              留存报告,修复后重验
  │
  └─ docs-maintenance ──▶ AGENTS.md / ARCH.md / DESIGN.md / README / llms.txt / 使用·开发说明
  │
  ▼
commit 完成
```

三道门各管一段,顺序由技能逻辑天然保证:验收门禁要求 story 已 approved,文档维护要求 story 已 verified,因此同一次 commit 中"先验收、后文档"自动成立,无需额外编排。

## 设计原则

- **hook 零逻辑,判断在 prompt**:hook 只做静态注入提醒,所有"是否触发、走哪条路径、是否跳过"的判断都在技能的 prompt 里由模型完成。逻辑迭代不必改 hook
- **提醒不阻断**:hook 永不拦截操作,最终决定权始终在用户手上。任意一道门都可用 `[skip-gate]` / `[跳过门禁]` 单条跳过
- **技能独立,串联不耦合**:三者各有独立的 hook 与 skill,通过 `story.md` 的状态字段(approved → verified)隐式衔接,而非直接调用彼此
- **意图与实现分层**:`story.md` 只承载用户视角的"要什么",`design.md` 承载"怎么做"。用户拍板意图,AI 落地方案,验收时两层各有基准——职责不混
- **尽量复用现有体系**:发散梳理交给 superpowers/brainstorming,开发计划交给 writing-plans 或 spec-kit,视觉设计交给 impeccable,机读导航遵循 llms.txt 规范——门禁只做编排与把关,不重造轮子

## 安装

每个技能目录放到 `~/.claude/skills/`(个人级)或项目 `.claude/skills/`(项目级):

```
~/.claude/skills/
├── requirements-gate/
├── verification-gate/
└── docs-maintenance/
```

将三个 hook 合并进 `settings.json`(个人级 `~/.claude/settings.json` 或项目级 `.claude/settings.json`)。三者并存时,两个 PreToolUse 条目同列于数组中:

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

使用 docs-maintenance 技能时,需在仓库根目录建立软链(AGENTS.md 为文档唯一主源):

```bash
# 仓库根目录执行
ln -sf AGENTS.md CLAUDE.md
```

已有实体 CLAUDE.md 的仓库:先把内容并入 AGENTS.md,再删实体文件、建软链。

可按需只装其中一道或两道门——技能彼此独立,删去对应目录与 hook 条目即可。完整安装说明见仓库根目录 `INSTALL.md`。

## 依赖与复用

- **[superpowers](https://github.com/obra/superpowers)**:brainstorming(需求发散)、writing-plans(开发计划)
- **spec-kit**:`/plan`、`/clarify` 等命令(可选,与 superpowers 二选一或并用)
- **impeccable**:DESIGN.md 的生成与维护
- **[llms.txt 规范](https://llmstxt.org/)**:对外机读导航文件格式

以上为软依赖:未安装时对应环节自然降级(如无 brainstorming,需求门禁自行处理参数级澄清),不影响门禁主干运行。

## 兼容性说明

hook 依赖 Claude Code 的 `UserPromptSubmit` 与 `PreToolUse` 事件及 `additionalContext` 注入机制。个别版本曾出现 Bash matcher 的 PreToolUse 注入通道失效的情况;若提醒不生效,各技能 description 中的触发条件仍可独立触发,亦可将约定写入 `AGENTS.md` 兜底。

## License

MIT
