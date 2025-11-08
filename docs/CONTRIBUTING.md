# Contributing to Skills

欢迎为个人技能集合贡献代码！

## 贡献指南

### 创建新技能

1. **创建技能目录**
   ```bash
   mkdir skills/your-skill-name
   cd skills/your-skill-name
   ```

2. **编写技能文档 (SKILL.md)**
   ```markdown
   # 技能名称

   简短的技能描述。

   ## 何时使用

   描述触发技能的场景和条件

   ## 技能功能

   详细说明技能的能力和用途

   ## 使用示例

   提供具体的使用示例
   ```

3. **创建安装脚本 (install.sh)**
   ```bash
   #!/bin/bash
   # 安装技能的脚本
   echo "Installing your-skill-name..."
   # 安装逻辑
   ```

4. **创建配置文件 (package.json)**
   ```json
   {
     "name": "your-skill-name",
     "version": "1.0.0",
     "description": "技能描述",
     "main": "index.js",
     "scripts": {
       "install": "echo 'Installing skill...'"
     },
     "keywords": ["claude-code", "skill", "automation"],
     "author": "Your Name",
     "license": "MIT"
   }
   ```

### 技能开发最佳实践

#### 文档要求
- 每个技能必须有 `SKILL.md` 文件
- 包含清晰的使用说明和示例
- 说明技能的触发条件和用途

#### 安装脚本要求
- 使用 shebang (`#!/bin/bash`)
- 包含适当的错误处理
- 提供清晰的安装反馈

#### 代码质量
- 遵循现有代码风格
- 添加适当的注释
- 测试技能功能

### 提交流程

1. **Fork 仓库**
2. **创建功能分支**
   ```bash
   git checkout -b feature/new-skill
   ```
3. **添加技能文件**
4. **验证技能**
   ```bash
   ./scripts/validate-skills.sh
   ```
5. **提交更改**
   ```bash
   git add .
   git commit -m "feat: add new-skill"
   ```
6. **推送分支**
   ```bash
   git push origin feature/new-skill
   ```
7. **创建 Pull Request**

### 技能验证

在提交前，请运行验证脚本确保技能符合标准：

```bash
# 验证所有技能
./scripts/validate-skills.sh

# 安装测试
./install.sh --list
./install.sh your-skill-name
```

### 技能命名规范

- 使用小写字母和连字符
- 简洁明了地描述技能功能
- 避免特殊字符和空格

### 示例技能结构

```
skills/example-skill/
├── SKILL.md           # 技能文档
├── install.sh         # 安装脚本
├── package.json       # 配置文件
├── index.js          # 主要逻辑 (可选)
└── examples/         # 示例文件 (可选)
    └── example.md
```

## 获得帮助

如果您有任何问题或需要帮助，请：
1. 查看现有技能的实现
2. 阅读项目文档
3. 创建 Issue 或 Discussion

## 许可证

通过贡献代码，您同意您的贡献将在 MIT 许可证下发布。