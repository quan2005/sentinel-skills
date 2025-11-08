# Skills Collection by Francis

<div align="center">

![Claude Code](https://img.shields.io/badge/Claude%20Code-Skills-blue)
![License](https://img.shields.io/badge/License-MIT-green)
![Version](https://img.shields.io/badge/Version-1.0.0-orange)

**A comprehensive collection of Claude Code skills for MCP development, presentation creation, and more**

[Installation](#installation) • [Skills](#available-skills) • [Usage](#usage) • [Contributing](#contributing)

</div>

## 🚀 Installation

### Option 1: Direct Installation (Recommended)

```bash
# Clone this repository
git clone https://github.com/quan2005/skills.git
cd skills

# Trust and install the plugin
claude plugin trust .
```

### Option 2: Manual Configuration

Add this to your `~/.claude/settings.json`:

```json
{
  "plugins": {
    "/path/to/skills": true
  }
}
```

### Option 3: Install Individual Skills

Copy specific skill folders to your existing Claude Code skills directory.

## ✨ Available Skills

### 🛠️ FastMCP App Creator

**Category**: Development Tools
**Tags**: `mcp`, `fastmcp`, `python`, `api-development`, `server`

Create professional MCP (Model Context Protocol) applications using FastMCP 2.x framework and uv package manager. Complete workflow from design to production-ready deployment.

**Features**:
- 🏗️ FastMCP 2.x framework support
- 🔒 Security best practices implementation
- 📊 Multiple app type templates (Basic, Web API, Database, File Processor)
- ⚡ Production-ready deployment with streamableHttp
- 🧪 Comprehensive testing and documentation

**When to use**:
- Creating MCP applications from design documents
- Building API servers and database integrations
- Developing file processing tools
- Generating production-ready MCP servers

---

### 📊 Slidev PPT Creator

**Category**: Productivity
**Tags**: `slidev`, `presentation`, `ppt`, `visualization`, `charts`

Create professional, feature-rich presentations using Slidev framework with automatic template recommendation, visual element generation, and multiple input methods.

**Features**:
- 🎨 Automatic template selection (Business, Technical, Educational, General)
- 📈 Data visualization and chart generation
- 🏗️ Architecture diagram creation
- 📝 Multiple input methods (Simple description, Structured input, Interactive)
- 📤 Multi-format export (PDF, PPTX, PNG, web)

**When to use**:
- Creating business presentations and proposals
- Building technical talks and training materials
- Generating educational content and tutorials
- Converting ideas into professional slide decks

## 💡 Usage

### Automatic Skill Selection

Claude Code automatically detects and uses the appropriate skill based on your requests:

```bash
# Create MCP applications
"Help me create an MCP app for database management"

# Generate presentations
"Create a technical presentation about microservices"

# Both skills will be activated automatically based on context
```

### Manual Skill Invocation

You can also explicitly reference skills:

```bash
# Use FastMCP App Creator
/skill fastmcp-app-creator "Create a knowledge base MCP app"

# Use Slidev PPT Creator
/skill slidev-ppt-creator "Generate a business proposal presentation"
```

## 📁 Project Structure

```
skills/
├── .claude-plugin/
│   └── marketplace.json          # Plugin metadata and configuration
├── skills/
│   ├── fastmcp-app-creator/      # MCP application development skill
│   │   ├── SKILL.md              # Skill documentation
│   │   ├── scripts/              # Automation scripts
│   │   ├── assets/               # Templates and configs
│   │   └── references/           # Documentation and guides
│   └── slidev-ppt-creator/       # Presentation creation skill
│       ├── SKILL.md              # Skill documentation
│       ├── scripts/              # Generation scripts
│       ├── assets/               # Templates and themes
│       └── references/           # Slidev guides and patterns
├── mcp-creator.py                # Advanced MCP creation utility
├── README.md                     # This file
└── agent_skills_spec.md          # Skill development guidelines
```

## 🔧 Development

### Creating New Skills

1. Create a new directory under `skills/`
2. Add a `SKILL.md` file with proper frontmatter
3. Include necessary scripts, templates, and documentation
4. Update `marketplace.json` with skill metadata
5. Test with Claude Code

### Skill Template

```markdown
---
name: your-skill-name
description: Brief description of when to use this skill
version: 1.0.0
author: Your Name
tags: ["tag1", "tag2", "tag3"]
---

# Your Skill Name

Detailed documentation...
```

## 🤝 Contributing

Contributions are welcome! Please read our [Contributing Guidelines](CONTRIBUTING.md) before submitting pull requests.

### How to Contribute

1. Fork this repository
2. Create a feature branch (`git checkout -b feature/amazing-skill`)
3. Add your skill with proper documentation
4. Update `marketplace.json`
5. Test thoroughly with Claude Code
6. Submit a pull request

## 📖 Documentation

- [Skill Development Guide](./agent_skills_spec.md) - Comprehensive skill creation guidelines
- [FastMCP Documentation](./skills/fastmcp-app-creator/references/) - MCP development resources
- [Slidev Documentation](./skills/slidev-ppt-creator/references/) - Presentation creation guides

## 🐛 Troubleshooting

### Common Issues

**Skill not detected**:
```bash
# Verify plugin is trusted
claude plugin list

# Reinstall plugin
claude plugin trust .
```

**Scripts not executable**:
```bash
# Make scripts executable
chmod +x skills/*/scripts/*.py
```

**Missing dependencies**:
- Check skill-specific documentation for required tools
- Ensure Python 3.8+ and Node.js 16+ are installed

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [Anthropic](https://anthropic.com) for Claude Code
- [FastMCP](https://github.com/jlowin/fastmcp) for the MCP framework
- [Slidev](https://sli.dev) for the presentation framework

## 🔗 Links

- [GitHub Repository](https://github.com/quan2005/skills)
- [Issues & Support](https://github.com/quan2005/skills/issues)
- [Discussions](https://github.com/quan2005/skills/discussions)

---

<div align="center">

**⭐ Star this repository if it helps you!**

Made with ❤️ by [Francis](https://github.com/quan2005)

</div>