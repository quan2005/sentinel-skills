#!/usr/bin/env python3
"""
Enhanced Chart Generator for Slidev PPT Creator
Generates charts, diagrams, and interactive visual elements for presentations.
Supports Vue components, Mermaid diagrams, and custom visualizations.
"""

import json
import re
from typing import Dict, Any, List, Optional
from pathlib import Path

class ChartGenerator:
    def __init__(self):
        self.chart_types = ['bar', 'pie', 'line', 'area', 'scatter']
        self.diagram_types = ['flowchart', 'architecture', 'timeline', 'process', 'mindmap']
        self.interactive_types = ['quiz', 'poll', 'interactive-demo']

        # Color schemes for different themes
        self.color_schemes = {
            'business': ['#1E40AF', '#3B82F6', '#60A5FA', '#93C5FD', '#DBEAFE'],
            'technical': ['#1F2937', '#374151', '#6B7280', '#9CA3AF', '#D1D5DB'],
            'education': ['#059669', '#10B981', '#34D399', '#6EE7B7', '#A7F3D0'],
            'general': ['#7C3AED', '#8B5CF6', '#A78BFA', '#C4B5FD', '#DDD6FE']
        }

    def generate_chart_code(self, chart_type: str, data: Dict[str, Any], title: str = None, theme: str = 'general') -> str:
        """
        Generate Slidev-compatible chart code using Vue components.

        Args:
            chart_type: Type of chart (bar, pie, line, area, scatter)
            data: Chart data with labels, values, and optional styling
            title: Optional chart title
            theme: Color theme for the chart

        Returns:
            Vue component code in Slidev format
        """
        if chart_type not in self.chart_types:
            chart_type = 'bar'

        chart_templates = {
            'bar': self._generate_bar_chart_component,
            'pie': self._generate_pie_chart_component,
            'line': self._generate_line_chart_component,
            'area': self._generate_area_chart_component,
            'scatter': self._generate_scatter_chart_component
        }

        return chart_templates[chart_type](data, title, theme)

    def generate_diagram_code(self, diagram_type: str, content: str, title: str = None, layout: str = 'vertical') -> str:
        """
        Generate diagram code using Vue components or Mermaid.

        Args:
            diagram_type: Type of diagram (flowchart, architecture, timeline, process, mindmap)
            content: Diagram content/description
            title: Optional diagram title
            layout: Layout direction (vertical, horizontal, grid)

        Returns:
            Diagram component code in Slidev format
        """
        if diagram_type not in self.diagram_types:
            diagram_type = 'flowchart'

        diagram_templates = {
            'flowchart': self._generate_flowchart_component,
            'architecture': self._generate_architecture_diagram,
            'timeline': self._generate_timeline_component,
            'process': self._generate_process_diagram,
            'mindmap': self._generate_mindmap_component
        }

        return diagram_templates[diagram_type](content, title, layout)

    def generate_interactive_code(self, interactive_type: str, content: Dict[str, Any], title: str = None) -> str:
        """
        Generate interactive element code.

        Args:
            interactive_type: Type of interactive element (quiz, poll, interactive-demo)
            content: Content for the interactive element
            title: Optional title

        Returns:
            Interactive component code in Slidev format
        """
        if interactive_type not in self.interactive_types:
            interactive_type = 'quiz'

        interactive_templates = {
            'quiz': self._generate_quiz_component,
            'poll': self._generate_poll_component,
            'interactive-demo': self._generate_demo_component
        }

        return interactive_templates[interactive_type](content, title)

    def _generate_bar_chart_component(self, data: Dict[str, Any], title: str = None, theme: str = 'general') -> str:
        """Generate BarChart Vue component code."""
        colors = self.color_schemes.get(theme, self.color_schemes['general'])

        # Process data
        labels = data.get('labels', [])
        values = data.get('values', [])
        if not labels and not values:
            # Generate sample data if none provided
            labels = ['Q1', 'Q2', 'Q3', 'Q4']
            values = [65, 78, 90, 81]

        # Ensure same length
        min_len = min(len(labels), len(values))
        labels = labels[:min_len]
        values = values[:min_len]

        # Generate data array for component
        data_array = []
        for i, (label, value) in enumerate(zip(labels, values)):
            data_array.append(f'{{ label: "{label}", value: {value}, color: "{colors[i % len(colors)]}" }}')

        data_string = ',\n    '.join(data_array)

        return f'''<BarChart
  title="{title or 'Data Visualization'}"
  subtitle="{data.get('subtitle', '')}"
  :data="[
    {data_string}
  ]"
  :maxValue="{data.get('maxValue', max(values) * 1.1)}"
  :showYAxis="{data.get('showYAxis', True)}"
  :showXAxis="{data.get('showXAxis', True)}"
/>'''

    def _generate_pie_chart_component(self, data: Dict[str, Any], title: str = None, theme: str = 'general') -> str:
        """Generate PieChart Vue component code."""
        colors = self.color_schemes.get(theme, self.color_schemes['general'])

        # Process data
        labels = data.get('labels', [])
        values = data.get('values', [])
        if not labels and not values:
            # Generate sample data if none provided
            labels = ['Category A', 'Category B', 'Category C', 'Category D']
            values = [30, 25, 20, 25]

        # Ensure same length
        min_len = min(len(labels), len(values))
        labels = labels[:min_len]
        values = values[:min_len]

        # Generate data array for component
        data_array = []
        for i, (label, value) in enumerate(zip(labels, values)):
            data_array.append(f'{{ label: "{label}", value: {value}, color: "{colors[i % len(colors)]}" }}')

        data_string = ',\n    '.join(data_array)

        return f'''<PieChart
  title="{title or 'Distribution Chart'}"
  subtitle="{data.get('subtitle', '')}"
  :data="[
    {data_string}
  ]"
  :donut="{data.get('donut', False)}"
  :centerText="{data.get('centerText', '')}"
  :showLegend="{data.get('showLegend', True)}"
/>'''

    def _generate_flowchart_component(self, content: str, title: str = None, layout: str = 'vertical') -> str:
        """Generate FlowChart Vue component code."""
        # Parse content to extract nodes and connections
        nodes = self._parse_flowchart_nodes(content)
        connections = self._parse_flowchart_connections(content)

        # Generate nodes array
        nodes_array = []
        for i, node in enumerate(nodes):
            nodes_array.append(f'''{{
  id: "{node.get('id', f'node-{i}')}",
  title: "{node.get('title', f'Step {i+1}')}",
  subtitle: "{node.get('subtitle', '')}",
  type: "{node.get('type', 'rectangle')}"
}}''')

        # Generate connections array
        connections_array = []
        for conn in connections:
            connections_array.append(f'''{{
  from: "{conn.get('from', '')}",
  to: "{conn.get('to', '')}",
  label: "{conn.get('label', '')}"
}}''')

        nodes_string = ',\n    '.join(nodes_array)
        connections_string = ',\n    '.join(connections_array)

        return f'''<FlowChart
  title="{title or 'Process Flow'}"
  :nodes="[
    {nodes_string}
  ]"
  :connections="[
    {connections_string}
  ]"
  :layout="{{ type: '{layout}', spacing: {{ x: 150, y: 100 }} }}"
  :width="800"
  :height="400"
/>'''

    def _generate_quiz_component(self, content: Dict[str, Any], title: str = None) -> str:
        """Generate Quiz Vue component code."""
        questions = content.get('questions', [])

        if not questions:
            # Generate sample quiz if none provided
            questions = [
                {
                    'text': 'What is the main benefit of this approach?',
                    'options': ['Efficiency', 'Cost', 'Simplicity', 'Scalability'],
                    'correctAnswer': 0,
                    'explanation': 'The main benefit is improved efficiency in processes.'
                }
            ]

        # Generate questions array
        questions_array = []
        for q in questions:
            options_str = "', '".join(q.get('options', []))
            questions_array.append(f'''{{
  text: "{q.get('text', '')}",
  options: ['{options_str}'],
  correctAnswer: {q.get('correctAnswer', 0)},
  explanation: "{q.get('explanation', '')}",
  hint: "{q.get('hint', '')}"
}}''')

        questions_string = ',\n    '.join(questions_array)

        return f'''<Quiz
  title="{title or 'Knowledge Check'}"
  subtitle="{content.get('subtitle', 'Test your understanding')}"
  :questions="[
    {questions_string}
  ]"
  :showProgress="true"
  :allowRetry="true"
/>'''

    def _parse_flowchart_nodes(self, content: str) -> List[Dict[str, Any]]:
        """Parse flowchart nodes from content."""
        # Simple parsing - look for step indicators
        nodes = []
        lines = content.split('\n')

        for line in lines:
            line = line.strip()
            if line.startswith(('->', '→', '1.', '2.', '3.', '4.', '5.')):
                # Extract node title
                title = re.sub(r'^(->|→|\d+\.)\s*', '', line)
                nodes.append({
                    'title': title,
                    'type': 'rectangle' if 'decision' not in title.lower() else 'diamond'
                })

        # If no nodes found, create default nodes
        if not nodes:
            nodes = [
                {'title': 'Start', 'type': 'rectangle'},
                {'title': 'Process', 'type': 'rectangle'},
                {'title': 'Decision', 'type': 'diamond'},
                {'title': 'End', 'type': 'rectangle'}
            ]

        return nodes

    def _parse_flowchart_connections(self, content: str) -> List[Dict[str, Any]]:
        """Parse flowchart connections from content."""
        # For now, create simple sequential connections
        connections = []
        lines = content.split('\n')
        node_count = len([line for line in lines if line.strip().startswith(('->', '→', '1.', '2.', '3.', '4.', '5.'))])

        # Ensure at least some connections
        if node_count == 0:
            node_count = 4

        for i in range(node_count - 1):
            connections.append({
                'from': f'node-{i}',
                'to': f'node-{i + 1}',
                'label': ''
            })

        return connections

    def _generate_line_chart_component(self, data: Dict[str, Any], title: str = None, theme: str = 'general') -> str:
        """Generate line chart (fallback to bar chart for now)."""
        return self._generate_bar_chart_component(data, title, theme)

    def _generate_area_chart_component(self, data: Dict[str, Any], title: str = None, theme: str = 'general') -> str:
        """Generate area chart (fallback to bar chart for now)."""
        return self._generate_bar_chart_component(data, title, theme)

    def _generate_scatter_chart_component(self, data: Dict[str, Any], title: str = None, theme: str = 'general') -> str:
        """Generate scatter chart (fallback to bar chart for now)."""
        return self._generate_bar_chart_component(data, title, theme)

    def _generate_architecture_diagram(self, content: str, title: str = None, layout: str = 'vertical') -> str:
        """Generate architecture diagram (fallback to flowchart)."""
        return self._generate_flowchart_component(content, title, layout)

    def _generate_timeline_component(self, content: str, title: str = None, layout: str = 'vertical') -> str:
        """Generate timeline component (fallback to flowchart)."""
        return self._generate_flowchart_component(content, title, layout)

    def _generate_process_diagram(self, content: str, title: str = None, layout: str = 'vertical') -> str:
        """Generate process diagram (fallback to flowchart)."""
        return self._generate_flowchart_component(content, title, layout)

    def _generate_mindmap_component(self, content: str, title: str = None, layout: str = 'vertical') -> str:
        """Generate mindmap component (fallback to flowchart)."""
        return self._generate_flowchart_component(content, title, layout)

    def _generate_poll_component(self, content: Dict[str, Any], title: str = None) -> str:
        """Generate poll component (fallback to quiz)."""
        return self._generate_quiz_component(content, title)

    def _generate_demo_component(self, content: Dict[str, Any], title: str = None) -> str:
        """Generate demo component (fallback to quiz)."""
        return self._generate_quiz_component(content, title)

    def generate_visual_elements_for_content(self, content: str, content_type: str = 'general') -> List[str]:
        """
        Generate appropriate visual elements based on content analysis.

        Args:
            content: Content to analyze
            content_type: Type of content (business, technical, education, general)

        Returns:
            List of visual element codes
        """
        elements = []
        theme = content_type

        # Analyze content for chart opportunities
        if self._contains_numerical_data(content):
            chart_data = self._extract_numerical_data(content)
            if chart_data:
                elements.append(self.generate_chart_code('bar', chart_data, 'Data Analysis', theme))

        # Analyze content for diagram opportunities
        if self._contains_process_description(content):
            elements.append(self.generate_diagram_code('flowchart', content, 'Process Overview'))

        # Analyze content for interactive opportunities
        if content_type == 'education' and self._contains_quiz_opportunity(content):
            quiz_data = self._generate_quiz_from_content(content)
            elements.append(self.generate_interactive_code('quiz', quiz_data, 'Knowledge Check'))

        return elements

    def _contains_numerical_data(self, content: str) -> bool:
        """Check if content contains numerical data that could be charted."""
        # Look for numbers, percentages, data-related keywords
        data_keywords = ['%', 'percent', 'growth', 'increase', 'decrease', 'data', 'statistics', 'metrics']
        content_lower = content.lower()
        return any(keyword in content_lower for keyword in data_keywords) or bool(re.search(r'\d+', content))

    def _contains_process_description(self, content: str) -> bool:
        """Check if content describes a process or workflow."""
        process_keywords = ['step', 'process', 'workflow', 'flow', 'sequence', 'first', 'then', 'finally', 'next']
        content_lower = content.lower()
        return any(keyword in content_lower for keyword in process_keywords)

    def _contains_quiz_opportunity(self, content: str) -> bool:
        """Check if content is suitable for a quiz."""
        question_keywords = ['what', 'how', 'why', 'when', 'which', 'explain', 'describe', 'define']
        content_lower = content.lower()
        return any(keyword in content_lower for keyword in question_keywords)

    def _extract_numerical_data(self, content: str) -> Optional[Dict[str, Any]]:
        """Extract numerical data from content for charting."""
        # Simple extraction - look for numbers and associated labels
        numbers = re.findall(r'(\d+(?:\.\d+)?)\s*%?', content)
        if len(numbers) >= 2:
            return {
                'labels': [f'Item {i+1}' for i in range(len(numbers))],
                'values': [float(n) for n in numbers[:5]]  # Limit to 5 items
            }
        return None

    def _generate_quiz_from_content(self, content: str) -> Dict[str, Any]:
        """Generate quiz questions based on content."""
        # Simple quiz generation based on content
        return {
            'questions': [
                {
                    'text': 'Based on the content, what is the main concept?',
                    'options': ['Option A', 'Option B', 'Option C', 'Option D'],
                    'correctAnswer': 0,
                    'explanation': 'This is derived from the main concept discussed.'
                }
            ],
            'subtitle': 'Test your understanding of the material'
        }

    def generate_visual_enhancement_suggestions(self, content: str, presentation_type: str) -> List[str]:
        """
        Suggest visual enhancements for the given content.

        Args:
            content: Content to analyze
            presentation_type: Type of presentation

        Returns:
            List of suggestions for visual enhancements
        """
        suggestions = []

        if self._contains_numerical_data(content):
            suggestions.append("Consider adding a bar chart to visualize numerical data")

        if self._contains_process_description(content):
            suggestions.append("Consider adding a flowchart to illustrate the process")

        if presentation_type == 'education':
            suggestions.append("Consider adding interactive quiz elements")

        if presentation_type == 'business':
            suggestions.append("Consider adding pie charts for market share visualization")

        if presentation_type == 'technical':
            suggestions.append("Consider adding architecture diagrams")

        return suggestions

def main():
    """Command line interface for chart generator."""
    import sys
    import argparse

    parser = argparse.ArgumentParser(description='Generate charts and diagrams')
    parser.add_argument('type', choices=['chart', 'diagram', 'interactive'], help='Type of visual element')
    parser.add_argument('subtype', help='Subtype (bar, pie, line, flowchart, quiz, etc.)')
    parser.add_argument('--data', help='Data as JSON string')
    parser.add_argument('--content', help='Content for diagrams/interactive elements')
    parser.add_argument('--title', help='Title for the visual element')
    parser.add_argument('--theme', help='Color theme (business, technical, education, general)', default='general')

    args = parser.parse_args()

    generator = ChartGenerator()

    if args.type == 'chart':
        data = json.loads(args.data) if args.data else {}
        result = generator.generate_chart_code(args.subtype, data, args.title, args.theme)
    elif args.type == 'diagram':
        result = generator.generate_diagram_code(args.subtype, args.content or '', args.title)
    elif args.type == 'interactive':
        content = json.loads(args.data) if args.data else {}
        result = generator.generate_interactive_code(args.subtype, content, args.title)
    else:
        print(f"Unknown type: {args.type}")
        sys.exit(1)

    print(result)

if __name__ == "__main__":
    main()