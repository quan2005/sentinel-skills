# Usage Examples

This document provides practical examples of using the Document Converter skill for various scenarios.

## Basic Web Page Conversion

### Convert a Blog Post
```bash
python scripts/converter.py "https://blog.samaltman.com/"
```

### Convert with Custom Output File
```bash
python scripts/converter.py "https://paulgraham.com/articles.html" --output "pg_articles.md"
```

### Convert JSON Response
```bash
python scripts/converter.py "https://example.com" --json
```

## Advanced Web Page Processing

### Clean Article Extraction
```bash
python scripts/converter.py "https://news.example.com/article" \
  --target-selector "article" \
  --remove-selector "nav, .ads, .social, .comments, .related" \
  --remove-images
```

### Documentation Site Processing
```bash
python scripts/converter.py "https://docs.example.com/guide" \
  --target-selector ".markdown-body, .documentation" \
  --remove-selector ".sidebar, .navigation, .toc" \
  --smart-selector \
  --timeout 45000
```

### Handle Complex JavaScript Pages
```bash
python scripts/converter.py "https://app.example.com" \
  --with-shadow-dom \
  --with-iframe \
  --timeout 60000
```

### Process Shortened URLs
```bash
python scripts/converter.py "https://bit.ly/example" \
  --follow-redirects
```

## File Conversion Examples

### Convert PDF to Markdown
```bash
python scripts/converter.py "document.pdf" --output "document.md"
```

### Convert PowerPoint with Image Descriptions
```bash
python scripts/converter.py "presentation.pptx" \
  --describe-images \
  --output "slides_with_descriptions.md"
```

### Convert Word Document
```bash
python scripts/converter.py "report.docx" \
  --target-selector ".content" \
  --remove-images \
  --output "report_text.md"
```

### Fast PDF Text Extraction
```bash
python scripts/converter.py "large_document.pdf" \
  --pdf-fast-parse \
  --timeout 60000 \
  --output "large_document_text.md"
```

## Network and Performance Options

### Use Proxy for Restricted Content
```bash
python scripts/converter.py "https://internal.company.com" \
  --proxy-url "http://proxy.company.com:8080"
```

### Handle Slow Pages
```bash
python scripts/converter.py "https://slow.example.com" \
  --timeout 60000
```

### Use Test Environment
```bash
python scripts/converter.py "https://example.com" --test
```

## Complex Combinations

### Academic Paper Processing
```bash
python scripts/converter.py "https://arxiv.org/abs/2301.07041" \
  --target-selector ".ltx_page_main" \
  --remove-selector ".ltx_page_nav, .abs affiliations" \
  --describe-images \
  --timeout 45000 \
  --output "academic_paper.md"
```

### E-commerce Product Page
```bash
python scripts/converter.py "https://shop.example.com/product" \
  --target-selector ".product-description, .specifications" \
  --remove-selector ".reviews, .related-products, .ads" \
  --remove-images \
  --output "product_info.md"
```

### News Article Extraction
```bash
python scripts/converter.py "https://news.example.com/story" \
  --target-selector "article" \
  --remove-selector "header, footer, .sidebar, .newsletter, .trending" \
  --smart-selector \
  --timeout 30000 \
  --output "news_article.md"
```

### Technical Documentation
```bash
python scripts/converter.py "https://docs.example.com/api" \
  --target-selector ".api-docs, .markdown-body" \
  --remove-selector ".navigation, .breadcrumb, .edit-link" \
  --with-iframe \
  --timeout 45000 \
  --output "api_docs.md"
```

## Troubleshooting Examples

### When No Content is Extracted
```bash
# Try different approaches
python scripts/converter.py "https://example.com" --no-smart-selector
python scripts/converter.py "https://example.com" --target-selector "body"
python scripts/converter.py "https://example.com" --target-selector "main, .content, article"
```

### When Processing Times Out
```bash
# Simplify the page
python scripts/converter.py "https://complex.example.com" \
  --remove-selector "script, .ads, .social, .videos" \
  --timeout 60000

# Try fast processing
python scripts/converter.py "document.pdf" --pdf-fast-parse
```

### When Images Cause Issues
```bash
# Remove images completely
python scripts/converter.py "https://image-heavy.example.com" --remove-images

# Or describe images instead
python scripts/converter.py "https://image-heavy.example.com" --describe-images --remove-images
```

## Batch Processing (Bash Script)

