# Error Handling Guide

Comprehensive guide to error codes, troubleshooting steps, and common solutions for document conversion issues.

## Error Classification

Errors are categorized into four main types:
1. **Client Errors (4xx)**: Issues with request format or input
2. **Server Errors (5xx)**: Service-side problems
3. **Network Errors**: Connection and timeout issues
4. **Content Errors**: Issues with the content being processed

## HTTP Status Codes

### 400 Bad Request

**Description**: The request format is invalid or malformed.

**Common Causes**:
- Invalid URL format
- Malformed JSON payload
- Missing required parameters
- Invalid header values

**Troubleshooting Steps**:
1. Check URL format and encoding
2. Verify JSON payload structure
3. Ensure all required headers are present
4. Validate parameter values

**Example Error**:
```json
{
  "status": "error",
  "error_code": 400,
  "error": "Invalid URL format",
  "url": "invalid-url"
}
```

**Solutions**:
```bash
# Bad: Invalid URL
python scripts/converter.py "invalid-url"

# Good: Proper URL
python scripts/converter.py "https://example.com"
```

### 401 Unauthorized

**Description**: Authentication required but not provided.

**Current Status**: Not implemented in current service version.
**Future Implementation**: Token-based authentication may be added.

### 403 Forbidden

**Description**: Access to the resource is forbidden.

**Common Causes**:
- Blocked by firewall or security policy
- Geographic restrictions
- Corporate network restrictions

**Troubleshooting Steps**:
1. Try using a proxy server
2. Check if the URL is accessible from browser
3. Verify network connectivity
4. Contact IT department if on corporate network

**Solutions**:
```bash
# Use proxy for restricted access
python scripts/converter.py "https://restricted.example.com" --proxy-url "http://proxy.company.com:8080"
```

### 404 Not Found

**Description**: The requested resource or file does not exist.

**Common Causes**:
- URL is incorrect or page doesn't exist
- Local file path is wrong
- Content has been moved or deleted

**Troubleshooting Steps**:
1. Verify URL spelling and correctness
2. Check if file exists at specified path
3. Try accessing URL in browser
4. Look for alternative URLs

**Examples**:
```bash
# File not found
python scripts/converter.py "nonexistent.pdf"

# URL not found
python scripts/converter.py "https://example.com/nonexistent-page"
```

### 408 Request Timeout

**Description**: The request took too long to complete.

**Common Causes**:
- Page is very slow to load
- Complex JavaScript rendering
- Large file processing
- Network connectivity issues

**Troubleshooting Steps**:
1. Increase timeout value
2. Use remove-selector to simplify page
3. Try processing smaller files
4. Check network connection

**Solutions**:
```bash
# Increase timeout for slow pages
python scripts/converter.py "https://slow.example.com" --timeout 60000

# Simplify page to reduce processing time
python scripts/converter.py "https://complex.example.com" \
  --remove-selector "script, .ads, .social" \
  --timeout 45000
```

### 413 Payload Too Large

**Description**: The uploaded file exceeds size limits.

**Current Limit**: Recommended maximum 50MB per file.

**Common Causes**:
- File is larger than 50MB
- Memory constraints during processing

**Troubleshooting Steps**:
1. Check file size
2. Split large documents if possible
3. Use pdf-fast-parse for large PDFs
4. Compress images in documents

**Solutions**:
```bash
# Fast processing for large PDFs
python scripts/converter.py "large-document.pdf" \
  --pdf-fast-parse \
  --remove-images
```

### 500 Internal Server Error

**Description**: Unexpected error occurred on the server.

**Common Causes**:
- Service temporarily unavailable
- Content parsing errors
- Resource constraints on server

**Troubleshooting Steps**:
1. Wait and retry after a few minutes
2. Try using test environment
3. Simplify request parameters
4. Check service status if available

**Solutions**:
```bash
# Retry after delay
python scripts/converter.py "https://example.com"

# Use test environment if available
python scripts/converter.py "https://example.com" --test
```

### 502 Bad Gateway

