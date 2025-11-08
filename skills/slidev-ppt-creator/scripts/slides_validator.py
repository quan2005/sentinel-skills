#!/usr/bin/env python3
"""
Enhanced Slides Validator for Slidev PPT Creator
Validates generated slides.md files for correct Slidev syntax and structure.
Includes comprehensive error handling and detailed reporting.
"""

import re
import os
import sys
from typing import Dict, List, Tuple, Any, Optional
from pathlib import Path

# Import error handling
try:
    from .error_handler import (
        SlidevError, ValidationError, handle_slidev_errors,
        validate_file_path, validate_string_input, SafeFileOperations
    )
except ImportError:
    # Fallback if running as standalone script
    sys.path.insert(0, os.path.dirname(__file__))
    from error_handler import (
        SlidevError, ValidationError, handle_slidev_errors,
        validate_file_path, validate_string_input, SafeFileOperations
    )

class SlidesValidator:
    """Enhanced slides validator with comprehensive error handling."""

    def __init__(self, strict_mode: bool = False):
        """
        Initialize the validator.

        Args:
            strict_mode: If True, treat warnings as errors
        """
        self.strict_mode = strict_mode
        self.errors = []
        self.warnings = []
        self.stats = {}

        # Slidev syntax patterns
        self.frontmatter_pattern = re.compile(r'^---\s*\n(.*?)\n---\s*$', re.MULTILINE | re.DOTALL)
        self.slide_separator_pattern = re.compile(r'^---\s*$', re.MULTILINE)
        self.vue_component_pattern = re.compile(r'<[^>]+>')
        self.mermaid_pattern = re.compile(r'```mermaid')
        self.code_block_pattern = re.compile(r'```(\w+)?')
        self.layout_pattern = re.compile(r'layout:\s*(\w+)')
        self.theme_pattern = re.compile(r'theme:\s*(\w+)')

        # Required frontmatter fields
        self.required_frontmatter = ['title']
        self.recommended_frontmatter = ['theme', 'author', 'date']

        # Valid layouts and themes
        self.valid_layouts = ['default', 'cover', 'section', 'end', 'center', 'intro', 'two-cols', 'image-right', 'image-left']
        self.valid_themes = ['default', 'seriph', 'shades-of-purple', 'dracula', 'minima', 'dev', 'smb']

    @handle_slidev_errors(fallback_result={'valid': False, 'errors': ['Validation failed due to system error']})
    def validate_file(self, file_path: str) -> Dict[str, Any]:
        """
        Validate a slides.md file.

        Args:
            file_path: Path to the slides.md file

        Returns:
            Validation result with errors, warnings, and statistics
        """
        # Reset error/warning lists
        self.errors = []
        self.warnings = []
        self.stats = {}

        # Validate input
        validate_file_path(file_path, must_exist=True)

        # Read file safely
        try:
            content = SafeFileOperations.read_file(file_path)
        except Exception as e:
            self.errors.append(f"Failed to read file: {e}")
            return self._build_result()

        # Validate file is not empty
        if not content.strip():
            self.errors.append("File is empty")
            return self._build_result()

        # Perform comprehensive validations
        self._validate_frontmatter(content)
        self._validate_slide_structure(content)
        self._validate_syntax(content)
        self._validate_content_quality(content)
        self._validate_components(content)
        self._validate_accessibility(content)

        # Build result
        result = self._build_result()

        # Treat warnings as errors if in strict mode
        if self.strict_mode and self.warnings:
            result['valid'] = False
            result['errors'].extend([f"Strict mode: {warning}" for warning in self.warnings])

        return result

    @handle_slidev_errors(fallback_result={'valid': False, 'errors': ['Frontmatter validation failed']})
    def _validate_frontmatter(self, content: str):
        """Validate YAML frontmatter."""
        frontmatter_match = self.frontmatter_pattern.match(content)

        if not frontmatter_match:
            self.errors.append("Missing or invalid YAML frontmatter")
            return

        frontmatter_text = frontmatter_match.group(1)
        self.stats['has_frontmatter'] = True

        # Parse frontmatter
        try:
            import yaml
            frontmatter_data = yaml.safe_load(frontmatter_text)
            self.stats['frontmatter_parsed'] = True
        except ImportError:
            self.warnings.append("PyYAML not available, skipping frontmatter validation")
            return
        except yaml.YAMLError as e:
            self.errors.append(f"Invalid YAML frontmatter: {e}")
            return

        # Validate required fields
        if not isinstance(frontmatter_data, dict):
            self.errors.append("Frontmatter must be a dictionary")
            return

        for field in self.required_frontmatter:
            if field not in frontmatter_data:
                self.errors.append(f"Missing required frontmatter field: {field}")

        # Check recommended fields
        for field in self.recommended_frontmatter:
            if field not in frontmatter_data:
                self.warnings.append(f"Missing recommended frontmatter field: {field}")

        # Validate theme
        if 'theme' in frontmatter_data:
            theme = frontmatter_data['theme']
            if theme not in self.valid_themes:
                self.warnings.append(f"Unknown theme: {theme}. Valid themes: {', '.join(self.valid_themes)}")

        # Store frontmatter stats
        self.stats['frontmatter_fields'] = list(frontmatter_data.keys())
        self.stats['frontmatter_size'] = len(frontmatter_text)

    @handle_slidev_errors(fallback_result={'valid': False, 'errors': ['Slide structure validation failed']})
    def _validate_slide_structure(self, content: str):
        """Validate slide structure and separators."""
        # Split content into slides
        parts = self.slide_separator_pattern.split(content)

        if not parts:
            self.errors.append("No slide separators found")
            return

        # Remove frontmatter from slide count
        if self.frontmatter_pattern.match(parts[0]):
            slides = parts[1:]
        else:
            slides = parts

        self.stats['slide_count'] = len(slides)

        if len(slides) == 0:
            self.errors.append("No slides found after frontmatter")
            return

        # Validate each slide
        for i, slide in enumerate(slides):
            slide_num = i + 1
            slide_content = slide.strip()

            if not slide_content:
                self.warnings.append(f"Slide {slide_num} is empty")
                continue

            # Check for slide title (first line starting with #)
            lines = slide_content.split('\n')
            has_title = any(line.strip().startswith('#') for line in lines if line.strip())

            if not has_title:
                self.warnings.append(f"Slide {slide_num} has no title (no # heading found)")

            # Check slide content length
            if len(slide_content) > 5000:  # Reasonable limit
                self.warnings.append(f"Slide {slide_num} is very long ({len(slide_content)} characters)")

    @handle_slidev_errors(fallback_result={'valid': False, 'errors': ['Syntax validation failed']})
    def _validate_syntax(self, content: str):
        """Validate Slidev-specific syntax."""
        # Check for unclosed code blocks
        code_blocks = self.code_block_pattern.findall(content)
        open_blocks = content.count('```')
        close_blocks = len(code_blocks)

        if open_blocks != close_blocks:
            self.errors.append(f"Unclosed code blocks: {open_blocks} opening, {close_blocks} closing")

        # Check for unclosed Vue components
        vue_components = self.vue_component_pattern.findall(content)
        self.stats['vue_components'] = len(vue_components)

        # Validate Vue component syntax
        for component in vue_components:
            if component.startswith('</'):
                # Closing tag
                pass  # Could validate matching opening tag
            else:
                # Opening tag
                if not component.endswith('/>') and not component.endswith('</' + component[1:-1].split()[0] + '>'):
                    # Unclosed tag (self-closing or should have closing tag)
                    pass  # More complex validation needed

        # Check Mermaid diagrams
        mermaid_matches = self.mermaid_pattern.findall(content)
        self.stats['mermaid_diagrams'] = len(mermaid_matches)

        # Validate layout usage
        layouts = self.layout_pattern.findall(content)
        for layout in layouts:
            if layout not in self.valid_layouts:
                self.warnings.append(f"Unknown layout: {layout}. Valid layouts: {', '.join(self.valid_layouts)}")

        self.stats['layouts_used'] = list(set(layouts))

    def _validate_content_quality(self, content: str):
        """Validate content quality and best practices."""
        # Check for common issues
        if content.count('{{') != content.count('}}'):
            self.errors.append("Mismatched Vue template delimiters")

        # Check for very long lines
        lines = content.split('\n')
        long_lines = [i for i, line in enumerate(lines, 1) if len(line) > 200]

        if long_lines:
            self.warnings.append(f"Very long lines found: {len(long_lines)} lines over 200 characters")

        # Check for potential accessibility issues
        if 'alt=' not in content and '![' in content:
            self.warnings.append("Images found without alt text (accessibility issue)")

        # Check for TODO comments
        if 'TODO' in content.upper():
            self.warnings.append("TODO comments found in presentation")

    def _validate_components(self, content: str):
        """Validate Vue component usage."""
        # Check for component imports
        component_imports = re.findall(r'import\s+(\w+)\s+from', content)
        self.stats['component_imports'] = component_imports

        # Check for component registration
        component_usage = re.findall(r'<([A-Z][a-zA-Z]+)', content)
        self.stats['components_used'] = list(set(component_usage))

        # Validate that used components are imported
        unimported_components = set(component_usage) - set(component_imports)
        if unimported_components and 'vue' not in unimported_components:
            # Filter out Vue built-in components
            filtered = [comp for comp in unimported_components if comp not in ['Transition', 'KeepAlive', 'Teleport']]
            if filtered:
                self.warnings.append(f"Components used but not imported: {', '.join(filtered)}")

    def _validate_accessibility(self, content: str):
        """Validate accessibility compliance."""
        # Check for heading structure
        headings = re.findall(r'^(#{1,6})\s+(.+)$', content, re.MULTILINE)
        if headings:
            levels = [len(h[0]) for h in headings]
            # Check for skipped heading levels
            for i in range(1, len(levels)):
                if levels[i] - levels[i-1] > 1:
                    self.warnings.append(f"Skipped heading level: H{levels[i-1]} to H{levels[i]}")
                    break

        # Check for color-only information
        color_indicators = ['red', 'green', 'blue', 'yellow', 'orange', 'purple']
        for color in color_indicators:
            if color in content.lower() and 'color' not in content.lower():
                self.warnings.append(f"Color reference found: '{color}'. Consider using symbols/text in addition to color.")

    def _build_result(self) -> Dict[str, Any]:
        """Build validation result dictionary."""
        return {
            'valid': len(self.errors) == 0,
            'errors': self.errors,
            'warnings': self.warnings,
            'stats': self.stats,
            'error_count': len(self.errors),
            'warning_count': len(self.warnings)
        }

    def validate_presentation(self, presentation_path: str) -> Dict[str, Any]:
        """
        Validate a complete presentation directory.

        Args:
            presentation_path: Path to presentation directory

        Returns:
            Validation result for the entire presentation
        """
        results = {
            'slides': {},
            'components': {},
            'overall': {'valid': True, 'errors': [], 'warnings': []}
        }

        # Validate slides.md
        slides_path = os.path.join(presentation_path, 'slides.md')
        if os.path.exists(slides_path):
            results['slides'] = self.validate_file(slides_path)
        else:
            results['overall']['valid'] = False
            results['overall']['errors'].append('slides.md not found')

        # Validate package.json if it exists
        package_path = os.path.join(presentation_path, 'package.json')
        if os.path.exists(package_path):
            try:
                from .error_handler import SafeJSONOperations
                package_data = SafeJSONOperations.load_json(package_path)

                # Check for Slidev dependencies
                deps = package_data.get('dependencies', {})
                dev_deps = package_data.get('devDependencies', {})

                if '@slidev/cli' not in deps and '@slidev/cli' not in dev_deps:
                    results['overall']['warnings'].append('@slidev/cli not found in dependencies')

                if '@slidev/theme-default' not in deps and '@slidev/theme-default' not in dev_deps:
                    results['overall']['warnings'].append('No Slidev theme found in dependencies')

            except Exception as e:
                results['overall']['warnings'].append(f'Could not validate package.json: {e}')

        # Validate components directory
        components_dir = os.path.join(presentation_path, 'components')
        if os.path.exists(components_dir):
            for component_file in Path(components_dir).glob('*.vue'):
                try:
                    component_content = SafeFileOperations.read_file(str(component_file))
                    if not component_content.strip():
                        results['overall']['warnings'].append(f'Component file is empty: {component_file.name}')
                except Exception as e:
                    results['overall']['warnings'].append(f'Could not read component {component_file.name}: {e}')

        # Combine all errors and warnings
        all_errors = results['slides'].get('errors', []) + results['overall']['errors']
        all_warnings = results['slides'].get('warnings', []) + results['overall']['warnings']

        results['overall']['valid'] = len(all_errors) == 0
        results['overall']['errors'] = all_errors
        results['overall']['warnings'] = all_warnings
        results['overall']['error_count'] = len(all_errors)
        results['overall']['warning_count'] = len(all_warnings)

        return results

