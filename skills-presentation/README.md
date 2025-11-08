# Skills项目技术展示

## 🚀 项目简介

这是一个使用 Slidev 框架创建的专业技术演示文稿，展示了 Skills 项目的核心架构、技术实现和功能特性。Skills 是一个专业的 Claude Code 技能集合项目，专注于 MCP 开发和演示文稿创建。

## 📊 演示内容

### 核心主题
- **项目概述** - Skills 项目整体介绍
- **架构总览** - 系统架构和模块关系
- **技术栈详解** - 核心技术和开发工具
- **FastMCP App Creator** - MCP 服务器开发技能
- **Slidev PPT Creator** - 演示文稿创建技能
- **开发工作流程** - 从需求到发布的完整流程
- **性能测试数据** - 效率提升和质量指标
- **未来展望** - 发展规划和长期愿景

### 技术亮点
- 🎨 **智能内容分析** - AI驱动的演示结构分析
- 📊 **丰富的可视化** - Mermaid 图表、架构图、流程图
- 💻 **代码示例** - 真实的 FastMCP 和 Vue 组件代码
- 🎯 **性能对比** - 直观的效率提升数据展示
- 🌟 **现代化设计** - 响应式布局和美观的界面

## 🛠️ 技术特性

### Slidev 功能
- ✨ **默认主题** - 简洁现代的设计风格
- 🎨 **深色模式** - 支持自动/手动切换
- 📱 **响应式布局** - 适配各种屏幕尺寸
- 🎯 **Mermaid 图表** - 丰富的流程图和架构图
- 💻 **代码高亮** - 多语言语法高亮支持
- 🖼️ **背景图片** - Unsplash 高质量背景
- 🎭 **动画效果** - 流畅的页面切换动画

### 依赖组件
- **@slidev/cli** - Slidev 核心框架
- **@slidev/theme-default** - 默认主题
- **mermaid** - 图表渲染引擎
- **chart.js** - 数据可视化图表
- **vue-chartjs** - Vue 图表组件
- **element-plus** - UI 组件库
- **playwright** - 导出功能支持

## 📦 安装与运行

### 环境要求
- Node.js 18+
- npm 或 yarn
- 现代浏览器（Chrome、Firefox、Safari、Edge）

### 安装依赖
```bash
# 克隆项目（如果需要）
git clone <repository-url>
cd skills-presentation

# 安装依赖
npm install
```

### 开发模式
```bash
# 启动开发服务器
npm run dev

# 访问演示文稿
# 浏览器会自动打开 http://localhost:3030
```

### 构建与导出
```bash
# 构建静态网站
npm run build

# 导出为 PDF
npm run export

# 导出为 PPTX
npm run export-pptx

# 导出为 PNG 图片
npm run export-png

# 启动静态服务器
npm run serve
```

## 📁 项目结构

```
skills-presentation/
├── slides.md              # 演示文稿主文件
├── package.json           # 项目配置和依赖
├── README.md             # 项目说明文档
├── dist/                 # 构建输出目录
└── node_modules/         # 依赖包目录
```

## 🎨 演示文稿结构

### 页面布局
1. **封面页** - 项目标题和简介
2. **目录页** - 演示内容导航
3. **项目概述** - Skills 项目介绍
4. **架构总览** - Mermaid 架构图
5. **技术栈详解** - 三列布局展示
6. **FastMCP 深度解析** - 双列布局和代码示例
7. **Slidev 技术实现** - 组件架构展示
8. **项目统计数据** - 四列数据卡片
9. **开发工作流程** - Mermaid 流程图
10. **核心优势与创新** - 渐变卡片布局
11. **使用示例** - 场景化演示
12. **性能测试数据** - 进度条和数据对比
13. **社区与生态** - 社区参与展示
14. **技术栈总结** - 图标化技术栈
15. **未来展望** - 季度规划路线图
16. **核心收获** - 经验总结和洞察
17. **结束页** - 感谢和联系方式

### 视觉设计
- **配色方案**: 蓝色为主色调，配合绿色、紫色、橙色等辅助色
- **布局风格**: 网格化布局，响应式设计
- **交互元素**: 悬停效果、渐变背景、动画过渡
- **数据可视化**: Mermaid 图表、进度条、统计卡片

## 🎯 使用场景

### 技术分享
- 团队内部技术分享会
- 开源社区项目展示
- 技术大会演讲
- 客户方案演示

### 教学培训
- 技术培训课程
- 工作坊演示
- 学术报告
- 学生毕业设计展示

### 项目汇报
- 项目进度汇报
- 成果展示
- 技术评审
- 投资者演示

## 🔧 自定义配置

### 修改主题
在 `slides.md` 文件的 frontmatter 中修改主题配置：

```yaml
---
theme: seriph          # 可选: default, seriph, apple-basic
colorSchema: auto      # 可选: auto, light, dark
background: 'https://source.unsplash.com/collection/94734566/1920x1080'
---
```

### 修改颜色主题
在 `package.json` 中的 `slidev.themeConfig` 部分：

```json
{
  "themeConfig": {
    "primary": "#1e40af",      // 主色调
    "primaryDark": "#1e3a8a",  // 深色主色调
    "secondary": "#7c3aed",    // 次要色调
    "tertiary": "#059669"      // 第三色调
  }
}
```

### 添加新页面
在 `slides.md` 中添加新的页面：

```markdown
---

# 新页面标题

## 页面内容

这里可以添加 Markdown 内容、代码块、图表等
```

## 📈 演示统计

- **总页数**: 17 页
- **代码示例**: 4 个
- **Mermaid 图表**: 2 个
- **数据可视化**: 多个进度条和统计卡片
- **交互元素**: 悬停效果和动画
- **响应式设计**: 支持多设备
- **导出格式**: PDF、PPTX、PNG

## 🤝 贡献指南

### 反馈问题
如果在使用过程中遇到问题，请：

1. 检查 Node.js 版本是否符合要求
2. 清理 node_modules 并重新安装
3. 检查网络连接（某些资源需要网络加载）

### 改进建议
欢迎提出改进建议：

- 内容准确性
- 视觉设计优化
- 用户体验改进
- 功能增强建议

## 📄 许可证

MIT License - 详见 LICENSE 文件

## 🔗 相关链接

- [Slidev 官方文档](https://sli.dev/)
- [Mermaid 图表语法](https://mermaid.js.org/)
- [Vue.js 官方网站](https://vuejs.org/)
- [Skills 项目主页](https://github.com/quan2005/skills)

---

**Author**: Francis
**Date**: 2025-11-08
**Version**: 1.0.0