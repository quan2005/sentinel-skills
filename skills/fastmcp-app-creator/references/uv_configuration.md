# uv 配置和最佳实践

## uv 简介

uv 是一个用 Rust 编写的极速 Python 包和项目管理器，提供了比 pip 和 conda 更快的依赖管理和项目初始化能力。

## 基本配置

### pyproject.toml 结构

```toml
[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"

[project]
name = "my-mcp-app"
version = "1.0.0"
description = "我的 MCP 应用"
authors = [
    {name = "开发者", email = "dev@example.com"},
]
license = {text = "MIT"}
readme = "README.md"
requires-python = ">=3.11"
classifiers = [
    "Development Status :: 4 - Beta",
    "Intended Audience :: Developers",
    "License :: OSI Approved :: MIT License",
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3.11",
    "Programming Language :: Python :: 3 :: Only",
]
dependencies = [
    "fastmcp>=2.0.0",
    "pydantic>=2.0.0",
    "python-dotenv>=1.0.0",
]

[project.optional-dependencies]
dev = [
    "pytest>=8.0.0",
    "pytest-asyncio>=0.24.0",
    "ruff>=0.6.0",
    "mypy>=1.11.0",
    "black>=24.0.0",
]

[project.scripts]
my-app-server = "my_app.server:main"

[project.urls]
Homepage = "https://github.com/username/my-app"
Repository = "https://github.com/username/my-app.git"
Issues = "https://github.com/username/my-app/issues"

[tool.hatch.build.targets.wheel]
packages = ["src/my_app"]
```

### 开发工具配置

#### ruff (代码检查和格式化)

```toml
[tool.ruff]
target-version = "py311"
line-length = 88
select = [
    "E",      # pycodestyle errors
    "W",      # pycodestyle warnings
    "F",      # pyflakes
    "I",      # isort
    "N",      # pep8-naming
    "UP",     # pyupgrade
    "B",      # flake8-bugbear
    "A",      # flake8-builtins
    "C4",     # flake8-comprehensions
    "DTZ",    # flake8-datetimez
    "T20",    # flake8-print
    "SIM",    # flake8-simplify
    "PTH",    # flake8-use-pathlib
    "PLC",    # pylint convention
    "PLE",    # pylint error
    "PLR",    # pylint refactor
    "PLW",    # pylint warning
]
ignore = [
    "E501",   # line too long
    "PLR0913", # too many arguments
    "PLR0915", # too many statements
]

[tool.ruff.format]
quote-style = "double"
indent-style = "space"
skip-magic-trailing-comma = false

[tool.ruff.lint.isort]
known-first-party = ["my_app"]
```

#### mypy (类型检查)

```toml
[tool.mypy]
python_version = "3.11"
warn_return_any = true
warn_unused_configs = true
disallow_untyped_defs = true
disallow_incomplete_defs = true
check_untyped_defs = true
disallow_untyped_decorators = true
no_implicit_optional = true
warn_redundant_casts = true
warn_unused_ignores = true
warn_no_return = true
warn_unreachable = true
strict_equality = true

[[tool.mypy.overrides]]
module = [
    "fastmcp.*",
    "httpx.*",
    "sqlalchemy.*",
]
ignore_missing_imports = true
```

#### pytest (测试配置)

```toml
[tool.pytest.ini_options]
asyncio_mode = "auto"
testpaths = ["tests"]
python_files = ["test_*.py", "*_test.py"]
python_classes = ["Test*"]
python_functions = ["test_*"]
addopts = [
    "-v",
    "--tb=short",
    "--strict-markers",
    "--disable-warnings",
    "--cov=src",
    "--cov-report=term-missing",
    "--cov-report=html",
]
markers = [
    "slow: marks tests as slow (deselect with '-m \"not slow\"')",
    "integration: marks tests as integration tests",
    "unit: marks tests as unit tests",
]
```

## uv 命令参考

### 项目初始化

```bash
# 创建新项目
uv init my-mcp-app

# 创建带工作区的项目
uv init --workspace my-workspace

# 在现有目录中初始化
uv init
```

### 依赖管理

```bash
# 添加生产依赖
uv add fastmcp pydantic python-dotenv

# 添加开发依赖
uv add --dev pytest ruff mypy

# 添加特定版本
uv add "fastmcp>=2.0.0,<3.0.0"

# 从 requirements.txt 安装
uv pip install -r requirements.txt

# 更新依赖
uv lock --upgrade

# 移除依赖
uv remove package-name
```

### 虚拟环境管理

```bash
# 创建虚拟环境
uv venv

# 指定 Python 版本
uv venv --python 3.11

# 激活虚拟环境 (uv 会自动管理)
# 不需要手动激活，uv 会自动找到 venv

# 运行命令
uv run python script.py
uv run pytest
uv run my-app-server
```

### 脚本和命令

