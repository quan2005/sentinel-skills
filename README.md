# Skills

个人Claude Code技能集合 - Claude Code插件

## 项目结构

```
skills/
├── .claude-plugin/     # 插件元数据 (必需)
│   └── plugin.json     # 插件配置文件
├── skills/             # 技能目录
│   └── skill-name/     # 具体技能
│       └── SKILL.md    # 技能说明
├── README.md           # 项目说明
└── agent_skills_spec.md # 技能规范
```

## 安装插件

这是一个Claude Code插件，安装后技能会被自动识别：

```bash
# 信任并安装插件
claude plugin trust .

# 或者通过settings.json配置
echo '{"plugins": {"./": true}}' > ~/.claude/settings.json
```

## 创建技能

1. 在 `skills/` 目录下创建技能文件夹
2. 编写 `SKILL.md` 文档
3. 参考 [agent_skills_spec.md](./agent_skills_spec.md) 了解详细规范

## 技能规范

请查看 [agent_skills_spec.md](./agent_skills_spec.md) 了解：
- 技能目录结构
- 文档编写规范
- 开发指南
- 质量标准

## 插件工作原理

- `.claude-plugin/plugin.json` 告诉Claude这是一个插件
- `skills/` 目录中的技能会被Claude自动发现
- Claude根据任务上下文自动选择合适的技能使用

## 许可证

MIT License