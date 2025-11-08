---
name: fastmcp-app-creator
description: This skill should be used when users need to create MCP (Model Context Protocol) applications using the latest FastMCP 2.x framework and uv package manager. It provides a complete workflow for generating production-ready MCP apps from design documents, with strict adherence to MCP standards and modern Python best practices.
---

# FastMCP App Creator

## Overview

This skill enables the creation of professional MCP (Model Context Protocol) applications using the latest FastMCP 2.x framework and uv package manager. It provides a complete workflow from design document parsing to fully functional, production-ready MCP apps with strict adherence to MCP standards.

## When to Use This Skill

Use this skill when:
- Users provide an MCP App design document following the v1.0 template format
- Users need to create MCP applications with streamableHttp deployment
- Users want to generate FastMCP 2.x applications with proper tool, resource, and prompt definitions
- Users need MCP apps with modern Python project structure using uv
- Users require production-ready MCP applications with testing, documentation, and configuration

## Core Workflow

### Step 1: Parse Design Document
Extract and validate the MCP App design document components:
- App name, background, and scenarios
- Access method configuration (streamableHttp)
- MCP Instructions with trigger conditions and limitations
- Tool definitions with parameters
- Usage examples

### Step 2: Validate MCP Compliance
Ensure the design document meets MCP standards:
- Verify streamableHttp configuration format
- Validate tool parameter definitions
- Check MCP Instructions completeness
- Ensure proper security considerations

### Step 3: Generate Project Structure
Create modern Python project structure:
- FastMCP 2.x based server implementation
- Proper `src/` package layout with uv configuration
- Tool modules with @mcp.tool decorators
- Resource definitions with @mcp.resource decorators
- Prompt definitions with @mcp.prompt decorators

### Step 4: Configure uv Build System
Set up modern Python project management:
- Generate `pyproject.toml` with hatchling build backend
- Configure FastMCP 2.x and required dependencies
- Set up development dependencies (pytest, ruff, mypy)
- Create project scripts for server execution

### Step 5: Apply Security Best Practices
Implement security controls:
- Input validation for all tool parameters
- SQL injection prevention for database tools
- File path traversal protection
- Authentication and authorization patterns

### Step 6: Generate Documentation
Create comprehensive project documentation:
- README.md with usage instructions
- API documentation for tools and resources
- Claude Desktop configuration examples
- Development and deployment guides

## Supported MCP App Types

### Basic MCP App
- Core functionality with ping, server info tools
- Basic configuration resources
- Help prompt templates
- Suitable for simple integrations

### Web API MCP App
- HTTP client tools with httpx integration
- Bearer token and API key authentication
- RESTful API endpoint management
- Request/response handling and error management

### Database MCP App
- SQLAlchemy-based database connectivity
- Secure SQL query execution (SELECT only)
- Table schema analysis
- Multi-database support (SQLite, PostgreSQL, MySQL)

### File Processor MCP App
- Text file reading and writing
- Image processing with Pillow
- CSV/Excel data analysis
- File validation and security controls

## FastMCP 2.x Implementation Patterns

### Tool Definition Pattern
```python
@mcp.tool()
def process_data(data: str, count: int = 1) -> Dict[str, Any]:
    """Process data with specified parameters.

    Args:
        data: Input data to process
        count: Number of iterations

    Returns:
        Processing results with status and data
    """
    try:
        result = execute_processing(data, count)
        return {
            "status": "success",
            "data": result,
            "message": "Processing completed successfully"
        }
    except Exception as e:
        logger.error(f"Processing error: {e}")
        return {
            "status": "error",
            "message": str(e),
            "code": "PROCESSING_ERROR"
        }
```

### Resource Definition Pattern
```python
@mcp.resource("config://server")
def get_server_config() -> str:
    """Get server configuration resource."""
    config_data = {
        "name": app_name,
        "version": version,
        "endpoints": available_endpoints,
        "tools_count": len(tools)
    }
    return json.dumps(config_data, indent=2, ensure_ascii=False)
```

### Prompt Definition Pattern
```python
@mcp.prompt("help")
def get_help_prompt() -> str:
    """Get help prompt for MCP application."""
    return f"""
    # {app_name} Help

    ## Available Tools
    {chr(10).join(f"- `{tool}`: {description}" for tool, description in tools_list)}

    ## Usage Examples
    {chr(10).join(f"- {example}" for example in usage_examples)}
    """
```

## Security Implementation

### Input Validation
- Parameter type checking with Pydantic models
- SQL injection prevention for database operations
- File path traversal protection
- Request size and rate limiting

### Authentication Patterns
- Bearer token authentication for HTTP tools
- API key management with secure storage
- Context-based user isolation
- Session management with context IDs

### Error Handling
- Structured error responses with status codes
- Detailed logging for debugging
- User-friendly error messages
- Graceful degradation for failures

## Deployment Configuration

### streamableHttp Configuration
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

### Claude Desktop Integration
```json
{
  "mcpServers": {
    "my-app": {
      "command": "uv",
      "args": ["run", "my-app-server"],
      "cwd": "/path/to/my-app"
    }
  }
}
```

## Quality Assurance