def main():
    """Command line interface for slides validator."""
    import argparse
    import json

    parser = argparse.ArgumentParser(description='Validate Slidev presentations')
    parser.add_argument('path', help='Path to slides.md file or presentation directory')
    parser.add_argument('--strict', action='store_true', help='Treat warnings as errors')
    parser.add_argument('--json', action='store_true', help='Output results as JSON')
    parser.add_argument('--output', '-o', help='Output file for validation report')

    args = parser.parse_args()

    validator = SlidesValidator(strict_mode=args.strict)

    if os.path.isfile(args.path):
        # Validate single file
        result = validator.validate_file(args.path)
    elif os.path.isdir(args.path):
        # Validate presentation directory
        result = validator.validate_presentation(args.path)
    else:
        print(f"Error: Path does not exist: {args.path}")
        return 1

    # Output results
    if args.json:
        output = json.dumps(result, indent=2)
    else:
        output = format_validation_report(result)

    if args.output:
        try:
            with open(args.output, 'w', encoding='utf-8') as f:
                f.write(output)
            print(f"Validation report saved to: {args.output}")
        except Exception as e:
            print(f"Error saving report: {e}")
            return 1
    else:
        print(output)

    return 0 if result.get('overall', result).get('valid', False) else 1

def format_validation_report(result: Dict[str, Any]) -> str:
    """Format validation result as readable report."""
    overall = result.get('overall', result)

    report = []
    report.append("📋 Slidev Presentation Validation Report")
    report.append("=" * 50)
    report.append(f"Status: {'✅ Valid' if overall['valid'] else '❌ Invalid'}")
    report.append(f"Errors: {overall['error_count']}")
    report.append(f"Warnings: {overall['warning_count']}")
    report.append("")

    if overall['errors']:
        report.append("🚨 Errors:")
        for error in overall['errors']:
            report.append(f"  ❌ {error}")
        report.append("")

    if overall['warnings']:
        report.append("⚠️  Warnings:")
        for warning in overall['warnings']:
            report.append(f"  ⚠️  {warning}")
        report.append("")

    if 'stats' in overall and overall['stats']:
        report.append("📊 Statistics:")
        for key, value in overall['stats'].items():
            report.append(f"  {key}: {value}")

    return "\n".join(report)

