# FastMCP 2.x 模式和最佳实践

## FastMCP 2.x 核心概念

### 装饰器模式

FastMCP 2.x 使用装饰器来定义服务器组件：

#### @mcp.tool() - 工具定义
```python
from fastmcp import FastMCP

mcp = FastMCP("my-server")

@mcp.tool()
def calculate_sum(a: int, b: int) -> int:
    """计算两个数的和。

    Args:
        a: 第一个数
        b: 第二个数

    Returns:
        两数之和
    """
    return a + b
```

#### @mcp.resource() - 资源定义
```python
@mcp.resource("config://server")
def get_server_config() -> str:
    """获取服务器配置资源。"""
    return json.dumps(config_data, indent=2)
```

#### @mcp.prompt() - 提示词定义
```python
@mcp.prompt("help")
def get_help_prompt() -> str:
    """获取帮助提示词。"""
    return "这是服务器的帮助信息..."
```

### 类型注解要求

FastMCP 2.x 强制要求使用类型注解：

```python
# ✅ 正确：使用类型注解
@mcp.tool()
def process_data(data: List[str], count: int = 1) -> Dict[str, Any]:
    return {"processed": data[:count]}

# ❌ 错误：缺少类型注解
@mcp.tool()
def process_data(data, count=1):
    return {"processed": data[:count]}
```

### 服务器初始化模式

```python
from fastmcp import FastMCP
import logging

# 配置日志
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# 初始化服务器
mcp = FastMCP(
    name="my-server",
    version="1.0.0",
    description="服务器描述",
)

def main():
    """主入口点"""
    logger.info("启动 MCP 服务器...")
    try:
        mcp.run()
    except KeyboardInterrupt:
        logger.info("服务器停止")
    except Exception as e:
        logger.error(f"服务器错误: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
```

## 常见工具模式

### 1. HTTP API 工具模式

```python
import httpx
from fastmcp import FastMCP
from typing import Dict, Any, Optional

mcp = FastMCP("api-client")

@mcp.tool()
def http_get(url: str, headers: Optional[Dict[str, str]] = None) -> Dict[str, Any]:
    """执行 HTTP GET 请求。

    Args:
        url: 请求的 URL
        headers: 可选的请求头

    Returns:
        包含状态码、头部和内容的响应数据
    """
    try:
        with httpx.Client() as client:
            response = client.get(url, headers=headers or {})
            response.raise_for_status()

            return {
                "status_code": response.status_code,
                "headers": dict(response.headers),
                "content": response.text,
                "url": str(response.url)
            }
    except httpx.HTTPError as e:
        logger.error(f"HTTP 错误: {e}")
        return {"error": str(e), "status_code": "error"}
```

### 2. 数据库工具模式

```python
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from sqlalchemy import text
from typing import List, Dict, Any

mcp = FastMCP("database-client")

# 数据库配置
DATABASE_URL = "sqlite+aiosqlite:///./data.db"

engine = create_async_engine(DATABASE_URL)
async_session = sessionmaker(engine, class_=AsyncSession)

@mcp.tool()
async def execute_query(query: str) -> List[Dict[str, Any]]:
    """执行 SQL 查询。

    Args:
        query: SQL 查询语句（仅允许 SELECT）

    Returns:
        查询结果行列表
    """
    if not query.strip().upper().startswith('SELECT'):
        raise ValueError("为安全起见，仅允许 SELECT 查询")

    try:
        async with async_session() as session:
            result = await session.execute(text(query))
            rows = result.fetchall()

            columns = result.keys()
            return [dict(zip(columns, row)) for row in rows]
    except Exception as e:
        logger.error(f"数据库错误: {e}")
        return [{"error": str(e)}]
```

### 3. 文件处理工具模式

```python
from pathlib import Path
from fastmcp.types import TextContent, ImageContent
from PIL import Image
import pandas as pd

mcp = FastMCP("file-processor")

@mcp.tool()
def read_text_file(file_path: str) -> str:
    """读取文本文件内容。

    Args:
        file_path: 文件路径

    Returns:
        文件内容
    """
    path = Path(file_path)
    if not path.exists():
        return f"错误: 文件不存在 - {file_path}"

    if path.stat().st_size > 1024 * 1024:  # 1MB 限制
        return "错误: 文件过大（最大 1MB）"

    with open(path, 'r', encoding='utf-8') as f:
        return f.read()

@mcp.tool()
def process_image(image_path: str, operation: str, **kwargs) -> Dict[str, Any]:
    """处理图像文件。

    Args:
        image_path: 图像文件路径
        operation: 操作类型（resize, rotate, grayscale）
        **kwargs: 操作特定参数

    Returns:
        处理结果信息
    """
    path = Path(image_path)
    if not path.exists():
        return {"error": f"图像文件不存在: {image_path}"}

    try:
        with Image.open(path) as img:
            if operation == "resize":
                width = kwargs.get("width", img.width)
                height = kwargs.get("height", img.height)
                resized = img.resize((width, height))

                output_path = path.parent / f"resized_{path.name}"
                resized.save(output_path)
                return {"message": f"图像已调整大小并保存至 {output_path}", "new_size": resized.size}

            elif operation == "grayscale":
                grayscale = img.convert('L')
                output_path = path.parent / f"grayscale_{path.name}"
                grayscale.save(output_path)
                return {"message": f"图像已转换为灰度并保存至 {output_path}"}

            else:
                return {"error": f"不支持的操作: {operation}"}

    except Exception as e:
        logger.error(f"图像处理错误: {e}")
        return {"error": str(e)}
```

