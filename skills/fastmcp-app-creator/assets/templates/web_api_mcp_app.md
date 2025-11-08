# Web API MCP 应用模板

## 模板描述

这是一个专门用于 HTTP API 集成的 MCP 应用模板，包含完整的 HTTP 客户端功能和错误处理。

## 项目结构

```
web-api-mcp-app/
├── pyproject.toml
├── README.md
├── .env.example
├── .gitignore
├── src/
│   └── web_api_mcp_app/
│       ├── __init__.py
│       ├── server.py
│       ├── api_tools.py   # HTTP API 工具
│       └── auth.py        # 认证处理
├── tests/
│   ├── __init__.py
│   ├── test_server.py
│   └── test_api_tools.py
└── config/
    ├── mcp_config.json
    └── api_endpoints.json # API 端点配置
```

## 核心功能

### HTTP 工具
- `http_get(url, headers=None)` - GET 请求
- `http_post(url, data, headers=None)` - POST 请求
- `http_put(url, data, headers=None)` - PUT 请求
- `http_delete(url, headers=None)` - DELETE 请求
- `batch_requests(requests)` - 批量请求

### 认证工具
- `set_bearer_token(token)` - 设置 Bearer Token
- `set_api_key(key, header_name)` - 设置 API Key
- `basic_auth(username, password)` - 基础认证

### 配置管理
- `load_api_config(config_file)` - 加载 API 配置
- `get_endpoints()` - 获取可用端点

## 配置示例

### pyproject.toml
```toml
[project]
name = "web-api-mcp-app"
version = "1.0.0"
description = "Web API 集成 MCP 应用"
dependencies = [
    "fastmcp>=2.0.0",
    "httpx>=0.27.0",
    "pydantic>=2.8.0",
    "python-dotenv>=1.0.0",
    "cryptography>=41.0.0",
]

[project.optional-dependencies]
dev = [
    "pytest>=8.0.0",
    "pytest-asyncio>=0.24.0",
    "pytest-httpx>=0.28.0",
    "ruff>=0.6.0",
    "mypy>=1.11.0",
]
```

### API 端点配置
```json
{
  "base_url": "https://api.example.com",
  "endpoints": {
    "users": {
      "list": "/users",
      "get": "/users/{user_id}",
      "create": "/users",
      "update": "/users/{user_id}",
      "delete": "/users/{user_id}"
    },
    "posts": {
      "list": "/posts",
      "get": "/posts/{post_id}",
      "create": "/posts",
      "update": "/posts/{post_id}",
      "delete": "/posts/{post_id}"
    }
  },
  "default_headers": {
    "Content-Type": "application/json",
    "Accept": "application/json"
  }
}
```

### 环境变量
```bash
# API 配置
API_BASE_URL=https://api.example.com
API_TOKEN=your_api_token_here
API_TIMEOUT=30

# 认证配置
AUTH_TYPE=bearer  # bearer, api_key, basic
AUTH_HEADER=Authorization

# 请求配置
MAX_CONCURRENT_REQUESTS=10
RETRY_ATTEMPTS=3
RATE_LIMIT_DELAY=1.0
```