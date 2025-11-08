# Skills

Skills are folders of instructions, scripts, and resources that Claude loads dynamically to improve performance on specialized tasks. Skills teach Claude how to complete specific tasks in a repeatable way, whether that's creating presentations with your company's brand guidelines, generating MCP servers for your APIs, or automating development workflows.

For more information, check out:

* [What are skills?](https://support.claude.com/en/articles/12512176-what-are-skills)
* [Using skills in Claude](https://support.claude.com/en/articles/12512180-using-skills-in-claude)
* [How to create custom skills](https://support.claude.com/en/articles/12512198-creating-custom-skills)
* [Equipping agents for the real world with Agent Skills](https://anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills)

# About This Repository

This repository contains a collection of specialized skills focused on MCP development, presentation creation, and automation workflows. These skills demonstrate practical applications ranging from technical tasks (MCP server generation, API integration) to creative workflows (professional presentations, visual design).

Each skill is self-contained in its own directory with a `SKILL.md` file containing the instructions and metadata that Claude uses. Browse through these skills to understand different patterns and approaches or use them directly in your projects.

# Example Skills

This repository includes skills focused on development productivity and content creation:

## Development & Technical

* **fastmcp-app-creator** - Create professional MCP (Model Context Protocol) applications using FastMCP 2.x framework and uv package manager. Complete workflow from design to production-ready deployment with security best practices.

## Content Creation & Design

* **slidev-ppt-creator** - Create professional, feature-rich presentations using Slidev framework with automatic template recommendation, visual element generation, and multiple input methods.

# Try in Claude Code, Claude.ai, and the API

## Claude Code

You can install this repository as a Claude Code Plugin by cloning it and running:

```bash
# Clone this repository
git clone https://github.com/quan2005/skills.git
cd skills

# Install as plugin
claude plugin install .
```

After installing the plugin, you can use the skills by just mentioning them. For instance:

* "Use the fastmcp-app-creator skill to create an MCP server for my database"
* "Use the slidev-ppt-creator skill to generate a technical presentation about microservices"

## Claude.ai

To use these skills in Claude.ai, follow the instructions in [Using skills in Claude](https://support.claude.com/en/articles/12512180-using-skills-in-claude#h_a4222fa77b).

## Claude API

You can use these skills via the Claude API. See the [Skills API Quickstart](https://docs.claude.com/en/api/skills-guide#creating-a-skill) for more.

# Creating a Basic Skill

Skills are simple to create - just a folder with a `SKILL.md` file containing YAML frontmatter and instructions.

Here's a basic template:

```
---
name: my-skill-name
description: A clear description of what this skill does and when to use it
---

# My Skill Name

My skill does...

## Examples
- Example usage of the skill

## Guidelines
- Guidelines for how the skill should work
```

The frontmatter requires only two fields:

* `name` - A unique identifier for your skill (lowercase, hyphens for spaces)
* `description` - A complete description of what the skill does and when to use it

For more details, see [How to create custom skills](https://support.claude.com/en/articles/12512198-creating-custom-skills).

# Project Structure

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

# Skill Details

## FastMCP App Creator

**When to use**: When you need to create MCP applications from design documents, build API servers, develop database integrations, or generate production-ready MCP servers.

**Key features**:
- FastMCP 2.x framework support with modern Python project structure
- Security best practices implementation (input validation, SQL injection prevention)
- Multiple app type templates (Basic, Web API, Database, File Processor)
- Production-ready deployment with streamableHttp configuration
- Comprehensive testing, documentation, and Claude Desktop integration

**Example usage**:
```
"Create an MCP app for knowledge base management using the fastmcp-app-creator skill"
```

## Slidev PPT Creator

**When to use**: When you need to create professional presentations, business proposals, technical talks, training materials, or educational content.

**Key features**:
- Automatic template selection (Business, Technical, Educational, General)
- Data visualization and chart generation
- Architecture diagram creation
- Multiple input methods (Simple description, Structured input, Interactive)
- Multi-format export (PDF, PPTX, PNG, web)

**Example usage**:
```
"Generate a technical presentation about microservices architecture using the slidev-ppt-creator skill"
```

# Contributing

Contributions are welcome! If you create a new skill or improve existing ones, please:

1. Create a new directory under `skills/`
2. Add a `SKILL.md` file with proper frontmatter and documentation
3. Include any necessary scripts, templates, or resources
4. Update `marketplace.json` with skill metadata if needed
5. Test thoroughly with Claude Code
6. Submit a pull request

# License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

# Disclaimer

**These skills are provided for demonstration and educational purposes only.** While these skills are designed to be useful, you should always test skills thoroughly in your own environment before relying on them for critical tasks.

# About

A collection of Claude Code skills by Francis for MCP development, presentation creation, and automation workflows.

### Resources

* [GitHub Repository](https://github.com/quan2005/skills)
* [Issues & Support](https://github.com/quan2005/skills/issues)
* [Discussions](https://github.com/quan2005/skills/discussions)