## 错误处理模式

### 统一错误响应格式

```python
@mcp.tool()
def risky_operation(data: str) -> Dict[str, Any]:
    """可能失败的操作示例。"""
    try:
        # 业务逻辑
        if not data:
            raise ValueError("数据不能为空")

        result = process_data(data)

        return {
            "status": "success",
            "data": result,
            "message": "操作成功完成"
        }

    except ValueError as e:
        logger.warning(f"参数错误: {e}")
        return {
            "status": "error",
            "error_type": "validation_error",
            "message": str(e),
            "code": "INVALID_INPUT"
        }

    except Exception as e:
        logger.error(f"未预期错误: {e}")
        return {
            "status": "error",
            "error_type": "internal_error",
            "message": "服务器内部错误",
            "code": "INTERNAL_ERROR"
        }
```

### 日志记录模式

```python
import logging

# 配置结构化日志
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

@mcp.tool()
def log_example(data: str) -> str:
    """展示日志记录最佳实践。"""
    logger.info(f"开始处理数据，长度: {len(data)}")

    try:
        result = process_data(data)
        logger.info(f"数据处理成功，结果长度: {len(result)}")
        return result

    except Exception as e:
        logger.error(f"数据处理失败: {e}", exc_info=True)
        raise
```

## 配置管理模式

### 环境变量配置

```python
import os
from dotenv import load_dotenv
from typing import Optional

# 加载环境变量
load_dotenv()

class Config:
    """配置类"""
    SERVER_HOST: str = os.getenv("SERVER_HOST", "localhost")
    SERVER_PORT: int = int(os.getenv("SERVER_PORT", "8000"))
    DEBUG: bool = os.getenv("DEBUG", "false").lower() == "true"

    # API 配置
    API_BASE_URL: str = os.getenv("API_BASE_URL", "https://api.example.com")
    API_TOKEN: Optional[str] = os.getenv("API_TOKEN")

    # 数据库配置
    DATABASE_URL: str = os.getenv("DATABASE_URL", "sqlite:///data.db")

# 全局配置实例
config = Config()

@mcp.resource("config://app")
def get_app_config() -> str:
    """获取应用配置。"""
    return json.dumps({
        "server": {
            "host": config.SERVER_HOST,
            "port": config.SERVER_PORT,
            "debug": config.DEBUG
        },
        "api": {
            "base_url": config.API_BASE_URL,
            "has_token": bool(config.API_TOKEN)
        }
    }, indent=2)
```

## 测试模式

### pytest 测试模板

```python
import pytest
import asyncio
from my_server import mcp

class TestBasicTools:
    """基础工具测试类"""

    @pytest.mark.asyncio
    async def test_ping(self):
        """测试 ping 工具"""
        result = await mcp.call_tool("ping", {})
        assert result == "pong"

    @pytest.mark.asyncio
    async def test_tool_with_params(self):
        """测试带参数的工具"""
        result = await mcp.call_tool("calculate_sum", {
            "a": 5,
            "b": 3
        })
        assert result == 8

    @pytest.mark.asyncio
    async def test_error_handling(self):
        """测试错误处理"""
        result = await mcp.call_tool("risky_operation", {
            "data": ""  # 空数据应该触发错误
        })
        assert result["status"] == "error"
        assert "INVALID_INPUT" in result.get("code", "")

class TestResources:
    """资源测试类"""

    @pytest.mark.asyncio
    async def test_server_config(self):
        """测试服务器配置资源"""
        result = await mcp.read_resource("config://server")
        assert isinstance(result, str)
        assert "name" in result

class TestPrompts:
    """提示词测试类"""

    @pytest.mark.asyncio
    async def test_help_prompt(self):
        """测试帮助提示词"""
        result = await mcp.get_prompt("help", {})
        assert isinstance(result, str)
        assert len(result) > 0
```

## 部署配置模式

### streamableHttp 配置

```json
{
  "mcpServers": {
    "my-app": {
      "type": "streamableHttp",
      "url": "https://api.example.com/mcp",
      "headers": {
        "Authorization": "Bearer <USER_AGENT_TOKEN>",
        "x-context-id": "<context_id>",
        "Content-Type": "application/json"
      }
    }
  }
}
```

### Docker 部署配置