### Code Quality Standards
- Type hints for all functions and methods
- Comprehensive error handling
- Structured logging with appropriate levels
- Code formatting with ruff
- Type checking with mypy

### Testing Requirements
- Unit tests for all tools
- Integration tests for API endpoints
- Mock external dependencies
- Coverage reporting with pytest-cov

### Documentation Standards
- Comprehensive README.md
- Inline docstrings for all functions
- API documentation for tools
- Usage examples and configuration guides

## Resources

### scripts/
Executable Python scripts for MCP app generation:

**`create_fastmcp_app.py`** - Main MCP app generator
- Parses design documents according to v1.0 template
- Generates FastMCP 2.x compliant server code
- Creates uv-based project structure
- Applies security best practices
- Handles all supported MCP app types

**Usage:**
```bash
python3 create_fastmcp_app.py \
  --name knowledge-base \
  --description "知识库查询应用" \
  --background "企业内部知识库查询需求" \
  --scenarios "员工快速查找公司文档和政策" \
  --instructions "知识库查询助手..." \
  --trigger-conditions "用户询问公司政策时" \
  --limitations "不支持实时数据查询" \
  --usage-examples "公司的请假政策是什么？" \
  --tools "search_docs:搜索知识库文档:query:字符串,limit:数字" \
  --access-url "https://api.company.com/mcp/knowledge-base" \
  --headers "Authorization:Bearer <USER_AGENT_TOKEN>;x-context-id:<context_id>"
```

### references/
Comprehensive documentation for FastMCP and uv:

**`fastmcp_patterns.md`** - FastMCP 2.x patterns and best practices
- Decorator usage (@mcp.tool, @mcp.resource, @mcp.prompt)
- Type annotation requirements
- Common implementation patterns
- Security and performance considerations

**`uv_configuration.md`** - uv package manager configuration
- pyproject.toml structure and best practices
- Development tool configuration (ruff, mypy, pytest)
- Dependency management patterns
- CI/CD integration examples

### assets/
Templates and configuration examples:

**`templates/`** - MCP app type templates
- `basic_mcp_app.md` - Basic application template
- `web_api_mcp_app.md` - HTTP API integration template
- `database_mcp_app.md` - Database operations template
- `file_processor_mcp_app.md` - File processing template

**`config_examples/`** - Configuration examples
- `claude_desktop_config.json` - Claude Desktop integration
- Environment variable templates
- MCP server configuration examples

## Usage Examples

### Example 1: Knowledge Base MCP App
```bash
python3 create_fastmcp_app.py \
  --name knowledge-base \
  --description "企业知识库查询应用" \
  --background "帮助企业员工快速查找内部文档和政策" \
  --scenarios "员工日常工作中需要查询公司信息" \
  --instructions "知识库查询助手，专为企业内部知识检索而设计" \
  --trigger-conditions "用户询问公司政策、规定、流程时" \
  --limitations "不支持实时数据查询，不能访问外部互联网内容" \
  --usage-examples "公司的请假政策是什么？;如何申请项目预算？" \
  --tools "search_docs:搜索知识库文档:query:字符串,limit:数字;get_document:获取文档内容:document_id:字符串" \
  --access-url "https://api.company.com/mcp/knowledge-base" \
  --headers "Authorization:Bearer <USER_AGENT_TOKEN>;x-context-id:<context_id>"
```

### Example 2: File Processor MCP App
```bash
python3 create_fastmcp_app.py \
  --name file-processor \
  --description "文件处理应用" \
  --background "处理各种格式的文件，支持文本、图像和数据文件" \
  --scenarios "用户需要处理和分析不同格式的文件" \
  --instructions "文件处理助手，支持多种文件格式的读取、处理和转换" \
  --trigger-conditions "用户需要处理文件时" \
  --limitations "文件大小限制100MB，不支持恶意文件处理" \
  --usage-examples "处理CSV文件并生成报告;转换图像格式" \
  --tools "read_file:读取文件:path:字符串,encoding:字符串;process_image:处理图像:image_path:字符串,operation:字符串;analyze_csv:分析CSV文件:csv_path:字符串" \
  --access-url "https://api.company.com/mcp/file-processor" \
  --headers "Authorization:Bearer <USER_AGENT_TOKEN>"
```

### Example 3: Database Query MCP App
```bash
python3 create_fastmcp_app.py \
  --name database-query \
  --description "数据库查询应用" \
  --background "安全的数据库查询和数据分析工具" \
  --scenarios "业务人员需要查询数据库获取业务数据" \
  --instructions "数据库查询助手，仅支持安全的SELECT查询操作" \
  --trigger-conditions "用户需要查询业务数据时" \
  --limitations "仅支持SELECT查询，不能修改数据库数据" \
  --usage-examples "查询本月销售额;分析用户行为数据" \
  --tools "execute_query:执行SQL查询:query:字符串,params:字典;get_table_schema:获取表结构:table_name:字符串;analyze_table:分析表数据:table_name:字符串" \
  --access-url "https://api.company.com/mcp/database-query" \
  --headers "Authorization:Bearer <USER_AGENT_TOKEN>;x-database:postgresql"
```