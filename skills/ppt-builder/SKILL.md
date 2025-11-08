---
name: ppt-builder
description: This skill should be used when the user needs to create professional, visually rich presentations using Slidev. It specializes in generating comprehensive slide decks with data visualizations, professional layouts, and compelling content structure.
version: 1.0.0
author: quan2005
capabilities:
  - "Create professional slide decks with Slidev"
  - "Generate data visualizations and charts"
  - "Design responsive layouts and themes"
  - "Structure content for maximum impact"
  - "Export presentations in multiple formats"
tags: ["slidev", "presentation", "ppt", "builder", "rich-content", "data-visualization"]
---

# PPT Builder

基于Slidev创建极致丰富的演示文稿生成器，专业级视觉体验与内容深度并重。

## 何时使用

- 需要创建专业演示文稿时
- 要求图文并茂的视觉呈现时
- 需要快速生成高质量PPT时
- 制作商业汇报或技术展示时
- 需要数据可视化图表时
- 制作培训材料或教程时

## 核心功能

### 🎨 视觉设计
- **丰富主题**: 多种专业主题模板
- **图表集成**: 自动生成数据可视化
- **图标系统**: 专业图标库支持
- **渐变色彩**: 现代色彩搭配
- **布局优化**: 智能页面布局
- **字体系统**: 专业字体配置

### 📊 内容生成
- **结构化内容**: 自动组织信息层次
- **数据图表**: 自动生成各类图表
- **代码高亮**: 技术内容展示
- **数学公式**: 学术内容支持
- **多媒体集成**: 图片、视频支持
- **交互元素**: 动画和过渡效果

### 🔧 技术特性
- **Slidev引擎**: 基于现代化PPT框架
- **Markdown语法**: 简洁的内容编写
- **Vue组件**: 自定义组件支持
- **实时预览**: 边写边看效果
- **热重载**: 开发时自动刷新
- **导出功能**: PDF、PNG、PPTX格式

## 使用示例

### 示例一：商业计划书
```
用户输入: "创建一个关于新产品发布的商业计划书PPT，包含市场分析、产品介绍、营销策略、财务预测"

技能输出: 生成15页专业商业计划书
- 封面页：品牌视觉 + 产品定位
- 目录页：清晰的内容导航
- 市场分析：数据图表 + 趋势分析
- 产品介绍：产品特性 + 视觉展示
- 竞品分析：对比图表 + 优势说明
- 营销策略：4P策略 + 执行计划
- 财务预测：收入图表 + 成本分析
- 团队介绍：组织架构 + 人员介绍
- 投资回报：ROI计算 + 风险评估
- 总结页：核心要点 + 行动号召
```

### 示例二：技术分享会
```
用户输入: "制作一个关于微服务架构的技术分享PPT，包含架构设计、技术选型、实施案例"

技能输出: 生成12页技术演示文稿
- 标题页：主题 + 讲师信息
- 背景介绍：传统架构痛点分析
- 微服务概述：定义 + 核心特征
- 架构设计：系统架构图 + 组件说明
- 技术选型：技术栈对比 + 决策依据
- 实施案例：真实项目案例分析
- 最佳实践：设计原则 + 经验总结
- 挑战与解决方案：常见问题 + 解决方案
- 性能优化：监控指标 + 优化策略
- 未来展望：技术趋势 + 发展方向
```

### 示例三：培训教程
```
用户输入: "创建一个关于数据分析入门的培训PPT，包含基础概念、工具介绍、实战案例"

技能输出: 生成20页培训材料
- 课程介绍：学习目标 + 课程大纲
- 基础概念：数据类型 + 分析流程
- 工具介绍：Excel/Python/R工具对比
- 数据收集：数据源 + 收集方法
- 数据清洗：常见问题 + 处理技巧
- 描述统计：均值/中位数/标准差
- 可视化基础：图表类型 + 选择原则
- 相关性分析：散点图 + 相关系数
- 回归分析：线性回归 + 模型评估
- 实战案例：完整数据分析流程
- 总结回顾：重点知识 + 学习建议
```

## 技术实现

### 核心依赖
- **Slidev**: 现代化演示文稿框架
- **Vue 3**: 组件化开发
- **Vite**: 快速构建工具
- **UnoCSS**: 原子化CSS
- **Prism**: 代码高亮
- **Mermaid**: 图表生成
- **KaTeX**: 数学公式渲染

### 模板系统
```typescript
interface SlideTemplate {
  layout: 'cover' | 'content' | 'two-cols' | 'image-text' | 'chart'
  theme: 'default' | 'corporate' | 'tech' | 'creative' | 'academic'
  components: string[]
  animations: AnimationConfig[]
}
```

### 内容生成器
- **智能分析**: 自动分析内容类型和结构
- **模板匹配**: 根据内容选择最佳布局
- **图表生成**: 自动创建数据可视化
- **样式优化**: 智能调整视觉呈现
- **质量检查**: 内容完整性和美观度验证

## 配置选项

### 基础配置
```yaml
# slidev配置
theme: corporate
title: 演示文稿标题
author: 作者姓名
date: YYYY-MM-DD
aspectRatio: 16:9
canvasWidth: 1280
```

### 高级配置
```yaml
# 自定义主题
colors:
  primary: '#1e40af'
  secondary: '#64748b'
  accent: '#f59e0b'
  background: '#ffffff'

# 字体配置
fonts:
  sans: 'Inter, system-ui, sans-serif'
  mono: 'Fira Code, monospace'

# 动画配置
animations:
  fadeIn: true
  slideUp: true
  stagger: 100
```

## 注意事项

### 内容优化
- 确保每页信息量适中，避免过度拥挤
- 图表数据需要准确且有意义
- 文字内容要简洁有力，突出重点
- 配色方案要符合品牌调性

### 技术要求
- 需要Node.js环境支持
- 建议使用现代浏览器预览
- 大型项目建议使用性能优化
- 导出功能需要额外依赖安装

### 使用限制
- 复杂动画可能影响导出质量
- 某些特殊字体需要额外配置
- 大量图片可能影响加载速度
- 代码示例需要语法正确性检查

## 扩展功能

### 组件库
- **数据图表**: 柱状图、饼图、折线图、散点图
- **流程图**: 流程图、组织架构图、思维导图
- **代码展示**: 语法高亮、执行结果展示
- **媒体组件**: 图片、视频、音频集成
- **交互组件**: 按钮、表单、弹窗、轮播

### 导出格式
- **PDF**: 高质量文档格式
- **PPTX**: PowerPoint兼容格式
- **PNG**: 图片序列格式
- **HTML**: 网页演示格式
- **PDF Speaker Notes**: 包含演讲者备注

这个技能将帮助您快速创建专业级的演示文稿，无论是商业汇报、技术分享还是培训教程，都能生成内容丰富、视觉精美的PPT。