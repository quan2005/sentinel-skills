#!/usr/bin/env python3
"""
Slides Validator for Slidev PPT Creator
Validates generated slides.md files for correct Slidev syntax and structure.
"""

import re
import os
from typing import Dict, List, Tuple, Any

class SlidesValidator:
    def __init__(self):
        self.errors = []
        self.warnings = []

        # Slidev syntax patterns
        self.frontmatter_pattern = r'^---\s*\n(.*?)\n---\s*$'
        self.slide_separator_pattern = r'^---\s*$'
        self.vue_component_pattern = r'<[^>]+>'
        self.mermaid_pattern = r'```mermaid'
        self.code_block_pattern = r'```(\w+)?'

    def validate_file(self, file_path: str) -> Dict[str, Any]:
        """
        Validate a slides.md file.

        Args:
            file_path: Path to the slides.md file

        Returns:
            Validation result with errors, warnings, and statistics
        """
        self.errors = []
        self.warnings = []

        if not os.path.exists(file_path):
            self.errors.append(f"File not found: {file_path}")
            return self._build_result()

        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
        except Exception as e:
            self.errors.append(f"Failed to read file: {e}")
            return self._build_result()

        # Perform validations
        self._validate_frontmatter(content)
        self._validate_slide_structure(content)
        self._validate_syntax(content)
        self._validate_components(content)
        self._calculate_statistics(content)

        return self._build_result()

    def _validate_frontmatter(self, content: str) -> None:
        """Validate YAML frontmatter."""
        frontmatter_match = re.match(self.frontmatter_pattern, content, re.DOTALL)

        if not frontmatter_match:
            self.errors.append("Missing or invalid YAML frontmatter")
            return

        frontmatter = frontmatter_match.group(1)

        # Check required fields
        required_fields = ['title', 'theme']
        for field in required_fields:
            if f'{field}:' not in frontmatter:
                self.errors.append(f"Missing required field in frontmatter: {field}")

        # Check optional but recommended fields
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