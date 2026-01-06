# Khartoum

Claude Agent SDK 的技能和命令集合 —— 让 AI 更懂你的意图。

## 概述

此项目提供了一套可复用的技能（Skills）和自定义命令（Commands），扩展 Claude Code 的能力，使其能更好地处理产品探索、代码协作、内容创作等任务。

## 结构

```
khartoum/
├── commands/           # 自定义斜杠命令
│   ├── product-philosophy.md
│   └── pr.md
├── skills/             # 技能包
│   ├── agent-builder/
│   ├── creating-images/
│   ├── media-writer/
│   ├── prompt-engineering-patterns/
│   ├── prompt-optimization/
│   ├── skill-judge/
│   ├── talent-discovery/
│   └── vibe-coding/
└── .context/           # 上下文存储
```

## 命令 (Commands)

| 命令 | 用途 |
|------|------|
| `/product-philosophy` | 产品设计哲学探索 —— 讨论产品定位、设计理念、战略方向 |
| `/pr` | 标准化 PR 创建流程 —— Sync → Clean → Verify → Docs → Diff → Push |

## 技能 (Skills)

| 技能 | 描述 |
|------|------|
| **agent-builder** | 为任何领域设计和构建 AI 代理 |
| **creating-images** | 图像生成与视觉创作 |
| **media-writer** | 平台原生内容创作（微信、Hacker News、Reddit 等） |
| **prompt-engineering-patterns** | 高级提示工程模式与优化 |
| **prompt-optimization** | 系统提示优化 |
| **skill-judge** | 技能设计质量评审 |
| **talent-discovery** | 天赋发现与职业探索 |
| **vibe-coding** | 人机协作编程 —— 有品味的代码伙伴 |

## 安装

将此项目放入你的 Claude Code 工作区，或复制相关文件到你的 `.claude/` 目录：

```bash
# 复制命令
cp commands/*.md ~/.claude/commands/

# 复制技能
cp -r skills/* ~/.claude/skills/
```

## 使用

### 命令使用

在 Claude Code 中直接输入：

```
/product-philosophy
```

```
/pr
```

### 技能使用

技能会根据上下文自动触发，例如：

- "帮我设计一个客服 agent" → 触发 `agent-builder`
- "把这篇文章改写成公众号风格" → 触发 `media-writer`
- "优化这个 prompt" → 触发 `prompt-optimization`
- "我的天赋是什么？" → 触发 `talent-discovery`

## 理念

**意图即产品** —— 核心价值在于理解用户意图，而非功能堆砌。

每个技能和命令都遵循以下原则：

- **80/20 法则** —— 区分核心意图与边缘实现
- **最小可行闭环** —— 完整的"意图→行动→反馈"循环
- **增量式演进** —— 每次只解决一个核心问题
- **知识显式化** —— 将隐性决策转化为文档

## 贡献

欢迎提交 Issue 和 Pull Request。

## 许可

MIT
