# Khartoum - Claude Code 项目说明

## 项目定位

这是一个 **Claude Agent SDK 扩展包**，提供自定义命令和技能集合。

## 你需要知道的事

### 项目结构

- **`commands/`** —— 斜杠命令定义
- **`skills/`** —— 技能包，每个技能都是可独立调用的知识模块
- **`.context/`** —— 运行时上下文存储（笔记、待办、计划）

### 可用命令

| 命令 | 何时使用 |
|------|----------|
| `/product-philosophy` | 用户讨论产品定位、设计哲学、"为什么做什么" |
| `/pr` | 用户需要创建 PR |

### 可用技能

| 技能 | 触发条件 |
|------|----------|
| `agent-builder` | 用户请求"创建 agent"、"构建助手"、"设计 AI 系统" |
| `creating-images` | 用户请求图像生成、视觉创作 |
| `media-writer` | 用户需要适配内容到特定平台（微信、Hacker News、LinkedIn 等） |
| `prompt-engineering-patterns` | 用户需要设计或优化复杂 prompt |
| `prompt-optimization` | 用户需要优化系统提示 |
| `skill-judge` | 用户需要审查或评审技能设计 |
| `talent-discovery` | 用户询问天赋、职业方向、优势探索 |
| `vibe-coding` | 用户进行开发任务（feature、bugfix、refactor） |

## 工作指南

### 添加新技能

1. 在 `skills/` 下创建新目录
2. 创建 `SKILL.md` 文件，遵循格式：

```markdown
---
name: skill-name
description: Use when...（清晰描述何时触发）
---

# 技能名称

## 核心功能
...
```

3. 可选：添加 `references/`、`scripts/`、`assets/` 子目录

### 添加新命令

1. 在 `commands/` 下创建 `command-name.md`
2. 遵循格式：

```markdown
---
description: 命令的简短描述
---

命令的完整提示内容...
```

## 项目约定

- **中文优先** —— 文档使用简体中文
- **意图驱动** —— 技能和命令都应明确"何时使用"
- **最小闭环** —— 每个技能都应能独立完成一个完整任务
- **显式文档** —— 重要决策应记录在文档中

## 常见场景

### 用户问"这个项目是做什么的？"

> 这是一个 Claude Code 扩展包，提供自定义命令和技能，用于产品探索、代码协作、内容创作等任务。

### 用户想添加新功能

先使用 `/product-philosophy` 探讨意图，再使用 `vibe-coding` 技能实现。

### 用户想创建 PR

直接使用 `/pr` 命令。
