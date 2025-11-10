# Local Document Converter Usage Examples

This document provides practical examples of using the Document Converter skill with the local markitdown tool for secure, private document processing.

## Basic Local Conversion

### Convert PDF to Markdown
```bash
# Basic PDF conversion
python3 scripts/converter.py "document.pdf"

# Save to specific file
python3 scripts/converter.py "document.pdf" --output "converted.md"

# JSON output with metadata
python3 scripts/converter.py "document.pdf" --json
```

### Convert Office Documents
```bash
# Word document
python3 scripts/converter.py "report.docx" --output "report.md"

# PowerPoint presentation
python3 scripts/converter.py "slides.pptx" --output "slides.md"

# Rich text format
python3 scripts/converter.py "notes.rtf" --output "notes.md"
```

### Convert Image Files with OCR
```bash
# Convert scanned PDF or image
python3 scripts/converter.py "scan.jpg" --output "text_content.md"

# Multiple image formats supported
python3 scripts/converter.py "chart.png" --output "chart_text.md"
```

## Advanced Local Processing

### Use Plugins for Enhanced Conversion
```bash
# Enable third-party plugins
python3 scripts/converter.py "complex_document.pdf" \
  --use-plugins \
  --output "enhanced.md"

# Combine multiple options
python3 scripts/converter.py "presentation.pptx" \
  --use-plugins \
  --keep-data-uris \
  --output "complete_slides.md"
```

### Preserve Images as Data URIs
```bash
# Keep base64-encoded images in output
python3 scripts/converter.py "image_heavy.pdf" \
  --keep-data-uris \
  --output "with_images.md"
```

### Document Intelligence Integration
```bash
# Use Azure Document Intelligence for enhanced OCR
python3 scripts/converter.py "scan.pdf" \
  --use-docintel \
  --endpoint "https://your-endpoint.cognitiveservices.azure.com/" \
  --output "enhanced_ocr.md"
```

### Format Hints for Better Conversion
```bash
# Provide MIME type hint
python3 scripts/converter.py "unknown_file" \
  --mime-type "application/pdf" \
  --output "converted.md"

# Provide character set hint
python3 scripts/converter.py "text_file.txt" \
  --charset "UTF-8" \
  --output "converted.md"
```

## URL Processing with Crawl4AI

### Intelligent Web Crawling
```bash
# Convert web page to Markdown
python3 scripts/converter.py "https://example.com/blog" \
  --output "blog.md"

# Handle JavaScript-heavy pages
python3 scripts/converter.py "https://spa-example.com" \
  --wait-time 5000 \
  --output "spa_content.md"

# Modern web applications
python3 scripts/converter.py "https://react-app.com" \
  --simulate-user \
  --remove-overlays \
  --output "react_content.md"
```

### Advanced Crawling Options
```bash
# Verbose crawling for debugging
python3 scripts/converter.py "https://example.com" \
  --verbose-crawling \
  --json

# Preserve overlays for specific sites
python3 scripts/converter.py "https://news-site.com" \
  --no-remove-overlays \
  --output "news_content.md"

# Use cache for repeated requests
python3 scripts/converter.py "https://example.com" \
  --no-bypass-cache \
  --output "cached_content.md"
```

### Batch URL Processing
```bash
#!/bin/bash
# batch_crawl.sh

urls=(
  "https://example.com/article1"
  "https://example.com/article2"
  "https://news.example.com/story"
)

for url in "${urls[@]}"; do
    echo "Crawling: $url"
    python3 scripts/converter.py "$url" \
      --wait-time 3000 \
      --remove-overlays \
      --output "crawled/$(basename "$url").md"
done
```

### Crawl4AI with File Downloads
```bash
# For URLs that point to downloadable files, Crawl4AI will handle them appropriately
python3 scripts/converter.py "https://example.com/document.pdf" \
  --output "downloaded_doc.md"

# Crawl4AI automatically detects file types and uses appropriate processing
```

## Utility Functions

### Check Supported Formats
```bash
# List all supported file formats
python3 scripts/converter.py --list-formats
```

### Check Markitdown Version
```bash
# Show markitdown version
python3 scripts/converter.py --markitdown-version
```

## Batch Processing Examples

### Process Multiple Files
```bash
#!/bin/bash
# batch_convert.sh

for file in *.pdf *.docx *.pptx; do
    if [ -f "$file" ]; then
        echo "Converting $file..."
        output_name="${file%.*}.md"
        python3 scripts/converter.py "$file" \
          --output "converted/$output_name" \
          --use-plugins
    fi
done
```

### Process with Different Options
```bash
#!/bin/bash
# advanced_batch.sh

# PDFs with plugins
for pdf in *.pdf; do
    python3 scripts/converter.py "$pdf" \
      --use-plugins \
      --output "pdf_converted/${pdf%.pdf}.md"
done

# Images with data URIs preserved
for img in *.jpg *.png; do
    python3 scripts/converter.py "$img" \
      --keep-data-uris \
      --output "img_converted/${img%.*}.md"
done
```

## Python Integration Examples

