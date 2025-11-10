# Markitdown API Reference

Complete reference for the markitdown tool and its integration with the Document Converter skill.

## Overview

The Document Converter skill uses the `markitdown` command-line tool for local document processing. This ensures complete data privacy as all processing happens on the local machine without external API calls.

## Markitdown Tool Installation

### Prerequisites

```bash
# Install markitdown tool
pip install markitdown

# Verify installation
markitdown --help
```

### System Requirements

- Python 3.7 or higher
- Sufficient disk space for temporary files
- Appropriate memory for document processing

## Command Line Interface

### Basic Syntax

```bash
markitdown [OPTIONS] <INPUT_FILE>
```

### Core Options

| Option | Short | Description | Example |
|--------|-------|-------------|---------|
| `--output` | `-o` | Output file name | `-o output.md` |
| `--extension` | `-x` | File extension hint for stdin | `-x pdf` |
| `--mime-type` | `-m` | MIME type hint | `-m application/pdf` |
| `--charset` | `-c` | Character set hint | `-c UTF-8` |
| `--use-docintel` | `-d` | Use Document Intelligence | `-d` |
| `--endpoint` | `-e` | Document Intelligence endpoint | `-e URL` |
| `--use-plugins` | `-p` | Use 3rd-party plugins | `-p` |
| `--list-plugins` | | List available plugins | `--list-plugins` |
| `--keep-data-uris` | | Keep data URIs in output | `--keep-data-uris` |
| `--version` | `-v` | Show version information | `-v` |
| `--help` | `-h` | Show help message | `-h` |

## Input Methods

### File Input

```bash
markitdown document.pdf
markitdown presentation.pptx -o slides.md
```

### Standard Input

```bash
cat document.pdf | markitdown
markitdown < document.pdf
```

### With Extension Hint

```bash
cat unknown_file | markitdown -x pdf
```

## Supported Formats

### Document Formats

| Format | Extension | Notes |
|--------|-----------|-------|
| PDF | `.pdf` | Full text and structure extraction |
| Word | `.docx`, `.doc` | Modern and legacy Word formats |
| PowerPoint | `.pptx`, `.ppt` | Slide content extraction |
| Rich Text | `.rtf` | Formatted text documents |
| Plain Text | `.txt` | Direct text processing |

### Web Formats

| Format | Extension | Notes |
|--------|-----------|-------|
| HTML | `.html`, `.htm` | Web page structure extraction |
| Markdown | `.md` | Validation and cleaning |

### Data Formats

| Format | Extension | Notes |
|--------|-----------|-------|
| CSV | `.csv` | Table structure preservation |
| JSON | `.json` | Structured data extraction |
| XML | `.xml` | Hierarchical data parsing |

### Image Formats

| Format | Extension | Notes |
|--------|-----------|-------|
| JPEG | `.jpg`, `.jpeg` | OCR text extraction |
| PNG | `.png` | OCR text extraction |
| GIF | `.gif` | OCR text extraction |
| BMP | `.bmp` | OCR text extraction |
| TIFF | `.tiff` | OCR text extraction |

## Advanced Features

### Plugin System

Enable third-party plugins for enhanced conversion:

```bash
markitdown document.pdf --use-plugins
```

List available plugins:

```bash
markitdown --list-plugins
```

### Document Intelligence Integration

Use Azure Document Intelligence for enhanced processing:

```bash
markitdown document.pdf --use-docintel --endpoint "https://your-endpoint.cognitiveservices.azure.com/"
```

**Requirements**:
- Azure Document Intelligence resource
- Valid endpoint URL and API key (configured separately)
- Internet connection for Azure service

### Data URI Handling

Control base64-encoded image handling:

```bash
# Keep data URIs (preserves images as base64)
markitdown document.pdf --keep-data-uris

# Default behavior (truncates large data URIs)
markitdown document.pdf
```

### Format Hints

Provide hints for better conversion accuracy:

```bash
# MIME type hint
markitdown unknown_file --mime-type "application/pdf"

# Character set hint
markitdown text_file --charset "UTF-8"

# File extension hint for stdin
cat file_data | markitdown -x pdf
```

## Integration with Document Converter Script

### Basic Usage

```bash
# Direct script usage
python scripts/converter.py document.pdf

# With output file
python scripts/converter.py document.pdf --output converted.md
```

### Advanced Options

```bash
# Use markitdown plugins
python scripts/converter.py complex_document.pdf --use-plugins

# Preserve data URIs
python scripts/converter.py image_heavy.pdf --keep-data-uris --output with_images.md

# Use Document Intelligence
python scripts/converter.py scan.pdf --use-docintel --endpoint "https://your-endpoint.cognitiveservices.azure.com/"

# Provide format hints
python scripts/converter.py unknown_file --mime-type "application/pdf"
```

### URL Processing

URLs are downloaded locally and processed with markitdown:

```bash
# Download and convert URL content
python scripts/converter.py https://example.com/document.pdf --output downloaded.md

# Process with options
python scripts/converter.py https://example.com/file.docx --use-plugins --output converted.docx.md
```

## Output Formats

### Standard Output

```bash
markitdown document.pdf
# Outputs Markdown content to stdout
```

### File Output

