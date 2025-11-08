# 贡献指南

感谢您对 Slidev Skills Marketplace 的关注！我们欢迎各种形式的贡献，包括技能开发、文档改进、bug 报告和功能建议。

## 🤝 如何贡献

### 📦 贡献技能

#### 🎯 技能要求

**基本要求：**
- ✅ **原创技能** - 必须是您自己创建的技能
- ✅ **完整文档** - 包含详细的 SKILL.md 和使用说明
- ✅ **实际价值** - 解决实际问题，提供实用功能
- ✅ **代码质量** - 遵循最佳实践和编码标准

**图文并茂要求：**
- ✅ **视觉丰富** - 每页至少包含3个专业图标
- ✅ **渐变色彩** - 使用现代化的渐变配色方案
- ✅ **数据可视化** - 包含图表、进度条等可视化元素
- ✅ **交互效果** - 使用 v-click 和动画效果
- ✅ **内容充实** - 每页包含200-500字的详细信息

#### 🚀 提交流程

1. **Fork 仓库**
   ```bash
   # Fork 这个仓库到您的 GitHub 账户
   git clone https://github.com/your-username/slidev-presentation-skill.git
   cd slidev-presentation-skill
   ```

2. **创建技能目录**
   ```bash
   mkdir -p marketplace/skills/your-skill-name
   cd marketplace/skills/your-skill-name
   ```

3. **编写技能文件**
   ```bash
   # 创建 SKILL.md 文件 (必需)
   touch SKILL.md

   # 创建其他支持文件
   touch README.md
   mkdir examples templates scripts
   ```

4. **提交更改**
   ```bash
   git add .
   git commit -m "feat: add your-skill-name skill"
   git push origin your-branch-name
   ```

5. **创建 Pull Request**
   - 访问 GitHub 页面
   - 点击 "New Pull Request"
   - 填写 PR 模板
   - 提交审核

#### 📁 技能结构

```
marketplace/skills/your-skill/
├── SKILL.md              # 技能主文件 (必需)
├── README.md             # 技能详细说明 (推荐)
├── examples/             # 使用示例 (推荐)
│   ├── basic-usage.md
│   ├── advanced-usage.md
│   └── troubleshooting.md
├── templates/            # 模板文件 (可选)
│   ├── presentation.md
│   └── report.md
├── scripts/              # 辅助脚本 (可选)
│   ├── setup.sh
│   └── validate.sh
├── assets/               # 资源文件 (可选)
│   ├── images/
│   └── icons/
└── tests/                # 测试文件 (可选)
    ├── skill.test.js
    └── examples.test.js
```

### 📝 文档贡献

#### 📖 改进文档

我们欢迎以下类型的文档贡献：

- **错误修正** - 修正文档中的错误或不准确信息
- **内容补充** - 添加缺失的信息或示例
- **结构优化** - 改进文档结构和可读性
- **翻译贡献** - 将文档翻译成其他语言

#### 🔄 文档贡献流程

1. **Fork 仓库**
2. **创建分支**
   ```bash
   git checkout -b docs/improve-documentation
   ```

3. **修改文档**
   - 修正错误或添加内容
   - 确保遵循我们的文档风格
   - 检查语法和拼写

4. **提交更改**
   ```bash
   git add docs/
   git commit -m "docs: improve [section] documentation"
   ```

5. **创建 Pull Request**

### 🐛 Bug 报告

#### 📋 Bug 报告模板

使用以下模板提交 bug 报告：

```markdown
## Bug 描述
简要描述遇到的问题

## 重现步骤
1. 执行步骤 1
2. 执行步骤 2
3. 观察到错误

## 期望行为
描述您期望发生的情况

## 实际行为
描述实际发生的情况

## 环境信息
- 操作系统: [Windows/macOS/Linux]
- Claude Code 版本: [版本号]
- 技能名称: [技能名称]
- 技能版本: [版本号]

## 附加信息
- 截图或录屏
- 错误日志
- 相关文件
```

### 💡 功能建议

#### 🎯 建议模板

