#!/usr/bin/env python3
"""
Chart Generator for Slidev PPT Creator
Generates charts and visual elements for presentations.
"""

import json
from typing import Dict, Any, List

class ChartGenerator:
    def __init__(self):
        self.chart_types = ['bar', 'pie', 'line', 'area']
        self.diagram_types = ['flowchart', 'architecture', 'timeline', 'process']

    def generate_chart_code(self, chart_type: str, data: Dict[str, Any], title: str = None) -> str:
        """
        Generate Slidev-compatible chart code.

        Args:
            chart_type: Type of chart (bar, pie, line, area)
            data: Chart data
            title: Optional chart title

        Returns:
            Chart component code in Slidev format
        """
        if chart_type not in self.chart_types:
            chart_type = 'bar'

        chart_templates = {
            'bar': self._generate_bar_chart,
            'pie': self._generate_pie_chart,
            'line': self._generate_line_chart,
            'area': self._generate_area_chart
        }

        return chart_templates[chart_type](data, title)

    def generate_diagram_code(self, diagram_type: str, content: str, title: str = None) -> str:
        """
        Generate Mermaid diagram code.

        Args:
            diagram_type: Type of diagram (flowchart, architecture, timeline, process)
            content: Diagram content/description
            title: Optional diagram title

        Returns:
            Mermaid diagram code in Slidev format
        """
        if diagram_type not in self.diagram_types:
            diagram_type = 'flowchart'

        diagram_templates = {
            'flowchart': self._generate_flowchart,
            'architecture': self._generate_architecture_diagram,
            'timeline': self._generate_timeline,
            'process': self._generate_process_diagram
        }

        return diagram_templates[diagram_type](content, title)

    def _generate_bar_chart(self, data: Dict[str, Any], title: str = None) -> str:
        """Generate bar chart using HTML/CSS."""
        chart_title = f"## {title}\n\n" if title else ""

        if 'labels' not in data or 'values' not in data:
            # Generate sample data
            data = {
                'labels': ['Q1', 'Q2', 'Q3', 'Q4'],
                'values': [65, 78, 90, 85]
            }

        chart_content = f"""{chart_title}<div class="grid grid-cols-4 gap-2 mt-4">
"""

        for i, (label, value) in enumerate(zip(data['labels'], data['values'])):
            height_percent = max(10, (value / max(data['values'])) * 100)
            chart_content += f"""<div class="text-center">
  <div class="bg-blue-500 rounded-t" style="height: {height_percent}px; margin-bottom: 8px;"></div>
  <div class="text-xs">{label}</div>
  <div class="text-sm font-bold">{value}</div>
</div>
"""

        chart_content += "</div>"

        return chart_content

    def _generate_pie_chart(self, data: Dict[str, Any], title: str = None) -> str:
        """Generate pie chart using Mermaid."""
        chart_title = f"## {title}\n\n" if title else ""

        if 'labels' not in data or 'values' not in data:
            # Generate sample data
            data = {
                'labels': ['Product A', 'Product B', 'Product C', 'Others'],
                'values': [35, 25, 20, 20]
            }

        pie_data = []
        for label, value in zip(data['labels'], data['values']):
            pie_data.append(f'"{label}" : {value}')

        mermaid_code = f"""{chart_title}```mermaid
pie title {title or 'Distribution'}
{chr(10).join(pie_data)}
```"""

        return mermaid_code

    def _generate_line_chart(self, data: Dict[str, Any], title: str = None) -> str:
        """Generate line chart using Mermaid."""
        chart_title = f"## {title}\n\n" if title else ""

        if 'labels' not in data or 'datasets' not in data:
            # Generate sample data
            data = {
                'labels': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun'],
                'datasets': [
                    {'label': 'Series 1', 'values': [10, 25, 30, 45, 40, 55]},
                    {'label': 'Series 2', 'values': [15, 20, 35, 30, 45, 50]}
                ]
            }

            mermaid_code = f"""{chart_title}```mermaid
graph LR
"""

            for i, label in enumerate(data['labels']):
                mermaid_code += f'    {label[0]}{i}["{label}"]\n'

            # Add connections
            for i in range(len(data['labels']) - 1):
                current = f"{data['labels'][i][0]}{i}"
                next_label = f"{data['labels'][i+1][0]}{i+1}"
                mermaid_code += f'    {current} --> {next_label}\n'

            mermaid_code += "```"

        return mermaid_code

    def _generate_area_chart(self, data: Dict[str, Any], title: str = None) -> str:
        """Generate area chart using Mermaid."""
        return self._generate_line_chart(data, title)  # Simplified as line chart

    def _generate_flowchart(self, content: str, title: str = None) -> str:
        """Generate flowchart diagram."""
        diagram_title = f"## {title}\n\n" if title else ""

        # Default flowchart structure
        mermaid_code = f"""{diagram_title}```mermaid
graph TD
    A[开始] --> B{分析}
    B --> C{处理}
    C --> D{验证}
    D --> E{完成}
```"""

        # Try to parse content for custom flow
        if '流程' in content or 'flow' in content.lower():
            # Generate a more specific flowchart
            mermaid_code = f"""{diagram_title}```mermaid
graph TD
    A[需求分析] --> B[方案设计]
    B --> C[开发实施]
    C --> D[测试验证]
    D --> E[部署上线]
    E --> F[运维监控]
```"""

        return mermaid_code

    def _generate_architecture_diagram(self, content: str, title: str = None) -> str:
        """Generate architecture diagram."""
        diagram_title = f"## {title}\n\n" if title else ""

        mermaid_code = f"""{diagram_title}```mermaid
graph TB
    subgraph "前端层"
        A[Web应用]
        B[移动应用]
    end

    subgraph "服务层"
        C[API网关]
        D[业务服务]
        E[认证服务]
    end

    subgraph "数据层"
        F[(主数据库)]
        G[(缓存)]
        H[(消息队列)]
    end

    A --> C
    B --> C
    C --> D
    C --> E
    D --> F
    D --> G
    D --> H
```"""

        return mermaid_code

    def _generate_timeline(self, content: str, title: str = None) -> str:
        """Generate timeline diagram."""
        diagram_title = f"## {title}\n\n" if title else ""

        mermaid_code = f"""{diagram_title}```mermaid
graph LR
    A[2024 Q1<br>项目启动] --> B[2024 Q2<br>开发阶段]
    B --> C[2024 Q3<br>测试验证]
    C --> D[2024 Q4<br>正式发布]
```"""

        return mermaid_code

    def _generate_process_diagram(self, content: str, title: str = None) -> str:
        """Generate process diagram."""
        diagram_title = f"## {title}\n\n" if title else ""

        mermaid_code = f"""{diagram_title}```mermaid
graph LR
    A[输入] --> B[处理]
    B --> C{验证}
    C -->|通过| D[输出]
    C -->|失败| E[重新处理]
    E --> B
```"""

        return mermaid_code

    def generate_chart_from_data(self, data_description: str) -> str:
        """
        Generate appropriate chart based on data description.

        Args:
            data_description: Natural language description of data

        Returns:
            Generated chart code
        """
        description_lower = data_description.lower()

        # Determine chart type based on description
        if 'percentage' in description_lower or '占比' in description_lower or '分布' in data_description:
            return self.generate_chart_code('pie', {
                'labels': ['类别A', '类别B', '类别C', '其他'],
                'values': [35, 30, 25, 10]
            }, '数据分布')
        elif 'trend' in description_lower or '趋势' in data_description or 'growth' in description_lower:
            return self.generate_chart_code('line', {
                'labels': ['1月', '2月', '3月', '4月', '5月', '6月'],
                'datasets': [
                    {'label': '增长趋势', 'values': [20, 35, 45, 60, 75, 90]}
                ]
            }, '增长趋势')
        elif 'comparison' in description_lower or '对比' in data_description:
            return self.generate_chart_code('bar', {
                'labels': ['方案A', '方案B', '方案C'],
                'values': [75, 85, 65]
            }, '方案对比')
        else:
            # Default bar chart
            return self.generate_chart_code('bar', {
                'labels': ['指标1', '指标2', '指标3', '指标4'],
                'values': [80, 65, 90, 75]
            }, '数据统计')

    def generate_visual_elements_for_section(self, section_type: str, content: str) -> List[str]:
        """
        Generate appropriate visual elements for a section.

        Args:
            section_type: Type of section (introduction, problem, solution, etc.)
            content: Section content

        Returns:
            List of visual element codes
        """
        elements = []

        if section_type == 'problem':
            elements.append(self.generate_diagram_code('flowchart', content, '问题分析'))

        elif section_type == 'solution':
            elements.append(self.generate_diagram_code('architecture', content, '解决方案架构'))

        elif section_type == 'features':
            elements.append(self.generate_chart_from_data('功能特性对比'))

        elif section_type == 'demo':
            # Code demonstrations are handled elsewhere
            pass

        elif section_type == 'conclusion':
            elements.append(self.generate_chart_from_data('总结指标'))

        # Add data visualization if content suggests it
        content_lower = content.lower()
        if any(keyword in content_lower for keyword in ['data', '数据', 'statistics', '统计', 'numbers', '数字']):
            elements.append(self.generate_chart_from_data(content))

        return elements

def main():
    """Command line interface for chart generator."""
    import sys
    import argparse

    parser = argparse.ArgumentParser(description='Generate charts and diagrams')
    parser.add_argument('type', choices=['chart', 'diagram'], help='Type of visual element')
    parser.add_argument('subtype', help='Subtype (bar, pie, line, flowchart, etc.)')
    parser.add_argument('--data', help='Data as JSON string')
    parser.add_argument('--content', help='Content for diagrams')
    parser.add_argument('--title', help='Title for the visual element')

    args = parser.parse_args()

    generator = ChartGenerator()

    if args.type == 'chart':
        data = json.loads(args.data) if args.data else {}
        result = generator.generate_chart_code(args.subtype, data, args.title)
    else:
        result = generator.generate_diagram_code(args.subtype, args.content or '', args.title)

    print(result)

if __name__ == "__main__":
    main()