```bash
markitdown document.pdf -o output.md
# Writes Markdown content to file
```

### JSON Metadata (via Script)

```bash
python scripts/converter.py document.pdf --json
# Returns structured JSON with metadata and content
```

## Error Handling

### Common Exit Codes

| Exit Code | Description | Solution |
|-----------|-------------|----------|
| 0 | Success | Normal operation |
| 1 | General Error | Check input file and permissions |
| 2 | File Not Found | Verify file path exists |
| 3 | Permission Denied | Check file read permissions |
| 4 | Unsupported Format | Use supported file formats |
| 5 | Processing Timeout | Try with smaller file or simpler content |
| 6 | Memory Error | Reduce file size or increase available memory |
| 7 | Plugin Error | Check plugin installation and compatibility |

### Error Messages

```
Error: markitdown tool not found. Please install it with: pip install markitdown
Error: File does not exist
Error: File processing timeout - file may be too complex
Error: Markitdown conversion failed: [error details]
```

## Performance Considerations

### File Size Limits

- **Recommended**: < 100MB for local processing
- **Maximum**: Depends on available system memory
- **Large Files**: Consider splitting or pre-processing

### Memory Usage

- Text files: ~2x file size during processing
- Image-heavy files: ~3-5x file size for OCR processing
- Complex documents: Varies based on content complexity

### Processing Time

- Simple text files: < 1 second per MB
- PDF documents: 2-5 seconds per MB
- Image processing: 5-10 seconds per MB
- Complex layouts: Additional processing time

## Configuration Options

### Environment Variables

```bash
# Optional: Set custom temp directory
export TEMP_DIR="/path/to/temp"

# Optional: Set default markitdown options
export MARKITDOWN_OPTS="--use-plugins"
```

### Script Configuration

The Document Converter script can be configured through command-line options:

```python
# Default settings in converter.py
DEFAULT_TIMEOUT = 300  # 5 minutes
DEFAULT_FILE_SIZE_LIMIT = 100 * 1024 * 1024  # 100MB
```

## Security Considerations

### Local Processing Benefits

- **No External Data Transmission**: All processing happens locally
- **Privacy Protection**: Sensitive data never leaves the system
- **No API Keys Required**: No external service dependencies
- **Offline Capability**: Works without internet connection
- **Audit Trail**: Local processing can be logged and monitored

### Temporary File Security

- Downloaded URL content stored in temporary files
- Automatic cleanup after processing
- Secure file permissions on temporary files
- No residual data left on disk

### Best Practices

1. **File Permissions**: Ensure appropriate read/write permissions
2. **Disk Space**: Monitor available disk space for large files
3. **Memory Usage**: Monitor memory usage for batch processing
4. **Network Security**: For URL downloads, use secure connections
5. **Clean Up**: Verify temporary file cleanup for sensitive content

## Troubleshooting

### Installation Issues

```bash
# Check markitdown installation
which markitdown
markitdown --version

# Reinstall if needed
pip uninstall markitdown
pip install markitdown
```

### Processing Problems

```bash
# Test with simple file
echo "test content" > test.txt
markitdown test.txt

# Check file permissions
ls -la document.pdf

# Test with verbose output
python scripts/converter.py document.pdf --json
```

### Performance Issues

```bash
# Check system resources
df -h  # Disk space
free -h  # Memory usage

# Test with smaller file
head -c 1M large_file.pdf > small_test.pdf
markitdown small_test.pdf
```

## Comparison with External Services

| Feature | Local Markitdown | External API Services |
|---------|------------------|---------------------|
| **Data Privacy** | ✅ Complete privacy | ❌ Data sent externally |
| **Network Dependency** | ❌ Offline capable | ✅ Requires internet |
| **Cost** | 💰 Free | 💸 Usage-based pricing |
| **Speed** | ⚡ Local processing speed | 🌐 Network latency |
| **Reliability** | 🟢 Stable local tool | 🟡 Service availability |
| **Customization** | 🔧 Full control | ⚙️ Limited options |
| **Security** | 🔒 Maximum security | 🔓 Potential risks |

## Integration Examples

### Batch Processing

```bash
#!/bin/bash
# batch_convert.sh

for file in *.pdf *.docx *.pptx; do
    echo "Converting $file..."
    python scripts/converter.py "$file" --output "converted/${file%.pdf}.md"
done
```

### CI/CD Pipeline

```yaml
# GitHub Actions example
- name: Install markitdown
  run: pip install markitdown

- name: Convert documents
  run: |
    python scripts/converter.py docs/specification.pdf --output docs/specification.md
```

### Python Integration

```python
from scripts.converter import DocumentConverter

converter = DocumentConverter()
result = converter.convert_file('document.pdf', use_plugins=True)

if result['status'] == 'success':
    print(f"Title: {result['title']}")
    print(f"Content length: {len(result['content'])} characters")
```

## Version Information

Check markitdown version:

```bash
markitdown --version

# Or via the script
python scripts/converter.py --markitdown-version
```

## Support and Resources

- **Markitdown Documentation**: Check `markitdown --help`
- **Script Documentation**: See `references/` directory
- **Error Handling**: See `references/error_handling.md`
- **Usage Examples**: See `assets/usage_examples.md`