---
name: document-converter
description: Convert PDF, PPT, DOCX, and web pages to Markdown format using a high-performance content parsing service. Handles complex page elements, intelligent content extraction, and advanced processing options.
---

# Document Converter

Convert various document formats and web pages to structured Markdown format with intelligent content extraction and advanced processing capabilities.

## When to Use

Use this skill when users need to:

- Convert web pages (blogs, news, online docs) to Markdown
- Extract content from PDF files as editable Markdown
- Convert PowerPoint presentations to text format
- Transform Word documents to Markdown
- Process complex web pages with iframes or Shadow DOM
- Extract specific content using CSS selectors
- Handle large documents with timeout and proxy options

## How to Use

### Basic Web Page Conversion

To convert a web page URL to Markdown:

1. Use the converter script from `scripts/converter.py`
2. Call with the URL using GET method for simple conversion
3. Receive structured Markdown output with title and content

```bash
python scripts/converter.py "https://blog.samaltman.com"
```

### File Upload Conversion

To convert local files (PDF, PPT, DOCX):

1. Use the converter script with file path
2. Script automatically detects file type and uploads
3. Process returns Markdown with extracted content

```bash
python scripts/converter.py "presentation.pdf" --output slides.md
```

### Advanced Conversion Options

For complex pages requiring specific content extraction:

1. Configure CSS selectors using `--target-selector` and `--remove-selector`
2. Enable iframe parsing with `--with-iframe` for embedded content
3. Use `--follow-redirects` for shortened URLs
4. Adjust timeout with `--timeout` for slow-loading pages

```bash
python scripts/converter.py "https://docs.example.com" \
  --target-selector "article" \
  --remove-selector "nav,footer" \
  --with-iframe \
  --timeout 45000
```

## Core Components

### Scripts

- **`scripts/converter.py`**: Main conversion engine handling URL conversion, file uploads, and advanced options. Supports both GET and POST methods with comprehensive error handling.

### References

- **`references/api_reference.md`**: Detailed API documentation including all endpoints, parameters, headers, and response formats
- **`references/conversion_options.md`**: Complete guide to conversion options, CSS selectors, and advanced features
- **`references/error_handling.md`**: Error codes, troubleshooting steps, and common solutions

### Assets

- **`assets/example_urls.txt`**: Collection of test URLs for different content types
- **`assets/test_documents/`**: Sample files for testing conversion capabilities

## Implementation Workflow

1. **Identify Input Type**: Determine if input is URL or local file
2. **Select Conversion Method**: Choose GET (URL direct), POST (URL via POST), or file upload
3. **Configure Options**: Apply relevant headers and options based on user requirements
4. **Execute Conversion**: Call the parsing service with appropriate parameters
5. **Process Results**: Handle JSON or text responses, extract title and content
6. **Error Handling**: Manage timeouts, invalid URLs, file errors gracefully
7. **Output Formatting**: Return structured results or save to specified file

## Advanced Features

### Content Extraction Control

- **Smart Content Selection**: Automatically identifies main content areas
- **CSS Selector Targeting**: Precise control over which elements to extract
- **Element Removal**: Exclude navigation, footers, advertisements
- **Image Processing**: Options to remove images or generate AI descriptions

### Technical Capabilities

- **iframe Support**: Parse embedded third-party content
- **Shadow DOM Parsing**: Handle modern web components
- **Redirect Following**: Resolve shortened URLs to final destinations
- **Proxy Integration**: Route requests through specific proxies
- **Timeout Management**: Configurable wait times for page loading
- **PDF Fast Parse**: Optimized text-only extraction for large PDFs

### Service Integration

- **Production URL**: https://reader-aigc.skyengine.com.cn
- **Testing URL**: http://knowledge-reader.external.bdp-testing-streaming.k8s.skyengine.com.cn:8000
- **Authentication**: Token not required for current implementation
- **Caching**: Automatic caching for repeated requests
- **Rate Limiting**: Built-in request pooling to prevent blocking

## Error Handling and Troubleshooting

Common error scenarios and solutions:

- **400 Invalid URL**: Check URL encoding and format
- **408 Timeout**: Increase timeout value or simplify target page
- **502 Service Error**: Retry with backoff or contact support
- **File Not Found**: Verify file path and permissions
- **Upload Size**: Check file size limits (recommended <50MB)

Refer to `references/error_handling.md` for detailed troubleshooting steps.

## Best Practices

- Use specific CSS selectors for cleaner content extraction
- Enable image removal for faster processing of image-heavy content
- Set appropriate timeouts for complex pages
- Use test environment for initial development
- Implement retry logic for network errors
- Cache results for frequently accessed content