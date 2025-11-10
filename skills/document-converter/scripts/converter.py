#!/usr/bin/env python3
"""
Document Converter - Convert PDF, PPT, DOCX, and web pages to Markdown format

This script provides a command-line interface for converting various document formats
to Markdown using local markitdown tool for security and privacy.
"""

import subprocess
import json
import sys
import os
import argparse
from urllib.parse import quote, urlparse
from typing import Optional, Dict, Any, Union
import mimetypes
from pathlib import Path
import tempfile
import shutil

class DocumentConverter:
    """Main document converter class using local markitdown tool"""

    def __init__(self):
        """
        Initialize the converter with markitdown tool
        """
        self.markitdown_path = self._find_markitdown()
        if not self.markitdown_path:
            raise RuntimeError("markitdown tool not found. Please install it with: pip install markitdown")

    def _find_markitdown(self) -> Optional[str]:
        """Find markitdown executable in PATH"""
        try:
            result = subprocess.run(['which', 'markitdown'],
                                  capture_output=True, text=True, timeout=10)
            if result.returncode == 0:
                return result.stdout.strip()
        except (subprocess.TimeoutExpired, subprocess.SubprocessError):
            pass
        return None

    def convert_file(self, file_path: Union[str, Path], **options) -> Dict[str, Any]:
        """
        Convert local file using markitdown tool

        Args:
            file_path: Path to local file
            **options: Conversion options (markitdown-specific)

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

        # Check file size (recommended < 100MB for local processing)
        file_size = file_path.stat().st_size
        if file_size > 100 * 1024 * 1024:  # 100MB
            return {
                'original_file': file_path.name,
                'error': f'File too large: {file_size / (1024*1024):.1f}MB (recommended < 100MB)',
                'status': 'error',
                'error_code': 413
            }

        try:
            # Prepare markitdown command
            cmd = [self.markitdown_path, str(file_path)]

            # Add markitdown options
            if options.get('use_plugins'):
                cmd.append('-p')

            if options.get('use_docintel'):
                cmd.append('-d')
                if options.get('endpoint'):
                    cmd.extend(['-e', options['endpoint']])

            if options.get('mime_type'):
                cmd.extend(['-m', options['mime_type']])

            if options.get('charset'):
                cmd.extend(['-c', options['charset']])

            if options.get('keep_data_uris'):
                cmd.append('--keep-data-uris')

            # Execute markitdown
            result = subprocess.run(
                cmd,
                capture_output=True,
                text=True,
                timeout=300,  # 5 minutes timeout for local processing
                encoding='utf-8'
            )

            if result.returncode != 0:
                return {
                    'original_file': file_path.name,
                    'error': f'Markitdown conversion failed: {result.stderr}',
                    'status': 'error',
                    'error_code': 500
                }

            content = result.stdout

            # Extract title from content
            title = self._extract_title_from_content(content)

            return {
                'original_file': file_path.name,
                'file_size': file_size,
                'title': title,
                'content': content,
                'status': 'success',
                'tool': 'markitdown',
                'processing_time': 'local'
            }

        except subprocess.TimeoutExpired:
            return {
                'original_file': file_path.name,
                'error': 'File processing timeout - file may be too complex',
                'status': 'error',
                'error_code': 408
            }
        except Exception as e:
            return {
                'original_file': file_path.name,
                'error': f'File processing error: {str(e)}',
                'status': 'error',
                'error_code': 500
            }

    def convert_file_to_output(self, file_path: Union[str, Path], output_path: Optional[str] = None, **options) -> Dict[str, Any]:
        """
        Convert file directly to output file using markitdown

        Args:
            file_path: Path to input file
            output_path: Path to output file (optional)
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

        try:
            # Prepare markitdown command with output
            cmd = [self.markitdown_path, str(file_path)]

            if output_path:
                cmd.extend(['-o', str(output_path)])

            # Add other options
            if options.get('use_plugins'):
                cmd.append('-p')

            if options.get('keep_data_uris'):
                cmd.append('--keep-data-uris')

            # Execute markitdown
            result = subprocess.run(
                cmd,
                capture_output=True,
                text=True,
                timeout=300,
                encoding='utf-8'
            )

            if result.returncode != 0:
                return {
                    'original_file': file_path.name,
                    'error': f'Markitdown conversion failed: {result.stderr}',
                    'status': 'error',
                    'error_code': 500
                }

            # Read output file if it was created
            content = ""
            if output_path:
                try:
                    with open(output_path, 'r', encoding='utf-8') as f:
                        content = f.read()
                except Exception as e:
                    return {
                        'original_file': file_path.name,
                        'output_file': str(output_path),
                        'error': f'Failed to read output file: {str(e)}',
                        'status': 'error',
                        'error_code': 500
                    }
            else:
                content = result.stdout

            title = self._extract_title_from_content(content)

            return {
                'original_file': file_path.name,
                'output_file': str(output_path) if output_path else None,
                'title': title,
                'content': content,
                'status': 'success',
                'tool': 'markitdown',
                'processing_time': 'local'
            }

        except subprocess.TimeoutExpired:
            return {
                'original_file': file_path.name,
                'error': 'File processing timeout - file may be too complex',
                'status': 'error',
                'error_code': 408
            }
        except Exception as e:
            return {
                'original_file': file_path.name,
                'error': f'File processing error: {str(e)}',
                'status': 'error',
                'error_code': 500
            }

    def convert_url(self, url: str, **options) -> Dict[str, Any]:
        """
        Convert web page URL to Markdown (Note: This downloads content locally)

        Args:
            url: URL to convert
            **options: Conversion options

        Returns:
            Conversion result as dictionary
        """
        try:
            import requests
        except ImportError:
            return {
                'url': url,
                'error': 'requests library not available for URL conversion. Install with: pip install requests',
                'status': 'error',
                'error_code': 501
            }

        try:
            # Download URL content
            response = requests.get(url, timeout=30, headers={
                'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36'
            })
            response.raise_for_status()

            # Determine file extension from URL or content type
            parsed_url = urlparse(url)
            url_path = parsed_url.path
            extension = os.path.splitext(url_path)[1].lower()

            if not extension:
                content_type = response.headers.get('content-type', '')
                if 'pdf' in content_type:
                    extension = '.pdf'
                elif 'html' in content_type:
                    extension = '.html'
                elif 'text' in content_type:
                    extension = '.txt'

            # Create temporary file
            with tempfile.NamedTemporaryFile(suffix=extension or '.tmp', delete=False) as tmp_file:
                tmp_file.write(response.content)
                tmp_file_path = tmp_file.name

            try:
                # Convert downloaded file using markitdown
                result = self.convert_file(tmp_file_path, **options)
                result['url'] = url
                result['original_filename'] = os.path.basename(url_path) or f'downloaded{extension}'

                # Clean up temporary file
                os.unlink(tmp_file_path)

                return result

            except Exception as e:
                # Clean up temporary file on error
                if os.path.exists(tmp_file_path):
                    os.unlink(tmp_file_path)
                raise e

        except requests.exceptions.RequestException as e:
            return {
                'url': url,
                'error': f'Failed to download URL: {str(e)}',
                'status': 'error',
                'error_code': 400
            }
        except Exception as e:
            return {
                'url': url,
                'error': f'URL processing error: {str(e)}',
                'status': 'error',
                'error_code': 500
            }

    def _extract_title_from_content(self, content: str) -> str:
        """
        Extract title from markdown content

        Args:
            content: Markdown content to analyze

        Returns:
            Extracted title or default
        """
        lines = content.strip().split('\n')
        for line in lines:
            line = line.strip()
            # Look for first non-empty line that could be a title
            if line and not line.startswith('©') and not line.isdigit():
                if len(line) < 100 and not line.startswith('```'):
                    # Remove common non-title patterns
                    if not any(pattern in line.lower() for pattern in ['page', '©', 'all rights reserved']):
                        return line
        return "Untitled Document"

    def get_supported_formats(self) -> Dict[str, list]:
        """
        Get list of supported file formats
        """
        return {
            'documents': ['.pdf', '.docx', '.doc', '.pptx', '.ppt', '.txt', '.rtf'],
            'images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff'],
            'web': ['.html', '.htm'],
            'other': ['.md', '.csv', '.json', '.xml']
        }