```bash
#!/bin/bash
# batch_convert.sh - Convert multiple URLs

urls=(
  "https://blog.example.com/post1"
  "https://blog.example.com/post2"
  "https://docs.example.com/guide"
  "https://news.example.com/story"
)

for url in "${urls[@]}"; do
  echo "Converting: $url"
  python scripts/converter.py "$url" \
    --target-selector "article, .content" \
    --remove-selector "nav, .ads, .social" \
    --timeout 30000 \
    --output "converted/$(basename "$url").md"
done
```

## Python Integration

```python
#!/usr/bin/env python3
# convert_multiple.py - Python script for batch conversion

import sys
import os
sys.path.append('scripts')
from converter import DocumentConverter

def convert_urls(urls, output_dir="converted"):
    converter = DocumentConverter()

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for url in urls:
        print(f"Converting: {url}")
        result = converter.convert_url_get(
            url,
            target_selector="article, .content",
            remove_selector="nav, .ads, .social",
            timeout=30000
        )

        if result.get('status') == 'success':
            filename = url.replace('https://', '').replace('/', '_') + '.md'
            filepath = os.path.join(output_dir, filename)

            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(result.get('content', ''))
            print(f"✅ Saved to: {filepath}")
        else:
            print(f"❌ Failed: {result.get('error')}")

if __name__ == '__main__':
    urls = [
        "https://blog.example.com/post1",
        "https://docs.example.com/guide"
    ]
    convert_urls(urls)
```

## Integration with Other Tools

### Combine with Pandoc for Further Processing
```bash
# Convert to Markdown, then to other formats
python scripts/converter.py "https://example.com" --output temp.md
pandoc temp.md -o output.docx
pandoc temp.md -o output.pdf
pandoc temp.md -o output.html
```

### Use with Git for Documentation Backup
```bash
# Convert documentation site and commit to git
python scripts/converter.py "https://docs.example.com" --output docs.md
git add docs.md
git commit -m "Update documentation from website"
git push
```

### Integrate with Obsidian
```bash
# Convert web content to Obsidian vault
python scripts/converter.py "https://example.com" \
  --output "~/Obsidian/Vault/Web Content/example.md"
```

## Configuration File Example

Create a `.env` file for default settings:

```bash
# .env
DEFAULT_TIMEOUT=45000
DEFAULT_REMOVE_IMAGES=true
DEFAULT_TARGET_SELECTOR=article
DEFAULT_REMOVE_SELECTOR=nav, .ads, .social
PROXY_URL=http://proxy.company.com:8080
USE_TEST_ENV=false
```

Then use with a wrapper script:

```python
#!/usr/bin/env python3
# convert_with_config.py

import os
from dotenv import load_dotenv
from converter import DocumentConverter

load_dotenv()

def convert_with_defaults(url, **options):
    # Set defaults from environment
    defaults = {
        'timeout': os.getenv('DEFAULT_TIMEOUT', 30000),
        'remove_images': os.getenv('DEFAULT_REMOVE_IMAGES', 'false').lower() == 'true',
        'target_selector': os.getenv('DEFAULT_TARGET_SELECTOR'),
        'remove_selector': os.getenv('DEFAULT_REMOVE_SELECTOR'),
        'proxy_url': os.getenv('PROXY_URL'),
    }

    # Override defaults with provided options
    defaults.update(options)

    # Remove None values
    defaults = {k: v for k, v in defaults.items() if v is not None}

    base_url = "http://knowledge-reader.external.bdp-testing-streaming.k8s.skyengine.com.cn:8000" \
        if os.getenv('USE_TEST_ENV', 'false').lower() == 'true' \
        else "https://reader-aigc.skyengine.com.cn"

    converter = DocumentConverter(base_url)
    return converter.convert_url_get(url, **defaults)

# Usage
result = convert_with_defaults(
    "https://example.com",
    describe_images=True,
    output_file="example.md"
)
```

## Best Practices Summary

1. **Start Simple**: Use default options first, then add complexity as needed
2. **Be Specific**: Use precise CSS selectors for better content extraction
3. **Handle Timeouts**: Set appropriate timeouts for page complexity
4. **Manage Images**: Remove images for speed or describe them for accessibility
5. **Test Thoroughly**: Try different selector combinations for best results
6. **Use JSON Output**: Enable JSON output for debugging and metadata
7. **Implement Error Handling**: Check status codes and handle errors gracefully
8. **Consider Performance**: Balance extraction quality with processing time