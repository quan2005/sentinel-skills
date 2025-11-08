#!/usr/bin/env python3
"""
Template Generator for Slidev PPT Creator
Generates appropriate Slidev templates based on content analysis.
"""

import os
import json
from typing import Dict, Any, List
from datetime import datetime

class TemplateGenerator:
    def __init__(self, assets_path: str):
        self.assets_path = assets_path
        self.template_configs = self._load_template_configs()

    def _load_template_configs(self) -> Dict[str, Dict]:
        """Load template configurations."""
        return {
            'business': {
                'theme': 'default',
                'layouts': ['cover', 'default', 'section', 'two-cols', 'image-right'],
                'colors': {
                    'primary': '#1e40af',
                    'secondary': '#64748b',
                    'accent': '#f59e0b'
                },
                'fonts': {
                    'heading': 'Inter',
                    'body': 'Inter'
                }
            },
            'technical': {
                'theme': 'seriph',
                'layouts': ['cover', 'default', 'section', 'two-cols', 'center'],
                'colors': {
                    'primary': '#7c3aed',
                    'secondary': '#059669',
                    'accent': '#dc2626'
                },
                'fonts': {
                    'heading': 'Inter',
                    'body': 'Fira Code',
                    'code': 'Fira Code'
                }
            },
            'education': {
                'theme': 'shades-of-purple',
                'layouts': ['cover', 'default', 'section', 'center', 'two-cols'],
                'colors': {
                    'primary': '#9333ea',
                    'secondary': '#0891b2',
                    'accent': '#ea580c'
                },
                'fonts': {
                    'heading': 'Source Sans Pro',
                    'body': 'Source Sans Pro'
                }
            },
            'general': {
                'theme': 'default',
                'layouts': ['cover', 'default', 'section', 'two-cols'],
                'colors': {
                    'primary': '#059669',
                    'secondary': '#6b7280',
                    'accent': '#f59e0b'
                },
                'fonts': {
                    'heading': 'Inter',
                    'body': 'Inter'
                }
            }
        }

    def generate_slides_markdown(self, analysis: Dict[str, Any], user_title: str = None) -> str:
        """
        Generate complete slides.md file based on analysis.

        Args:
            analysis: Content analysis results
            user_title: Optional user-provided title

        Returns:
            Complete slides.md content
        """
        template_type = analysis['recommended_template']
        config = self.template_configs[template_type]

        # Generate frontmatter
        frontmatter = self._generate_frontmatter(config, user_title, analysis)

        # Generate slides
        slides = self._generate_slides(analysis, config, user_title)

        return f"{frontmatter}\n\n{slides}"

    def _generate_frontmatter(self, config: Dict, user_title: str, analysis: Dict) -> str:
        """Generate YAML frontmatter for slides.md."""
        title = user_title or "Presentation"

        frontmatter = f"""---
title: "{title}"
author: "Presenter"
date: "{datetime.now().strftime('%Y-%m-%d')}"
theme: {config['theme']}
"""

        # Add color customizations
        if 'colors' in config:
            frontmatter += "\ncolorSchema: 'auto'\n"

        # Add layout information
        if 'layouts' in config:
            frontmatter += f"\nlayouts: {config['layouts']}\n"

        frontmatter += "\n---"

        return frontmatter

    def _generate_slides(self, analysis: Dict[str, Any], config: Dict, user_title: str = None) -> str:
        """Generate slide content based on structure."""
        slides = []
        structure = analysis['structure']

        # Title slide
        slides.append(self._generate_title_slide(analysis, config, user_title))

        # Table of contents (if many sections)
        if len(structure) > 3:
            slides.append(self._generate_toc_slide(structure))

        # Content slides
        for section in structure:
            section_slides = self._generate_section_slides(section, analysis, config)
            slides.extend(section_slides)

        # Closing slide
        slides.append(self._generate_closing_slide(config))

        return '\n\n---\n\n'.join(slides)

    def _generate_title_slide(self, analysis: Dict, config: Dict, user_title: str = None) -> str:
        """Generate title slide."""
        # Use provided title or generate from keywords
        if user_title:
            title = user_title
        else:
            title = analysis.get('keywords', ['Presentation'])[0].title()

        subtitle = self._generate_subtitle(analysis)

        slide_content = f"# {title}\n"

        if subtitle:
            slide_content += f"## {subtitle}\n"

        slide_content += f"\n### Presenter\n{datetime.now().strftime('%Y-%m-%d')}"

        return slide_content

    def _generate_subtitle(self, analysis: Dict) -> str:
        """Generate subtitle based on analysis."""
        type_map = {
            'business': 'Business Presentation',
            'technical': 'Technical Sharing',
            'education': 'Educational Content',
            'general': 'General Presentation'
        }

        return type_map.get(analysis['presentation_type'], 'Presentation')

    def _generate_toc_slide(self, structure: List[Dict]) -> str:
        """Generate table of contents slide."""
        content = "# 目录\n\n## Contents\n\n"

        for section in structure:
            if section['type'] != 'main':
                content += f"- {section['content']}\n"

        return content

    def _generate_section_slides(self, section: Dict, analysis: Dict, config: Dict) -> List[str]:
        """Generate slides for a section."""
        slides = []

        # Section title slide (for major sections)
        if section['type'] in ['introduction', 'conclusion']:
            slides.append(self._generate_section_title_slide(section))

        # Content slides
        content_slides = self._generate_content_slides(section, analysis, config)
        slides.extend(content_slides)

        return slides

    def _generate_section_title_slide(self, section: Dict) -> str:
        """Generate section title slide."""
        titles = {
            'introduction': '背景介绍',
            'problem': '问题与挑战',
            'solution': '解决方案',
            'features': '核心特性',
            'demo': '演示案例',
            'conclusion': '总结展望'
        }

        title = titles.get(section['type'], section['content'])
        return f"# {title}"

    def _generate_content_slides(self, section: Dict, analysis: Dict, config: Dict) -> List[str]:
        """Generate content slides for a section."""
        visual_elements = analysis.get('visual_elements', [])
        slides = []

        if section['estimated_slides'] == 1:
            # Single slide for this section
            slides.append(self._generate_single_content_slide(section, visual_elements, config))
        else:
            # Multiple slides
            if section['type'] == 'features':
                slides.append(self._generate_features_slide(section))
            elif section['type'] == 'demo' and 'code' in visual_elements:
                slides.append(self._generate_code_demo_slide(section))
            else:
                # Generate multiple general content slides
                for i in range(section['estimated_slides']):
                    slides.append(self._generate_general_content_slide(section, i))

        return slides

    def _generate_single_content_slide(self, section: Dict, visual_elements: List[str], config: Dict) -> str:
        """Generate a single content slide."""
        content = f"# {section['content']}\n\n"

        if 'chart' in visual_elements:
            content += self._generate_chart_placeholder()
        elif 'diagram' in visual_elements:
            content += self._generate_diagram_placeholder()
        elif 'code' in visual_elements:
            content += self._generate_code_placeholder()
        else:
            content += self._generate_bullet_points(section['type'])

        return content

    def _generate_features_slide(self, section: Dict) -> str:
        """Generate features slide."""
        content = f"# {section['content']}\n\n"

        features = [
            "核心功能模块",
            "技术优势",
            "应用场景",
            "创新亮点"
        ]

        for feature in features:
            content += f"- **{feature}**: 详细说明\n"

        return content

    def _generate_code_demo_slide(self, section: Dict) -> str:
        """Generate code demonstration slide."""
        language = 'javascript'  # Default language
        code_example = self._get_code_example(language)

        content = f"# {section['content']}\n\n"
        content += f"## 代码演示\n\n"
        content += f"```{language}\n{code_example}\n```"

        return content

    def _generate_general_content_slide(self, section: Dict, slide_index: int) -> str:
        """Generate general content slide."""
        titles = {
            0: section['content'],
            1: f"{section['content']} - 详细说明",
            2: f"{section['content']} - 实践应用"
        }

        title = titles.get(slide_index, section['content'])
        content = f"# {title}\n\n"

        # Add appropriate content based on section type
        if section['type'] == 'problem':
            content += "- 核心挑战分析\n- 影响因素探讨\n- 解决需求识别\n"
        elif section['type'] == 'solution':
            content += "- 解决方案概述\n- 实施路径规划\n- 预期效果评估\n"
        else:
            content += "- 要点一\n- 要点二\n- 要点三\n- 要点四\n"

        return content

    def _generate_closing_slide(self, config: Dict) -> str:
        """Generate closing slide."""
        return """# 谢谢！

## 欢迎提问与交流

---

<div class="abs-br m-6 flex gap-2">
  <a href="https://github.com/slidevjs/slidev" target="_blank" alt="GitHub"
    class="text-xl slidev-icon-btn opacity-50 !border-none !hover:text-white">
    <carbon-logo-github />
  </a>
  <a href="https://sli.dev" target="_blank" alt="Slidev"
    class="text-xl slidev-icon-btn opacity-50 !border-none !hover:text-white">
    <carbon-logos-slidev />
  </a>
</div>"""

    def _generate_chart_placeholder(self) -> str:
        """Generate chart placeholder."""
        return """## 数据分析

<div class="grid grid-cols-2 gap-4">
<div>

### 关键指标
- 指标一: 85%
- 指标二: 92%
- 指标三: 78%

</div>
<div>

```mermaid
graph TD
    A[开始] --> B[分析]
    B --> C[评估]
    C --> D[结论]
```

</div>
</div>"""

    def _generate_diagram_placeholder(self) -> str:
        """Generate diagram placeholder."""
        return """## 架构设计

```mermaid
graph TB
    subgraph "前端层"
        A[Web应用]
        B[移动应用]
    end

    subgraph "服务层"
        C[API网关]
        D[业务服务]
    end

    subgraph "数据层"
        E[(数据库)]
        F[(缓存)]
    end

    A --> C
    B --> C
    C --> D
    D --> E
    D --> F
```"""

    def _generate_code_placeholder(self) -> str:
        """Generate code placeholder."""
        return """## 代码示例

```javascript
// 示例代码
function createPresentation(topic) {
  const slides = generateSlides(topic);
  const template = selectTemplate(topic);

  return {
    slides,
    template,
    theme: customizeTheme(template)
  };
}

// 使用示例
const presentation = createPresentation('AI in Healthcare');
console.log('Generated presentation:', presentation);
```"""

    def _generate_bullet_points(self, section_type: str) -> str:
        """Generate bullet points based on section type."""
        point_map = {
            'introduction': "- 背景介绍\n- 问题定义\n- 目标设定\n- 意义说明",
            'problem': "- 现状分析\n- 痛点识别\n- 挑战评估\n- 影响分析",
            'solution': "- 解决方案\n- 实施策略\n- 技术路径\n- 预期效果",
            'conclusion': "- 核心总结\n- 主要收获\n- 未来展望\n- 行动建议"
        }

        return point_map.get(section_type, "- 要点一\n- 要点二\n- 要点三\n- 要点四")

    def _get_code_example(self, language: str) -> str:
        """Get code example for specified language."""
        examples = {
            'javascript': '// JavaScript示例\nfunction example() {\n  console.log("Hello Slidev!");\n  return "Success";\n}',
            'python': '# Python示例\ndef example():\n    print("Hello Slidev!")\n    return "Success"',
            'typescript': '// TypeScript示例\nfunction example(): string {\n  console.log("Hello Slidev!");\n  return "Success";\n}'
        }

        return examples.get(language, examples['javascript'])

    def generate_package_json(self, title: str, template_type: str) -> str:
        """Generate package.json file."""
        config = self.template_configs[template_type]

        package_data = {
            "name": title.lower().replace(' ', '-'),
            "version": "0.1.0",
            "description": f"Presentation generated by Slidev PPT Creator",
            "scripts": {
                "dev": "slidev",
                "build": "slidev build",
                "export": "slidev export"
            },
            "dependencies": {
                "@slidev/cli": "latest",
                "@slidev/theme-default": "latest",
                "@slidev/theme-seriph": "latest"
            },
            "devDependencies": {
                "@iconify-json/carbon": "^0.1.0",
                "playwright-chromium": "^1.0.0"
            }
        }

        return json.dumps(package_data, indent=2, ensure_ascii=False)

    def generate_readme(self, title: str, template_type: str) -> str:
        """Generate README.md file."""
        config = self.template_configs[template_type]

        readme_content = f"""# {title}

Generated with Slidev PPT Creator using {template_type} template.

## Getting Started

### Install Dependencies
```bash
npm install
```

### Start Development Server
```bash
npm run dev
```

### Build for Production
```bash
npm run build
```

### Export as PDF
```bash
npm run export
```

## Template Information

- **Theme**: {config['theme']}
- **Primary Color**: {config['colors']['primary']}
- **Secondary Color**: {config['colors']['secondary']}

## Learn More

- [Slidev Documentation](https://sli.dev/)
- [Slidev Themes](https://sli.dev/themes/)
"""

        return readme_content

def main():
    """Command line interface for template generator."""
    import sys
    import argparse

    parser = argparse.ArgumentParser(description='Generate Slidev templates')
    parser.add_argument('analysis_file', help='JSON file with content analysis')
    parser.add_argument('--title', help='Presentation title')
    parser.add_argument('--output', help='Output directory', default='.')

    args = parser.parse_args()

    # Load analysis
    with open(args.analysis_file, 'r', encoding='utf-8') as f:
        analysis = json.load(f)

    # Generate template
    generator = TemplateGenerator(args.output)
    slides_content = generator.generate_slides_markdown(analysis, args.title)

    # Write slides.md
    with open(os.path.join(args.output, 'slides.md'), 'w', encoding='utf-8') as f:
        f.write(slides_content)

    # Generate package.json
    package_content = generator.generate_package_json(
        args.title or "Presentation",
        analysis['recommended_template']
    )
    with open(os.path.join(args.output, 'package.json'), 'w', encoding='utf-8') as f:
        f.write(package_content)

    print(f"Generated Slidev presentation in {args.output}")

if __name__ == "__main__":
    main()