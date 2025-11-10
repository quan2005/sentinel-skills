# Conversion Options Guide

Complete guide to available conversion options for fine-tuning content extraction and processing.

## Overview

The Document Converter supports numerous options for controlling how content is extracted, processed, and formatted. These options can be specified via HTTP headers or command-line arguments.

## Content Processing Options

### Image Handling

#### `X-Remove-Images` / `--remove-images`
**Purpose**: Remove all images from the output Markdown

**Values**:
- `true` (default): Remove images
- `false`: Keep images as Markdown image links

**Use Cases**:
- Reduce file size and processing time
- Focus on text content only
- Faster conversion for image-heavy pages

**Examples**:
```bash
# Remove images (default)
python scripts/converter.py "https://news.example.com" --remove-images

# Keep images
python scripts/converter.py "https://news.example.com" --no-remove-images
```

#### `X-Describe-Images` / `--describe-images`
**Purpose**: Use AI to generate text descriptions for images

**Values**:
- `false` (default): Don't describe images
- `true`: Generate AI descriptions for images

**Use Cases**:
- Make content accessible for screen readers
- Preserve image information when removing images
- Create text-only documentation

**Examples**:
```bash
# Generate AI descriptions for images
python scripts/converter.py "https://tutorial.example.com" --describe-images --remove-images
```

### Smart Content Extraction

#### `X-Smart-Selector` / `--smart-selector`
**Purpose**: Enable intelligent main content detection

**Values**:
- `true` (default): Use smart extraction
- `false`: Disable smart extraction

**How it Works**:
- Analyzes page structure to identify main content areas
- Filters out navigation, headers, footers, advertisements
- Uses machine learning models trained on web page patterns

**Use Cases**:
- Extract clean article content from news sites
- Remove boilerplate content from blog posts
- Focus on documentation content

**Examples**:
```bash
# Use smart extraction (default)
python scripts/converter.py "https://blog.example.com" --smart-selector

# Disable smart extraction
python scripts/converter.py "https://blog.example.com" --no-smart-selector
```

## CSS Selector Options

### Target Content Selection

#### `X-Target-Selector` / `--target-selector`
**Purpose**: Specify CSS selector for content to extract

**Common Selectors**:
- `article`: Extract article elements
- `.content`, `.main-content`: Extract main content areas
- `.post-body`, `.entry-content`: Extract blog post content
- `#main`, `#content`: Extract elements by ID
- `.documentation`, `.docs`: Extract documentation sections

**Advanced Selectors**:
- `main article`: Article elements within main
- `.content > p`: Direct paragraphs in content area
- `[role="main"]`: Elements with main ARIA role
- `.markdown-body, .md-content`: Markdown content areas

**Examples**:
```bash
# Extract article content only
python scripts/converter.py "https://news.example.com" --target-selector "article"

# Extract specific documentation section
python scripts/converter.py "https://docs.example.com" --target-selector ".documentation"

# Multiple selectors (comma-separated)
python scripts/converter.py "https://example.com" --target-selector "main, .content, article"
```

#### `X-Remove-Selector` / `--remove-selector`
**Purpose**: Specify CSS selectors for elements to remove

**Common Removal Targets**:
- `nav, header, footer`: Navigation and layout elements
- `.sidebar, .menu`: Side navigation elements
- `.ads, .advertisement, .sponsored`: Advertisement content
- `.social, .share-buttons`: Social media widgets
- `.comments, .related`: User interaction elements
- `.breadcrumb, .pagination`: Navigation helpers

**Advanced Removal**:
- `script, style, noscript`: Code and style elements
- `[class*="ad"], [id*="ad"]`: Elements with ad-related classes/IDs
- `.popup, .modal, .overlay`: Overlay elements
- `.cookie-banner, .privacy-notice`: Cookie notices

**Examples**:
```bash
# Remove navigation and footer
python scripts/converter.py "https://example.com" --remove-selector "nav, footer, .sidebar"

# Remove advertisements and social widgets
python scripts/converter.py "https://news.example.com" --remove-selector ".ads, .social, .related"

# Complex removal pattern
python scripts/converter.py "https://example.com" --remove-selector "nav, header, footer, .ads, .sidebar, .comments, script, style"
```

## Advanced Processing Options

### Embedded Content

#### `X-With-Iframe` / `--with-iframe`
**Purpose**: Parse and extract content from iframes

**Values**:
- `false` (default): Skip iframe content
- `true`: Parse iframe content

**Use Cases**:
- Extract content from embedded documents
- Parse embedded videos and media
- Handle iframe-based documentation systems

**Limitations**:
- Same-origin policy restrictions
- Increased processing time
- Some iframes may be inaccessible

**Examples**:
```bash
# Parse iframe content
python scripts/converter.py "https://docs.example.com" --with-iframe
```

#### `X-With-Shadow-DOM` / `--with-shadow-dom`
**Purpose**: Parse Shadow DOM content from web components

**Values**:
- `false` (default): Skip Shadow DOM
- `true`: Parse Shadow DOM content

**Use Cases**:
- Extract content from modern web applications
- Parse content from component-based frameworks
- Handle custom element content

