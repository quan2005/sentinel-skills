---
name: document-converter
description: Convert PDF, PPT, DOCX, and other files to Markdown format using local markitdown tool. Ensures complete data privacy by processing all files locally without external API calls.
---

# Document Converter

Convert various document formats to structured Markdown format using the local markitdown tool for complete data privacy and security.

## When to Use

Use this skill when users need to:

- Convert local documents (PDF, PPT, DOCX) to Markdown securely
- Process sensitive files without sending data to external services
- Extract text content from various file formats
- Convert web content by downloading and processing locally
- Handle batch conversions with privacy assurance
- Work with documents containing confidential information

## How to Use

### Basic File Conversion

To convert a local file to Markdown:

1. Use the converter script from `scripts/converter.py`
2. Provide the local file path as input
3. Receive structured Markdown output locally processed

```bash
python scripts/converter.py "document.pdf"
```

### File Conversion with Output

To convert and save to specific file:

```bash
python scripts/converter.py "presentation.pptx" --output "slides.md"
```

### Advanced Local Processing

For enhanced conversion with markitdown options:

```bash
python scripts/converter.py "document.pdf" \
  --use-plugins \
  --keep-data-uris \
  --output "converted.md"
```

### URL Conversion (Local Processing)

Convert URLs by downloading and processing locally:

```bash
python scripts/converter.py "https://example.com/document.pdf"
```

## Core Components

### Scripts

- **`scripts/converter.py`**: Local conversion engine using markitdown tool. Handles file processing, URL downloads, and advanced conversion options with complete privacy.

### References

- **`references/api_reference.md`**: Markitdown tool documentation and command options
- **`references/conversion_options.md`**: Complete guide to markitdown conversion features
- **`references/error_handling.md`**: Error codes and troubleshooting for local processing

### Assets

- **`assets/example_urls.txt`**: Collection of test URLs for local download and conversion
- **`assets/usage_examples.md`**: Detailed examples and best practices for secure conversion

## Implementation Workflow

1. **Security Check**: All processing happens locally using markitdown tool
2. **Input Validation**: Verify file exists and is within size limits
3. **Tool Detection**: Ensure markitdown is available in the system PATH
4. **Local Processing**: Execute markitdown with specified options
5. **Content Extraction**: Parse markitdown output and extract metadata
6. **URL Handling** (if needed): Download content to temporary file, process locally, clean up
7. **Error Handling**: Manage local processing errors gracefully
8. **Output Formatting**: Return structured results or save to specified file

## Markitdown Integration

### Markitdown Options

- **Plugin Support**: Use `--use-plugins` for third-party conversion plugins
- **Document Intelligence**: Use `--use-docintel` with endpoint for enhanced processing
- **Data URIs**: Use `--keep-data-uris` to preserve base64-encoded images
- **Format Hints**: Provide MIME type and charset hints for better conversion
- **Output Control**: Direct output to file or stdout

### Supported Formats

**Documents**:
- PDF files (.pdf)
- Word documents (.docx, .doc)
- PowerPoint presentations (.pptx, .ppt)
- Rich text format (.rtf)
- Plain text files (.txt)

**Web Content**:
- HTML files (.html, .htm) - downloaded and processed locally

**Other Formats**:
- Markdown files (.md) - for validation and cleaning
- CSV files (.csv)
- JSON files (.json)
- XML files (.xml)

### Security Features

- **Local Processing Only**: No data leaves the local system
- **Temporary File Cleanup**: Automatic cleanup of downloaded URL content
- **Privacy by Design**: All conversion happens using local markitdown tool
- **Size Limits**: Configurable file size limits for local processing
- **No External Dependencies**: All processing done with installed markitdown tool

## Error Handling and Troubleshooting

Common local processing errors and solutions:

- **markitdown not found**: Install with `pip install markitdown`
- **File not found**: Verify file path and permissions
- **Processing timeout**: File may be too complex or large
- **Permission denied**: Check file and directory permissions
- **Memory issues**: File may be too large for available memory

Refer to `references/error_handling.md` for detailed troubleshooting steps.

## Best Practices

### Security and Privacy
- All processing happens locally - no external API calls
- Temporary files are automatically cleaned up
- No data transmission to external services
- Suitable for sensitive and confidential documents

### Performance Optimization
- Use appropriate file size limits (recommended < 100MB)
- Enable plugins only when needed for specific formats
- Consider Document Intelligence for complex documents
- Monitor memory usage for large files

### Quality Enhancement
- Provide MIME type hints for better conversion accuracy
- Use plugins for specialized format handling
- Keep data URIs for image preservation when needed
- Validate output for critical applications

## Installation Requirements

### Prerequisites

```bash
# Install markitdown tool
pip install markitdown

# Optional: For URL conversion capabilities
pip install requests
```

### System Requirements

- Python 3.7 or higher
- markitdown tool installed and in PATH
- Sufficient disk space for temporary files
- Appropriate memory for document processing

## Usage Examples

### Basic Secure Conversion
```bash
# Convert PDF locally
python scripts/converter.py "confidential.pdf" --output "secure.md"

# Process with plugin support
python scripts/converter.py "complex.docx" --use-plugins
```

### Advanced Local Processing
```bash
# Enhanced conversion with data URIs
python scripts/converter.py "presentation.pptx" \
  --keep-data-uris \
  --use-plugins \
  --output "complete.md"

# URL conversion with local processing
python scripts/converter.py "https://example.com/document.pdf" \
  --output "downloaded.md"
```

### Document Intelligence Integration
```bash
# Use Document Intelligence for enhanced processing
python scripts/converter.py "scan.pdf" \
  --use-docintel \
  --endpoint "https://your-docintel-endpoint.cognitiveservices.azure.com/"
```

## Comparison with External Services

| Feature | Local Markitdown | External API Services |
|---------|------------------|---------------------|
| **Data Privacy** | ✅ Complete privacy | ❌ Data sent externally |
| **Processing Speed** | ⚡ Fast local processing | 🌐 Network dependent |
| **Internet Required** | ❌ Offline capable | ✅ Requires connection |
| **Cost** | 💰 Free (local) | 💸 Usage-based pricing |
| **Security** | 🔒 Maximum security | 🔓 Potential security risks |
| **Customization** | 🔧 Full control | ⚙️ Limited options |
| **Reliability** | 🟢 Stable local tool | 🟡 Service dependent |

## Migration from External Services

For users migrating from external document conversion services:

1. **Install markitdown**: `pip install markitdown`
2. **Update commands**: Replace API calls with local script usage
3. **Adjust options**: Map external service options to markitdown equivalents
4. **Test locally**: Verify conversion quality with sample documents
5. **Update workflows**: Integrate local processing into existing pipelines

## Data Privacy Assurance

This skill ensures complete data privacy through:

- **Local Processing**: All conversion happens on your local machine
- **No External Calls**: No data is sent to external APIs or services
- **Temporary Security**: Downloaded URL content is processed locally and cleaned up
- **Memory Safety**: Processed data exists only in local memory during conversion
- **File Security**: No files are uploaded or shared externally

This makes the skill ideal for:
- Confidential business documents
- Personal sensitive information
- Government and military applications
- Healthcare and legal documents
- Intellectual property and trade secrets