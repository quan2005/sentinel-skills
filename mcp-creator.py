#!/usr/bin/env python3
"""
MCP Creator Skill - Modern MCP Service Generator

Creates MCP (Model Context Protocol) services using FastMCP 2.x + uv framework.
This skill generates production-ready MCP servers with modern Python patterns.

Usage:
  python mcp-creator.py create <project-name> [options]
  python mcp-creator.py template <template-name>
  python mcp-creator.py add-tool <tool-name>

Examples:
  python mcp-creator.py create my-mcp-server --template=web-api
  python mcp-creator.py create database-proxy --template=database --postgres
  python mcp-creator.py add-tool file-uploader
"""

import os
import sys
import json
import argparse
import subprocess
from pathlib import Path
from typing import Dict, List, Any, Optional
from dataclasses import dataclass, asdict
from datetime import datetime


@dataclass
class MCPProjectConfig:
    """Configuration for MCP project creation"""
    name: str
    description: str
    author: str
    version: str = "0.1.0"
    python_version: str = "3.11"
    template: str = "basic"
    dependencies: List[str] = None
    dev_dependencies: List[str] = None
    features: List[str] = None
    fastmcp_version: str = "^2.0.0"

    def __post_init__(self):
        if self.dependencies is None:
            self.dependencies = []
        if self.dev_dependencies is None:
            self.dev_dependencies = []
        if self.features is None:
            self.features = []


class MCPCreator:
    """Main MCP service creator using FastMCP 2.x + uv patterns"""

    def __init__(self):
        self.templates_dir = Path(__file__).parent / "mcp-templates"
        self.templates_dir.mkdir(exist_ok=True)

    def create_project(self, config: MCPProjectConfig) -> bool:
        """Create a new MCP project with modern structure"""
        try:
            project_path = Path.cwd() / config.name
            if project_path.exists():
                print(f"❌ Directory '{config.name}' already exists")
                return False

            print(f"🚀 Creating MCP project: {config.name}")

            # Create project structure
            self._create_project_structure(project_path, config)

            # Generate pyproject.toml with uv build system
            self._create_pyproject_toml(project_path, config)

            # Generate main server file
            self._create_main_server(project_path, config)

            # Generate template-specific files
            self._apply_template(project_path, config)

            # Initialize uv project and install dependencies
            self._initialize_uv_project(project_path, config)

            # Create development files
            self._create_development_files(project_path, config)

            print(f"✅ MCP project '{config.name}' created successfully!")
            print(f"📁 Location: {project_path}")
            print(f"🎯 Next steps:")
            print(f"   cd {config.name}")
            print(f"   uv run mcp-server")

            return True

        except Exception as e:
            print(f"❌ Error creating project: {e}")
            return False

    def _create_project_structure(self, project_path: Path, config: MCPProjectConfig):
        """Create modern Python project structure"""
        directories = [
            config.name,
            f"{config.name}/src",
            f"{config.name}/src/{config.name}",
            f"{config.name}/tests",
            f"{config.name}/docs",
            f"{config.name}/examples",
            f"{config.name}/.github/workflows"
        ]

        for directory in directories:
            Path(directory).mkdir(parents=True, exist_ok=True)
            # Create __init__.py files for Python packages
            if "src" in directory and not directory.endswith("workflows"):
                (Path(directory) / "__init__.py").touch()

    def _create_pyproject_toml(self, project_path: Path, config: MCPProjectConfig):
        """Generate modern pyproject.toml for uv build system"""
        dependencies = [f"fastmcp{config.fastmcp_version}"] + config.dependencies
        dev_dependencies = [
            "pytest>=8.0.0",
            "pytest-asyncio>=0.24.0",
            "ruff>=0.6.0",
            "mypy>=1.11.0",
            "black>=24.0.0",
            "pre-commit>=3.8.0"
        ] + config.dev_dependencies

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

[project.urls]
Homepage = "https://github.com/username/{config.name}"
Documentation = "https://{config.name}.readthedocs.io/"
Repository = "https://github.com/username/{config.name}.git"
Issues = "https://github.com/username/{config.name}/issues"

