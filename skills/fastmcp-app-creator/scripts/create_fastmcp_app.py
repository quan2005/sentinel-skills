#!/usr/bin/env python3
"""
FastMCP App Creator - 基于 FastMCP 2.x 和 uv 的现代化 MCP 应用生成器

该脚本通过命令行参数接收所有需求信息，创建符合规范的 MCP 应用。
"""

import json
import sys
import argparse
from pathlib import Path
from typing import Dict, List, Any, Optional
from dataclasses import dataclass
import logging

# 配置日志
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


@dataclass
class MCPAppConfig:
    """MCP 应用配置"""
    name: str
    description: str
    background: str
    scenarios: str
    instructions: str
    trigger_conditions: str
    limitations: str
    usage_examples: List[str]
    tools: List[Dict[str, Any]]
    access_url: str
    headers: Dict[str, str]
    author: str = "Developer"
    version: str = "1.0.0"
    python_version: str = "3.11"


class FastMCPAppCreator:
    """FastMCP 应用创建器"""

    def __init__(self):
        self.templates_dir = Path(__file__).parent.parent / "assets" / "templates"
        self.templates_dir.mkdir(parents=True, exist_ok=True)

    def create_mcp_app(self, config: MCPAppConfig, output_dir: Path) -> bool:
        """创建 MCP 应用"""
        try:
            logger.info(f"开始创建 MCP 应用: {config.name}")

            # 创建项目目录结构
            project_dir = output_dir / config.name
            self._create_project_structure(project_dir, config)

            # 生成主应用文件
            self._create_main_app(project_dir, config)

            # 生成工具文件
            self._create_tools(project_dir, config)

            # 生成配置文件
            self._create_config_files(project_dir, config)

            # 生成 uv 配置
            self._create_uv_config(project_dir, config)

            logger.info(f"✅ MCP 应用 '{config.name}' 创建成功!")
            logger.info(f"📍 位置: {project_dir}")
            logger.info(f"🚀 启动命令: uv run {config.name}-server")

            return True

        except Exception as e:
            logger.error(f"❌ 创建 MCP 应用失败: {e}")
            return False

    def _create_project_structure(self, project_dir: Path, config: MCPAppConfig):
        """创建项目目录结构"""
        directories = [
            "src",
            f"src/{config.name}",
            "tests",
            "config"
        ]

        for directory in directories:
            dir_path = project_dir / directory
            dir_path.mkdir(parents=True, exist_ok=True)
            if "src" in directory:
                (dir_path / "__init__.py").touch()

    def _create_main_app(self, project_dir: Path, config: MCPAppConfig):
        """创建主应用文件"""
        main_content = f'''"""
{config.name} - {config.background}

{config.scenarios}
"""

from fastmcp import FastMCP
from fastmcp.types import TextContent
import logging
import sys
from typing import Any, Dict, List, Optional
import json

# 配置日志
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# 初始化 FastMCP 服务器
mcp = FastMCP(
    name="{config.name}",
    version="{config.version}",
    description="{config.description}",
)

# MCP Instructions
"""
{config.instructions}

### 触发条件 / 使用场景
{config.trigger_conditions}

### 不适用场景 / 限制
{config.limitations}

### 使用示例
{chr(10).join(f"- {example}" for example in config.usage_examples) if config.usage_examples else "- 基本使用示例"}
"""

@mcp.tool()
def ping() -> str:
    """测试 MCP 服务器连接性。

    Returns:
        pong 响应，验证服务器工作正常
    """
    logger.info("Ping 工具被调用")
    return "pong!"

@mcp.tool()
def server_info() -> Dict[str, Any]:
    """获取 MCP 服务器信息。

    Returns:
        包含服务器元数据和状态的字典
    """
    logger.info("服务器信息工具被调用")
    return {{
        "name": "{config.name}",
        "version": "{config.version}",
        "description": "{config.description}",
        "python_version": sys.version,
        "status": "running"
    }}

@mcp.resource("config://server")
def get_server_config() -> str:
    """获取服务器配置。

    Returns:
        服务器配置的 JSON 字符串
    """
    config_data = {{
        "name": "{config.name}",
        "version": "{config.version}",
        "description": "{config.description}",
        "background": "{config.background}",
        "scenarios": "{config.scenarios}",
        "access_url": "{config.access_url}",
        "tools_count": {len(config.tools)}
    }}
    return json.dumps(config_data, indent=2, ensure_ascii=False)

def main():
    """MCP 服务器主入口点"""
    logger.info(f"启动 {config.name} MCP 服务器...")
    try:
        mcp.run()
    except KeyboardInterrupt:
        logger.info("用户停止服务器")
    except Exception as e:
        logger.error(f"服务器错误: {{e}}")
        sys.exit(1)

if __name__ == "__main__":
    main()
'''

        main_path = project_dir / "src" / config.name / "server.py"
        with open(main_path, 'w', encoding='utf-8') as f:
            f.write(main_content)

    def _create_tools(self, project_dir: Path, config: MCPAppConfig):
        """创建工具文件"""
        if not config.tools:
            return

        tools_content = f'''"""
{config.name} 的自定义工具

{config.scenarios}
"""

from fastmcp import FastMCP
from fastmcp.types import TextContent
import logging
import sys
from typing import Any, Dict, List, Optional
import json

logger = logging.getLogger(__name__)

def register_tools(mcp: FastMCP):
    """注册所有自定义工具到 MCP 服务器"""

'''

        # 为每个工具生成代码
        for tool in config.tools:
            tool_name = tool["name"]
            tool_desc = tool["description"]
            params = tool.get("parameters", [])

            # 生成函数参数
            param_strs = []
            doc_params = []
            for param in params:
                param_name = param["name"]
                param_type = param["type"]

                # 类型映射
                type_map = {
                    "字符串": "str",
                    "string": "str",
                    "数字": "int",
                    "int": "int",
                    "整数": "int",
                    "浮点数": "float",
                    "float": "float",
                    "布尔": "bool",
                    "boolean": "bool",
                    "列表": "List[str]",
                    "list": "List[str]",
                    "字典": "Dict[str, Any]",
                    "dict": "Dict[str, Any]"
                }

                python_type = type_map.get(param_type.lower(), "str")

                # 添加默认值
                default_value = ""
                if param_type.lower() in ["字符串", "string"]:
                    default_value = ' = ""'
                elif param_type.lower() in ["数字", "int", "整数"]:
                    default_value = " = 0"
                elif param_type.lower() in ["布尔", "boolean", "bool"]:
                    default_value = " = False"
                elif param_type.lower() in ["列表", "list"]:
                    default_value = " = []"
                elif param_type.lower() in ["字典", "dict"]:
                    default_value = " = {}"

                param_strs.append(f"{param_name}: {python_type}{default_value}")
                doc_params.append(f"        {param_name} ({python_type}): {param_name}参数说明")

            params_str = ", ".join(param_strs)
            doc_params_str = "\n".join(doc_params) if doc_params else "        无参数"

            tools_content += f'''    @mcp.tool()
    def {tool_name}({params_str}) -> Dict[str, Any]:
        """{tool_desc}

        Args:
{doc_params_str}

        Returns:
            工具执行结果
        """
        logger.info(f"调用 {tool_name} 工具")

        try:
            # TODO: 实现具体的工具逻辑
            result = {{
                "status": "success",
                "message": "{tool_name} 工具执行成功",
                "data": {{
                    # TODO: 添加具体返回数据
                }}
            }}

            logger.info(f"{tool_name} 工具执行完成")
            return result

        except Exception as e:
            logger.error(f"{tool_name} 工具执行错误: {{e}}")
            return {{
                "status": "error",
                "message": str(e),
                "error": True
            }}

'''

        # 在主文件中导入工具
        tools_content += '''
# 注册工具到主服务器
from .server import mcp
register_tools(mcp)
'''

        tools_path = project_dir / "src" / config.name / "tools.py"
        with open(tools_path, 'w', encoding='utf-8') as f:
            f.write(tools_content)

    def _create_config_files(self, project_dir: Path, config: MCPAppConfig):
        """创建配置文件"""

        # MCP 配置文件
        mcp_config = {
            "mcpServers": {
                config.name: {
                    "type": "streamableHttp",
                    "url": config.access_url,
                    "headers": config.headers
                }
            }
        }

        config_path = project_dir / "config" / "mcp_config.json"
        with open(config_path, 'w', encoding='utf-8') as f:
            json.dump(mcp_config, f, indent=2, ensure_ascii=False)

        # 环境配置文件
        env_content = f'''# {config.name} 环境配置
# 复制此文件为 .env 并填入实际值

# 服务器配置
SERVER_HOST=localhost
SERVER_PORT=8000
DEBUG=false

# 认证配置
USER_AGENT_TOKEN=your_user_agent_token_here
CONTEXT_ID=your_context_id_here

# API 端点
API_BASE_URL={config.access_url}

# 日志配置
LOG_LEVEL=INFO
LOG_FILE=logs/{config.name}.log
'''

        env_path = project_dir / ".env.example"
        with open(env_path, 'w', encoding='utf-8') as f:
            f.write(env_content)

    def _create_uv_config(self, project_dir: Path, config: MCPAppConfig):
        """创建 uv 配置文件 (pyproject.toml)"""

        dependencies = [
            f"fastmcp>=2.0.0",
            "pydantic>=2.0.0",
            "python-dotenv>=1.0.0"
        ]

        dev_dependencies = [
            "pytest>=8.0.0",
            "pytest-asyncio>=0.24.0",
            "ruff>=0.6.0",
            "mypy>=1.11.0"
        ]

        pyproject_content = f'''[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"

[project]
name = "{config.name}"
version = "{config.version}"
description = "{config.description}"
authors = [
    {{name = "{config.author}", email = "dev@example.com"}},
]
license = {{text = "MIT"}}
readme = "README.md"
requires-python = ">={config.python_version}"
classifiers = [
    "Development Status :: 4 - Beta",
    "Intended Audience :: Developers",
    "License :: OSI Approved :: MIT License",
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3.{config.python_version.split('.')[1]}",
    "Programming Language :: Python :: 3 :: Only",
]
dependencies = {json.dumps(dependencies, indent=4)}

[project.optional-dependencies]
dev = {json.dumps(dev_dependencies, indent=4)}

[project.scripts]
{config.name}-server = "{config.name}.server:main"

[project.urls]
Homepage = "https://github.com/username/{config.name}"
Repository = "https://github.com/username/{config.name}.git"

[tool.hatch.build.targets.wheel]
packages = ["src/{config.name}"]

[tool.ruff]
target-version = "py{config.python_version.replace('.', '')}"
line-length = 88
select = ["E", "F", "W", "I", "N", "UP", "B", "A", "C4", "DTZ", "T20", "SIM", "PTH", "PLC", "PLE", "PLR", "PLW"]
ignore = ["E501", "PLR0913"]

[tool.ruff.format]
quote-style = "double"
indent-style = "space"

[tool.mypy]
python_version = "{config.python_version}"
warn_return_any = true
warn_unused_configs = true
disallow_untyped_defs = true
disallow_incomplete_defs = true

[tool.pytest.ini_options]
asyncio_mode = "auto"
testpaths = ["tests"]
python_files = ["test_*.py", "*_test.py"]
'''

        pyproject_path = project_dir / "pyproject.toml"
        with open(pyproject_path, 'w', encoding='utf-8') as f:
            f.write(pyproject_content)

        # 创建 README.md
        readme_content = f'''# {config.name}

{config.background}

## 场景

{config.scenarios}

## 安装和运行

### 使用 uv (推荐)

```bash
cd {config.name}
uv sync
uv run {config.name}-server
```

### 使用 pip

```bash
pip install -e .
{config.name}-server
```

## MCP Instructions

{config.instructions}

### 触发条件 / 使用场景
{config.trigger_conditions}

### 不适用场景 / 限制
{config.limitations}

### 使用示例
{chr(10).join(f"- {example}" for example in config.usage_examples) if config.usage_examples else "- 基本使用示例"}

## 可用工具

{"\\n".join(f"- `{tool['name']}()`: {tool['description']}" for tool in config.tools) if config.tools else "- `ping()`: 测试连接性"}

## 配置

1. 复制 `.env.example` 为 `.env`
2. 填入实际的配置值
3. 根据需要修改 `config/mcp_config.json`

## Claude Desktop 配置

在 Claude Desktop 配置中添加：

```json
{{
  "mcpServers": {{
    "{config.name}": {{
      "command": "uv",
      "args": ["run", "{config.name}-server"],
      "cwd": "{project_dir.absolute()}"
    }}
  }}
}}
```

## 开发

```bash
# 运行测试
uv run pytest

# 代码检查
uv run ruff check .
uv run mypy src/

# 格式化代码
uv run ruff format .
```

## 许可证

MIT License
'''

        readme_path = project_dir / "README.md"
        with open(readme_path, 'w', encoding='utf-8') as f:
            f.write(readme_content)


