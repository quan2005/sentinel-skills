# Slidev PPT Creator - 使用指南

## 🎉 技能创建完成！

我已经使用 skill-creator 方法成功创建了基于 Slidev 的 PPT 构建技能。该技能现在可以打包并分发使用了。

## 📦 技能包信息

- **包名**: `slidev-ppt-creator.zip`
- **大小**: 74.8 KB
- **状态**: ✅ 验证通过，可正常使用

## 🚀 快速开始

### 方法1：直接使用技能
将 `slidev-ppt-creator.zip` 解压到你的技能目录，然后可以立即使用：

```bash
# 在Claude中使用
使用slidev-ppt-creator创建一个关于"人工智能在医疗健康领域应用"的商业演示文稿
```

### 方法2：使用脚本运行
```bash
# 解压技能包
unzip slidev-ppt-creator.zip
cd slidev-ppt-creator

# 直接运行脚本
python3 scripts/create_presentation.py "Create a business presentation about AI in healthcare" --title "AI in Healthcare"

# 或交互式模式
python3 scripts/create_presentation.py --interactive
```

## ✨ 核心功能

### 🎯 智能内容分析
- 自动识别演示类型（商务、技术、教育、通用）
- 提取内容结构和关键要点
- 推荐合适的模板和布局

### 🎨 丰富的模板系统
- **商务模板**: 产品发布、企业介绍、投资路演
- **技术模板**: 代码演示、架构讲解、技术培训
- **教育模板**: 课程教学、知识分享、学术报告
- **通用模板**: 多种场景的基础模板

### 🖼️ 可视化元素生成
- 数据图表（柱状图、饼图、折线图）
- 流程图和架构图（Mermaid）
- 代码高亮和语法展示
- 专业的视觉设计

### 📝 完整项目生成
- `slides.md` - 主演示文件
- `package.json` - 项目配置
- `README.md` - 使用说明
- `style.css` - 自定义样式

## 🛠️ 技术架构

### 核心模块
1. **ContentAnalyzer** - 内容分析和类型识别
2. **TemplateGenerator** - 模板生成和项目构建
3. **ChartGenerator** - 图表和可视化元素生成
4. **SlidesValidator** - 内容验证和质量检查

### 技能结构
```
slidev-ppt-creator/
├── SKILL.md                    # 技能配置和使用说明
├── scripts/                    # 核心功能脚本
│   ├── content_analyzer.py     # 内容分析器
│   ├── template_generator.py   # 模板生成器
│   ├── chart_generator.py      # 图表生成器
│   ├── slides_validator.py     # 内容验证器
│   ├── create_presentation.py  # 主要创建脚本
│   └── package_skill.py        # 技能打包脚本
├── references/                 # 参考资料
│   ├── slidev_syntax.md        # Slidev语法参考
│   └── template_patterns.md    # 模板模式参考
├── assets/                     # 资源文件
│   └── templates/              # 演示模板
│       ├── business/           # 商务模板
│       └── technical/          # 技术模板
└── examples/                   # 使用示例
    └── sample-config.json      # 示例配置
```

## 📋 使用示例

### 商务演示
```bash
# 商务提案演示
python3 scripts/create_presentation.py \
  "Create a business proposal for an AI-powered customer service platform that reduces costs by 60% while improving customer satisfaction. Include market analysis, features, business model, and investment opportunities." \
  --title "AI Customer Service Platform"
```

### 技术分享
```bash
# 技术架构分享
python3 scripts/create_presentation.py \
  "Create a technical presentation about migrating from monolithic architecture to microservices. Include challenges, design patterns, implementation strategies, and lessons learned with code examples." \
  --title "Microservices Migration Journey"
```

### 教育培训
```bash
# React教学课程
python3 scripts/create_presentation.py \
  "Create an educational presentation about React Hooks for frontend developers. Cover useState, useEffect, useContext, and custom hooks with practical examples and exercises." \
  --title "Mastering React Hooks"
```

## 🎯 技能特点

### ✅ 完全符合 Skill Creator 标准
- 标准的 YAML 前置元数据
- 清晰的使用说明和指导
- 模块化的脚本和资源组织
- 完整的验证和打包流程

### ✅ 功能完整
- 支持多种演示类型和场景
- 智能内容分析和模板推荐
- 丰富的可视化元素
- 完整的 Slidev 项目生成

### ✅ 易于使用
- 自然语言输入，自动生成
- 多种使用方式（直接使用、脚本运行、交互模式）
- 详细的错误处理和验证
- 完善的文档和示例

## 📈 验证结果

技能已通过完整验证：
- ✅ YAML 前置元数据格式正确
- ✅ 必需字段（name, description）完整
- ✅ 目录结构符合标准
- ✅ Python 脚本语法正确
- ✅ 文档和参考资料完整

## 🎊 下一步

1. **安装技能**: 将 `slidev-ppt-creator.zip` 解压到技能目录
2. **开始使用**: 通过自然语言描述创建演示文稿
3. **定制扩展**: 根据需要添加新的模板和功能
4. **分享反馈**: 使用后提供反馈和改进建议

这个技能将大大简化你创建专业演示文稿的流程，只需简单的描述就能生成内容丰富、视觉精美的 Slidev 演示文稿！🚀