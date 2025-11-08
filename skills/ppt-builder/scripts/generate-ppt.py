#!/usr/bin/env python3
"""
PPT Builder - Slidev Presentation Generator
This script generates Slidev presentations based on user requirements.
"""

import os
import sys
import json
import argparse
from pathlib import Path
from typing import Dict, List, Any

class PPTBuilder:
    def __init__(self, output_dir: str = "./output"):
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(exist_ok=True)

    def create_presentation(self, config: Dict[str, Any]) -> str:
        """Create a Slidev presentation based on configuration."""

        # Generate frontmatter
        frontmatter = self._generate_frontmatter(config)

        # Generate slides content
        slides = self._generate_slides(config)

        # Combine into complete presentation
        presentation = f"---\n{frontmatter}\n---\n\n{slides}"

        # Save to file
        output_file = self.output_dir / f"{config['title_slug']}.md"
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(presentation)

        return str(output_file)

    def _generate_frontmatter(self, config: Dict[str, Any]) -> str:
        """Generate YAML frontmatter for Slidev."""
        frontmatter_data = {
            'theme': config.get('theme', 'default'),
            'title': config.get('title', 'Presentation'),
            'author': config.get('author', 'Author'),
            'date': config.get('date', '2024'),
            'aspectRatio': config.get('aspect_ratio', '16:9'),
            'canvasWidth': config.get('canvas_width', 1280),
        }

        # Convert to YAML
        yaml_lines = []
        for key, value in frontmatter_data.items():
            yaml_lines.append(f'{key}: "{value}"')

        return '\n'.join(yaml_lines)

    def _generate_slides(self, config: Dict[str, Any]) -> str:
        """Generate slide content based on presentation type."""
        presentation_type = config.get('type', 'business')

        if presentation_type == 'business':
            return self._generate_business_slides(config)
        elif presentation_type == 'technical':
            return self._generate_technical_slides(config)
        elif presentation_type == 'educational':
            return self._generate_educational_slides(config)
        else:
            return self._generate_generic_slides(config)

    def _generate_business_slides(self, config: Dict[str, Any]) -> str:
        """Generate business presentation slides."""
        title = config.get('title', 'Business Presentation')
        content = config.get('content', {})

        slides = []

        # Title slide
        slides.append(f"""# {title}

<div class="text-6xl font-bold text-blue-600 mb-4">
  {content.get('subtitle', 'Business Excellence')}
</div>

<div class="text-2xl text-gray-600">
  {content.get('tagline', 'Professional · Innovative · Results-Driven')}
</div>

<div class="mt-8 text-lg text-gray-500">
  {config.get('author', 'Business Team')} · {config.get('date', '2024')}
</div>
""")

        # Content slides based on outline
        outline = content.get('outline', [])
        for i, section in enumerate(outline, 1):
            slides.append(f"""## {section['title']}

{self._format_content(section.get('content', ''))}
""")

        return '\n\n---\n\n'.join(slides)

    def _generate_technical_slides(self, config: Dict[str, Any]) -> str:
        """Generate technical presentation slides."""
        title = config.get('title', 'Technical Presentation')
        content = config.get('content', {})

        slides = []

        # Title slide
        slides.append(f"""# {title}

<div class="text-center">
  <div class="text-5xl font-bold text-purple-600 mb-4">
    {content.get('subtitle', 'Technical Deep Dive')}
  </div>
  <div class="text-xl text-gray-600 mb-6">
    {content.get('description', 'Advanced technical concepts and implementation')}
  </div>
  <div class="text-lg text-gray-500">
    {config.get('author', 'Technical Team')} · {config.get('date', '2024')}
  </div>
</div>
""")

        # Technical content slides
        topics = content.get('topics', [])
        for topic in topics:
            slides.append(f"""## {topic['title']}

```{topic.get('language', 'javascript')}
{topic.get('code', '// Code example')}
```

{topic.get('explanation', 'Explanation of the code')}
""")

        return '\n\n---\n\n'.join(slides)

    def _generate_educational_slides(self, config: Dict[str, Any]) -> str:
        """Generate educational presentation slides."""
        title = config.get('title', 'Educational Content')
        content = config.get('content', {})

        slides = []

        # Title slide
        slides.append(f"""# {title}

<div class="text-center space-y-4">
  <div class="text-5xl font-bold text-green-600">
    {content.get('subtitle', 'Learning Journey')}
  </div>
  <div class="text-xl text-gray-600">
    {content.get('description', 'Comprehensive educational content')}
  </div>
  <div class="flex justify-center space-x-8 text-lg text-gray-500">
    <div>📚 Theory</div>
    <div>🛠️ Practice</div>
    <div>🎯 Application</div>
  </div>
</div>
""")

        # Learning modules
        modules = content.get('modules', [])
        for module in modules:
            slides.append(f"""## {module['title']}

<div class="grid grid-cols-2 gap-8">
  <div>
    <h3 class="text-xl font-bold text-green-700 mb-3">Key Concepts</h3>
    <ul class="space-y-2">
{self._format_list(module.get('concepts', []))}
    </ul>
  </div>
  <div>
    <h3 class="text-xl font-bold text-blue-700 mb-3">Learning Objectives</h3>
    <ul class="space-y-2">
{self._format_list(module.get('objectives', []))}
    </ul>
  </div>
</div>
""")

        return '\n\n---\n\n'.join(slides)

    def _generate_generic_slides(self, config: Dict[str, Any]) -> str:
        """Generate generic presentation slides."""
        title = config.get('title', 'Presentation')
        content = config.get('content', {})

        slides = []

        # Title slide
        slides.append(f"""# {title}

<div class="text-center">
  <div class="text-6xl font-bold mb-6">
    {content.get('subtitle', 'Professional Presentation')}
  </div>
  <div class="text-xl text-gray-600">
    {content.get('description', 'High-quality content delivery')}
  </div>
</div>
""")

        # Content slides
        sections = content.get('sections', [])
        for section in sections:
            slides.append(f"""## {section['title']}

{self._format_content(section.get('content', ''))}
""")

        return '\n\n---\n\n'.join(slides)

    def _format_content(self, content: str) -> str:
        """Format content for slides."""
        if not content:
            return ""

        # Convert basic formatting to slide-friendly format
        lines = content.split('\n')
        formatted_lines = []

        for line in lines:
            line = line.strip()
            if line:
                # Convert bullet points
                if line.startswith('- ') or line.startswith('* '):
                    formatted_lines.append(f"- {line[2:]}")
                else:
                    formatted_lines.append(line)

        return '\n'.join(formatted_lines)

    def _format_list(self, items: List[str]) -> str:
        """Format list items for slides."""
        if not items:
            return ""

        formatted_items = []
        for item in items:
            formatted_items.append(f"      <li>{item}</li>")

        return '\n'.join(formatted_items)

def main():
    parser = argparse.ArgumentParser(description='Generate Slidev presentations')
    parser.add_argument('--config', required=True, help='JSON configuration file')
    parser.add_argument('--output', default='./output', help='Output directory')

    args = parser.parse_args()

    # Load configuration
    with open(args.config, 'r', encoding='utf-8') as f:
        config = json.load(f)

    # Generate presentation
    builder = PPTBuilder(args.output)
    output_file = builder.create_presentation(config)

    print(f"Presentation generated: {output_file}")

    # Generate package.json if needed
    package_json_path = Path(args.output) / 'package.json'
    if not package_json_path.exists():
        # Create basic package.json for Slidev
        package_content = {
            "name": "generated-presentation",
            "version": "1.0.0",
            "description": "Generated presentation",
            "scripts": {
                "dev": "slidev",
                "build": "slidev build",
                "export": "slidev export"
            },
            "dependencies": {
                "@slidev/cli": "^0.48.0",
                "@slidev/theme-default": "^0.21.0"
            }
        }

        with open(package_json_path, 'w', encoding='utf-8') as f:
            json.dump(package_content, f, indent=2, ensure_ascii=False)
        print(f"Package.json created: {package_json_path}")

if __name__ == "__main__":
    main()