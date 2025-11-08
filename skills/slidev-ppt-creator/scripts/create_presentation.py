#!/usr/bin/env python3
"""
Main script for Slidev PPT Creator
Coordinates all components to create presentations from user input.
"""

import os
import sys
import json
import argparse
from pathlib import Path

# Import our modules
from content_analyzer import ContentAnalyzer
from template_generator import TemplateGenerator
from chart_generator import ChartGenerator
from slides_validator import SlidesValidator

class SlidevPPTCreator:
    def __init__(self, output_dir: str = None):
        self.output_dir = output_dir or os.getcwd()
        self.analyzer = ContentAnalyzer()
        self.template_generator = TemplateGenerator(
            os.path.join(os.path.dirname(__file__), '..', 'assets')
        )
        self.chart_generator = ChartGenerator()
        self.validator = SlidesValidator()

    def create_presentation(self, user_input: str, title: str = None) -> dict:
        """
        Create a complete Slidev presentation from user input.

        Args:
            user_input: Natural language description of the presentation
            title: Optional title for the presentation

        Returns:
            Dictionary with creation results and file paths
        """
        print("🔍 Analyzing user input...")
        analysis = self.analyzer.analyze(user_input)

        print(f"📊 Presentation type: {analysis['presentation_type']}")
        print(f"🎨 Recommended template: {analysis['recommended_template']}")
        print(f"📋 Structure: {len(analysis['structure'])} sections")
        print(f"🖼️  Visual elements: {', '.join(analysis['visual_elements'])}")

        print("\n📝 Generating slides content...")
        slides_content = self.template_generator.generate_slides_markdown(
            analysis, title
        )

        print("📦 Creating project files...")
        result = self._create_project_files(slides_content, analysis, title)

        print("✅ Validating generated slides...")
        validation_result = self.validator.validate_file(result['slides_path'])

        if not validation_result['valid']:
            print("⚠️  Validation warnings/errors found:")
            for warning in validation_result['warnings']:
                print(f"  ⚠️  {warning}")
            for error in validation_result['errors']:
                print(f"  ❌ {error}")

        print(f"\n🎉 Presentation created successfully!")
        print(f"📁 Output directory: {result['project_dir']}")
        print(f"📄 Main file: {result['slides_path']}")

        return {
            'analysis': analysis,
            'files_created': result,
            'validation': validation_result,
            'success': True
        }

    def _create_project_files(self, slides_content: str, analysis: dict, title: str) -> dict:
        """Create all necessary project files."""
        # Create output directory
        project_name = (title or "presentation").lower().replace(' ', '-')
        project_dir = os.path.join(self.output_dir, project_name)

        os.makedirs(project_dir, exist_ok=True)

        # Create slides.md
        slides_path = os.path.join(project_dir, 'slides.md')
        with open(slides_path, 'w', encoding='utf-8') as f:
            f.write(slides_content)

        # Create package.json
        package_content = self.template_generator.generate_package_json(
            title or "Presentation", analysis['recommended_template']
        )
        package_path = os.path.join(project_dir, 'package.json')
        with open(package_path, 'w', encoding='utf-8') as f:
            f.write(package_content)

        # Create README.md
        readme_content = self.template_generator.generate_readme(
            title or "Presentation", analysis['recommended_template']
        )
        readme_path = os.path.join(project_dir, 'README.md')
        with open(readme_path, 'w', encoding='utf-8') as f:
            f.write(readme_content)

        # Create style.css if needed
        if analysis['visual_elements']:
            style_content = self._generate_custom_styles(analysis)
            style_path = os.path.join(project_dir, 'style.css')
            with open(style_path, 'w', encoding='utf-8') as f:
                f.write(style_content)

        return {
            'project_dir': project_dir,
            'slides_path': slides_path,
            'package_path': package_path,
            'readme_path': readme_path,
            'style_path': os.path.join(project_dir, 'style.css') if analysis['visual_elements'] else None
        }

    def _generate_custom_styles(self, analysis: dict) -> str:
        """Generate custom CSS based on analysis."""
        template_type = analysis['recommended_template']
        visual_elements = analysis['visual_elements']

        base_styles = {
            'business': """
.slidev-layout {
  font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
}

.business-highlight {
  background: linear-gradient(135deg, #1e40af 0%, #3b82f6 100%);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
  font-weight: 600;
}

.metric-card {
  background: linear-gradient(135deg, #f8fafc 0%, #e2e8f0 100%);
  border-radius: 12px;
  padding: 20px;
  border: 1px solid #cbd5e1;
  transition: transform 0.2s ease, box-shadow 0.2s ease;
}

.metric-card:hover {
  transform: translateY(-2px);
  box-shadow: 0 8px 25px rgba(0, 0, 0, 0.1);
}
            """,

            'technical': """
.slidev-layout {
  font-family: 'JetBrains Mono', 'Fira Code', monospace;
}

.code-block {
  background: #1e1e1e;
  border-radius: 8px;
  padding: 16px;
  font-size: 14px;
  line-height: 1.6;
  overflow-x: auto;
}

.tech-highlight {
  background: linear-gradient(135deg, #7c3aed 0%, #a855f7 100%);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
  font-weight: 600;
}
            """,

            'education': """
.slidev-layout {
  font-family: 'Source Sans Pro', -apple-system, BlinkMacSystemFont, sans-serif;
}

.learning-objective {
  background: linear-gradient(135deg, #9333ea 0%, #a855f7 100%);
  color: white;
  padding: 16px;
  border-radius: 8px;
  margin: 16px 0;
}

.key-point {
  border-left: 4px solid #9333ea;
  padding-left: 16px;
  margin: 12px 0;
}
            """,

            'general': """
.slidev-layout {
  font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
}

.highlight-box {
  background: #f0f9ff;
  border: 1px solid #0284c7;
  border-radius: 8px;
  padding: 16px;
  margin: 12px 0;
}
            """
        }

        styles = base_styles.get(template_type, base_styles['general'])

        # Add visual element specific styles
        if 'chart' in visual_elements:
            styles += """

.chart-container {
  margin: 16px 0;
  padding: 16px;
  background: #f9fafb;
  border-radius: 8px;
  border: 1px solid #e5e7eb;
}

.chart-title {
  font-size: 18px;
  font-weight: 600;
  margin-bottom: 12px;
  color: #374151;
}
            """

        if 'diagram' in visual_elements:
            styles += """

.diagram-container {
  margin: 16px 0;
  text-align: center;
}

.diagram-title {
  font-size: 18px;
  font-weight: 600;
  margin-bottom: 12px;
  color: #374151;
}
            """

        return styles

