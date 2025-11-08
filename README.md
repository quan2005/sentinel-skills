# Slidev Skills Marketplace

<div align="center">

![Slidev Skills Marketplace](https://img.shields.io/badge/Slidev-Skills%20Marketplace-blue?style=for-the-badge&logo=vue)
![Claude Code](https://img.shields.io/badge/Claude%20Code-Compatible-success?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)
![Skills](https://img.shields.io/badge/Skills-1+-important?style=for-the-badge&color=blue)

**🎨 发现、分享、创建令人惊叹的演示文稿技能**

[🌟 探索市场](./marketplace/) • [🚀 快速开始](#-快速开始) • [📦 安装技能](#-安装技能) • [🤝 贡献技能](./marketplace/docs/CONTRIBUTING.md)

</div>

## ✨ 什么是 Slidev Skills Marketplace？

**Slidev Skills Marketplace** 是一个为 Claude Code 用户打造的专业演示文稿技能平台，提供高质量、图文并茂、视觉震撼的演示文稿创建技能。

### 🌟 核心特色

- 🎨 **图文并茂标准** - 每页都包含丰富图表、专业图标、渐变色彩
- ⚡ **极致丰富内容** - 200-500字详细信息，深度分析和实用建议
- 🚀 **商业级视觉** - 企业级视觉效果，现代化卡片式布局
- 🎯 **智能交互** - 渐进展示、悬浮动画、点击交互
- 📊 **数据可视化** - 进度条、图表、流程图、统计信息

### 🏆 精选技能

<div align="center">

| 技能名称 | 分类 | 状态 | 特色 |
|---------|------|------|------|
| [Slidev Presentation Creator](./marketplace/skills/slidev-presentation-creator/) | 演示文稿工具 | ✅ 精选 | 图文并茂、视觉震撼、商业级 |

</div>

## 🚀 快速开始

### 📦 安装技能

```bash
# 使用我们的安装脚本
./scripts/install-skill.sh slidev-presentation-creator

# 或查看所有可用技能
./scripts/install-skill.sh --list

# 检查技能是否已安装
./scripts/install-skill.sh --check slidev-presentation-creator
```

### 🎯 使用技能

安装完成后，在 Claude Code 中直接使用：

```bash
# 创建图文并茂的演示文稿
"帮我创建一个关于人工智能的演示文稿，要求图文并茂、视觉震撼"

# 商务级演示文稿
"我需要制作商业级的财务分析PPT，包含详细图表和数据"

# 技术演示文稿
"创建一个关于React性能优化的技术分享，需要代码示例和架构图"

# 教程演示文稿
"制作一个Vue.js入门教程，包含循序渐进的内容和练习"
```

### 🌟 立即体验

访问我们的技能市场了解更多：[🌟 Slidev Skills Marketplace](./marketplace/)

## 📁 技能结构

```
slidev-presentation-skill/
├── SKILL.md                    # 主要技能文档
├── README.md                   # 本文件
├── package.json                # 项目元数据
├── install.sh                  # 安装脚本
├── examples/                   # 演示文稿示例
│   ├── basic-presentation.md   # 简单演示文稿示例
│   └── tech-talk.md           # 技术演示示例
└── templates/                  # 模板文件
    ├── business-presentation.md # 业务演示模板
    └── tutorial.md             # 教程模板
```

## 🎨 功能特性

### 核心能力
- 📝 **基于Markdown**：使用熟悉的markdown语法编写演示文稿
- 🎨 **专业主题**：多种内置主题（seriph、default、apple-basic等）
- 📱 **响应式设计**：适用于所有屏幕尺寸的演示文稿
- ⚡ **交互元素**：代码高亮、点击交互、动画
- 🎯 **布局系统**：预构建布局（two-cols、center、image、section）
- 🔧 **开发者工具**：代码片段、实时演示、技术内容支持

### 高级功能
- 📊 **丰富组件**：图表（Mermaid、PlantUML）、图表、图标
- 🎪 **演示模式**：演讲者备注、绘图工具、远程控制
- 🔄 **幻灯片过渡**：平滑的幻灯片间动画
- 📤 **导出选项**：PDF、PPTX、PNG和静态站点导出
- 🎯 **点击交互**：Vue.js交互元素
- 📋 **演讲者备注**：演讲者私人备注

## 🎯 可用主题

- **seriph** - 专业衬线字体，适用于商务/技术演示
- **default** - 简洁极简，适用于通用场景
- **apple-basic** - Apple风格设计，适用于产品演示
- **dev** - 面向开发者，具有终端美学
- **shades-of-purple** - 紫色调深色主题
- **bricks** - 创意乐高积木主题，适用于创意内容
- **minami** - 清爽明快的设计
- **meetup** - 社区导向主题

## 📚 文档

- **[SKILL.md](SKILL.md)** - 包含快速开始指南的主要技能文档
- **[examples/](examples/)** - 完整演示文稿示例
- **[templates/](templates/)** - 即用型演示文稿模板

## 🔧 要求

- Node.js 16+（用于本地Slidev开发）
- 可选：全局安装Slidev（`npm i -g @slidev/cli`）

## 💡 获得最佳效果的技巧

### 技术演示
- 使用**seriph**主题获得专业外观
- 为代码片段启用行号
- 使用`highlighter: "shiki"`进行语法高亮
- 包含带有`v-click`的渐进式展示

### 业务演示
- 使用**apple-basic**主题获得简洁设计
- 包含图表和指标可视化
- 添加专业背景
- 用清晰的部分和要点构建结构

### 教程
- 使用**default**主题保持简单
- 包含分步说明
- 添加带有解释的代码示例
- 使用渐进式展示促进更好的学习

## 🎪 示例演示文稿类型

### 技术演讲
```markdown
---
title: "高级React模式"
theme: "seriph"
highlighter: "shiki"
lineNumbers: true
---

# 代码示例内容
```

### 业务演示
```markdown
---
title: "Q4结果"
theme: "apple-basic"
layout: "cover"
background: "https://source.unsplash.com/..."
---

# 业务指标和图表
```

### 教程
```markdown
---
title: "Vue入门"
theme: "default"
highlighter: "shiki"
---

# 分步学习内容
```

## 🚀 安装方法

### 方法1：克隆仓库
```bash
git clone https://github.com/your-username/slidev-presentation-skill.git
cd slidev-presentation-skill
./install.sh
```

### 方法2：手动安装
```bash
# 将整个技能复制到你的Claude技能目录
cp -r . ~/.claude/skills/slidev-presentation-creator/
```

### 方法3：使用安装脚本
```bash
chmod +x install.sh
./install.sh
```

## 📖 高级使用

对于自定义Vue组件、高级布局和复杂集成，请查看[高级功能文档](SKILL.md#高级使用)。

## 🤝 贡献

这个技能遵循[Claude Code技能](https://docs.claude.com)开发指南。

## 📄 许可证

此技能按原样提供，供教育和专业使用。

---

**准备好创建精彩的演示文稿了吗？直接要求Claude帮你制作幻灯片！** 🎉

## 🌟 中英文触发词

### 英文触发词
- "create presentation"
- "make slides"
- "PowerPoint alternative"
- "technical presentation"
- "developer slides"

### 中文触发词
- "创建演示文稿"
- "制作幻灯片"
- "PPT制作"
- "技术演讲"
- "业务演示"
- "教程幻灯片"
- "帮我做个演讲"
- "我要做汇报"
- **"要图文并茂的PPT"**
- **"需要视觉震撼的演示"**
- **"制作商业级演示文稿"**
- **"需要内容丰富的幻灯片"**

### 🎨 **特色功能 - 图文并茂标准**

**每页演示文稿都包含：**
- 🎯 **丰富视觉元素** - 专业图标、渐变色彩、卡片布局
- 📊 **数据可视化** - 进度条、图表、流程图、统计信息
- ⚡ **交互效果** - 渐进展示、悬浮动画、点击交互
- 💡 **充实内容** - 详细信息、案例分析、实用建议
- 🚀 **商业级标准** - 专业设计、企业级视觉效果

**质量保证：**
- ❌ 禁止纯文字页面
- ❌ 禁止内容简单空洞
- ✅ 每页必含丰富视觉元素
- ✅ 每页内容必须充实详细
- ✅ 必须达到商业级视觉效果

现在您可以用中文或英文激活这个技能！