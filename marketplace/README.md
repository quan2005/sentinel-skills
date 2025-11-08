# Slidev Skills Marketplace

<div align="center">

![Slidev Skills Marketplace](https://img.shields.io/badge/Slidev-Skills%20Marketplace-blue?style=for-the-badge&logo=vue)
![Claude Code](https://img.shields.io/badge/Claude%20Code-Compatible-success?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

**🎨 发现、分享、创建令人惊叹的演示文稿技能**

[探索技能](#-技能分类) • [贡献技能](#-贡献技能) • [社区](#-社区) • [文档](#文档)

</div>

## ✨ 什么是 Slidev Skills Marketplace？

Slidev Skills Marketplace 是一个专门为 Claude Code 用户打造的演示文稿技能平台。在这里，您可以：

- 🚀 **发现** 高质量的 Slidev 演示文稿技能
- 🎨 **创建** 图文并茂的视觉震撼演示
- 🔧 **自定义** 适合特定需求的技能
- 🌟 **分享** 您的创作与全球用户

## 🌟 特色技能

### 📊 [Slidev Presentation Creator](../skills/slidev-presentation-creator/)
> 🎯 **创建极致丰富的图文并茂演示文稿**
>
> 使用 Slidev 框架制作商业级视觉体验，每一页都包含丰富图表、数据可视化、专业图标、渐变色彩、交互元素和动画效果。
>
> [查看技能 →](../skills/slidev-presentation-creator/)

---

## 🎯 技能分类

### 📊 **演示文稿工具**
- 🎨 **演示文稿创建** - 构建专业演示文稿的完整解决方案
- 📈 **数据可视化** - 图表、统计和数据分析展示
- 🎪 **互动演示** - 包含动画和交互效果的动态演示

### 🎨 **设计与美学**
- 🎭 **主题设计** - 专业主题和视觉风格
- 🎯 **布局优化** - 响应式和现代化布局设计
- 🌈 **色彩搭配** - 专业配色方案和渐变效果

### 💻 **技术集成**
- ⚡ **代码高亮** - 专业的代码展示和语法高亮
- 🔧 **开发工具** - 面向开发者的专业工具
- 📱 **跨平台** - 多平台兼容和响应式设计

### 📚 **教育内容**
- 🎓 **教程制作** - 结构化的教学演示文稿
- 📖 **知识分享** - 专业知识和经验分享
- 🏆 **最佳实践** - 行业标准和最佳实践展示

---

## 🚀 快速开始

### 1. 安装技能

```bash
# 方法1: 使用我们的技能安装器
./scripts/install-skill.sh slidev-presentation-creator

# 方法2: 手动安装
cp -r marketplace/skills/slidev-presentation-creator ~/.claude/skills/
```

### 2. 使用技能

在 Claude Code 中直接使用：

```
帮我创建一个关于人工智能的演示文稿，要求图文并茂、视觉震撼
```

### 3. 自定义技能

```bash
# 基于现有技能创建自定义版本
cp -r marketplace/skills/slidev-presentation-creator my-custom-skill
cd my-custom-skill
# 编辑 SKILL.md 文件以满足您的特定需求
```

---

## 📈 技能统计

<div align="center">

| 指标 | 数值 | 说明 |
|------|------|------|
| 📦 **技能总数** | 1+ | 持续增长中 |
| ⭐ **精选技能** | 1+ | 经过严格筛选 |
| 🌟 **社区贡献** | 欢迎 | 欢迎提交新技能 |
| 📥 **下载次数** | 100+ | 技能使用统计 |

</div>

---

## 🤝 贡献技能

我们欢迎社区贡献！分享您的技能，让更多人受益。

### 📋 贡献要求

- ✅ **原创技能** - 必须是您自己创建的技能
- ✅ **完整文档** - 包含详细的使用说明和示例
- ✅ **高质量** - 遵循最佳实践和编码标准
- ✅ **图文并茂** - 每页都包含丰富的视觉元素
- ✅ **实用价值** - 解决实际问题，提供实用功能

### 🚀 提交流程

1. **Fork** 这个仓库
2. **创建** 您的技能目录 (`marketplace/skills/your-skill-name/`)
3. **编写** `SKILL.md` 文件和必要的文档
4. **提交** Pull Request
5. **等待** 我们的审核和反馈

### 📁 技能结构

```
marketplace/skills/your-skill/
├── SKILL.md              # 技能主文件 (必需)
├── README.md             # 技能说明 (推荐)
├── examples/             # 使用示例 (推荐)
├── templates/            # 模板文件 (可选)
├── scripts/              # 辅助脚本 (可选)
└── assets/               # 资源文件 (可选)
```

---

## 🏆 精选技能标准

我们的精选技能必须满足以下标准：

### 🎨 **视觉标准**
- ✅ 每页至少包含3个专业图标
- ✅ 使用渐变色彩和现代化设计
- ✅ 包含数据可视化和图表
- ✅ 采用卡片式布局和响应式设计

### 📝 **内容标准**
- ✅ 每页包含200-500字的详细信息
- ✅ 提供具体案例和实际数据
- ✅ 包含深度分析和实用建议
- ✅ 内容结构清晰，逻辑合理

### ⚡ **交互标准**
- ✅ 使用 v-click 实现渐进式展示
- ✅ 包含悬浮效果和过渡动画
- ✅ 提供可点击交互元素
- ✅ 代码高亮和实时演示效果

### 🔧 **技术标准**
- ✅ 遵循 Slidev 最佳实践
- ✅ 支持多主题和自定义配置
- ✅ 提供完整的错误处理
- ✅ 包含详细的使用文档

---

## 🌟 社区

### 💬 讨论和交流

- **GitHub Issues**: [提出问题和建议](https://github.com/your-username/slidev-presentation-skill/issues)
- **GitHub Discussions**: [社区讨论](https://github.com/your-username/slidev-presentation-skill/discussions)
- **技能展示**: 分享您的优秀作品和创意

### 📢 最新动态

- 🔥 **新技能**: 持续添加新的高质量技能
- 🎨 **设计更新**: 定期更新技能设计风格
- 📊 **功能增强**: 根据用户反馈持续改进
- 🌍 **国际化**: 支持多语言和本地化

---

## 📚 文档

### 📖 **用户指南**
- [快速开始](./docs/getting-started.md)
- [技能使用](./docs/using-skills.md)
- [自定义技能](./docs/custom-skills.md)
- [故障排除](./docs/troubleshooting.md)

### 🔧 **开发者文档**
- [技能开发指南](./docs/development.md)
- [API 参考](./docs/api-reference.md)
- [贡献指南](./docs/contributing.md)
- [代码规范](./docs/coding-standards.md)

### 🎨 **设计资源**
- [设计原则](./docs/design-principles.md)
- [视觉指南](./docs/visual-guidelines.md)
- [模板库](./docs/template-library.md)
- [最佳实践](./docs/best-practices.md)

---

## 🏅 致谢

### 🌟 贡献者
感谢所有为这个项目做出贡献的开发者和用户！

### 🤖 技术支持
- **Claude Code** - 强大的 AI 编程助手
- **Slidev** - 现代化的演示文稿框架
- **Vue.js** - 渐进式 JavaScript 框架

### 📊 数据统计
- 使用统计和分析
- 用户反馈收集
- 性能监控和优化

---

## 📄 许可证

本项目采用 MIT 许可证 - 详见 [LICENSE](../LICENSE) 文件。

---

<div align="center">

**🎉 开始您的演示创作之旅！**

[立即开始](#-快速开始) • [探索技能](#-技能分类) • [加入社区](#-社区) • [查看文档](#文档)

Made with ❤️ by the Slidev Skills Community

</div>