```bash
# 运行项目脚本
uv run my-app-server

# 运行测试
uv run pytest

# 代码检查
uv run ruff check .

# 代码格式化
uv run ruff format .

# 类型检查
uv run mypy src/

# 构建包
uv build

# 发布包
uv publish
```

## 环境配置

### .env 文件

```bash
# 服务器配置
SERVER_HOST=localhost
SERVER_PORT=8000
DEBUG=false

# API 配置
API_BASE_URL=https://api.example.com
API_TOKEN=your_token_here

# 数据库配置
DATABASE_URL=sqlite:///data.db

# 日志配置
LOG_LEVEL=INFO
LOG_FILE=logs/app.log
```

### 环境变量使用

```python
import os
from dotenv import load_dotenv

# 加载环境变量
load_dotenv()

class Config:
    SERVER_HOST: str = os.getenv("SERVER_HOST", "localhost")
    SERVER_PORT: int = int(os.getenv("SERVER_PORT", "8000"))
    DEBUG: bool = os.getenv("DEBUG", "false").lower() == "true"

    API_BASE_URL: str = os.getenv("API_BASE_URL")
    API_TOKEN: str = os.getenv("API_TOKEN")

    DATABASE_URL: str = os.getenv("DATABASE_URL", "sqlite:///data.db")
```

## 开发工作流

### 1. 项目设置

```bash
# 克隆项目
git clone https://github.com/username/my-mcp-app.git
cd my-mcp-app

# 安装依赖
uv sync

# 激活开发环境 (可选)
source .venv/bin/activate  # Linux/Mac
# 或
.venv\Scripts\activate     # Windows
```

### 2. 开发过程

```bash
# 启动开发服务器
uv run my-app-server

# 运行测试
uv run pytest

# 代码检查
uv run ruff check .
uv run mypy src/

# 修复代码问题
uv run ruff check --fix .
uv run ruff format .
```

### 3. 构建和部署

```bash
# 构建包
uv build

# 本地安装测试
uv pip install dist/my_mcp_app-1.0.0-py3-none-any.whl

# 发布到 PyPI
uv publish
```

## 性能优化

### 依赖优化

```toml
[project]
dependencies = [
    # 使用版本范围而不是固定版本
    "fastmcp>=2.0.0,<3.0.0",

    # 避免重复依赖
    "pydantic>=2.0.0",  # 如果 fastmcp 已经包含，可能不需要

    # 最小化依赖
    "python-dotenv>=1.0.0",
]

[tool.uv]
# uv 特定配置
prerelease = "disallow"
index-url = "https://pypi.org/simple"
```

### 构建优化

```toml
[tool.hatch.build.targets.wheel]
# 只包含必要的文件
packages = ["src/my_app"]
exclude = [
    "tests/",
    "docs/",
    "*.md",
    ".gitignore",
]

[tool.hatch.build]
# 构建时忽略的文件
artifacts = [
    "src/my_app/py.typed",
]
```

## 故障排除

### 常见问题

1. **依赖冲突**
```bash
# 查看依赖树
uv tree

# 解决冲突
uv add package==specific_version
```

2. **虚拟环境问题**
```bash
# 重新创建虚拟环境
rm -rf .venv
uv venv
uv sync
```

3. **缓存问题**
```bash
# 清除 uv 缓存
uv cache clean

# 重新安装
uv sync --refresh
```

4. **权限问题**
```bash
# 使用用户安装
uv pip install --user package

# 或修复权限
sudo chown -R $USER ~/.local
```

### 调试技巧

```bash
# 详细输出
uv --verbose sync

# 显示解析的依赖
uv lock --verbose

# 检查虚拟环境
uv venv --python python3.11

# 运行时显示详细信息
uv run --verbose python script.py
```

## 最佳实践

### 1. 依赖管理

- 使用版本范围而不是固定版本
- 定期更新依赖：`uv lock --upgrade`
- 在 CI/CD 中使用 `uv sync --frozen`

### 2. 项目结构

```
my-mcp-app/
├── pyproject.toml
├── README.md
├── .env.example
├── .gitignore
├── src/
│   └── my_app/
│       ├── __init__.py
│       ├── server.py
│       └── tools.py
├── tests/
│   ├── __init__.py
│   └── test_server.py
└── docs/
    └── usage.md
```

### 3. 开发配置

```bash
# 安装开发依赖
uv add --dev pytest ruff mypy black pre-commit

# 设置 pre-commit hooks
uv run pre-commit install
```

### 4. CI/CD 集成

```yaml
# .github/workflows/ci.yml
name: CI
on: [push, pull_request]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v4
    - name: Set up Python
      uses: actions/setup-python@v4
      with:
        python-version: '3.11'
    - name: Install uv
      uses: astral-sh/setup-uv@v1
    - name: Install dependencies
      run: uv sync --frozen
    - name: Run tests
      run: uv run pytest
    - name: Run linting
      run: uv run ruff check .
    - name: Run type checking
      run: uv run mypy src/
```