def create_argument_parser() -> argparse.ArgumentParser:
    """Create and configure argument parser"""
    parser = argparse.ArgumentParser(
        description='Convert PDF, PPT, DOCX, and other files to Markdown format using local markitdown tool',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s document.pdf
  %(prog)s document.pdf --output converted.md
  %(prog)s presentation.pptx --use-plugins
  %(prog)s https://example.com/document.pdf
        """
    )

    # Input arguments
    parser.add_argument(
        'input',
        nargs='?',  # Make input optional for utility commands
        help='Path to local file or URL to convert'
    )

    # Output options
    parser.add_argument(
        '-o', '--output',
        help='Output file path (default: print to console)'
    )

    parser.add_argument(
        '--json',
        action='store_true',
        help='Output result in JSON format'
    )

    # Markitdown specific options
    markitdown_group = parser.add_argument_group('Markitdown Options')

    markitdown_group.add_argument(
        '--use-plugins',
        action='store_true',
        help='Use 3rd-party plugins for conversion'
    )

    markitdown_group.add_argument(
        '--use-docintel',
        action='store_true',
        help='Use Document Intelligence (requires endpoint)'
    )

    markitdown_group.add_argument(
        '--endpoint',
        help='Document Intelligence endpoint (required with --use-docintel)'
    )

    markitdown_group.add_argument(
        '--mime-type',
        help='Provide hint about file MIME type'
    )

    markitdown_group.add_argument(
        '--charset',
        help='Provide hint about file charset (e.g., UTF-8)'
    )

    markitdown_group.add_argument(
        '--keep-data-uris',
        action='store_true',
        help='Keep data URIs (like base64-encoded images) in output'
    )

    # Utility options
    parser.add_argument(
        '--list-formats',
        action='store_true',
        help='List supported file formats and exit'
    )

    parser.add_argument(
        '--markitdown-version',
        action='store_true',
        help='Show markitdown version and exit'
    )

    return parser

def main():
    """Main entry point"""
    parser = create_argument_parser()
    args = parser.parse_args()

    # Handle utility options
    if args.list_formats:
        try:
            converter = DocumentConverter()
            formats = converter.get_supported_formats()
            print("Supported file formats:")
            for category, extensions in formats.items():
                print(f"\n{category.title()}:")
                for ext in extensions:
                    print(f"  {ext}")
            return
        except RuntimeError as e:
            print(f"Error: {e}")
            sys.exit(1)

    if args.markitdown_version:
        try:
            result = subprocess.run(['markitdown', '--version'],
                                  capture_output=True, text=True, timeout=10)
            if result.returncode == 0:
                print(f"Markitdown version: {result.stdout.strip()}")
            else:
                print("Failed to get markitdown version")
        except Exception as e:
            print(f"Error getting version: {e}")
        return

    # Check if input is provided for conversion commands
    if not args.input:
        parser.error("input file or URL is required for conversion")

    # Create converter
    try:
        converter = DocumentConverter()
    except RuntimeError as e:
        print(f"❌ Error: {e}")
        sys.exit(1)

    # Determine input type and convert
    input_path = args.input
    print(f"📄 Processing: {input_path}")

    # Prepare conversion options
    options = {
        'use_plugins': args.use_plugins,
        'use_docintel': args.use_docintel,
        'endpoint': args.endpoint,
        'mime_type': args.mime_type,
        'charset': args.charset,
        'keep_data_uris': args.keep_data_uris
    }

    # Remove None values
    options = {k: v for k, v in options.items() if v is not None}

    # Validate Document Intelligence requirements
    if args.use_docintel and not args.endpoint:
        print("❌ Error: --endpoint is required when using --use-docintel")
        sys.exit(1)

    # Execute conversion
    if input_path.startswith(('http://', 'https://')):
        # URL conversion
        print("🌐 Detected URL - downloading and converting locally")
        result = converter.convert_url(input_path, **options)
        input_type = "URL"
    else:
        # File conversion
        input_path_obj = Path(input_path)
        if input_path_obj.exists() and input_path_obj.is_file():
            print("📁 Detected local file - using secure local processing")
            if args.output:
                result = converter.convert_file_to_output(input_path_obj, args.output, **options)
            else:
                result = converter.convert_file(input_path_obj, **options)
            input_type = "File"
        else:
            print(f"❌ Error: File not found: {input_path}")
            sys.exit(1)

    # Handle results
    if result.get('status') == 'error':
        error_code = result.get('error_code', 'Unknown')
        error_msg = result.get('error', 'Unknown error')
        print(f"❌ {input_type} conversion failed (Error {error_code})")
        print(f"   Details: {error_msg}")
        sys.exit(1)

    print(f"✅ {input_type} conversion successful")
    print(f"🔧 Tool used: {result.get('tool', 'markitdown')}")
    print(f"🔒 Processing: {result.get('processing_time', 'local')}")

    # Prepare output content
    if args.json:
        output_content = json.dumps(result, ensure_ascii=False, indent=2)
    else:
        output_content = result.get('content', '')
        if not output_content:
            print("⚠️  Warning: No content extracted")
            output_content = json.dumps(result, ensure_ascii=False, indent=2)

    # Output to file or console
    if args.output and not result.get('output_file'):
        # Only save if markitdown didn't already save to output file
        output_path = Path(args.output)
        try:
            output_path.write_text(output_content, encoding='utf-8')
            print(f"💾 Result saved to: {output_path}")
        except Exception as e:
            print(f"❌ Failed to save file: {e}")
            print("📄 Outputting to console instead:")
            print("\n" + "="*50)
            print(output_content)
    elif result.get('output_file'):
        print(f"💾 Result saved to: {result['output_file']}")
        if args.json:
            print("\n" + "="*50)
            print("JSON METADATA:")
            print("="*50)
            metadata = {k: v for k, v in result.items() if k != 'content'}
            print(json.dumps(metadata, ensure_ascii=False, indent=2))
    else:
        print("\n" + "="*50)
        print("CONVERSION RESULT:")
        print("="*50)
        print(output_content)

if __name__ == '__main__':
    main()