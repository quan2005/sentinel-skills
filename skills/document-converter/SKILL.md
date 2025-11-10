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

### URL Conversion with Crawl4AI

Convert web pages to Markdown using intelligent crawling:

```bash
python scripts/converter.py "https://example.com/blog"
```

Crawl4AI provides intelligent web page extraction:
- **JavaScript Rendering**: Handles dynamic content and SPAs
- **Content Filtering**: Automatically removes ads and overlays
- **Smart Extraction**: Identifies main content areas
- **Modern Web Support**: Works with React, Vue, Angular applications

## Core Components

### Scripts

- **`scripts/converter.py`**: Local conversion engine using markitdown tool for files and Crawl4AI for URLs. Handles file processing, intelligent web crawling, and advanced conversion options with complete privacy.

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
6. **URL Handling** (if needed): Use Crawl4AI for intelligent web crawling, process locally with JavaScript rendering
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
- **Modern Web Pages**: Processed with Crawl4AI for JavaScript rendering
- **Single Page Applications**: React, Vue, Angular applications
- **Dynamic Content**: Pages with AJAX-loaded content
- **Static HTML**: Traditional web pages
- **Blog Posts**: News articles and blog platforms

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
- **No External Dependencies**: All processing done with installed markitdown tool and Crawl4AI

## Crawl4AI Integration

### Intelligent Web Crawling

Crawl4AI provides advanced web crawling capabilities:

- **JavaScript Rendering**: Full browser automation for dynamic content
- **Content Extraction**: Automatic identification of main content areas
- **Noise Filtering**: Removes ads, popups, and irrelevant elements
- **SPA Support**: Handles modern JavaScript applications
- **Privacy**: All crawling happens locally with headless browser

### Crawl4AI Options

- **`--wait-time`**: Page load wait time in milliseconds (default: 2000)
- **`--remove-overlays`**: Remove popups and overlays (default: enabled)
- **`--simulate-user`**: Simulate user behavior for better access (default: enabled)
- **`--bypass-cache`**: Get fresh content (default: enabled)
- **`--verbose-crawling`**: Enable detailed crawling output

### Advanced URL Processing

```bash
# Basic web page conversion
python scripts/converter.py "https://example.com/article"

# Wait longer for slow-loading pages
python scripts/converter.py "https://slow-site.com" --wait-time 5000

# Preserve overlays for specific sites
python scripts/converter.py "https://example.com" --no-remove-overlays

# Verbose crawling for debugging
python scripts/converter.py "https://example.com" --verbose-crawling --json
```

## Error Handling and Troubleshooting

Common local processing errors and solutions:

- **markitdown not found**: Install with `pip install markitdown`
- **Crawl4AI not found**: Install with `pip install crawl4ai`
- **File not found**: Verify file path and permissions
- **Processing timeout**: File may be too complex or large
- **Crawling failed**: Check URL accessibility and wait time
- **JavaScript errors**: Increase wait time or disable overlay removal
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
# Install markitdown tool for file conversion
pip install markitdown

# Install Crawl4AI for intelligent web crawling
pip install crawl4ai

# Optional: For additional URL handling
pip install requests
```

### System Requirements

- Python 3.7 or higher
- markitdown tool installed and in PATH
- Crawl4AI installed for web crawling
- Sufficient disk space for temporary files
- Appropriate memory for document processing
- Browser dependencies for Crawl4AI (automatically installed)

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

# URL conversion with Crawl4AI crawling
python scripts/converter.py "https://example.com/blog" \
  --output "blog.md"

# URL conversion with custom wait time for slow pages
python scripts/converter.py "https://slow-loading-site.com" \
  --wait-time 5000 \
  --output "content.md"

# URL conversion with verbose output for debugging
python scripts/converter.py "https://example.com" \
  --verbose-crawling \
  --json
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