**Description**: Server received invalid response from upstream service.

**Common Causes**:
- Service maintenance or restart
- Overloaded service
- Network issues between services

**Troubleshooting Steps**:
1. Wait and retry
2. Check service status
3. Use test environment
4. Report issue if persistent

### 503 Service Unavailable

**Description**: Service is temporarily unavailable.

**Common Causes**:
- Scheduled maintenance
- High load or resource exhaustion
- Service scaling issues

**Troubleshooting Steps**:
1. Wait and retry with exponential backoff
2. Check for maintenance announcements
3. Use test environment if available

### 504 Gateway Timeout

**Description**: Gateway timed out waiting for upstream service.

**Common Causes**:
- Complex content processing
- Server resource constraints
- Network timeouts between services

**Troubleshooting Steps**:
1. Increase client timeout
2. Simplify content extraction
3. Retry with different parameters

## Content-Specific Errors

### No Content Extracted

**Symptoms**: Successful response but empty or minimal content.

**Common Causes**:
- Smart selector failed to identify main content
- CSS selectors are too restrictive
- Content is loaded via JavaScript and not captured
- Page structure is unusual

**Troubleshooting Steps**:
1. Disable smart selector: `--no-smart-selector`
2. Use broader target selector
3. Enable iframe/shadow-dom parsing
4. Increase timeout for JavaScript rendering

**Solutions**:
```bash
# Try different extraction approaches
python scripts/converter.py "https://example.com" --no-smart-selector
python scripts/converter.py "https://example.com" --target-selector "body"
python scripts/converter.py "https://example.com" --with-shadow-dom --timeout 45000
```

### Poor Content Quality

**Symptoms**: Content extracted but contains unwanted elements or missing important parts.

**Common Causes**:
- Incorrect CSS selectors
- Missing remove-selector for unwanted content
- Smart selector confused by page structure

**Troubleshooting Steps**:
1. Inspect page structure in browser dev tools
2. Adjust target and remove selectors
3. Combine smart selector with manual selectors
4. Test with different selector combinations

**Solutions**:
```bash
# Fine-tune content extraction
python scripts/converter.py "https://example.com" \
  --target-selector ".article-content, main" \
  --remove-selector "nav, .ads, .sidebar, footer"

# Combine extraction methods
python scripts/converter.py "https://example.com" \
  --smart-selector \
  --target-selector ".post-content" \
  --remove-selector ".related, .comments"
```

### Image Processing Issues

**Symptoms**: Images not handled as expected, broken image links.

**Common Causes**:
- Remove images option conflicts
- Image description generation failures
- Image URLs are relative or blocked

**Troubleshooting Steps**:
1. Check remove-images setting
2. Verify describe-images option
3. Inspect image URLs in source
4. Consider content without images

**Solutions**:
```bash
# Handle images differently
python scripts/converter.py "https://example.com" --remove-images
python scripts/converter.py "https://example.com" --describe-images
python scripts/converter.py "https://example.com" --no-remove-images
```

## File Processing Errors

### PDF Processing Issues

**Common Causes**:
- Password-protected PDFs
- Corrupted PDF files
- Very large PDF files
- Scanned image-based PDFs

**Solutions**:
```bash
# Try different PDF processing modes
python scripts/converter.py "document.pdf" --pdf-fast-parse
python scripts/converter.py "document.pdf" --timeout 60000
```

### Office Document Issues

**Common Causes**:
- Corrupted DOCX/PPTX files
- Very old file formats
- Files with macros or complex formatting

**Solutions**:
```bash
# Try with increased timeout
python scripts/converter.py "presentation.pptx" --timeout 60000

# Remove images for faster processing
python scripts/converter.py "document.docx" --remove-images
```

## Network and Connectivity Issues

### Connection Refused

**Symptoms**: Unable to connect to the service.

**Troubleshooting Steps**:
1. Check internet connection
2. Verify service URL is correct
3. Try alternative service URL
4. Check firewall settings

### DNS Resolution Issues

