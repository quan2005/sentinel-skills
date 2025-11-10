#!/usr/bin/env python3
"""
Document Converter - Convert PDF, PPT, DOCX, and web pages to Markdown format
Enhanced with professional dependency management and advanced extraction features

This script provides a command-line interface for converting various document formats
to Markdown using local markitdown tool for security and privacy and Crawl4AI for
intelligent web crawling with advanced extraction capabilities.
"""

import subprocess
import json
import sys
import os
import argparse
from urllib.parse import quote, urlparse
from typing import Optional, Dict, Any, Union, List
import mimetypes
from pathlib import Path
import tempfile
import shutil
import asyncio

class DocumentConverter:
    """Enhanced document converter class with professional dependency management"""

    # Minimum required versions
    MIN_CRAWL4AI_VERSION = "0.7.4"
    MIN_PYTHON_VERSION = (3, 7)

    def __init__(self):
        """
        Initialize the converter with comprehensive dependency checking
        """
        self._check_python_version()

        # Store dependency availability for later use
        self.crawl4ai_available = self._check_crawl4ai_available()
        self.beautifulsoup_available = self._check_beautifulsoup_available()

        self._check_dependencies()
        self.markitdown_path = self._find_markitdown()
        if not self.markitdown_path:
            raise RuntimeError("markitdown tool not found. Please install it with: pip install markitdown")

    def _check_python_version(self):
        """Check Python version compatibility"""
        if sys.version_info < self.MIN_PYTHON_VERSION:
            raise RuntimeError(f"Python {self.MIN_PYTHON_VERSION[0]}.{self.MIN_PYTHON_VERSION[1]}+ required (you have {sys.version_info[0]}.{sys.version_info[1]})")

    def _check_dependencies(self):
        """Check all dependencies and their versions"""
        self._check_crawl4ai_version()
        self._check_optional_dependencies()

    def _check_crawl4ai_version(self):
        """Check Crawl4AI version with detailed feedback"""
        try:
            from crawl4ai.__version__ import __version__
            try:
                from packaging import version
                if version.parse(__version__) < version.parse(self.MIN_CRAWL4AI_VERSION):
                    print(f"⚠️  Warning: Crawl4AI {self.MIN_CRAWL4AI_VERSION}+ recommended (you have {__version__})")
                    print("   Some advanced features may not work correctly")
                else:
                    print(f"✅ Crawl4AI version {__version__} meets requirements")
            except ImportError:
                print(f"ℹ️  Installing 'packaging' recommended for version checking")
                print(f"   Crawl4AI {__version__} detected")
        except ImportError:
            print("ℹ️  Crawl4AI not available - web crawling features disabled")
            print("   Install with: pip install crawl4ai")

    def _check_crawl4ai_available(self) -> bool:
        """Check if Crawl4AI is available and return status"""
        try:
            from crawl4ai import AsyncWebCrawler, CrawlerRunConfig, CacheMode
            return True
        except ImportError:
            return False

    def _check_beautifulsoup_available(self) -> bool:
        """Check if BeautifulSoup is available and return status"""
        try:
            import bs4
            return True
        except ImportError:
            return False

    def _check_optional_dependencies(self):
        """Check optional dependencies with helpful messages"""
        # Check for BeautifulSoup (needed for HTML processing)
        if self.beautifulsoup_available:
            print("✅ BeautifulSoup4 available for HTML processing")
        else:
            print("ℹ️  BeautifulSoup4 not found - install with: pip install beautifulsoup4")
            print("   Required for advanced HTML-to-Markdown conversion")

        # Check for packaging (needed for version comparison)
        try:
            import packaging
            print("✅ Packaging library available for version checking")
        except ImportError:
            print("ℹ️  Packaging library not found - install with: pip install packaging")

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
        Convert web page URL to Markdown using Crawl4AI for intelligent extraction

        Args:
            url: URL to convert
            **options: Conversion options

        Returns:
            Conversion result as dictionary
        """
        # Check if Crawl4AI is available using pre-checked status
        if not self.crawl4ai_available:
            # Fallback to simple URL download if Crawl4AI is not available
            return self._fallback_url_download(url)

        try:
            from crawl4ai import AsyncWebCrawler, CrawlerRunConfig, CacheMode
            import asyncio
            # Try to import extraction strategies (some may not be available in all versions)
            try:
                from crawl4ai.extraction_strategy import LLMExtractionStrategy, CssExtractionStrategy, JsonCssExtractionStrategy
            except ImportError:
                # Fallback for different versions of Crawl4AI
                try:
                    from crawl4ai.extraction_strategy import LLMExtractionStrategy
                    CssExtractionStrategy = None
                    JsonCssExtractionStrategy = None
                except ImportError:
                    LLMExtractionStrategy = None
                    CssExtractionStrategy = None
                    JsonCssExtractionStrategy = None
        except ImportError as e:
            return {
                'url': url,
                'error': f'Crawl4AI library import failed: {str(e)}. Please reinstall with: pip install crawl4ai',
                'status': 'error',
                'error_code': 501
            }

        async def crawl_url(crawl_options):
            """Async function to crawl URL with Crawl4AI"""
            try:

                wait_time = crawl_options.get('wait_time', 2000)
                remove_overlays = crawl_options.get('remove_overlays', True)
                simulate_user = crawl_options.get('simulate_user', True)
                bypass_cache = crawl_options.get('bypass_cache', True)
                verbose = crawl_options.get('verbose_crawling', False)

                # Configure caching mode
                cache_mode = CacheMode.BYPASS if bypass_cache else CacheMode.ENABLED

                # Configure crawling options
                crawl_config = CrawlerRunConfig(
                    cache_mode=cache_mode,            # Always get fresh content or use cache
                    remove_overlay_elements=remove_overlays,  # Remove popups and overlays
                    simulate_user=simulate_user,      # Simulate user behavior
                    override_navigator=True,           # Override navigator for better compatibility
                    js_code=[f"""
                    // Wait for page to fully load
                    await new Promise(resolve => setTimeout(resolve, {wait_time}));

                    // Remove unwanted elements
                    const elementsToRemove = [
                        'script', 'style', 'iframe',
                        '.ads', '.advertisement', '.popup', '.modal',
                        '[style*="display:none"]', '[style*="visibility:hidden"]'
                    ];

                    elementsToRemove.forEach(selector => {{
                        document.querySelectorAll(selector).forEach(el => el.remove());
                    }});

                    // Scroll to ensure lazy-loaded content is visible
                    window.scrollTo(0, document.body.scrollHeight);
                    await new Promise(resolve => setTimeout(resolve, 1000));
                    window.scrollTo(0, 0);
                    """]
                )

                # Create crawler instance
                async with AsyncWebCrawler(
                    headless=True,
                    verbose=verbose,
                    user_agent="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
                ) as crawler:

                    # Crawl the URL
                    result = await crawler.arun(url=url, config=crawl_config)

                    if not result.success:
                        return {
                            'url': url,
                            'error': f'Crawling failed: {result.error_message}',
                            'status': 'error',
                            'error_code': 500
                        }

                    # Get HTML content and convert to Markdown manually
                    html_content = result.html if hasattr(result, 'html') else result.cleaned_html

                    if not html_content and hasattr(result, 'cleaned_html'):
                        html_content = result.cleaned_html

                    # Convert HTML to Markdown using BeautifulSoup
                    markdown_content = ""
                    if html_content:
                        try:
                            import re
                            from bs4 import BeautifulSoup

                            soup = BeautifulSoup(html_content, 'html.parser')

                            # Remove script and style elements
                            for script in soup(["script", "style", "noscript"]):
                                script.decompose()

                            # Extract text content
                            text = soup.get_text()

                            # Clean up text and create markdown
                            lines = (line.strip() for line in text.splitlines())
                            chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
                            text = '\n'.join(chunk for chunk in chunks if chunk)

                            # Add title from HTML if available
                            title_tag = soup.find('title')
                            title = title_tag.get_text().strip() if title_tag else ""

                            # Create markdown content
                            if title:
                                markdown_content = f"# {title}\n\n{text}"
                            else:
                                markdown_content = text

                        except Exception as e:
                            # Final fallback - use raw HTML
                            markdown_content = f"# {url}\n\n{html_content}"

                    # Extract title
                    title = self._extract_title_from_markdown(markdown_content)

                    # If no title found, try to get from HTML
                    if not title and hasattr(result, 'html'):
                        try:
                            from bs4 import BeautifulSoup
                            soup = BeautifulSoup(result.html, 'html.parser')
                            title_tag = soup.find('title')
                            if title_tag:
                                title = title_tag.get_text().strip()
                        except Exception:
                            pass

                    return {
                        'url': url,
                        'title': title or "Untitled Web Page",
                        'content': markdown_content,
                        'status': 'success',
                        'tool': 'Crawl4AI',
                        'processing_time': 'local_crawling',
                        'success': result.success,
                        'session_id': getattr(result, 'session_id', None)
                    }

            except Exception as e:
                return {
                    'url': url,
                    'error': f'Crawling error: {str(e)}',
                    'status': 'error',
                    'error_code': 500
                }

        try:
            # Extract crawl options from options dict
            crawl_options = {}
            crawl_option_keys = ['wait_time', 'remove_overlays', 'simulate_user', 'bypass_cache', 'verbose_crawling']
            for key in crawl_option_keys:
                if key in options:
                    crawl_options[key] = options[key]

            # Run the async function
            import sys
            if sys.version_info >= (3, 7):
                return asyncio.run(crawl_url(crawl_options))
            else:
                # Fallback for older Python versions
                import asyncio
                loop = asyncio.get_event_loop()
                if loop.is_running():
                    # If already in event loop, create new one
                    import concurrent.futures
                    with concurrent.futures.ThreadPoolExecutor() as executor:
                        future = executor.submit(asyncio.run, crawl_url(crawl_options))
                        return future.result()
                else:
                    return loop.run_until_complete(crawl_url(crawl_options))

        except Exception as e:
            return {
                'url': url,
                'error': f'URL processing error: {str(e)}',
                'status': 'error',
                'error_code': 500
            }

    def convert_urls_batch(self, urls: List[str], **options) -> Dict[str, Any]:
        """
        Convert multiple URLs efficiently with concurrent processing

        Args:
            urls: List of URLs to convert
            **options: Conversion options including max_concurrent

        Returns:
            Conversion results for all URLs as dictionary with 'results' list
        """
        # Check if Crawl4AI is available
        if not self.crawl4ai_available:
            # Fallback to sequential processing using fallback_url_download
            print(f"🔄 Crawl4AI not available, using sequential fallback processing for {len(urls)} URLs")
            results = []

            for url in urls:
                result = self._fallback_url_download(url)
                results.append(result)

            return {
                'results': results,
                'total_processed': len(results),
                'successful': sum(1 for r in results if r.get('status') == 'success'),
                'failed': sum(1 for r in results if r.get('status') == 'error'),
                'processing_method': 'fallback_sequential',
                'warning': 'Crawl4AI not available - used sequential fallback method. For advanced features, install: pip install crawl4ai'
            }

        try:
            from crawl4ai import AsyncWebCrawler, BrowserConfig, CrawlerRunConfig, CacheMode
            import asyncio
        except ImportError:
            # This should not happen since we checked above, but just in case
            return {
                'urls': urls,
                'error': 'Crawl4AI library not available. Install with: pip install crawl4ai',
                'status': 'error',
                'error_code': 501
            }

        async def crawl_batch_urls(batch_options):
            """Async function to crawl multiple URLs concurrently"""
            try:
                max_concurrent = batch_options.get('max_concurrent', 5)
                wait_time = batch_options.get('wait_time', 2000)
                remove_overlays = batch_options.get('remove_overlays', True)
                simulate_user = batch_options.get('simulate_user', True)
                bypass_cache = batch_options.get('bypass_cache', True)
                verbose = batch_options.get('verbose_crawling', False)

                # Configure caching mode
                cache_mode = CacheMode.BYPASS if bypass_cache else CacheMode.ENABLED

                # Configure browser for batch processing (optimized for efficiency)
                browser_config = BrowserConfig(
                    headless=True,
                    viewport_width=1280,
                    viewport_height=800,
                    verbose=False
                )

                # Configure crawler for batch processing
                crawl_config = CrawlerRunConfig(
                    cache_mode=cache_mode,
                    remove_overlay_elements=remove_overlays,
                    simulate_user=simulate_user,
                    override_navigator=True,
                    js_code=[f"""
                    // Wait for page to fully load
                    await new Promise(resolve => setTimeout(resolve, {wait_time}));

                    // Remove unwanted elements
                    const elementsToRemove = [
                        'script', 'style', 'iframe',
                        '.ads', '.advertisement', '.popup', '.modal',
                        '[style*="display:none"]', '[style*="visibility:hidden"]'
                    ];

                    elementsToRemove.forEach(selector => {{
                        document.querySelectorAll(selector).forEach(el => el.remove());
                    }});

                    // Scroll to ensure lazy-loaded content is visible
                    window.scrollTo(0, document.body.scrollHeight);
                    await new Promise(resolve => setTimeout(resolve, 1000));
                    window.scrollTo(0, 0);
                    """],
                    page_timeout=30000,  # 30 seconds timeout per page
                    screenshot=False  # Disable screenshots for batch processing
                )

                # Create crawler instance
                async with AsyncWebCrawler(config=browser_config, verbose=verbose) as crawler:

                    # Batch crawl with concurrent processing
                    results = await crawler.arun_many(
                        urls=urls,
                        config=crawl_config,
                        max_concurrent=max_concurrent
                    )

                    # Process results
                    processed_results = []
                    successful = 0
                    failed = 0

                    for result in results:
                        if result.success:
                            # Convert HTML to Markdown using BeautifulSoup
                            html_content = result.html if hasattr(result, 'html') else result.cleaned_html
                            markdown_content = ""

                            if html_content:
                                try:
                                    import re
                                    from bs4 import BeautifulSoup

                                    soup = BeautifulSoup(html_content, 'html.parser')

                                    # Remove script and style elements
                                    for script in soup(["script", "style", "noscript"]):
                                        script.decompose()

                                    # Extract text content
                                    text = soup.get_text()

                                    # Clean up text and create markdown
                                    lines = (line.strip() for line in text.splitlines())
                                    chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
                                    text = '\n'.join(chunk for chunk in chunks if chunk)

                                    # Add title from HTML if available
                                    title_tag = soup.find('title')
                                    title = title_tag.get_text().strip() if title_tag else ""

                                    # Create markdown content
                                    if title:
                                        markdown_content = f"# {title}\n\n{text}"
                                    else:
                                        markdown_content = text

                                except Exception:
                                    markdown_content = f"# {result.url}\n\n{html_content}"

                            # Extract title
                            if not title_tag and hasattr(result, 'html'):
                                try:
                                    from bs4 import BeautifulSoup
                                    soup = BeautifulSoup(result.html, 'html.parser')
                                    title_tag = soup.find('title')
                                    title = title_tag.get_text().strip() if title_tag else ""
                                except Exception:
                                    title = ""

                            processed_results.append({
                                'url': result.url,
                                'title': title or "Untitled Web Page",
                                'content': markdown_content,
                                'status': 'success',
                                'tool': 'Crawl4AI',
                                'processing_time': 'batch_crawling',
                                'success': result.success,
                                'content_length': len(markdown_content)
                            })
                            successful += 1
                        else:
                            processed_results.append({
                                'url': result.url,
                                'error': result.error_message if hasattr(result, 'error_message') else 'Crawling failed',
                                'status': 'error',
                                'error_code': 500
                            })
                            failed += 1

                    return {
                        'urls': urls,
                        'results': processed_results,
                        'summary': {
                            'total': len(urls),
                            'successful': successful,
                            'failed': failed,
                            'success_rate': f"{(successful/len(urls)*100):.1f}%" if urls else "0%"
                        },
                        'status': 'completed',
                        'tool': 'Crawl4AI',
                        'processing_mode': 'batch_concurrent'
                    }

            except Exception as e:
                return {
                    'urls': urls,
                    'error': f'Batch crawling error: {str(e)}',
                    'status': 'error',
                    'error_code': 500
                }

        try:
            # Extract crawl options from options dict
            crawl_options = {}
            crawl_option_keys = ['max_concurrent', 'wait_time', 'remove_overlays', 'simulate_user', 'bypass_cache', 'verbose_crawling']
            for key in crawl_option_keys:
                if key in options:
                    crawl_options[key] = options[key]

            # Run the async function
            import sys
            if sys.version_info >= (3, 7):
                return asyncio.run(crawl_batch_urls(crawl_options))
            else:
                # Fallback for older Python versions
                import asyncio
                loop = asyncio.get_event_loop()
                if loop.is_running():
                    # If already in event loop, create new one
                    import concurrent.futures
                    with concurrent.futures.ThreadPoolExecutor() as executor:
                        future = executor.submit(asyncio.run, crawl_batch_urls(crawl_options))
                        return future.result()
                else:
                    return loop.run_until_complete(crawl_batch_urls(crawl_options))

        except Exception as e:
            return {
                'urls': urls,
                'error': f'Batch URL processing error: {str(e)}',
                'status': 'error',
                'error_code': 500
            }

    def generate_extraction_schema(self, url: str, instruction: str, output_file: str = "extraction_schema.json") -> Dict[str, Any]:
        """
        Generate a reusable extraction schema using LLM analysis (one-time cost)
        Best for: E-commerce sites, blogs, news sites with repetitive patterns

        Args:
            url: URL to analyze for schema generation
            instruction: Natural language instruction for what to extract
            output_file: File to save the generated schema

        Returns:
            Schema generation result as dictionary
        """
        try:
            from crawl4ai import AsyncWebCrawler, BrowserConfig, CrawlerRunConfig
            from crawl4ai.extraction_strategy import LLMExtractionStrategy
            import asyncio
            import json
        except ImportError:
            return {
                'url': url,
                'error': 'Crawl4AI library not available. Install with: pip install crawl4ai',
                'status': 'error',
                'error_code': 501
            }

        async def generate_schema_async():
            """Async function to generate extraction schema"""
            try:
                # Configure browser for schema generation
                browser_config = BrowserConfig(
                    headless=True,
                    viewport_width=1920,
                    viewport_height=1080,
                    verbose=False
                )

                # Configure crawler for schema generation
                crawl_config = CrawlerRunConfig(
                    wait_for="css:body",
                    page_timeout=30000,
                    # Use LLM to analyze the page structure and generate schema
                    extraction_strategy=LLMExtractionStrategy(
                        provider="openai/gpt-4o-mini",  # Cost-effective for schema generation
                        instruction=f"""Analyze this webpage and generate a JSON schema for extracting: {instruction}

                        Requirements:
                        1. Create a schema with "name", "baseSelector", and "fields" array
                        2. Each field should have: "name", "selector", "type", and optional "description"
                        3. Use CSS selectors that uniquely identify the elements
                        4. Focus on the main content areas and ignore navigation/footer
                        5. The schema should be reusable for similar pages on this site

                        Return ONLY the JSON schema, no explanations.""",
                        schema_type="json_schema"
                    )
                )

                # Create crawler instance
                async with AsyncWebCrawler(config=browser_config, verbose=False) as crawler:

                    # Crawl the URL to generate schema
                    result = await crawler.arun(url=url, config=crawl_config)

                    if not result.success:
                        return {
                            'url': url,
                            'error': f'Schema generation failed: {result.error_message}',
                            'status': 'error',
                            'error_code': 500
                        }

                    # Extract the generated schema
                    if hasattr(result, 'extracted_content') and result.extracted_content:
                        try:
                            # Parse the generated schema
                            import json
                            schema = json.loads(result.extracted_content)

                            # Validate schema structure
                            if not self._validate_extraction_schema(schema):
                                return {
                                    'url': url,
                                    'error': 'Generated schema has invalid structure',
                                    'status': 'error',
                                    'error_code': 500
                                }

                            # Save schema to file
                            with open(output_file, 'w', encoding='utf-8') as f:
                                json.dump(schema, f, indent=2, ensure_ascii=False)

                            return {
                                'url': url,
                                'instruction': instruction,
                                'schema_file': output_file,
                                'schema': schema,
                                'status': 'success',
                                'tool': 'Crawl4AI',
                                'message': f'Schema generated and saved to {output_file}'
                            }

                        except json.JSONDecodeError as e:
                            return {
                                'url': url,
                                'error': f'Failed to parse generated schema: {str(e)}',
                                'raw_content': result.extracted_content,
                                'status': 'error',
                                'error_code': 500
                            }
                    else:
                        return {
                            'url': url,
                            'error': 'No schema content generated',
                            'status': 'error',
                            'error_code': 500
                        }

            except Exception as e:
                return {
                    'url': url,
                    'error': f'Schema generation error: {str(e)}',
                    'status': 'error',
                    'error_code': 500
                }

        try:
            # Run the async function
            import sys
            if sys.version_info >= (3, 7):
                return asyncio.run(generate_schema_async())
            else:
                # Fallback for older Python versions
                import asyncio
                loop = asyncio.get_event_loop()
                if loop.is_running():
                    # If already in event loop, create new one
                    import concurrent.futures
                    with concurrent.futures.ThreadPoolExecutor() as executor:
                        future = executor.submit(asyncio.run, generate_schema_async())
                        return future.result()
                else:
                    return loop.run_until_complete(generate_schema_async())

        except Exception as e:
            return {
                'url': url,
                'error': f'Schema generation processing error: {str(e)}',
                'status': 'error',
                'error_code': 500
            }

    def extract_with_schema(self, url: str, schema_file: str, **options) -> Dict[str, Any]:
        """
        Extract structured data using a pre-generated schema (most efficient approach)
        10-100x more efficient than LLM extraction for repetitive patterns

        Args:
            url: URL to extract data from
            schema_file: Path to JSON schema file
            **options: Additional extraction options

        Returns:
            Structured extraction result as dictionary
        """
        try:
            from crawl4ai import AsyncWebCrawler, BrowserConfig, CrawlerRunConfig
            from crawl4ai.extraction_strategy import JsonCssExtractionStrategy
            import asyncio
            import json
        except ImportError:
            return {
                'url': url,
                'error': 'Crawl4AI library not available. Install with: pip install crawl4ai',
                'status': 'error',
                'error_code': 501
            }

        # Load and validate schema
        try:
            with open(schema_file, 'r', encoding='utf-8') as f:
                schema = json.load(f)
        except FileNotFoundError:
            return {
                'url': url,
                'error': f'Schema file not found: {schema_file}',
                'status': 'error',
                'error_code': 404
            }
        except json.JSONDecodeError as e:
            return {
                'url': url,
                'error': f'Invalid schema JSON: {str(e)}',
                'status': 'error',
                'error_code': 400
            }

        if not self._validate_extraction_schema(schema):
            return {
                'url': url,
                'error': 'Invalid schema structure',
                'status': 'error',
                'error_code': 400
            }

        async def extract_with_schema_async():
            """Async function to extract data using schema"""
            try:
                # Configure browser for efficient extraction
                browser_config = BrowserConfig(
                    headless=True,
                    viewport_width=1280,
                    viewport_height=800,
                    verbose=False
                )

                # Configure crawler for schema-based extraction
                crawl_config = CrawlerRunConfig(
                    extraction_strategy=JsonCssExtractionStrategy(schema=schema),
                    cache_mode=CacheMode.BYPASS,  # Get fresh content
                    page_timeout=30000
                )

                # Create crawler instance
                async with AsyncWebCrawler(config=browser_config, verbose=False) as crawler:

                    # Extract data using schema
                    result = await crawler.arun(url=url, config=crawl_config)

                    if not result.success:
                        return {
                            'url': url,
                            'error': f'Schema extraction failed: {result.error_message}',
                            'status': 'error',
                            'error_code': 500
                        }

                    # Process extracted data
                    if hasattr(result, 'extracted_content') and result.extracted_content:
                        try:
                            extracted_data = json.loads(result.extracted_content)

                            return {
                                'url': url,
                                'schema_file': schema_file,
                                'schema_name': schema.get('name', 'unnamed'),
                                'extracted_data': extracted_data,
                                'data_count': len(extracted_data) if isinstance(extracted_data, list) else 1,
                                'status': 'success',
                                'tool': 'Crawl4AI',
                                'extraction_method': 'json_css_schema',
                                'processing_time': 'schema_based'
                            }

                        except json.JSONDecodeError as e:
                            return {
                                'url': url,
                                'error': f'Failed to parse extracted data: {str(e)}',
                                'raw_content': result.extracted_content,
                                'status': 'error',
                                'error_code': 500
                            }
                    else:
                        return {
                            'url': url,
                            'error': 'No data extracted with schema',
                            'status': 'error',
                            'error_code': 500
                        }

            except Exception as e:
                return {
                    'url': url,
                    'error': f'Schema extraction error: {str(e)}',
                    'status': 'error',
                    'error_code': 500
                }

        try:
            # Run the async function
            import sys
            if sys.version_info >= (3, 7):
                return asyncio.run(extract_with_schema_async())
            else:
                # Fallback for older Python versions
                import asyncio
                loop = asyncio.get_event_loop()
                if loop.is_running():
                    # If already in event loop, create new one
                    import concurrent.futures
                    with concurrent.futures.ThreadPoolExecutor() as executor:
                        future = executor.submit(asyncio.run, extract_with_schema_async())
                        return future.result()
                else:
                    return loop.run_until_complete(extract_with_schema_async())

        except Exception as e:
            return {
                'url': url,
                'error': f'Schema extraction processing error: {str(e)}',
                'status': 'error',
                'error_code': 500
            }

    def _validate_extraction_schema(self, schema: dict) -> bool:
        """
        Validate that the extraction schema has the required structure

        Args:
            schema: Schema dictionary to validate

        Returns:
            True if schema is valid, False otherwise
        """
        required_fields = ['name', 'baseSelector', 'fields']
        if not all(field in schema for field in required_fields):
            return False

        if not isinstance(schema['fields'], list):
            return False

        for field in schema['fields']:
            field_required = ['name', 'selector', 'type']
            if not all(f in field for f in field_required):
                return False

        return True

    def _extract_title_from_markdown(self, content: str) -> str:
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
            if line and not line.startswith('#') and not line.startswith('©') and not line.isdigit():
                if len(line) < 100 and not line.startswith('```'):
                    # Remove common non-title patterns
                    if not any(pattern in line.lower() for pattern in ['page', '©', 'all rights reserved', 'error']):
                        return line
        return "Untitled Document"

    def _fallback_url_download(self, url: str) -> Dict[str, Any]:
        """
        Fallback URL download when Crawl4AI is not available
        Uses Python's built-in urllib to download and process simple web pages

        Args:
            url: URL to download and convert

        Returns:
            Conversion result as dictionary
        """
        try:
            import urllib.request
            import urllib.error
            from urllib.parse import urlparse

            print(f"📥 Using fallback download method for: {url}")

            # Download the URL content
            try:
                with urllib.request.urlopen(url, timeout=30) as response:
                    content_type = response.headers.get('content-type', '')
                    content = response.read().decode('utf-8', errors='replace')

            except urllib.error.URLError as e:
                return {
                    'url': url,
                    'error': f'Failed to download URL: {str(e)}',
                    'status': 'error',
                    'error_code': 404
                }
            except Exception as e:
                return {
                    'url': url,
                    'error': f'Download error: {str(e)}',
                    'status': 'error',
                    'error_code': 500
                }

            # Basic HTML to Markdown conversion
            if 'text/html' in content_type.lower():
                markdown_content = self._html_to_markdown_basic(content, url)
            else:
                # For non-HTML content, create a simple markdown
                markdown_content = f"# {url}\n\n**Content Type**: {content_type}\n\n**Content Length**: {len(content)} characters\n\n```\n{content[:1000]}\n...\n```\n"

            # Extract title
            title = self._extract_title_from_html(content) or urlparse(url).netloc

            return {
                'url': url,
                'title': title,
                'content': markdown_content,
                'status': 'success',
                'tool': 'fallback_download',
                'processing_time': 'basic_download',
                'warning': 'Crawl4AI not available - used basic download method. For advanced features, install: pip install crawl4ai'
            }

        except Exception as e:
            return {
                'url': url,
                'error': f'Fallback processing error: {str(e)}',
                'status': 'error',
                'error_code': 500
            }

    def _html_to_markdown_basic(self, html_content: str, url: str) -> str:
        """
        Basic HTML to Markdown conversion without BeautifulSoup

        Args:
            html_content: HTML content to convert
            url: Source URL for reference

        Returns:
            Markdown content
        """
        # If BeautifulSoup is available, use it
        if self.beautifulsoup_available:
            return self._html_to_markdown_with_bs4(html_content)

        # Basic regex-based conversion as fallback
        import re

        # Remove HTML tags
        content = re.sub(r'<script[^>]*>.*?</script>', '', html_content, flags=re.DOTALL | re.IGNORECASE)
        content = re.sub(r'<style[^>]*>.*?</style>', '', content, flags=re.DOTALL | re.IGNORECASE)
        content = re.sub(r'<[^>]+>', '\n', content)

        # Clean up whitespace
        lines = content.split('\n')
        cleaned_lines = []
        for line in lines:
            line = line.strip()
            if line and not line.isspace():
                cleaned_lines.append(line)

        # Add title
        title = self._extract_title_from_html_basic(html_content) or url

        markdown_content = f"# {title}\n\n" + '\n'.join(cleaned_lines)
        return markdown_content

    def _html_to_markdown_with_bs4(self, html_content: str) -> str:
        """Convert HTML to Markdown using BeautifulSoup"""
        try:
            from bs4 import BeautifulSoup
            soup = BeautifulSoup(html_content, 'html.parser')

            # Remove script and style elements
            for script in soup(["script", "style", "noscript"]):
                script.decompose()

            # Extract text content
            text = soup.get_text()

            # Clean up text and create markdown
            lines = (line.strip() for line in text.splitlines())
            chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
            text = '\n'.join(chunk for chunk in chunks if chunk)

            # Add title from HTML if available
            title_tag = soup.find('title')
            title = title_tag.get_text().strip() if title_tag else "Web Page"

            return f"# {title}\n\n{text}"

        except Exception:
            # Fallback to basic conversion
            return self._html_to_markdown_basic(html_content, "")

    def _extract_title_from_html(self, html_content: str) -> Optional[str]:
        """Extract title from HTML content"""
        if self.beautifulsoup_available:
            return self._extract_title_from_html_basic(html_content)
        return None

    def _extract_title_from_html_basic(self, html_content: str) -> Optional[str]:
        """Extract title from HTML using regex"""
        import re

        # Try to find title tag
        title_match = re.search(r'<title[^>]*>(.*?)</title>', html_content, re.IGNORECASE | re.DOTALL)
        if title_match:
            return title_match.group(1).strip()

        # Try to find h1 tag
        h1_match = re.search(r'<h1[^>]*>(.*?)</h1>', html_content, re.IGNORECASE | re.DOTALL)
        if h1_match:
            return h1_match.group(1).strip()

        return None

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

    # Crawl4AI specific options
    crawl4ai_group = parser.add_argument_group('Crawl4AI Options (for URLs)')

    crawl4ai_group.add_argument(
        '--wait-time',
        type=int,
        default=2000,
        help='Wait time in milliseconds for page loading (default: 2000)'
    )

    crawl4ai_group.add_argument(
        '--remove-overlays',
        action='store_true',
        default=True,
        help='Remove overlay elements and popups'
    )

    crawl4ai_group.add_argument(
        '--simulate-user',
        action='store_true',
        default=True,
        help='Simulate user behavior for better access'
    )

    crawl4ai_group.add_argument(
        '--bypass-cache',
        action='store_true',
        default=True,
        help='Bypass cache to get fresh content'
    )

    crawl4ai_group.add_argument(
        '--verbose-crawling',
        action='store_true',
        help='Enable verbose crawling output'
    )

    crawl4ai_group.add_argument(
        '--batch-file',
        help='File containing URLs to process (one per line)'
    )

    crawl4ai_group.add_argument(
        '--max-concurrent',
        type=int,
        default=5,
        help='Maximum concurrent requests for batch processing (default: 5)'
    )

    crawl4ai_group.add_argument(
        '--generate-schema',
        help='Generate extraction schema: --generate-schema <url> "<instruction>"'
    )

    crawl4ai_group.add_argument(
        '--use-schema',
        help='Use pre-generated schema for extraction: --use-schema <url> <schema_file>'
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

    # Handle batch processing
    if args.batch_file:
        # Batch URL processing from file
        if not os.path.exists(args.batch_file):
            print(f"❌ Error: Batch file not found: {args.batch_file}")
            sys.exit(1)

        try:
            with open(args.batch_file, 'r', encoding='utf-8') as f:
                urls = [line.strip() for line in f if line.strip() and not line.strip().startswith('#')]

            if not urls:
                print(f"❌ Error: No URLs found in batch file: {args.batch_file}")
                sys.exit(1)

            print(f"🚀 Starting batch processing of {len(urls)} URLs from {args.batch_file}")

            # Create converter
            try:
                converter = DocumentConverter()
            except RuntimeError as e:
                print(f"❌ Error: {e}")
                sys.exit(1)

            # Prepare batch options
            batch_options = {
                'max_concurrent': args.max_concurrent,
                'wait_time': args.wait_time,
                'remove_overlays': args.remove_overlays,
                'simulate_user': args.simulate_user,
                'bypass_cache': args.bypass_cache,
                'verbose_crawling': args.verbose_crawling
            }

            # Remove None values
            batch_options = {k: v for k, v in batch_options.items() if v is not None}

            # Execute batch conversion
            result = converter.convert_urls_batch(urls, **batch_options)

            if result['status'] == 'completed':
                print(f"✅ Batch processing completed!")
                print(f"📊 Summary: {result['summary']['successful']}/{result['summary']['total']} successful ({result['summary']['success_rate']})")

                # Save results if output specified
                if args.output:
                    with open(args.output, 'w', encoding='utf-8') as f:
                        json.dump(result, f, indent=2, ensure_ascii=False)
                    print(f"💾 Batch results saved to: {args.output}")
                else:
                    # Print individual results
                    for item in result['results']:
                        if item['status'] == 'success':
                            print(f"✅ {item['url']}: {item['content_length']} chars")
                        else:
                            print(f"❌ {item['url']}: {item.get('error', 'Unknown error')}")
            else:
                print(f"❌ Batch processing failed: {result.get('error', 'Unknown error')}")
                sys.exit(1)

            return

        except Exception as e:
            print(f"❌ Error reading batch file: {e}")
            sys.exit(1)

    # Check if input is provided for single conversion
    if not args.input:
        parser.error("input file/URL or --batch-file is required for conversion")

    # Handle Schema Generation
    if args.generate_schema:
        # Parse schema generation arguments
        if not args.input:
            parser.error("--generate-schema requires a URL")

        # Extract instruction from generate_schema argument
        parts = args.generate_schema.split(' ', 1)
        if len(parts) != 2:
            parser.error("--generate-schema format: <url> \"<instruction>\"")

        schema_url, instruction = parts
        output_file = args.output or "extraction_schema.json"

        print(f"🔍 Generating extraction schema for: {schema_url}")
        print(f"📝 Instruction: {instruction}")

        # Create converter
        try:
            converter = DocumentConverter()
        except RuntimeError as e:
            print(f"❌ Error: {e}")
            sys.exit(1)

        # Generate schema
        result = converter.generate_extraction_schema(schema_url, instruction, output_file)

        if result['status'] == 'success':
            print(f"✅ Schema generated successfully!")
            print(f"📁 Saved to: {result['schema_file']}")
            print(f"🏷️  Schema name: {result['schema'].get('name', 'unnamed')}")
            print(f"📊 Fields defined: {len(result['schema'].get('fields', []))}")
        else:
            print(f"❌ Schema generation failed: {result.get('error', 'Unknown error')}")
            sys.exit(1)

        return

    # Handle Schema-based Extraction
    if args.use_schema:
        # Parse schema extraction arguments
        if not args.input:
            parser.error("--use-schema requires a URL")

        parts = args.use_schema.split(' ', 1)
        if len(parts) != 2:
            parser.error("--use-schema format: <url> <schema_file>")

        extract_url, schema_file = parts

        print(f"🎯 Extracting data from: {extract_url}")
        print(f"📋 Using schema: {schema_file}")

        # Create converter
        try:
            converter = DocumentConverter()
        except RuntimeError as e:
            print(f"❌ Error: {e}")
            sys.exit(1)

        # Extract data using schema
        result = converter.extract_with_schema(extract_url, schema_file)

        if result['status'] == 'success':
            print(f"✅ Data extraction successful!")
            print(f"🏷️  Schema: {result['schema_name']}")
            print(f"📊 Records extracted: {result['data_count']}")

            # Save results if output specified
            if args.output:
                with open(args.output, 'w', encoding='utf-8') as f:
                    json.dump(result, f, indent=2, ensure_ascii=False)
                print(f"💾 Results saved to: {args.output}")
            else:
                # Print extracted data
                print(f"\n📄 Extracted Data:")
                print(json.dumps(result['extracted_data'], indent=2, ensure_ascii=False))
        else:
            print(f"❌ Data extraction failed: {result.get('error', 'Unknown error')}")
            sys.exit(1)

        return

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

    # Add Crawl4AI options for URLs
    if input_path.startswith(('http://', 'https://')):
        options.update({
            'wait_time': args.wait_time,
            'remove_overlays': args.remove_overlays,
            'simulate_user': args.simulate_user,
            'bypass_cache': args.bypass_cache,
            'verbose_crawling': args.verbose_crawling
        })

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