[project.scripts]
{config.name}-server = "{config.name}.server:main"

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

        pyproject_path = project_path / "pyproject.toml"
        with open(pyproject_path, 'w') as f:
            f.write(pyproject_content)

    def _create_main_server(self, project_path: Path, config: MCPProjectConfig):
        """Create the main MCP server file with FastMCP 2.x patterns"""
        server_content = f'''"""
{config.name} - {config.description}

A modern MCP server built with FastMCP 2.x and uv.
"""

from fastmcp import FastMCP
from fastmcp.types import TextContent, ImageContent, AudioContent
import logging
import sys
from typing import Any, Dict, List, Optional

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Initialize FastMCP server
mcp = FastMCP(
    name="{config.name}",
    version="{config.version}",
    description="{config.description}",
)

@mcp.tool()
def ping() -> str:
    """Test connectivity with the MCP server.

    Returns:
        A simple pong response to verify the server is working.
    """
    logger.info("Ping tool called")
    return "pong!"

@mcp.tool()
def server_info() -> Dict[str, Any]:
    """Get information about the MCP server.

    Returns:
        Dictionary containing server metadata and status.
    """
    logger.info("Server info tool called")
    return {{
        "name": "{config.name}",
        "version": "{config.version}",
        "description": "{config.description}",
        "python_version": sys.version,
        "status": "running"
    }}

@mcp.tool()
def echo_message(message: str, repeat: int = 1) -> str:
    """Echo a message multiple times.

    Args:
        message: The message to echo
        repeat: Number of times to repeat the message (default: 1)

    Returns:
        The echoed message(s)
    """
    logger.info(f"Echo tool called with message: {{message}}, repeat: {{repeat}}")
    if repeat < 1:
        raise ValueError("Repeat count must be at least 1")

    return " ".join([message] * repeat)

@mcp.resource("config://server")
def get_server_config() -> str:
    """Get server configuration.

    Returns:
        Server configuration as JSON string.
    """
    config_data = {{
        "name": "{config.name}",
        "version": "{config.version}",
        "description": "{config.description}",
        "features": {json.dumps(config.features, indent=2)}
    }}
    return json.dumps(config_data, indent=2)

@mcp.prompt("help")
def get_help_prompt() -> str:
    """Get help information for using this MCP server.

    Returns:
        Help text for server usage.
    """
    return """
# {config.name} MCP Server Help

## Available Tools
- `ping()`: Test server connectivity
- `server_info()`: Get server information
- `echo_message(message, repeat=1)`: Echo a message

## Available Resources
- `config://server`: Server configuration

## Available Prompts
- `help`: This help message

## Usage Examples
1. Test connectivity: Call the `ping()` tool
2. Get server info: Call the `server_info()` tool
3. Echo a message: Call `echo_message("Hello, World!", 3)`

For more information, see the project documentation.
"""

def main():
    """Main entry point for the MCP server."""
    logger.info("Starting {config.name} MCP server...")
    try:
        mcp.run()
    except KeyboardInterrupt:
        logger.info("Server stopped by user")
    except Exception as e:
        logger.error(f"Server error: {{e}}")
        sys.exit(1)

if __name__ == "__main__":
    main()
'''

        server_path = project_path / "src" / config.name / "server.py"
        with open(server_path, 'w') as f:
            f.write(server_content)

    def _apply_template(self, project_path: Path, config: MCPProjectConfig):
        """Apply template-specific configurations and files"""
        if config.template == "web-api":
            self._apply_web_api_template(project_path, config)
        elif config.template == "database":
            self._apply_database_template(project_path, config)
        elif config.template == "file-processor":
            self._apply_file_processor_template(project_path, config)

    def _apply_web_api_template(self, project_path: Path, config: MCPProjectConfig):
        """Apply web API template with HTTP client tools"""
        # Add HTTP dependencies
        config.dependencies.extend(["httpx>=0.27.0", "pydantic>=2.8.0"])

        api_tools_content = f'''"""
Web API tools for {config.name}
"""

import httpx
from fastmcp import FastMCP
from fastmcp.types import TextContent
from typing import Dict, Any, Optional
import logging

logger = logging.getLogger(__name__)

def register_api_tools(mcp: FastMCP):
    """Register web API tools with the MCP server."""

    @mcp.tool()
    def http_get(url: str, headers: Optional[Dict[str, str]] = None) -> Dict[str, Any]:
        """Make an HTTP GET request.

        Args:
            url: The URL to request
            headers: Optional headers to include

        Returns:
            Response data with status, headers, and content
        """
        logger.info(f"Making GET request to: {{url}}")

        try:
            with httpx.Client() as client:
                response = client.get(url, headers=headers or {{}})
                response.raise_for_status()

                return {{
                    "status_code": response.status_code,
                    "headers": dict(response.headers),
                    "content": response.text,
                    "url": str(response.url)
                }}
        except httpx.HTTPError as e:
            logger.error(f"HTTP error: {{e}}")
            return {{"error": str(e), "status_code": "error"}}

    @mcp.tool()
    def http_post(url: str, data: Dict[str, Any], headers: Optional[Dict[str, str]] = None) -> Dict[str, Any]:
        """Make an HTTP POST request.

        Args:
            url: The URL to request
            data: JSON data to send
            headers: Optional headers to include

        Returns:
            Response data with status, headers, and content
        """
        logger.info(f"Making POST request to: {{url}}")

        try:
            with httpx.Client() as client:
                response = client.post(url, json=data, headers=headers or {{}})
                response.raise_for_status()

                return {{
                    "status_code": response.status_code,
                    "headers": dict(response.headers),
                    "content": response.text,
                    "url": str(response.url)
                }}
        except httpx.HTTPError as e:
            logger.error(f"HTTP error: {{e}}")
            return {{"error": str(e), "status_code": "error"}}

# Import and register tools in main server
from .server import mcp
register_api_tools(mcp)
'''

        api_tools_path = project_path / "src" / config.name / "api_tools.py"
        with open(api_tools_path, 'w') as f:
            f.write(api_tools_content)

    def _apply_database_template(self, project_path: Path, config: MCPProjectConfig):
        """Apply database template with DB connection tools"""
        # Add database dependencies
        config.dependencies.extend(["sqlalchemy>=2.0.0", "asyncpg>=0.29.0" if "postgres" in config.features else "aiosqlite>=0.20.0"])

        db_tools_content = f'''"""
Database tools for {config.name}
"""

from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from sqlalchemy import text
from fastmcp import FastMCP
from typing import Dict, Any, List, Optional
import logging

logger = logging.getLogger(__name__)

def register_db_tools(mcp: FastMCP):
    """Register database tools with the MCP server."""

    # Database connection (configure as needed)
    DATABASE_URL = "sqlite+aiosqlite:///./data.db"  # Change for PostgreSQL

    engine = create_async_engine(DATABASE_URL)
    async_session = sessionmaker(engine, class_=AsyncSession)

    @mcp.tool()
    async def execute_query(query: str) -> List[Dict[str, Any]]:
        """Execute a SQL query and return results.

        Args:
            query: SQL query to execute (SELECT statements only for safety)

        Returns:
            List of result rows as dictionaries
        """
        logger.info(f"Executing query: {{query[:100]}}...")

        if not query.strip().upper().startswith('SELECT'):
            raise ValueError("Only SELECT queries are allowed for safety")

        try:
            async with async_session() as session:
                result = await session.execute(text(query))
                rows = result.fetchall()

                # Convert to list of dictionaries
                columns = result.keys()
                return [dict(zip(columns, row)) for row in rows]

        except Exception as e:
            logger.error(f"Database error: {{e}}")
            return [{{"error": str(e)}}]

    @mcp.tool()
    async def get_table_schema(table_name: str) -> Dict[str, Any]:
        """Get schema information for a database table.

        Args:
            table_name: Name of the table to inspect

        Returns:
            Table schema information
        """
        logger.info(f"Getting schema for table: {{table_name}}")

        try:
            async with async_session() as session:
                # SQLite pragma for table info
                if "sqlite" in DATABASE_URL:
                    result = await session.execute(text(f"PRAGMA table_info({{table_name}})"))
                    columns = result.fetchall()

                    schema = {{
                        "table_name": table_name,
                        "columns": [
                            {{
                                "name": col[1],
                                "type": col[2],
                                "nullable": not col[3],
                                "primary_key": bool(col[5])
                            }}
                            for col in columns
                        ]
                    }}
                    return schema
                else:
                    # PostgreSQL query
                    query = """
                    SELECT column_name, data_type, is_nullable, column_default
                    FROM information_schema.columns
                    WHERE table_name = :table_name
                    """
                    result = await session.execute(text(query), {{"table_name": table_name}})
                    columns = result.fetchall()

                    schema = {{
                        "table_name": table_name,
                        "columns": [
                            {{
                                "name": col[0],
                                "type": col[1],
                                "nullable": col[2] == "YES",
                                "default": col[3]
                            }}
                            for col in columns
                        ]
                    }}
                    return schema

        except Exception as e:
            logger.error(f"Database error: {{e}}")
            return {{"error": str(e)}}

# Import and register tools in main server
from .server import mcp
register_db_tools(mcp)
'''

        db_tools_path = project_path / "src" / config.name / "db_tools.py"
        with open(db_tools_path, 'w') as f:
            f.write(db_tools_content)

    def _apply_file_processor_template(self, project_path: Path, config: MCPProjectConfig):
        """Apply file processor template with file handling tools"""
        # Add file processing dependencies
        config.dependencies.extend(["pillow>=10.0.0", "pandas>=2.2.0", "openpyxl>=3.1.0"])

        file_tools_content = f'''"""
File processing tools for {config.name}
"""

from pathlib import Path
from fastmcp import FastMCP
from fastmcp.types import TextContent, ImageContent
from PIL import Image
import pandas as pd
import logging
from typing import Dict, Any, List, Optional

logger = logging.getLogger(__name__)

def register_file_tools(mcp: FastMCP):
    """Register file processing tools with the MCP server."""

    @mcp.tool()
    def read_text_file(file_path: str) -> str:
        """Read contents of a text file.

        Args:
            file_path: Path to the text file

        Returns:
            File contents as string
        """
        logger.info(f"Reading text file: {{file_path}}")

        try:
            path = Path(file_path)
            if not path.exists():
                return f"Error: File not found at {{file_path}}"

            if path.stat().st_size > 1024 * 1024:  # 1MB limit
                return "Error: File too large (max 1MB)"

            with open(path, 'r', encoding='utf-8') as f:
                return f.read()

        except Exception as e:
            logger.error(f"Error reading file: {{e}}")
            return f"Error reading file: {{e}}"

    @mcp.tool()
    def write_text_file(file_path: str, content: str) -> str:
        """Write content to a text file.

        Args:
            file_path: Path to the text file
            content: Content to write

        Returns:
            Success message
        """
        logger.info(f"Writing text file: {{file_path}}")

        try:
            path = Path(file_path)
            path.parent.mkdir(parents=True, exist_ok=True)

            with open(path, 'w', encoding='utf-8') as f:
                f.write(content)

            return f"Successfully wrote {{len(content)}} characters to {{file_path}}"

        except Exception as e:
            logger.error(f"Error writing file: {{e}}")
            return f"Error writing file: {{e}}"

    @mcp.tool()
    def process_image(image_path: str, operation: str, **kwargs) -> Dict[str, Any]:
        """Process an image with various operations.

        Args:
            image_path: Path to the image file
            operation: Operation to perform (resize, rotate, grayscale, info)
            **kwargs: Operation-specific parameters

        Returns:
            Processing result information
        """
        logger.info(f"Processing image: {{image_path}}, operation: {{operation}}")

        try:
            path = Path(image_path)
            if not path.exists():
                return {{"error": f"Image file not found: {{image_path}}"}}

            with Image.open(path) as img:
                if operation == "info":
                    return {{
                        "format": img.format,
                        "size": img.size,
                        "mode": img.mode,
                        "file_size": path.stat().st_size
                    }}

                elif operation == "resize":
                    width = kwargs.get("width", img.width)
                    height = kwargs.get("height", img.height)
                    resized = img.resize((width, height))

                    output_path = path.parent / f"resized_{{path.name}}"
                    resized.save(output_path)
                    return {{"message": f"Image resized and saved to {{output_path}}", "new_size": resized.size}}

                elif operation == "rotate":
                    angle = kwargs.get("angle", 90)
                    rotated = img.rotate(angle, expand=True)

                    output_path = path.parent / f"rotated_{{path.name}}"
                    rotated.save(output_path)
                    return {{"message": f"Image rotated and saved to {{output_path}}", "angle": angle}}

                elif operation == "grayscale":
                    grayscale = img.convert('L')

                    output_path = path.parent / f"grayscale_{{path.name}}"
                    grayscale.save(output_path)
                    return {{"message": f"Image converted to grayscale and saved to {{output_path}}"}}

                else:
                    return {{"error": f"Unsupported operation: {{operation}}"}}

        except Exception as e:
            logger.error(f"Error processing image: {{e}}")
            return {{"error": str(e)}}

    @mcp.tool()
    def analyze_csv(csv_path: str) -> Dict[str, Any]:
        """Analyze a CSV file and return statistics.

        Args:
            csv_path: Path to the CSV file

        Returns:
            CSV analysis results
        """
        logger.info(f"Analyzing CSV file: {{csv_path}}")

        try:
            path = Path(csv_path)
            if not path.exists():
                return {{"error": f"CSV file not found: {{csv_path}}"}}

            df = pd.read_csv(path)

            analysis = {{
                "shape": df.shape,
                "columns": list(df.columns),
                "dtypes": df.dtypes.to_dict(),
                "null_counts": df.isnull().sum().to_dict(),
                "memory_usage": df.memory_usage(deep=True).sum(),
                "sample_data": df.head().to_dict() if len(df) > 0 else {{}}
            }}

            # Numeric column statistics
            numeric_cols = df.select_dtypes(include=['number']).columns
            if len(numeric_cols) > 0:
                analysis["numeric_stats"] = df[numeric_cols].describe().to_dict()

            return analysis

        except Exception as e:
            logger.error(f"Error analyzing CSV: {{e}}")
            return {{"error": str(e)}}

# Import and register tools in main server
from .server import mcp
register_file_tools(mcp)
'''

        file_tools_path = project_path / "src" / config.name / "file_tools.py"
        with open(file_tools_path, 'w') as f:
            f.write(file_tools_content)

    def _initialize_uv_project(self, project_path: Path, config: MCPProjectConfig):
        """Initialize uv project and install dependencies"""
        try:
            # Change to project directory
            original_cwd = os.getcwd()
            os.chdir(project_path)

            # Initialize uv project
            subprocess.run(["uv", "init", "--no-workspace"], check=True, capture_output=True)

            # Install dependencies
            subprocess.run(["uv", "add"] + config.dependencies, check=True, capture_output=True)

            # Install dev dependencies
            subprocess.run(["uv", "add", "--dev"] + config.dev_dependencies, check=True, capture_output=True)

            os.chdir(original_cwd)

        except subprocess.CalledProcessError as e:
            logger.error(f"Error initializing uv project: {e}")
            # Don't fail the whole project creation if uv commands fail
            pass

    def _create_development_files(self, project_path: Path, config: MCPProjectConfig):
        """Create development and configuration files"""

        # README.md
        readme_content = f'''# {config.name}

{config.description}

A modern MCP server built with FastMCP 2.x and uv.

## Features

{chr(10).join(f"- {feature}" for feature in config.features) if config.features else "- Basic MCP server functionality"}

## Installation

### Using uv (recommended)

```bash
cd {config.name}
uv sync
```

### Using pip

```bash
pip install -e .
```

## Usage

### Running the server

```bash
uv run {config.name}-server
```

### Using with Claude Desktop

Add this to your Claude Desktop configuration:

```json
{{
  "mcpServers": {{
    "{config.name}": {{
      "command": "uv",
      "args": ["run", "{config.name}-server"],
      "cwd": "{project_path.absolute()}"
    }}
  }}
}}
```

## Development

### Running tests

```bash
uv run pytest
```

### Code formatting

```bash
uv run ruff check .
uv run ruff format .
```

### Type checking

```bash
uv run mypy src/
```

## Available Tools

- `ping()`: Test server connectivity
- `server_info()`: Get server information
- `echo_message(message, repeat=1)`: Echo a message

{"## Web API Tools" if config.template == "web-api" else ""}
{"- `http_get(url, headers=None)`: Make HTTP GET requests" if config.template == "web-api" else ""}
{"- `http_post(url, data, headers=None)`: Make HTTP POST requests" if config.template == "web-api" else ""}

{"## Database Tools" if config.template == "database" else ""}
{"- `execute_query(query)`: Execute SQL queries" if config.template == "database" else ""}
{"- `get_table_schema(table_name)`: Get table schema information" if config.template == "database" else ""}

{"## File Processing Tools" if config.template == "file-processor" else ""}
{"- `read_text_file(file_path)`: Read text files" if config.template == "file-processor" else ""}
{"- `write_text_file(file_path, content)`: Write text files" if config.template == "file-processor" else ""}
{"- `process_image(image_path, operation, **kwargs)`: Process images" if config.template == "file-processor" else ""}
{"- `analyze_csv(csv_path)`: Analyze CSV files" if config.template == "file-processor" else ""}

## License

MIT License - see LICENSE file for details.
'''

        readme_path = project_path / "README.md"
        with open(readme_path, 'w') as f:
            f.write(readme_content)

        # .gitignore
        gitignore_content = '''# Byte-compiled / optimized / DLL files
__pycache__/
*.py[cod]
*$py.class

# C extensions
*.so

# Distribution / packaging
.Python
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
share/python-wheels/
*.egg-info/
.installed.cfg
*.egg
MANIFEST

# PyInstaller
*.manifest
*.spec

# Installer logs
pip-log.txt
pip-delete-this-directory.txt

# Unit test / coverage reports
htmlcov/
.tox/
.nox/
.coverage
.coverage.*
.cache
nosetests.xml
coverage.xml
*.cover
*.py,cover
.hypothesis/
.pytest_cache/
cover/

# Jupyter Notebook
.ipynb_checkpoints

# IPython
profile_default/
ipython_config.py

# pyenv
.python-version

# pipenv
Pipfile.lock

# poetry
poetry.lock

# uv
.venv
.uv_cache/

# IDEs
.vscode/
.idea/
*.swp
*.swo
*~

# OS
.DS_Store
.DS_Store?
._*
.Spotlight-V100
.Trashes
ehthumbs.db
Thumbs.db

# Project specific
*.db
*.sqlite
*.sqlite3
data/
logs/
temp/
uploads/
.env
.env.local
.env.*.local
'''

        gitignore_path = project_path / ".gitignore"
        with open(gitignore_path, 'w') as f:
            f.write(gitignore_content)

        # Basic test file
        test_content = f'''"""
Tests for {config.name} MCP server
"""

import pytest
import asyncio
from {config.name}.server import mcp


class TestBasicTools:
    """Test basic MCP server tools."""

    @pytest.mark.asyncio
    async def test_ping(self):
        """Test the ping tool."""
        result = await mcp.call_tool("ping", {{}})
        assert result == "pong"

    @pytest.mark.asyncio
    async def test_server_info(self):
        """Test the server_info tool."""
        result = await mcp.call_tool("server_info", {{}})
        assert isinstance(result, dict)
        assert "name" in result
        assert "version" in result
        assert result["name"] == "{config.name}"

    @pytest.mark.asyncio
    async def test_echo_message(self):
        """Test the echo_message tool."""
        result = await mcp.call_tool("echo_message", {{
            "message": "Hello, World!",
            "repeat": 2
        }})
        assert result == "Hello, World! Hello, World!"


class TestResources:
    """Test MCP server resources."""

    @pytest.mark.asyncio
    async def test_server_config(self):
        """Test the server configuration resource."""
        result = await mcp.read_resource("config://server")
        assert isinstance(result, str)
        assert "{config.name}" in result


class TestPrompts:
    """Test MCP server prompts."""

    @pytest.mark.asyncio
    async def test_help_prompt(self):
        """Test the help prompt."""
        result = await mcp.get_prompt("help", {{}})
        assert isinstance(result, str)
        assert "{config.name}" in result
'''

        test_path = project_path / "tests" / f"test_{config.name}.py"
        with open(test_path, 'w') as f:
            f.write(test_content)