**Symptoms**: Unable to resolve service hostname.

**Troubleshooting Steps**:
1. Check DNS settings
2. Try using IP address directly
3. Flush DNS cache
4. Use alternative DNS servers

### Proxy Issues

**Symptoms**: Unable to connect through proxy server.

**Troubleshooting Steps**:
1. Verify proxy URL format
2. Check proxy authentication
3. Test proxy connectivity
4. Try without proxy

## Debugging Strategies

### 1. Enable JSON Output

Use JSON output to get detailed error information and metadata:

```bash
python scripts/converter.py "https://example.com" --json
```

### 2. Use Test Environment

Try the testing environment for debugging:

```bash
python scripts/converter.py "https://example.com" --test
```

### 3. Incremental Testing

Start with minimal options and add complexity:

```bash
# Start simple
python scripts/converter.py "https://example.com"

# Add options one by one
python scripts/converter.py "https://example.com" --target-selector "article"
python scripts/converter.py "https://example.com" --target-selector "article" --remove-selector "nav"
```

### 4. Validate Inputs

Check inputs before processing:

```bash
# Verify URL is accessible
curl -I "https://example.com"

# Verify file exists
ls -la document.pdf
```

### 5. Test Selectors

Test CSS selectors in browser console first:

```javascript
// Test target selector
document.querySelectorAll('article')

// Test remove selector
document.querySelectorAll('nav, .ads')
```

## Error Recovery Patterns

### Retry with Exponential Backoff

```python
import time
import random

def convert_with_retry(url, max_retries=3):
    for attempt in range(max_retries):
        result = converter.convert_url_get(url)
        if result.get('status') == 'success':
            return result

        if attempt < max_retries - 1:
            delay = (2 ** attempt) + random.uniform(0, 1)
            time.sleep(delay)

    return result
```

### Fallback Strategies

```bash
# Try multiple approaches
python scripts/converter.py "https://example.com" --smart-selector
python scripts/converter.py "https://example.com" --no-smart-selector --target-selector "body"
python scripts/converter.py "https://example.com" --with-iframe --timeout 60000
```

## Reporting Issues

When reporting persistent issues, include:

1. **Error Information**:
   - Full error message
   - HTTP status code
   - Timestamp of error

2. **Request Details**:
   - URL or file being processed
   - All options/parameters used
   - Service environment (prod/test)

3. **Environment Information**:
   - Network connection type
   - Proxy/firewall configuration
   - Geographic location

4. **Debug Output**:
   - JSON response with `--json` flag
   - Browser screenshots if applicable
   - Network logs if available

## Preventive Measures

### Best Practices

1. **Validate Inputs**: Check URLs and files before processing
2. **Use Appropriate Timeouts**: Set reasonable timeouts for content complexity
3. **Handle Errors Gracefully**: Implement retry logic and fallback strategies
4. **Monitor Performance**: Track processing times and success rates
5. **Test Regularly**: Verify service connectivity and performance

### Monitoring

Set up monitoring for:
- Request success rates
- Average processing times
- Error frequency by type
- Service availability

### Circuit Breaker Pattern

Implement circuit breakers to handle service outages:

```python
class CircuitBreaker:
    def __init__(self, failure_threshold=5, timeout=60):
        self.failure_threshold = failure_threshold
        self.timeout = timeout
        self.failure_count = 0
        self.last_failure_time = None
        self.state = 'closed'  # closed, open, half-open

    def call(self, func, *args, **kwargs):
        if self.state == 'open':
            if time.time() - self.last_failure_time > self.timeout:
                self.state = 'half-open'
            else:
                return {'status': 'error', 'error': 'Circuit breaker is open'}

        try:
            result = func(*args, **kwargs)
            if result.get('status') == 'success':
                self.failure_count = 0
                self.state = 'closed'
            return result
        except Exception as e:
            self.failure_count += 1
            self.last_failure_time = time.time()
            if self.failure_count >= self.failure_threshold:
                self.state = 'open'
            return {'status': 'error', 'error': str(e)}
```