**Examples**:
```bash
# Parse Shadow DOM content
python scripts/converter.py "https://app.example.com" --with-shadow-dom
```

### URL Handling

#### `X-Follow-Redirects` / `--follow-redirects`
**Purpose**: Follow URL redirects to final destination

**Values**:
- `false` (default): Don't follow redirects
- `true`: Follow all redirects

**Use Cases**:
- Handle shortened URLs (bit.ly, t.co)
- Follow content management system redirects
- Resolve canonical URLs

**Examples**:
```bash
# Follow redirects to final URL
python scripts/converter.py "https://bit.ly/example" --follow-redirects
```

## Performance and Network Options

### Timeout Configuration

#### `X-Timeout` / `--timeout`
**Purpose**: Set maximum page load time

**Range**: 1000-60000 milliseconds (1-60 seconds)
**Default**: 30000 milliseconds (30 seconds)

**Recommended Values**:
- `15000`: Fast pages, simple content
- `30000`: Standard web pages (default)
- `45000`: Complex pages with lots of content
- `60000`: Very slow or complex pages

**Use Cases**:
- Increase timeout for slow-loading pages
- Decrease timeout for faster processing
- Handle pages with heavy JavaScript

**Examples**:
```bash
# 45 second timeout for complex pages
python scripts/converter.py "https://slow.example.com" --timeout 45000

# 15 second timeout for faster processing
python scripts/converter.py "https://fast.example.com" --timeout 15000
```

### Proxy Configuration

#### `X-Proxy-Url` / `--proxy-url`
**Purpose**: Route requests through proxy server

**Format**: Standard proxy URL (`http://proxy.example.com:8080`)

**Use Cases**:
- Access content behind corporate firewalls
- Bypass geographic restrictions
- Route through specific network paths

**Examples**:
```bash
# Use proxy for restricted content
python scripts/converter.py "https://internal.example.com" --proxy-url "http://proxy.company.com:8080"
```

## File Processing Options

### PDF Processing

#### `X-Pdf-Fast-Parse` / `--pdf-fast-parse`
**Purpose**: Use fast PDF parsing (text extraction only)

**Values**:
- `false` (default): Full PDF processing with layout
- `true`: Fast text-only extraction

**Use Cases**:
- Large PDF files where only text is needed
- Faster processing for text-heavy documents
- When layout and formatting are not important

**Trade-offs**:
- Faster processing
- May lose some formatting
- Better for text extraction accuracy

**Examples**:
```bash
# Fast PDF text extraction
python scripts/converter.py "document.pdf" --pdf-fast-parse
```

## Response Format Options

### JSON vs Plain Text

#### `Accept` Header / `--json`
**Purpose**: Choose response format

**Values**:
- `text/plain` (default): Plain Markdown text
- `application/json`: JSON format with metadata

**JSON Response Includes**:
- Original URL or filename
- Extracted title
- Markdown content
- Timestamp (for web pages)
- File size (for file uploads)
- Processing status

**Use Cases**:
- Need metadata about the conversion
- Programmatic processing of results
- Debugging conversion issues

**Examples**:
```bash
# Get JSON response with metadata
python scripts/converter.py "https://example.com" --json
```

## Combination Examples

### Clean Article Extraction
```bash
python scripts/converter.py "https://news.example.com/article" \
  --target-selector "article" \
  --remove-selector "nav, .ads, .social, .comments" \
  --remove-images \
  --timeout 45000
```

### Documentation Site Processing
```bash
python scripts/converter.py "https://docs.example.com" \
  --target-selector ".documentation, .markdown-body" \
  --remove-selector ".sidebar, .navigation, .footer" \
  --smart-selector \
  --with-iframe \
  --timeout 30000
```

### PDF to Text Conversion
```bash
python scripts/converter.py "manual.pdf" \
  --pdf-fast-parse \
  --describe-images \
  --json \
  --output "manual.md"
```

### Complex Web Application
```bash
python scripts/converter.py "https://app.example.com" \
  --with-shadow-dom \
  --with-iframe \
  --follow-redirects \
  --timeout 60000 \
  --proxy-url "http://proxy.company.com:8080"
```

## Best Practices

1. **Start Simple**: Begin with default options, add complexity as needed
2. **Test Incrementally**: Add options one at a time to see effects
3. **Use Selectors Wisely**: Be specific with CSS selectors to avoid over-inclusion
4. **Timeout Management**: Set appropriate timeouts for page complexity
5. **Consider Performance**: More options may increase processing time
6. **Validate Results**: Check output quality and adjust options accordingly

## Troubleshooting

### Common Issues

- **No Content Extracted**: Try disabling smart selector or using target selector
- **Processing Timeout**: Increase timeout value or simplify with remove selector
- **Missing Images**: Check remove-images and describe-images settings
- **Poor Content Quality**: Adjust target/remove selectors for better extraction
- **Slow Processing**: Remove unnecessary options like iframe/shadow-dom parsing

### Debug Strategy

1. Start with minimal options
2. Add options incrementally
3. Use JSON output to see metadata
4. Test with different selector combinations
5. Check service logs if available