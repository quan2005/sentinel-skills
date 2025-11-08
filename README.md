# Skills

个人技能集合 - 个人创建的Claude Code技能存储库

## 项目结构

```
skills/
├── marketplace/           # 技能市场
│   └── skills/           # 个人技能
│       └── skill-name/   # 具体技能目录
│           ├── SKILL.md  # 技能说明文档
│           ├── install.sh # 安装脚本
│           └── package.json # 技能配置
├── examples/             # 示例文件
├── templates/            # 模板文件
├── scripts/              # 构建和工具脚本
├── docs/                 # 项目文档
├── README.md             # 项目说明
├── package.json          # 项目配置
└── install.sh            # 全局安装脚本
```

## 技能开发指南

### 创建新技能

1. 在 `marketplace/skills/` 下创建新目录
2. 编写 `SKILL.md` 技能说明文档
3. 创建 `install.sh` 安装脚本
4. 添加 `package.json` 配置文件

### 技能文档结构 (SKILL.md)

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

## 安装技能

```bash
# 安装单个技能
./install.sh skill-name

# 安装所有技能
./install.sh

# 或使用npm
npm install
```

## 贡献

欢迎提交新的技能到这个仓库。

## 许可证

MIT License