### Basic Python Usage
```python
#!/usr/bin/env python3
from scripts.converter import DocumentConverter

# Create converter instance
converter = DocumentConverter()

# Convert a file
result = converter.convert_file('document.pdf', use_plugins=True)

if result['status'] == 'success':
    print(f"Title: {result['title']}")
    print(f"File size: {result['file_size']} bytes")
    print(f"Content length: {len(result['content'])} characters")

    # Save content
    with open('output.md', 'w', encoding='utf-8') as f:
        f.write(result['content'])
else:
    print(f"Error: {result['error']}")
```

### Advanced Python Integration
```python
#!/usr/bin/env python3
from scripts.converter import DocumentConverter
import json
from pathlib import Path

def convert_directory(input_dir, output_dir):
    """Convert all supported files in a directory"""
    converter = DocumentConverter()
    input_path = Path(input_dir)
    output_path = Path(output_dir)

    # Create output directory
    output_path.mkdir(exist_ok=True)

    # Supported extensions
    extensions = ['.pdf', '.docx', '.doc', '.pptx', '.ppt', '.txt', '.rtf']

    results = []

    for file_path in input_path.rglob('*'):
        if file_path.suffix.lower() in extensions:
            print(f"Converting {file_path.name}...")

            result = converter.convert_file(
                file_path,
                use_plugins=True,
                keep_data_uris=True
            )

            if result['status'] == 'success':
                # Save converted content
                output_file = output_path / f"{file_path.stem}.md"
                output_file.write_text(result['content'], encoding='utf-8')

                results.append({
                    'original_file': file_path.name,
                    'output_file': str(output_file),
                    'title': result['title'],
                    'file_size': result['file_size']
                })
            else:
                results.append({
                    'original_file': file_path.name,
                    'error': result['error']
                })

    # Save results summary
    with open(output_path / 'conversion_results.json', 'w') as f:
        json.dump(results, f, indent=2)

    return results

# Usage
if __name__ == '__main__':
    results = convert_directory('documents', 'converted_docs')
    print(f"Converted {len([r for r in results if 'error' not in r])} files successfully")
```

## Security and Privacy Examples

### Convert Sensitive Documents
```bash
# All processing happens locally - no external data transmission
python3 scripts/converter.py "confidential_report.pdf" \
  --output "secure_conversion.md"

# Process financial documents privately
python3 scripts/converter.py "financial_data.xlsx" \
  --output "financial_analysis.md"

# Convert legal documents securely
python3 scripts/converter.py "legal_contract.docx" \
  --output "contract_text.md"
```

### Offline Processing
```bash
# Works completely offline - no internet required
python3 scripts/converter.py "local_document.pdf" --output "offline_convert.md"

# Batch process without network access
for file in /path/to/documents/*.{pdf,docx,pptx}; do
    python3 scripts/converter.py "$file" \
      --output "/path/to/converted/$(basename "$file").md"
done
```

## Error Handling Examples

### Robust Error Handling
```python
#!/usr/bin/env python3
from scripts.converter import DocumentConverter
import sys

def safe_convert_with_retry(file_path, max_retries=3):
    """Convert file with retry logic and error handling"""
    converter = DocumentConverter()

    for attempt in range(max_retries):
        try:
            result = converter.convert_file(file_path, use_plugins=True)

            if result['status'] == 'success':
                return result
            else:
                print(f"Attempt {attempt + 1} failed: {result['error']}")

        except Exception as e:
            print(f"Attempt {attempt + 1} error: {str(e)}")

    print(f"Failed to convert {file_path} after {max_retries} attempts")
    return None

# Usage
result = safe_convert_with_retry('problematic_file.pdf')
if result:
    print("Conversion successful!")
else:
    print("Conversion failed")
```

### Validate Before Conversion
```python
#!/usr/bin/env python3
from scripts.converter import DocumentConverter
from pathlib import Path

def validate_and_convert(file_path):
    """Validate file before conversion"""
    file_path = Path(file_path)

    # Check if file exists
    if not file_path.exists():
        return {'error': 'File does not exist'}

    # Check file size (limit to 50MB for example)
    max_size = 50 * 1024 * 1024  # 50MB
    if file_path.stat().st_size > max_size:
        return {'error': f'File too large: {file_path.stat().st_size / (1024*1024):.1f}MB'}

    # Check file extension
    supported_extensions = ['.pdf', '.docx', '.doc', '.pptx', '.ppt', '.txt', '.rtf']
    if file_path.suffix.lower() not in supported_extensions:
        return {'error': f'Unsupported file type: {file_path.suffix}'}

    # Convert if validation passes
    converter = DocumentConverter()
    return converter.convert_file(file_path)

# Usage
result = validate_and_convert('document.pdf')
if result['status'] == 'success':
    print("Conversion successful!")
else:
    print(f"Validation failed: {result['error']}")
```

## Performance Optimization Examples

### Large File Processing
```bash
# Process large files with specific settings
python3 scripts/converter.py "large_document.pdf" \
  --timeout 600 \
  --output "large_converted.md"

# Monitor memory usage (Linux/macOS)
python3 scripts/converter.py "huge_file.pdf" &
PID=$!
while kill -0 $PID 2>/dev/null; do
    ps -p $PID -o pid,ppid,cmd,%mem,%cpu --no-headers
    sleep 5
done
```

