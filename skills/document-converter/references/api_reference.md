# API Reference

Document Converter API reference for the content parsing service.

## Base URLs

- **Production**: `https://reader-aigc.skyengine.com.cn`
- **Testing**: `http://knowledge-reader.external.bdp-testing-streaming.k8s.skyengine.com.cn:8000`

## Authentication

Currently no authentication required. Token-based authentication may be added in future versions.

## Endpoints

### GET /{encoded_url}

Convert a web page by appending the URL (URL-encoded) to the base URL.

**URL Encoding**: The target URL must be URL-encoded, preserving safe characters: `:/?#[]@!$&'()*+,;=`

**Example**:
```bash
curl -X GET "https://reader-aigc.skyengine.com.cn/https%3A%2F%2Fblog.samaltman.com"
```

### POST / (JSON Body)

Convert a URL by sending JSON payload.

**Request Body**:
```json
{
  "url": "https://example.com/page"
}
```

**Example**:
```bash
curl -X POST "https://reader-aigc.skyengine.com.cn" \
  -H "Content-Type: application/json" \
  -d '{"url":"https://example.com"}'
```

### POST / (Multipart Form)

Upload a local file for conversion.

**Form Fields**:
- `file`: File to upload (PDF, PPT, DOCX, etc.)

**Example**:
```bash
curl -X POST "https://reader-aigc.skyengine.com.cn" \
  -F "file=@document.pdf"
```

## Request Headers

### Content Processing Headers

| Header | Default | Values | Description |
|--------|---------|--------|-------------|
| `X-Remove-Images` | `true` | `true`, `false` | Remove all images from output |
| `X-Describe-Images` | `false` | `true`, `false` | Use AI to describe images in text |
| `X-Smart-Selector` | `true` | `true`, `false` | Enable smart content extraction |
| `X-Pdf-Fast-Parse` | `false` | `true`, `false` | Fast PDF parsing (text only) |

### Content Targeting Headers

| Header | Default | Values | Description |
|--------|---------|--------|-------------|
| `X-Target-Selector` | `body > div` | CSS Selector | CSS selector for target content |
| `X-Remove-Selector` | `header` | CSS Selector | CSS selector for elements to remove |

### Advanced Processing Headers

| Header | Default | Values | Description |
|--------|---------|--------|-------------|
| `X-With-Iframe` | `false` | `true`, `false` | Parse iframe content |
| `X-With-Shadow-Dom` | `false` | `true`, `false` | Parse Shadow DOM content |
| `X-Follow-Redirects` | `false` | `true`, `false` | Follow redirects to final URL |

### Network and Performance Headers

| Header | Default | Range | Description |
|--------|---------|-------|-------------|
| `X-Timeout` | `30000` | 1000-60000 | Page load timeout in milliseconds |
| `X-Proxy-Url` | `null` | Valid proxy URL | Route requests through proxy |

### Response Format Headers

| Header | Default | Values | Description |
|--------|---------|--------|-------------|
| `Accept` | `text/plain` | `application/json`, `text/plain` | Response format preference |

## Response Formats

### Plain Text Response (Default)

```
# Document Title

Document content converted to Markdown format...

## Section Header

More content here...
```

### JSON Response (with `Accept: application/json`)

```json
{
  "url": "https://example.com",
  "title": "Example Page Title",
  "content": "# Example Page Title\n\nContent in Markdown format...",
  "timestamp": "Wed, 21 Oct 2023 07:28:00 GMT"
}
```

### File Upload Response

```json
{
  "original_file": "document.pdf",
  "title": "Document Title",
  "content": "# Document Title\n\nExtracted content...",
  "file_size": 1048576,
  "status": "success"
}
```

## Error Responses

### HTTP Status Codes

| Status Code | Meaning | Common Causes |
|-------------|---------|---------------|
| 200 | Success | Conversion completed successfully |
| 400 | Bad Request | Invalid URL format, malformed request |
| 408 | Request Timeout | Page loading timeout |
| 413 | Payload Too Large | File size exceeds limit |
| 500 | Internal Server Error | Service error |
| 502 | Bad Gateway | Service unavailable |

### Error Response Format

```json
{
  "status": "error",
  "error_code": 400,
  "error": "Invalid URL format",
  "url": "https://invalid-url"
}
```

## Rate Limits and Quotas

- **Request Rate**: No explicit rate limiting currently enforced
- **File Size**: Recommended maximum 50MB per file
- **Timeout**: Maximum 60 seconds per request
- **Concurrent Requests**: Limited by service capacity

## Caching

- **Enabled**: Automatic caching for repeated requests
- **Cache Duration**: Varies by content type and update frequency
- **Cache Invalidation**: Manual cache invalidation not available
- **Cache Bypass**: No cache bypass headers available

## Supported File Types

### Web Content
- HTML pages
- Single Page Applications (SPAs)
- Pages with JavaScript rendering
- Pages with iframes (when enabled)
- Shadow DOM content (when enabled)

### Document Formats
- PDF files (.pdf)
- PowerPoint presentations (.ppt, .pptx)
- Word documents (.doc, .docx)
- Plain text files (.txt)
- Rich text format (.rtf)

### Unsupported Content
- Password-protected files
- Encrypted documents
- Feishu documents (require OAuth)
- Content requiring specific browser plugins

## Browser Compatibility

The service uses a headless browser engine that supports:
- Modern JavaScript (ES6+)
- CSS3 and modern web standards
- Canvas and WebGL rendering
- Local storage and session storage
- Cookies and authentication headers

## Regional Restrictions

- **China Mainland**: Full service availability
- **International**: Service availability may vary
- **Corporate Networks**: May require proxy configuration
- **Firewall Restrictions**: Some corporate firewalls may block access