```markdown
## 功能描述
简要描述您建议的功能

## 问题解决
这个功能解决了什么问题？

## 建议的解决方案
描述您希望的实现方式

## 替代方案
您考虑过的其他解决方案

## 使用场景
描述具体的使用场景

## 附加信息
- 相关链接
- 参考实现
- 设计草图
```

## 🎨 技能开发指南

### 📋 SKILL.md 文件规范

#### 必需字段

```yaml
---
name: your-skill-name
description: 简洁明确的技能描述，包含使用场景和触发词
version: 1.0.0
author: Your Name
category: skill-category
tags: [tag1, tag2, tag3]
---
```

#### 描述字段要求

- **简洁明了** - 用最少的文字说明功能
- **包含触发词** - 明确说明何时使用此技能
- **突出特色** - 强调技能的独特价值
- **用户友好** - 使用用户容易理解的语言

#### 内容结构

```markdown
# 技能名称

## Quick start
快速开始指南和基本用法

## Instructions
详细的使用说明和最佳实践

## Examples
具体的使用示例和模板

## Requirements
依赖项和前置条件

## Advanced usage
高级功能和自定义选项
```

### 🎨 设计原则

#### 图文并茂标准

1. **视觉元素**
   - 每页至少包含3个专业图标
   - 使用渐变色彩和现代化设计
   - 采用卡片式布局
   - 包含数据可视化元素

2. **内容丰富性**
   - 每页包含200-500字的详细信息
   - 提供具体案例和实际数据
   - 包含深度分析和实用建议
   - 结构清晰，逻辑合理

3. **交互效果**
   - 使用 v-click 实现渐进式展示
   - 添加悬浮效果和过渡动画
   - 提供可点击交互元素
   - 包含代码高亮和实时演示

#### 技术要求

- **代码质量** - 遵循 JavaScript/TypeScript 最佳实践
- **错误处理** - 包含完整的错误处理机制
- **性能优化** - 避免不必要的计算和渲染
- **可维护性** - 代码结构清晰，易于理解和修改

### 🧪 测试指南

#### 基本测试

```bash
# 测试技能安装
./scripts/install-skill.sh your-skill-name

# 测试技能功能
claude --debug
# 在 Claude Code 中测试技能功能

# 测试技能文档
./scripts/validate-docs.sh
```

#### 测试清单

- [ ] 技能能够正确安装
- [ ] 技能能够正确激活
- [ ] 技能功能正常工作
- [ ] 技能文档完整准确
- [ ] 示例能够正常运行
- [ ] 错误处理机制正常

## 🏆 贡献者认可

### 🌟 贡献者类型

- **技能贡献者** - 贡献新技能的开发者
- **文档贡献者** - 改进文档内容的贡献者
- **bug 报告者** - 发现和报告问题的用户
- **功能建议者** - 提出有价值建议的用户
- **社区推广者** - 帮助推广项目的支持者

### 📋 认可方式

#### 技能贡献者

- 在技能文档中添加贡献者信息
- 在市场页面展示贡献者头像
- 在贡献者列表中永久记录
- 获得技能优先使用权限

#### 其他贡献者

- 在项目 README 中致谢
- 在发布日志中感谢
- 社区积分奖励
- 项目周边福利

## 📞 联系方式

### 💬 讨论和交流

- **GitHub Issues**: [问题和建议](https://github.com/your-username/slidev-presentation-skill/issues)
- **GitHub Discussions**: [社区讨论](https://github.com/your-username/slidev-presentation-skill/discussions)
- **邮件联系**: [your-email@example.com](mailto:your-email@example.com)

### 📚 相关资源

- [项目主页](https://github.com/your-username/slidev-presentation-skill)
- [文档网站](https://your-username.github.io/slidev-presentation-skill)
- [技能市场](https://github.com/your-username/slidev-presentation-skill/tree/main/marketplace)

## 📄 许可证

贡献的内容将遵循项目的 MIT 许可证。通过贡献，您同意将您的贡献内容在 MIT 许可证下发布。

---

感谢您对 Slidev Skills Marketplace 的贡献！您的参与让这个项目变得更好。🎉