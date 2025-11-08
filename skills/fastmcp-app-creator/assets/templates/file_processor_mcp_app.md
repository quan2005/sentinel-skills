# 文件处理 MCP 应用模板

## 模板描述

这是一个专门用于文件处理的 MCP 应用模板，支持多种文件格式的读取、处理和转换。

## 项目结构

```
file-processor-mcp-app/
├── pyproject.toml
├── README.md
├── .env.example
├── .gitignore
├── src/
│   └── file_processor_mcp_app/
│       ├── __init__.py
│       ├── server.py
│       ├── file_tools.py    # 文件处理工具
│       ├── image_tools.py   # 图像处理工具
│       ├── data_tools.py    # 数据文件工具
│       └── validators.py    # 文件验证
├── tests/
│   ├── __init__.py
│   ├── test_server.py
│   └── test_file_tools.py
├── data/                   # 测试数据
│   ├── samples/
│   └── temp/
└── config/
    ├── mcp_config.json
    └── file_limits.json
```

## 核心功能

### 文件工具
- `read_text_file(file_path, encoding='utf-8')` - 读取文本文件
- `write_text_file(file_path, content, encoding='utf-8')` - 写入文本文件
- `list_files(directory, pattern='*')` - 列出目录文件
- `file_info(file_path)` - 获取文件信息
- `create_directory(path)` - 创建目录

### 图像处理工具
- `process_image(image_path, operation, **kwargs)` - 图像处理
- `resize_image(image_path, width, height)` - 调整图像大小
- `convert_format(image_path, target_format)` - 格式转换
- `extract_metadata(image_path)` - 提取元数据

### 数据文件工具
- `analyze_csv(csv_path)` - 分析 CSV 文件
- `process_excel(file_path, sheet_name=None)` - 处理 Excel 文件
- `read_json(file_path)` - 读取 JSON 文件
- `convert_csv_to_json(csv_path, json_path)` - CSV 转 JSON

### 压缩工具
- `compress_files(file_paths, output_path)` - 压缩文件
- `extract_archive(archive_path, extract_to)` - 解压文件

## 支持的文件格式

### 文本文件
- .txt, .md, .json, .yaml, .yml, .xml, .csv
- .py, .js, .html, .css, .sql

### 图像文件
- .jpg, .jpeg, .png, .gif, .bmp, .tiff, .webp

### 数据文件
- .csv, .xlsx, .xls, .json, .xml

### 压缩文件
- .zip, .tar, .gz, .rar

## 配置示例

### pyproject.toml
```toml
[project]
name = "file-processor-mcp-app"
version = "1.0.0"
description = "文件处理 MCP 应用"
dependencies = [
    "fastmcp>=2.0.0",
    "pillow>=10.0.0",
    "pandas>=2.2.0",
    "openpyxl>=3.1.0",
    "pydantic>=2.8.0",
    "python-dotenv>=1.0.0",
    "aiofiles>=23.0.0",
]

[project.optional-dependencies]
dev = [
    "pytest>=8.0.0",
    "pytest-asyncio>=0.24.0",
    "ruff>=0.6.0",
    "mypy>=1.11.0",
]
```

### 文件限制配置
```json
{
  "file_limits": {
    "max_file_size": 104857600,
    "max_text_size": 1048576,
    "max_image_size": 52428800,
    "max_concurrent_files": 50,
    "allowed_extensions": [
      ".txt", ".md", ".json", ".yaml", ".yml", ".xml", ".csv",
      ".py", ".js", ".html", ".css", ".sql",
      ".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff", ".webp",
      ".xlsx", ".xls", ".zip", ".tar", ".gz"
    ],
    "forbidden_patterns": [
      "*.exe", "*.dll", "*.so", "*.dylib",
      "*.bat", "*.cmd", "*.sh",
      ".env", "*.key", "*.pem", "*.p12"
    ]
  },
  "image_processing": {
    "max_width": 4096,
    "max_height": 4096,
    "allowed_formats": ["JPEG", "PNG", "GIF", "BMP", "TIFF"],
    "quality": 85
  },
  "directories": {
    "temp_dir": "./data/temp",
    "upload_dir": "./data/uploads",
    "output_dir": "./data/output",
    "auto_cleanup": true,
    "cleanup_interval": 3600
  }
}
```

### 环境变量
```bash
# 文件限制
MAX_FILE_SIZE=104857600
MAX_TEXT_SIZE=1048576
MAX_IMAGE_SIZE=52428800
MAX_CONCURRENT_FILES=50

# 目录配置
TEMP_DIR=./data/temp
UPLOAD_DIR=./data/uploads
OUTPUT_DIR=./data/output
AUTO_CLEANUP=true
CLEANUP_INTERVAL=3600

# 图像处理
MAX_IMAGE_WIDTH=4096
MAX_IMAGE_HEIGHT=4096
DEFAULT_IMAGE_QUALITY=85

# 安全配置
ALLOW_PATH_TRAVERSAL=false
STRICT_MODE=true
VALIDATE_FILE_SIGNATURES=true
```