def main():
    """Main CLI entry point"""
    parser = argparse.ArgumentParser(
        description="Create modern MCP services with FastMCP 2.x + uv"
    )
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # Create command
    create_parser = subparsers.add_parser("create", help="Create a new MCP project")
    create_parser.add_argument("name", help="Project name")
    create_parser.add_argument("--description", default="", help="Project description")
    create_parser.add_argument("--author", default="Developer", help="Author name")
    create_parser.add_argument("--template", default="basic",
                             choices=["basic", "web-api", "database", "file-processor"],
                             help="Project template")
    create_parser.add_argument("--postgres", action="store_true",
                             help="Use PostgreSQL for database template")
    create_parser.add_argument("--version", default="0.1.0", help="Initial version")
    create_parser.add_argument("--python-version", default="3.11", help="Python version")

    # Template command
    template_parser = subparsers.add_parser("template", help="List available templates")
    template_parser.add_argument("template_name", nargs="?", help="Show template details")

    # Add tool command
    add_tool_parser = subparsers.add_parser("add-tool", help="Add a tool to existing project")
    add_tool_parser.add_argument("tool_name", help="Tool name to add")
    add_tool_parser.add_argument("--type", default="basic",
                                choices=["basic", "api", "database", "file"],
                                help="Tool type")

    args = parser.parse_args()

    if not args.command:
        parser.print_help()
        return

    creator = MCPCreator()

    if args.command == "create":
        # Determine features based on template
        features = []
        if args.template == "web-api":
            features = ["HTTP client", "REST API integration"]
        elif args.template == "database":
            features = ["Database connectivity", "SQL queries"]
            if args.postgres:
                features.append("PostgreSQL support")
            else:
                features.append("SQLite support")
        elif args.template == "file-processor":
            features = ["File I/O", "Image processing", "CSV analysis"]

        config = MCPProjectConfig(
            name=args.name,
            description=args.description or f"MCP server for {args.name}",
            author=args.author,
            version=args.version,
            python_version=args.python_version,
            template=args.template,
            features=features
        )

        if "postgres" in args and args.postgres:
            config.features.append("PostgreSQL")

        success = creator.create_project(config)
        sys.exit(0 if success else 1)

    elif args.command == "template":
        if args.template_name:
            # Show template details
            print(f"Template: {args.template_name}")
            # TODO: Implement template details
        else:
            # List available templates
            print("Available templates:")
            print("  basic       - Basic MCP server with essential tools")
            print("  web-api     - MCP server with HTTP client capabilities")
            print("  database    - MCP server with database connectivity")
            print("  file-processor - MCP server with file processing tools")

    elif args.command == "add-tool":
        print(f"Adding tool '{args.tool_name}' of type '{args.type}' to current project...")
        # TODO: Implement tool addition logic
        print("This feature is coming soon!")


if __name__ == "__main__":
    main()