def main():
    """Command line interface for Slidev PPT Creator."""
    parser = argparse.ArgumentParser(
        description='Create Slidev presentations from natural language descriptions'
    )
    parser.add_argument('input', help='Natural language description of the presentation')
    parser.add_argument('--title', help='Title for the presentation')
    parser.add_argument('--output', help='Output directory', default='.')
    parser.add_argument('--interactive', action='store_true', help='Interactive mode')
    parser.add_argument('--validate-only', action='store_true', help='Only validate existing slides.md')

    args = parser.parse_args()

    if args.validate_only:
        # Validation mode
        slides_path = os.path.join(args.output, 'slides.md')
        if not os.path.exists(slides_path):
            print(f"❌ slides.md not found in {args.output}")
            sys.exit(1)

        validator = SlidesValidator()
        result = validator.validate_file(slides_path)

        print(result['summary'])
        if result['errors']:
            print("\nErrors:")
            for error in result['errors']:
                print(f"  ❌ {error}")
        if result['warnings']:
            print("\nWarnings:")
            for warning in result['warnings']:
                print(f"  ⚠️  {warning}")

        sys.exit(0 if result['valid'] else 1)

    if args.interactive:
        # Interactive mode
        print("🚀 Slidev PPT Creator - Interactive Mode")
        print("=" * 50)

        user_input = args.input
        if not user_input:
            print("Please describe the presentation you want to create:")
            user_input = input("> ")

        title = args.title
        if not title:
            print("\nEnter a title for your presentation (press Enter to use auto-generated title):")
            title_input = input("> ").strip()
            if title_input:
                title = title_input

        output_dir = args.output
        if output_dir == '.':
            print(f"\nEnter output directory (press Enter to use current directory):")
            output_input = input("> ").strip()
            if output_input:
                output_dir = output_input

        print(f"\nCreating presentation...")
        creator = SlidevPPTCreator(output_dir)
        result = creator.create_presentation(user_input, title)

    else:
        # Direct mode
        creator = SlidevPPTCreator(args.output)
        result = creator.create_presentation(args.input, args.title)

        # Print usage instructions
        print(f"\n📖 Usage Instructions:")
        print(f"   cd {result['files_created']['project_dir']}")
        print(f"   npm install")
        print(f"   npm run dev    # Start development server")
        print(f"   npm run build  # Build for production")
        print(f"   npm run export # Export as PDF")

        # Show statistics
        if 'statistics' in result['validation']:
            stats = result['validation']['statistics']
            print(f"\n📊 Presentation Statistics:")
            print(f"   Slides: {stats.get('slide_count', 'N/A')}")
            print(f"   Words: {stats.get('word_count', 'N/A')}")
            print(f"   Avg words per slide: {stats.get('avg_words_per_slide', 'N/A'):.1f}")

if __name__ == "__main__":
    main()