if __name__ == "__main__":
    import sys
    sys.exit(main())
        recommended_fields = ['author', 'date']
        for field in recommended_fields:
            if f'{field}:' not in frontmatter:
                self.warnings.append(f"Missing recommended field in frontmatter: {field}")

        # Validate theme format
        if 'theme:' in frontmatter:
            theme_match = re.search(r'time:\s*(.+)', frontmatter)
            if theme_match:
                theme = theme_match.group(1).strip()
                if not re.match(r'^[a-zA-Z0-9_-]+$', theme):
                    self.warnings.append(f"Theme name may contain invalid characters: {theme}")

    def _validate_slide_structure(self, content: str) -> None:
        """Validate overall slide structure."""
        # Split content into slides
        parts = re.split(r'\n^---\s*\n', content, flags=re.MULTILINE)

        if len(parts) < 2:
            self.errors.append("Presentation must have at least one slide (frontmatter + content)")
            return

        # Remove frontmatter from slide count
        slide_count = len(parts) - 1

        if slide_count < 2:
            self.warnings.append("Presentation has fewer than 2 slides")

        if slide_count > 50:
            self.warnings.append(f"Presentation has many slides ({slide_count}). Consider splitting into multiple presentations.")

        # Validate each slide
        for i, slide_content in enumerate(parts[1:], 1):  # Skip frontmatter
            self._validate_individual_slide(slide_content, i)

    def _validate_individual_slide(self, slide_content: str, slide_number: int) -> None:
        """Validate an individual slide."""
        slide_content = slide_content.strip()

        if not slide_content:
            self.warnings.append(f"Slide {slide_number} is empty")
            return

        # Check for slide title (first line should be a heading)
        lines = slide_content.split('\n')
        first_line = lines[0].strip() if lines else ''

        if not first_line.startswith('#'):
            self.warnings.append(f"Slide {slide_number} should start with a heading (# ## ###)")
        elif len(first_line) > 100:
            self.warnings.append(f"Slide {slide_number} title is very long ({len(first_line)} characters)")

        # Check slide content length
        if len(slide_content) > 2000:
            self.warnings.append(f"Slide {slide_number} is very long ({len(slide_content)} characters). Consider splitting into multiple slides.")

        # Validate code blocks
        code_blocks = re.findall(self.code_block_pattern, slide_content)
        for lang in code_blocks:
            if lang and not re.match(r'^[a-zA-Z0-9_-]+$', lang):
                self.warnings.append(f"Slide {slide_number} contains code block with potentially invalid language: {lang}")

    def _validate_syntax(self, content: str) -> None:
        """Validate Slidev-specific syntax."""
        # Check for unclosed Vue components
        vue_openings = len(re.findall(r'<[^/][^>]*[^/]>', content))
        vue_closings = len(re.findall(r'</[^>]+>', content))
        vue_self_closing = len(re.findall(r'<[^>]+/>', content))

        if vue_openings != vue_closings + vue_self_closing:
            self.errors.append("Unclosed Vue components detected")

        # Validate Mermaid diagrams
        mermaid_blocks = re.findall(r'```mermaid\n(.*?)\n```', content, re.DOTALL)
        for i, mermaid_code in enumerate(mermaid_blocks, 1):
            self._validate_mermaid_syntax(mermaid_code, i)

        # Validate Slidev directives
        self._validate_slidev_directives(content)

    def _validate_mermaid_syntax(self, mermaid_code: str, diagram_number: int) -> None:
        """Validate Mermaid diagram syntax."""
        lines = mermaid_code.strip().split('\n')
        if not lines:
            self.errors.append(f"Mermaid diagram {diagram_number} is empty")
            return

        # Check diagram type
        first_line = lines[0].strip().lower()
        valid_types = ['graph', 'flowchart', 'sequencediagram', 'classdiagram', 'stateDiagram', 'erDiagram', 'pie', 'gitgraph']

        if not any(first_line.startswith(dt) for dt in valid_types):
            self.warnings.append(f"Mermaid diagram {diagram_number} may have invalid diagram type: {first_line}")

    def _validate_slidev_directives(self, content: str) -> None:
        """Validate Slidev-specific directives."""
        # Check v-click usage
        v_clicks = re.findall(r'v-click', content)
        if len(v_clicks) > 20:
            self.warnings.append(f"Many v-click directives found ({len(v_clicks)}). Ensure they are used effectively.")

        # Check layout directives
        layouts = re.findall(r'layout:\s*(\w+)', content)
        valid_layouts = ['cover', 'default', 'section', 'center', 'two-cols', 'image-right', 'image-left', 'quote', 'none']

        for layout in layouts:
            if layout not in valid_layouts:
                self.warnings.append(f"Potentially invalid layout: {layout}")

    def _validate_components(self, content: str) -> None:
        """Validate component usage."""
        # Check for custom components
        custom_components = re.findall(r'<([A-Z][a-zA-Z0-9-]*)', content)
        standard_components = ['div', 'span', 'p', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'ul', 'ol', 'li', 'img', 'a', 'button']

        custom_components = [comp for comp in custom_components if comp not in standard_components]

        if custom_components:
            unique_custom = list(set(custom_components))
            self.warnings.append(f"Custom components detected: {', '.join(unique_custom)}. Ensure these components are properly defined.")

    def _calculate_statistics(self, content: str) -> None:
        """Calculate presentation statistics."""
        slides = re.split(r'\n^---\s*\n', content, flags=re.MULTILINE)
        slide_count = max(0, len(slides) - 1)  # Exclude frontmatter

        word_count = len(content.split())
        char_count = len(content)

        # Store statistics for the report
        self.statistics = {
            'slide_count': slide_count,
            'word_count': word_count,
            'char_count': char_count,
            'avg_words_per_slide': word_count / max(1, slide_count)
        }

    def _build_result(self) -> Dict[str, Any]:
        """Build validation result."""
        return {
            'valid': len(self.errors) == 0,
            'errors': self.errors,
            'warnings': self.warnings,
            'statistics': getattr(self, 'statistics', {}),
            'summary': self._generate_summary()
        }

    def _generate_summary(self) -> str:
        """Generate validation summary."""
        error_count = len(self.errors)
        warning_count = len(self.warnings)

        if error_count == 0 and warning_count == 0:
            return "✅ Validation passed with no issues found."
        elif error_count == 0:
            return f"⚠️  Validation passed with {warning_count} warning(s)."
        else:
            return f"❌ Validation failed with {error_count} error(s) and {warning_count} warning(s)."

    def validate_project_structure(self, project_path: str) -> Dict[str, Any]:
        """
        Validate the entire Slidev project structure.

        Args:
            project_path: Path to the Slidev project directory

        Returns:
            Validation result for the project
        """
        project_errors = []
        project_warnings = []

        # Check required files
        required_files = ['slides.md', 'package.json']
        for file in required_files:
            if not os.path.exists(os.path.join(project_path, file)):
                project_errors.append(f"Missing required file: {file}")

        # Check optional but recommended files
        recommended_files = ['README.md', 'style.css']
        for file in recommended_files:
            if not os.path.exists(os.path.join(project_path, file)):
                project_warnings.append(f"Missing recommended file: {file}")

        # Validate package.json
        package_json_path = os.path.join(project_path, 'package.json')
        if os.path.exists(package_json_path):
            try:
                import json
                with open(package_json_path, 'r') as f:
                    package_data = json.load(f)

                # Check for Slidev dependencies
                if 'dependencies' in package_data:
                    slidev_deps = [dep for dep in package_data['dependencies'] if 'slidev' in dep]
                    if not slidev_deps:
                        project_warnings.append("No Slidev dependencies found in package.json")

                # Check for required scripts
                if 'scripts' in package_data:
                    required_scripts = ['dev', 'build']
                    for script in required_scripts:
                        if script not in package_data['scripts']:
                            project_warnings.append(f"Missing recommended script: {script}")

            except Exception as e:
                project_errors.append(f"Invalid package.json: {e}")

        # Check components directory
        components_dir = os.path.join(project_path, 'components')
        if os.path.exists(components_dir):
            vue_files = [f for f in os.listdir(components_dir) if f.endswith('.vue')]
            if vue_files:
                project_warnings.append(f"Found {len(vue_files)} custom Vue component(s)")

        return {
            'valid': len(project_errors) == 0,
            'errors': project_errors,
            'warnings': project_warnings,
            'summary': self._generate_project_summary(project_errors, project_warnings)
        }

    def _generate_project_summary(self, errors: List[str], warnings: List[str]) -> str:
        """Generate project validation summary."""
        error_count = len(errors)
        warning_count = len(warnings)

        if error_count == 0 and warning_count == 0:
            return "✅ Project structure is valid."
        elif error_count == 0:
            return f"⚠️  Project structure is valid with {warning_count} warning(s)."
        else:
            return f"❌ Project structure validation failed with {error_count} error(s) and {warning_count} warning(s)."

