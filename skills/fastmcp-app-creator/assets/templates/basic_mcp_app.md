# 基本 MCP 应用模板

## 模板描述

这是一个基本的 MCP 应用模板，包含核心功能和最佳实践。

## 项目结构

```
basic-mcp-app/
├── pyproject.toml          # uv 项目配置
├── README.md              # 项目文档
├── .env.example           # 环境变量模板
├── .gitignore             # Git 忽略文件
├── src/
│   └── basic_mcp_app/
│       ├── __init__.py
│       ├── server.py      # 主服务器文件
│       └── tools.py       # 自定义工具
├── tests/
│   ├── __init__.py
│   └── test_server.py     # 测试文件
└── config/
    └── mcp_config.json    # MCP 配置
```

## 核心功能

### 基础工具
- `ping()` - 连接测试
- `server_info()` - 服务器信息
- `echo_message()` - 消息回显

### 资源
- `config://server` - 服务器配置

### 提示词
- `help` - 帮助信息

## 配置示例

### pyproject.toml
```toml
[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"

[project]
name = "basic-mcp-app"
version = "1.0.0"
description = "基本 MCP 应用"
authors = [{name = "Developer", email = "dev@example.com"}]
license = {text = "MIT"}
readme = "README.md"
requires-python = ">=3.11"
dependencies = ["fastmcp>=2.0.0", "pydantic>=2.0.0"]

[project.optional-dependencies]
dev = ["pytest>=8.0.0", "pytest-asyncio>=0.24.0", "ruff>=0.6.0"]

[project.scripts]
basic-mcp-server = "basic_mcp_app.server:main"

[tool.ruff]
target-version = "py311"
line-length = 88

[tool.mypy]
python_version = "3.11"
disallow_untyped_defs = true
```

### MCP 配置
```json
{
  "mcpServers": {
    "basic-mcp-app": {
      "type": "streamableHttp",
      "url": "https://api.example.com/mcp/basic",
      "headers": {
        "Authorization": "Bearer <USER_AGENT_TOKEN>",
        "x-context-id": "<context_id>"
      }
    }
  }
}
```