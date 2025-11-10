#!/usr/bin/env python3
"""
Document Converter - Convert PDF, PPT, DOCX, and web pages to Markdown format

This script provides a command-line interface for converting various document formats
to Markdown using a high-performance content parsing service.
"""

import requests
import json
import sys
import os
import argparse
from urllib.parse import quote
from typing import Optional, Dict, Any, Union
import mimetypes
from pathlib import Path

class DocumentConverter:
    """Main document converter class"""

    def __init__(self, base_url: str = "https://reader-aigc.skyengine.com.cn"):
        """
        Initialize the converter

        Args:
            base_url: Base URL for the conversion service
        """
        self.base_url = base_url
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Document-Converter/1.0',
            'Accept': 'application/json'
        })

    def convert_url_get(self, url: str, **options) -> Dict[str, Any]:
        """
        Convert URL using GET method

        Args:
            url: URL to convert
            **options: Conversion options

        Returns:
            Conversion result as dictionary
        """
        # URL encode the target URL
        encoded_url = quote(url, safe=':/?#[]@!$&\'()*+,;=')
        full_url = f"{self.base_url}/{encoded_url}"

        # Build headers from options
        headers = self._build_headers(options)

        try:
            response = self.session.get(full_url, headers=headers, timeout=60)
            response.raise_for_status()

            # Parse response based on content type
            content_type = response.headers.get('content-type', '').lower()

            if 'application/json' in content_type:
                return response.json()
            else:
                return {
                    'url': url,
                    'title': self._extract_title_from_text(response.text),
                    'content': response.text,
                    'status': 'success',
                    'content_type': content_type
                }

        except requests.exceptions.Timeout:
            return {
                'url': url,
                'error': 'Request timeout - page took too long to load',
                'status': 'error',
                'error_code': 408
            }
        except requests.exceptions.RequestException as e:
            return {
                'url': url,
                'error': f'Request failed: {str(e)}',
                'status': 'error',
                'error_code': getattr(e.response, 'status_code', 500) if hasattr(e, 'response') else 500
            }

    def convert_url_post(self, url: str, **options) -> Dict[str, Any]:
        """
        Convert URL using POST method

        Args:
            url: URL to convert
            **options: Conversion options

        Returns:
            Conversion result as dictionary
        """
        headers = self._build_headers(options)
        headers['Content-Type'] = 'application/json'

        data = {'url': url}

        try:
            response = self.session.post(
                self.base_url,
                json=data,
                headers=headers,
                timeout=60
            )
            response.raise_for_status()

            result = response.json()
            return result

        except requests.exceptions.RequestException as e:
            return {
                'url': url,
                'error': f'POST request failed: {str(e)}',
                'status': 'error',
                'error_code': getattr(e.response, 'status_code', 500) if hasattr(e, 'response') else 500
            }
        except json.JSONDecodeError as e:
            return {
                'url': url,
                'error': f'Response parsing error: {str(e)}',
                'status': 'error',
                'error_code': 500
            }

    def convert_file(self, file_path: Union[str, Path], **options) -> Dict[str, Any]:
        """
        Convert local file by uploading

        Args:
            file_path: Path to local file
            **options: Conversion options

        Returns:
            Conversion result as dictionary
        """
        file_path = Path(file_path)

        if not file_path.exists():
            return {
                'original_file': file_path.name,
                'error': 'File does not exist',
                'status': 'error',
                'error_code': 404
            }

        # Check file size (recommended < 50MB)
        file_size = file_path.stat().st_size
        if file_size > 50 * 1024 * 1024:  # 50MB
            return {
                'original_file': file_path.name,
                'error': f'File too large: {file_size / (1024*1024):.1f}MB (recommended < 50MB)',
                'status': 'error',
                'error_code': 413
            }

        # Build headers
        headers = self._build_headers(options)

        try:
            with open(file_path, 'rb') as f:
                mime_type = mimetypes.guess_type(str(file_path))[0] or 'application/octet-stream'
                files = {
                    'file': (file_path.name, f, mime_type)
                }

                response = self.session.post(
                    self.base_url,
                    files=files,
                    headers=headers,
                    timeout=120  # Longer timeout for file uploads
                )
                response.raise_for_status()

                content_type = response.headers.get('content-type', '').lower()

                if 'application/json' in content_type:
                    result = response.json()
                    result['original_file'] = file_path.name
                    result['file_size'] = file_size
                    return result
                else:
                    return {
                        'original_file': file_path.name,
                        'file_size': file_size,
                        'title': file_path.stem,
                        'content': response.text,
                        'status': 'success',
                        'content_type': content_type
                    }

        except requests.exceptions.Timeout:
            return {
                'original_file': file_path.name,
                'error': 'File upload timeout - try a smaller file or check network connection',
                'status': 'error',
                'error_code': 408
            }
        except requests.exceptions.RequestException as e:
            return {
                'original_file': file_path.name,
                'error': f'Upload failed: {str(e)}',
                'status': 'error',
                'error_code': getattr(e.response, 'status_code', 500) if hasattr(e, 'response') else 500
            }
        except Exception as e:
            return {
                'original_file': file_path.name,
                'error': f'File processing error: {str(e)}',
                'status': 'error',
                'error_code': 500
            }

    def _build_headers(self, options: Dict[str, Any]) -> Dict[str, str]:
        """
        Build HTTP headers from options

        Args:
            options: Dictionary of conversion options

        Returns:
            Dictionary of HTTP headers
        """
        headers = {}

        # Map option names to header names
        header_mapping = {
            'remove_images': 'X-Remove-Images',
            'describe_images': 'X-Describe-Images',
            'proxy_url': 'X-Proxy-Url',
            'timeout': 'X-Timeout',
            'smart_selector': 'X-Smart-Selector',
            'target_selector': 'X-Target-Selector',
            'remove_selector': 'X-Remove-Selector',
            'with_iframe': 'X-With-Iframe',
            'with_shadow_dom': 'X-With-Shadow-Dom',
            'follow_redirects': 'X-Follow-Redirects',
            'pdf_fast_parse': 'X-Pdf-Fast-Parse',
            'accept_json': 'Accept'
        }

        for option_key, header_name in header_mapping.items():
            if option_key in options:
                value = options[option_key]
                if isinstance(value, bool):
                    value = str(value).lower()
                elif value is None:
                    continue
                headers[header_name] = str(value)

        return headers

    def _extract_title_from_text(self, text: str) -> str:
        """
        Extract title from plain text content

        Args:
            text: Text content to analyze

        Returns:
            Extracted title or default
        """
        lines = text.strip().split('\n')
        for line in lines:
            line = line.strip()
            # Skip empty lines and markdown headers
            if line and not line.startswith('#') and not line.startswith('http'):
                # Look for reasonable title candidates
                if len(line) < 100 and not line.startswith('```'):
                    return line

        return "Untitled Document"