def main():
    """Command line interface for slides validator."""
    import sys
    import argparse
    import json

    parser = argparse.ArgumentParser(description='Validate Slidev presentations')
    parser.add_argument('path', help='Path to slides.md file or project directory')
    parser.add_argument('--project', action='store_true', help='Validate entire project structure')
    parser.add_argument('--output', help='Output validation result to JSON file')

    args = parser.parse_args()

    validator = SlidesValidator()

    if args.project:
        result = validator.validate_project_structure(args.path)
    else:
        result = validator.validate_file(args.path)

    # Print result
    print(result['summary'])
    if result['errors']:
        print("\nErrors:")
        for error in result['errors']:
            print(f"  ❌ {error}")
    if result['warnings']:
        print("\nWarnings:")
        for warning in result['warnings']:
            print(f"  ⚠️  {warning}")

    if hasattr(result, 'statistics'):
        print(f"\nStatistics:")
        print(f"  Slides: {result['statistics'].get('slide_count', 'N/A')}")
        print(f"  Words: {result['statistics'].get('word_count', 'N/A')}")
        print(f"  Avg words per slide: {result['statistics'].get('avg_words_per_slide', 'N/A'):.1f}")

    # Save to JSON if requested
    if args.output:
        with open(args.output, 'w', encoding='utf-8') as f:
            json.dump(result, f, indent=2, ensure_ascii=False)
        print(f"\nValidation result saved to: {args.output}")

    sys.exit(0 if result['valid'] else 1)

if __name__ == "__main__":
    main()