```dockerfile
FROM python:3.11-slim

WORKDIR /app

# 安装 uv
COPY --from=ghcr.io/astral-sh/uv:latest /uv /bin/uv

# 复制项目文件
COPY pyproject.toml .
COPY src/ ./src/

# 安装依赖
RUN uv sync --frozen

# 暴露端口
EXPOSE 8000

# 启动命令
CMD ["uv", "run", "my-app-server"]
```

## 性能优化模式

### 异步工具模式

```python
import asyncio
import aiohttp
from fastmcp import FastMCP

mcp = FastMCP("async-server")

@mcp.tool()
async def fetch_multiple_urls(urls: List[str]) -> List[Dict[str, Any]]:
    """并发获取多个 URL。

    Args:
        urls: URL 列表

    Returns:
        每个 URL 的响应结果
    """
    async with aiohttp.ClientSession() as session:
        tasks = []
        for url in urls:
            task = fetch_single_url(session, url)
            tasks.append(task)

        results = await asyncio.gather(*tasks, return_exceptions=True)

        return [
            {
                "url": url,
                "success": not isinstance(result, Exception),
                "data": result if not isinstance(result, Exception) else str(result)
            }
            for url, result in zip(urls, results)
        ]

async def fetch_single_url(session, url):
    """获取单个 URL 的辅助函数"""
    async with session.get(url) as response:
        return await response.text()
```

### 缓存模式

```python
from functools import lru_cache
import time
from typing import Dict, Any

# 内存缓存
_cache: Dict[str, Dict[str, Any]] = {}

@mcp.tool()
def cached_api_call(endpoint: str, ttl: int = 300) -> Dict[str, Any]:
    """带缓存的 API 调用。

    Args:
        endpoint: API 端点
        ttl: 缓存生存时间（秒）

    Returns:
        API 响应数据
    """
    now = time.time()
    cache_key = endpoint

    # 检查缓存
    if cache_key in _cache:
        cache_entry = _cache[cache_key]
        if now - cache_entry["timestamp"] < ttl:
            logger.info(f"从缓存返回结果: {endpoint}")
            return cache_entry["data"]

    # 执行 API 调用
    logger.info(f"执行 API 调用: {endpoint}")
    result = call_api(endpoint)

    # 存入缓存
    _cache[cache_key] = {
        "data": result,
        "timestamp": now
    }

    return result

@lru_cache(maxsize=128)
def cpu_intensive_calculation(param1: int, param2: int) -> int:
    """CPU 密集型计算，使用 LRU 缓存。"""
    # 复杂计算逻辑
    return expensive_computation(param1, param2)
```

## 安全模式

### 输入验证模式

```python
import re
from typing import List

def validate_sql_query(query: str) -> bool:
    """验证 SQL 查询安全性"""
    # 只允许 SELECT, SHOW, DESCRIBE
    allowed_patterns = [
        r'^SELECT\s+.+\s+FROM\s+.+$',
        r'^SHOW\s+.+$',
        r'^DESCRIBE\s+.+$'
    ]

    query_upper = query.strip().upper()

    for pattern in allowed_patterns:
        if re.match(pattern, query_upper):
            return True

    # 检查危险关键词
    dangerous_keywords = [
        'DROP', 'DELETE', 'UPDATE', 'INSERT', 'CREATE',
        'ALTER', 'TRUNCATE', 'EXEC', 'EXECUTE', 'UNION'
    ]

    for keyword in dangerous_keywords:
        if keyword in query_upper:
            return False

    return True

def validate_file_path(file_path: str) -> bool:
    """验证文件路径安全性"""
    path = Path(file_path)

    # 防止路径遍历攻击
    try:
        path.resolve().relative_to(Path.cwd())
        return True
    except ValueError:
        return False
```

### 认证和授权模式

```python
import jwt
import hashlib
from typing import Optional, Dict, Any

def verify_token(token: str, secret_key: str) -> Optional[Dict[str, Any]]:
    """验证 JWT 令牌"""
    try:
        payload = jwt.decode(token, secret_key, algorithms=["HS256"])
        return payload
    except jwt.InvalidTokenError:
        return None

def check_permission(user_id: str, resource: str, action: str) -> bool:
    """检查用户权限"""
    # 实现权限检查逻辑
    permissions = load_user_permissions(user_id)
    return f"{resource}:{action}" in permissions

@mcp.tool()
def protected_operation(user_token: str, data: str) -> Dict[str, Any]:
    """需要认证的操作"""
    # 验证令牌
    payload = verify_token(user_token, SECRET_KEY)
    if not payload:
        return {"error": "认证失败", "code": "AUTH_ERROR"}

    user_id = payload.get("user_id")

    # 检查权限
    if not check_permission(user_id, "protected_operation", "execute"):
        return {"error": "权限不足", "code": "PERMISSION_DENIED"}

    # 执行操作
    result = execute_protected_operation(data)

    return {
        "status": "success",
        "data": result,
        "user_id": user_id
    }
```