def create_argument_parser() -> argparse.ArgumentParser:
    """Create and configure argument parser"""
    parser = argparse.ArgumentParser(
        description='Convert PDF, PPT, DOCX, and web pages to Markdown format',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s "https://blog.samaltman.com"
  %(prog)s "document.pdf" --output converted.md
  %(prog)s "https://example.com" --target-selector "article" --remove-selector "nav,footer"
  %(prog)s "presentation.pptx" --remove-images --timeout 45000
        """
    )

    # Input arguments
    parser.add_argument(
        'input',
        help='URL to convert or path to local file'
    )

    # Output options
    parser.add_argument(
        '-o', '--output',
        help='Output file path (default: print to console)'
    )

    parser.add_argument(
        '--method',
        choices=['get', 'post'],
        default='get',
        help='HTTP method for URL conversion (default: get)'
    )

    parser.add_argument(
        '--json',
        action='store_true',
        help='Output result in JSON format'
    )

    # Content processing options
    content_group = parser.add_argument_group('Content Processing Options')

    content_group.add_argument(
        '--remove-images',
        action='store_true',
        help='Remove all images from the output'
    )

    content_group.add_argument(
        '--describe-images',
        action='store_true',
        help='Use AI to describe images in text'
    )

    content_group.add_argument(
        '--smart-selector',
        action='store_true',
        default=True,
        help='Enable smart content extraction (default: enabled)'
    )

    content_group.add_argument(
        '--no-smart-selector',
        dest='smart_selector',
        action='store_false',
        help='Disable smart content extraction'
    )

    # CSS selector options
    selector_group = parser.add_argument_group('CSS Selector Options')

    selector_group.add_argument(
        '--target-selector',
        help='CSS selector for target content (e.g., "article", ".content")'
    )

    selector_group.add_argument(
        '--remove-selector',
        help='CSS selector for elements to remove (e.g., "nav,footer,.ads")'
    )

    # Advanced options
    advanced_group = parser.add_argument_group('Advanced Options')

    advanced_group.add_argument(
        '--with-iframe',
        action='store_true',
        help='Parse iframe content'
    )

    advanced_group.add_argument(
        '--with-shadow-dom',
        action='store_true',
        help='Parse Shadow DOM content'
    )

    advanced_group.add_argument(
        '--follow-redirects',
        action='store_true',
        help='Follow URL redirects to final destination'
    )

    advanced_group.add_argument(
        '--timeout',
        type=int,
        help='Page load timeout in milliseconds (default: 30000, max: 60000)'
    )

    advanced_group.add_argument(
        '--pdf-fast-parse',
        action='store_true',
        help='Use fast PDF parsing (text only)'
    )

    # Service options
    service_group = parser.add_argument_group('Service Options')

    service_group.add_argument(
        '--test',
        action='store_true',
        help='Use testing environment instead of production'
    )

    service_group.add_argument(
        '--proxy-url',
        help='Proxy URL for accessing restricted pages'
    )

    return parser

def main():
    """Main entry point"""
    parser = create_argument_parser()
    args = parser.parse_args()

    # Determine service URL
    if args.test:
        base_url = "http://knowledge-reader.external.bdp-testing-streaming.k8s.skyengine.com.cn:8000"
        print("🧪 Using testing environment")
    else:
        base_url = "https://reader-aigc.skyengine.com.cn"
        print("🚀 Using production environment")

    # Create converter
    converter = DocumentConverter(base_url)

    # Prepare conversion options
    options = {
        'remove_images': args.remove_images,
        'describe_images': args.describe_images,
        'smart_selector': args.smart_selector,
        'target_selector': args.target_selector,
        'remove_selector': args.remove_selector,
        'with_iframe': args.with_iframe,
        'with_shadow_dom': args.with_shadow_dom,
        'follow_redirects': args.follow_redirects,
        'timeout': args.timeout,
        'pdf_fast_parse': args.pdf_fast_parse,
        'proxy_url': args.proxy_url,
        'accept_json': 'application/json' if args.json else None
    }

    # Remove None values
    options = {k: v for k, v in options.items() if v is not None}

    # Determine input type and convert
    input_path = Path(args.input)
    print(f"📄 Processing: {args.input}")

    if input_path.exists() and input_path.is_file():
        # File conversion
        print("📁 Detected local file")
        result = converter.convert_file(input_path, **options)
        input_type = "File"
    else:
        # URL conversion
        print("🌐 Detected URL")
        if args.method == 'post':
            result = converter.convert_url_post(args.input, **options)
        else:
            result = converter.convert_url_get(args.input, **options)
        input_type = "URL"

    # Handle results
    if result.get('status') == 'error':
        error_code = result.get('error_code', 'Unknown')
        error_msg = result.get('error', 'Unknown error')
        print(f"❌ {input_type} conversion failed (Error {error_code})")
        print(f"   Details: {error_msg}")

        # Provide helpful suggestions
        if error_code == 400:
            print("💡 Suggestion: Check URL format and encoding")
        elif error_code == 408:
            print("💡 Suggestion: Try increasing timeout with --timeout or simplify the target page")
        elif error_code == 413:
            print("💡 Suggestion: File too large, try with a smaller file (< 50MB)")
        elif error_code >= 500:
            print("💡 Suggestion: Service error, try again later or use --test environment")

        sys.exit(1)

    print(f"✅ {input_type} conversion successful")

    # Prepare output content
    if args.json:
        output_content = json.dumps(result, ensure_ascii=False, indent=2)
    else:
        output_content = result.get('content', '')
        if not output_content:
            print("⚠️  Warning: No content extracted")
            output_content = json.dumps(result, ensure_ascii=False, indent=2)

    # Output to file or console
    if args.output:
        output_path = Path(args.output)
        try:
            output_path.write_text(output_content, encoding='utf-8')
            print(f"💾 Result saved to: {output_path}")
        except Exception as e:
            print(f"❌ Failed to save file: {e}")
            print("📄 Outputting to console instead:")
            print("\n" + "="*50)
            print(output_content)
    else:
        print("\n" + "="*50)
        print("CONVERSION RESULT:")
        print("="*50)
        print(output_content)

if __name__ == '__main__':
    main()