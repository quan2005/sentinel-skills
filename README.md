# My Claude Code 技能集

> **个人技能，持续积累** — 一个精心策划的 Claude Code 技能集合，助你构建 AI 辅助的编程工作流。

---

## 概述

My Claude Code 是为 Claude Code CLI 设计的技能（Skills）和命令（Commands）集合。每个技能都是一个独立的工具集，可根据任务需求灵活调用。

### 核心理念

**人类提供愿景，AI 提供执行。**

- **品味 + 纪律 + 透明** = 专业开发伙伴
- 技能永不手过期，只需正确激活
- 显式知识 > 隐性决策

---

## 技能包一览

### 本地技能

| 技能 | 描述 | 适用场景 |
|------|------|----------|
| **talent-discovery** | 才能发现 — 结合盖洛普优势理论、心流理论和荣格心理学的苏格拉底式指导 | 职业规划、自我发现、优势探索、潜在能力挖掘 |
| **prompt-engineering-patterns** | 提示工程模式 — 提示工程最佳实践和模式库 | 学习提示工程技巧、创建提示模板 |
| **prompt-optimization** | 提示优化 — 优化和改进系统提示词 | 改进现有提示词效果、提示词诊断 |
| **creating-images** | 图像生成 — 创建和生成图像内容 | 视觉内容创作、图像生成 |

### 更多技能

专业开发、代理工作流等更多技能请从以下仓库获取：

| 仓库 | 描述 |
|------|------|
| **[shareAI-skills](https://github.com/shareAI-lab/shareAI-skills)** | 开发、内容创作等专业技能 |
| **[superpowers](https://github.com/obra/superpowers)** | Agent 开发工作流技能集 |

```bash
# 克隆 shareAI-skills
git clone https://github.com/shareAI-lab/shareAI-skills.git

# 克隆 superpowers
git clone https://github.com/obra/superpowers.git
```

---

## 自定义命令

| 命令 | 描述 |
|------|------|
| **/product-philosophy** | 产品设计哲学探索 — 通过讨论探索产品定位、设计哲学和战略方向 |
| **/pr** | PR 相关命令 — 创建和管理 Pull Request |

---

## For LLM Agents: 安装指南

如果你是一个 AI 代理，正在帮助用户设置 Rome，欢迎！以下是完整的安装流程。

### Step 0: 确认环境

```bash
# 检查 Claude Code 是否已安装
if command -v claude &> /dev/null; then
    echo "Claude Code $(claude --version) is installed"
else
    echo "Claude Code is not installed. Please install it first."
    echo "Ref: https://claude.ai/claude-code"
fi
```

### Step 1: 克隆仓库

```bash
# 克隆到本地
git clone git@github.com:quan2005/my_claude_code.git ~/my_claude_code

# 复制技能到 Claude Code 技能目录
cp -r ~/my_claude_code/skills/* ~/.claude/skills/

# 复制命令到 Claude Code 命令目录
cp -r ~/my_claude_code/commands/* ~/.claude/commands/
```

### Step 2: 验证安装

```bash
# 检查技能包
ls ~/.claude/skills/
# 应看到: creating-images, prompt-engineering-patterns, prompt-optimization, talent-discovery

# 检查命令
ls ~/.claude/commands/
# 应看到: product-philosophy.md, pr.md
```

### Step 3: 安装更多技能（可选）

从以下仓库获取更多专业技能：

**shareAI-skills** — 开发、内容创作等专业技能：
```bash
git clone https://github.com/shareAI-lab/shareAI-skills.git
cp -r shareAI-skills/skills/<skill-name> ~/.claude/skills/
```

**superpowers** — Agent 开发工作流技能集：
```bash
git clone https://github.com/obra/superpowers.git
cp -r superpowers/skills/<skill-name> ~/.claude/skills/
```

### Step 4: 激活技能

在 Claude Code 中，技能会自动加载。使用时调用：

```
@talent-discovery 帮我探索我的潜在才能
@prompt-optimization 优化这个系统提示词
```

或使用命令：

```
/product-philosophy 让我们讨论这个产品的设计哲学
```

### Step 5: 验证技能可用性

在 Claude Code 中输入：

```
列出所有可用的 Rome 技能
```

你应该看到所有技能及其描述的列表。

---

## 技能深度解析

### talent-discovery — 才能发现

结合盖洛普优势理论、心流理论和荣格心理学的苏格拉底式指导过程。

**核心理念**：
- 天赋永不手过期，我们只是要找到它
- 真正的天赋让你回血，而不是你单纯擅长但做完很累的事
- 你的缺点、怪癖、甚至嫉妒，往往是天赋被压抑的背面

**流程**：通过 4-10 个深度问题，挖掘用户的底层天赋，最终生成万字《个人天赋使用说明书》。

### prompt-engineering-patterns — 提示工程模式

包含：
- 提示模板库
- 少样本学习技术
- 链式思考（Chain-of-Thought）
- 系统提示设计
- 提示优化技巧

---

## 项目结构

```
my_claude_code/
├── skills/                        # 技能包（复制到 ~/.claude/skills/）
│   ├── talent-discovery/         # 才能发现
│   ├── prompt-engineering-patterns/  # 提示工程模式
│   ├── prompt-optimization/      # 提示优化
│   └── creating-images/          # 图像生成
├── commands/                      # 自定义命令（复制到 ~/.claude/commands/）
│   ├── product-philosophy.md     # 产品哲学探索
│   └── pr.md                    # PR 命令
├── .context/                      # 上下文文件（gitignored）
│   ├── todos.md
│   └── notes.md
├── CLAUDE.md                      # 项目级指导
└── README.md                      # 本文件
```

---

## 技能开发规范

每个技能都是一个独立的工具集，遵循以下结构：

```
skill-name/
├── SKILL.md              # 技能核心定义（必需）
├── references/           # 深度专业知识（可选）
│   ├── domains/          # 领域知识
│   ├── patterns/         # 可复用模式
│   ├── scenarios/        # 场景工作流
│   └── phases/          # 阶段流程
└── assets/              # 资源文件（可选）
    └── templates/       # 模板文件
```

### SKILL.md 必需格式

```yaml
---
name: skill-name
description: 简洁描述技能的用途和触发时机
---

# Skill Name

技能的核心内容...
```

---

## 贡献

欢迎贡献！以下是贡献方式：

1. **新增技能** — 遵循技能开发规范创建新技能
2. **改进现有技能** — 优化技能内容和参考资料
3. **修复问题** — 提交 Issue 或 PR

---

## 许可

MIT License

---

## 致谢

本项目的设计深受以下项目启发：

- **[oh-my-opencode](https://github.com/code-yeongyu/oh-my-opencode)** — 技能结构和工作流设计
- **[Claude Code](https://claude.ai/claude-code)** — Claude Code CLI 技能系统
- **[AmpCode](https://github.com/androlol/ampcode)** — 代理编排理念

---

**仓库**: git@github.com:quan2005/my_claude_code.git

> **非一日之功，持续积累。**