def parse_tools_input(tools_input: str) -> List[Dict[str, Any]]:
    """解析工具输入字符串"""
    tools = []

    if not tools_input.strip():
        return tools

    # 简单的解析格式：name:description:param1:type1,param2:type2
    for tool_line in tools_input.strip().split(';'):
        if not tool_line.strip():
            continue

        parts = tool_line.strip().split(':', 2)
        if len(parts) < 2:
            continue

        tool_name = parts[0].strip()
        tool_desc = parts[1].strip()

        # 解析参数
        params = []
        if len(parts) > 2 and parts[2].strip():
            param_str = parts[2].strip()
            for param_part in param_str.split(','):
                if ':' in param_part:
                    param_name, param_type = param_part.split(':', 1)
                    params.append({
                        "name": param_name.strip(),
                        "type": param_type.strip()
                    })

        tools.append({
            "name": tool_name,
            "description": tool_desc,
            "parameters": params
        })

    return tools


def main():
    """主函数 - 命令行接口"""
    parser = argparse.ArgumentParser(
        description="FastMCP App Creator - 创建符合规范的 MCP 应用",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
示例用法:
  # 基本用法
  python3 create_fastmcp_app.py \\
    --name knowledge-base \\
    --description "知识库查询应用" \\
    --background "企业内部知识库查询需求" \\
    --scenarios "员工快速查找公司文档和政策" \\
    --instructions "知识库查询助手..." \\
    --trigger-conditions "用户询问公司政策时" \\
    --limitations "不支持实时数据查询" \\
    --usage-examples "公司的请假政策是什么？" \\
    --tools "search_docs:搜索知识库文档:query:字符串,limit:数字" \\
    --access-url "https://api.company.com/mcp/knowledge-base" \\
    --headers "Authorization:Bearer <USER_AGENT_TOKEN>;x-context-id:<context_id>"

  # 多个工具
  python3 create_fastmcp_app.py \\
    --name file-processor \\
    --description "文件处理应用" \\
    ... \\
    --tools "read_file:读取文件:path:字符串;write_file:写入文件:path:字符串,content:字符串;list_files:列出文件:directory:字符串"
        """
    )

    # 基本信息
    parser.add_argument("--name", required=True, help="MCP 应用名称")
    parser.add_argument("--description", required=True, help="应用描述")
    parser.add_argument("--background", required=True, help="应用背景")
    parser.add_argument("--scenarios", required=True, help="应用场景")
    parser.add_argument("--instructions", required=True, help="MCP Instructions 引导提示词")
    parser.add_argument("--trigger-conditions", required=True, help="触发条件 / 使用场景")
    parser.add_argument("--limitations", required=True, help="不适用场景 / 限制")

    # 配置信息
    parser.add_argument("--access-url", required=True, help="MCP 接入 URL")
    parser.add_argument("--headers", required=True, help="请求头，格式：'Header1:Value1;Header2:Value2'")

    # 可选信息
    parser.add_argument("--usage-examples", help="使用示例，多个用分号分隔")
    parser.add_argument("--tools", help="工具定义，格式：'name:description:param1:type1,param2:type2;name2:...'")
    parser.add_argument("--author", default="Developer", help="作者")
    parser.add_argument("--version", default="1.0.0", help="版本")
    parser.add_argument("--python-version", default="3.11", help="Python 版本")
    parser.add_argument("-o", "--output", default="./output", help="输出目录")

    args = parser.parse_args()

    # 解析使用示例
    usage_examples = []
    if args.usage_examples:
        usage_examples = [ex.strip() for ex in args.usage_examples.split(';') if ex.strip()]

    # 解析工具定义
    tools = parse_tools_input(args.tools)

    # 解析请求头
    headers = {}
    if args.headers:
        for header_part in args.headers.split(';'):
            if ':' in header_part:
                key, value = header_part.split(':', 1)
                headers[key.strip()] = value.strip()

    # 创建配置
    config = MCPAppConfig(
        name=args.name,
        description=args.description,
        background=args.background,
        scenarios=args.scenarios,
        instructions=args.instructions,
        trigger_conditions=args.trigger_conditions,
        limitations=args.limitations,
        usage_examples=usage_examples,
        tools=tools,
        access_url=args.access_url,
        headers=headers,
        author=args.author,
        version=args.version,
        python_version=args.python_version
    )

    # 创建输出目录
    output_dir = Path(args.output)
    output_dir.mkdir(parents=True, exist_ok=True)

    # 创建 MCP 应用
    creator = FastMCPAppCreator()

    print(f"🎯 正在创建 MCP 应用: {config.name}")
    print(f"📋 配置 {len(config.tools)} 个工具")
    print(f"🌐 接入地址: {config.access_url}")

    success = creator.create_mcp_app(config, output_dir)

    if success:
        print(f"🎉 MCP 应用创建完成!")
        print(f"📁 输出目录: {output_dir / config.name}")
        print(f"📖 请查看 README.md 了解使用方法")
        print(f"🚀 启动命令: uv run {config.name}-server")
    else:
        print(f"❌ MCP 应用创建失败")

    return success


if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)