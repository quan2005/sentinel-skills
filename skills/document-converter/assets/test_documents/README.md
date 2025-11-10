# Test Documents Directory

This directory contains sample files for testing the document converter functionality.

## Usage Examples

### Convert PDF File
```bash
python scripts/converter.py "assets/test_documents/sample.pdf" --output converted.md
```

### Convert PowerPoint Presentation
```bash
python scripts/converter.py "assets/test_documents/presentation.pptx" --remove-images --output slides.md
```

### Convert Word Document
```bash
python scripts/converter.py "assets/test_documents/report.docx" --describe-images --output report.md
```

### Convert with Options
```bash
python scripts/converter.py "assets/test_documents/document.pdf" \
  --pdf-fast-parse \
  --remove-images \
  --timeout 45000 \
  --json
```

## Test Files

To add your own test files:

1. Place files in this directory
2. Supported formats: PDF, PPT, PPTX, DOC, DOCX, TXT, RTF
3. Recommended file size: < 10MB for testing
4. Include various content types for comprehensive testing

### Test Categories

**Simple Text Documents**
- Plain text files (.txt)
- Simple Word documents (.docx)
- Basic PDFs with text only

**Complex Documents**
- PDFs with images and formatting
- PowerPoint presentations with slides
- Word documents with complex formatting

**Edge Cases**
- Very large files (for timeout testing)
- Password-protected files (expected to fail)
- Corrupted files (error handling testing)

**Multi-language Content**
- Documents in different languages
- Mixed language content
- Right-to-left language documents