### Parallel Processing
```python
#!/usr/bin/env python3
import concurrent.futures
from scripts.converter import DocumentConverter
from pathlib import Path

def parallel_convert(file_paths, max_workers=4):
    """Convert multiple files in parallel"""
    converter = DocumentConverter()

    def convert_single(file_path):
        return converter.convert_file(file_path, use_plugins=True)

    with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures = {executor.submit(convert_single, path): path for path in file_paths}

        results = {}
        for future in concurrent.futures.as_completed(futures):
            file_path = futures[future]
            try:
                result = future.result()
                results[file_path] = result
            except Exception as e:
                results[file_path] = {'error': str(e)}

    return results

# Usage
if __name__ == '__main__':
    file_paths = list(Path('documents').glob('*.pdf'))
    results = parallel_convert(file_paths[:10])  # Process first 10 files

    for file_path, result in results.items():
        if result['status'] == 'success':
            print(f"✅ {file_path.name}: Conversion successful")
        else:
            print(f"❌ {file_path.name}: {result['error']}")
```

## Integration with Workflows

### Git Hook Integration
```bash
#!/bin/bash
# .git/hooks/pre-commit - Convert documents before commit

# Convert any PDFs in the commit
for pdf in $(git diff --cached --name-only --diff-filter=ACM | grep '\.pdf$'); do
    echo "Converting $pdf to Markdown..."
    python3 scripts/converter.py "$pdf" \
      --output "docs/${pdf%.pdf}.md"
    git add "docs/${pdf%.pdf}.md"
done

exit 0
```

### Makefile Integration
```makefile
# Makefile for document processing

.PHONY: convert-docs clean-docs

DOCS_DIR = documents
OUTPUT_DIR = converted

convert-docs:
	@echo "Converting all documents..."
	@mkdir -p $(OUTPUT_DIR)
	@for file in $(DOCS_DIR)/*.{pdf,docx,pptx,txt}; do \
		if [ -f "$$file" ]; then \
			echo "Converting $$file..."; \
			python3 scripts/converter.py "$$file" \
				--output "$(OUTPUT_DIR)/$$(basename $$file | cut -d. -f1).md"; \
		fi; \
	done

clean-docs:
	@echo "Cleaning converted files..."
	@rm -rf $(OUTPUT_DIR)

help:
	@echo "Available targets:"
	@echo "  convert-docs - Convert all documents to Markdown"
	@echo "  clean-docs   - Remove converted files"
	@echo "  help         - Show this help"
```

### CI/CD Pipeline Integration
```yaml
# .github/workflows/convert-docs.yml
name: Convert Documents

on:
  push:
    paths:
      - 'documents/**'
    branches: [ main ]

jobs:
  convert:
    runs-on: ubuntu-latest

    steps:
    - uses: actions/checkout@v2

    - name: Set up Python
      uses: actions/setup-python@v2
      with:
        python-version: '3.9'

    - name: Install markitdown
      run: pip install markitdown

    - name: Convert documents
      run: |
        mkdir -p converted_docs
        for file in documents/*.{pdf,docx,pptx,txt}; do
          if [ -f "$file" ]; then
            python3 skills/document-converter/scripts/converter.py "$file" \
              --output "converted_docs/$(basename "$file" | cut -d. -f1).md"
          fi
        done

    - name: Upload converted documents
      uses: actions/upload-artifact@v2
      with:
        name: converted-documents
        path: converted_docs/
```

## Troubleshooting Examples

### Debug Conversion Issues
```bash
# Check markitdown installation
which markitdown
markitdown --version

# Test with simple file
echo "Test content" > test.txt
python3 scripts/converter.py test.txt --json

# Check file permissions
ls -la document.pdf

# Test different options
python3 scripts/converter.py problem_file.pdf --use-plugins
python3 scripts/converter.py problem_file.pdf --keep-data-uris
```

### Monitor Resource Usage
```bash
# Monitor conversion process
python3 scripts/converter.py large_file.pdf &
PID=$!
top -pid $PID

# Check disk space during conversion
df -h

# Check memory usage
ps aux | grep python3
```

## Best Practices Summary

### Security
1. **Always process locally**: No external data transmission
2. **Clean temporary files**: Automatic cleanup of downloads
3. **Check file permissions**: Ensure proper access rights
4. **Validate inputs**: Check file size and format before processing

### Performance
1. **Use appropriate options**: Enable plugins only when needed
2. **Monitor resources**: Watch memory and disk usage for large files
3. **Batch efficiently**: Process multiple files with consistent options
4. **Handle timeouts**: Set appropriate timeout values for large documents

### Quality
1. **Test conversion quality**: Validate output for critical documents
2. **Use format hints**: Provide MIME types for unknown files
3. **Preserve data URIs**: Keep images when needed
4. **Handle errors gracefully**: Implement retry logic for failed conversions

These examples demonstrate the flexibility and security of the local markitdown-based Document Converter skill.