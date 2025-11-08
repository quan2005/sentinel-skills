# 数据库 MCP 应用模板

## 模板描述

这是一个专门用于数据库操作的安全 MCP 应用模板，支持多种数据库类型和查询安全控制。

## 项目结构

```
database-mcp-app/
├── pyproject.toml
├── README.md
├── .env.example
├── .gitignore
├── src/
│   └── database_mcp_app/
│       ├── __init__.py
│       ├── server.py
│       ├── db_tools.py     # 数据库工具
│       ├── models.py       # 数据模型
│       └── security.py     # 安全控制
├── tests/
│   ├── __init__.py
│   ├── test_server.py
│   └── test_db_tools.py
├── migrations/             # 数据库迁移
│   └── __init__.py
└── config/
    ├── mcp_config.json
    └── database_config.json
```

## 核心功能

### 查询工具
- `execute_query(query, params=None)` - 执行 SQL 查询（只读）
- `get_table_schema(table_name)` - 获取表结构
- `list_tables()` - 列出所有表
- `get_table_info(table_name)` - 获取表详细信息

### 安全工具
- `validate_query(query)` - 验证查询安全性
- `explain_query(query)` - 查询执行计划
- `check_permissions(operation, table_name)` - 权限检查

### 数据分析工具
- `analyze_table(table_name)` - 表数据分析
- `get_table_stats(table_name)` - 表统计信息
- `export_table(table_name, format='csv')` - 导出表数据

## 支持的数据库

- SQLite (默认)
- PostgreSQL
- MySQL
- SQL Server

## 配置示例

### pyproject.toml
```toml
[project]
name = "database-mcp-app"
version = "1.0.0"
description = "数据库操作 MCP 应用"
dependencies = [
    "fastmcp>=2.0.0",
    "sqlalchemy>=2.0.0",
    "alembic>=1.13.0",
    "pydantic>=2.8.0",
    "python-dotenv>=1.0.0",
]

[project.optional-dependencies]
postgres = ["asyncpg>=0.29.0"]
mysql = ["aiomysql>=0.2.0"]
mssql = ["aioodbc>=0.5.0"]
dev = [
    "pytest>=8.0.0",
    "pytest-asyncio>=0.24.0",
    "pytest-sqlalchemy>=0.22.0",
    "ruff>=0.6.0",
    "mypy>=1.11.0",
]
```

### 数据库配置
```json
{
  "default": "sqlite",
  "connections": {
    "sqlite": {
      "url": "sqlite+aiosqlite:///./data.db",
      "echo": false,
      "pool_pre_ping": true
    },
    "postgresql": {
      "url": "postgresql+asyncpg://user:password@localhost:5432/dbname",
      "echo": false,
      "pool_size": 10,
      "max_overflow": 20
    },
    "mysql": {
      "url": "mysql+aiomysql://user:password@localhost:3306/dbname",
      "echo": false,
      "pool_size": 10,
      "max_overflow": 20
    }
  },
  "security": {
    "allowed_operations": ["SELECT", "SHOW", "DESCRIBE", "EXPLAIN"],
    "max_query_time": 30,
    "max_result_rows": 10000,
    "forbidden_keywords": [
      "DROP", "DELETE", "UPDATE", "INSERT", "CREATE",
      "ALTER", "TRUNCATE", "EXEC", "EXECUTE", "UNION",
      "GRANT", "REVOKE", "COMMIT", "ROLLBACK"
    ]
  }
}
```

### 环境变量
```bash
# 数据库配置
DATABASE_URL=sqlite+aiosqlite:///./data.db
DATABASE_TYPE=sqlite

# 安全配置
DB_MAX_QUERY_TIME=30
DB_MAX_RESULT_ROWS=10000
DB_ENABLE_QUERY_LOG=true

# 连接配置
DB_POOL_SIZE=10
DB_MAX_OVERFLOW=20
DB_POOL_RECYCLE=3600
```