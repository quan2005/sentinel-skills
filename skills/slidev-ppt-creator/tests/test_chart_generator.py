#!/usr/bin/env python3
"""
Test suite for Chart Generator
Tests chart, diagram, and interactive component generation functionality.
"""

import unittest
import json
import sys
import os

# Add the parent directory to sys.path to import the script
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from scripts.chart_generator import ChartGenerator

class TestChartGenerator(unittest.TestCase):
    """Test cases for ChartGenerator class."""

    def setUp(self):
        """Set up test fixtures."""
        self.generator = ChartGenerator()

    def test_initialization(self):
        """Test ChartGenerator initialization."""
        self.assertIn('bar', self.generator.chart_types)
        self.assertIn('pie', self.generator.chart_types)
        self.assertIn('flowchart', self.generator.diagram_types)
        self.assertIn('quiz', self.generator.interactive_types)
        self.assertIn('business', self.generator.color_schemes)

    def test_generate_bar_chart_component(self):
        """Test bar chart component generation."""
        data = {
            'labels': ['Q1', 'Q2', 'Q3', 'Q4'],
            'values': [65, 78, 90, 81],
            'subtitle': 'Quarterly Performance'
        }

        result = self.generator.generate_chart_code('bar', data, 'Sales Data', 'business')

        self.assertIn('<BarChart', result)
        self.assertIn('title="Sales Data"', result)
        self.assertIn('subtitle="Quarterly Performance"', result)
        self.assertIn('Q1', result)
        self.assertIn('65', result)
        self.assertIn('#1E40AF', result)  # Business color

    def test_generate_pie_chart_component(self):
        """Test pie chart component generation."""
        data = {
            'labels': ['Product A', 'Product B', 'Product C'],
            'values': [35, 25, 40]
        }

        result = self.generator.generate_chart_code('pie', data, 'Market Share')

        self.assertIn('<PieChart', result)
        self.assertIn('title="Market Share"', result)
        self.assertIn('Product A', result)
        self.assertIn('35', result)

    def test_generate_chart_with_empty_data(self):
        """Test chart generation with empty data."""
        result = self.generator.generate_chart_code('bar', {}, 'Test Chart')

        self.assertIn('<BarChart', result)
        self.assertIn('Q1', result)  # Should use default data

    def test_generate_flowchart_component(self):
        """Test flowchart component generation."""
        content = "1. Start process\n2. Analyze data\n3. Make decision\n4. Complete"

        result = self.generator.generate_diagram_code('flowchart', content, 'Process Flow')

        self.assertIn('<FlowChart', result)
        self.assertIn('title="Process Flow"', result)
        self.assertIn('Start process', result)

    def test_generate_quiz_component(self):
        """Test quiz component generation."""
        content = {
            'questions': [
                {
                    'text': 'What is 2+2?',
                    'options': ['3', '4', '5', '6'],
                    'correctAnswer': 1,
                    'explanation': '2+2 equals 4'
                }
            ],
            'subtitle': 'Math Quiz'
        }

        result = self.generator.generate_interactive_code('quiz', content, 'Test Quiz')

        self.assertIn('<Quiz', result)
        self.assertIn('title="Test Quiz"', result)
        self.assertIn('What is 2+2?', result)
        self.assertIn('Math Quiz', result)

    def test_generate_quiz_with_empty_content(self):
        """Test quiz generation with empty content."""
        result = self.generator.generate_interactive_code('quiz', {}, 'Test Quiz')

        self.assertIn('<Quiz', result)
        self.assertIn('What is the main benefit', result)  # Default question

    def test_contains_numerical_data(self):
        """Test numerical data detection."""
        self.assertTrue(self.generator._contains_numerical_data("Sales increased by 25%"))
        self.assertTrue(self.generator._contains_numerical_data("We have 1000 users"))
        self.assertTrue(self.generator._contains_numerical_data("Growth: 50, 75, 100"))
        self.assertFalse(self.generator._contains_numerical_data("No numbers here"))

    def test_contains_process_description(self):
        """Test process description detection."""
        self.assertTrue(self.generator._contains_process_description("First step, then second step"))
        self.assertTrue(self.generator._contains_process_description("The workflow includes..."))
        self.assertTrue(self.generator._contains_process_description("Process flow: start -> process -> end"))
        self.assertFalse(self.generator._contains_process_description("Just some text"))

    def test_contains_quiz_opportunity(self):
        """Test quiz opportunity detection."""
        self.assertTrue(self.generator._contains_quiz_opportunity("What is the best approach?"))
        self.assertTrue(self.generator._contains_quiz_opportunity("How does this work?"))
        self.assertTrue(self.generator._contains_quiz_opportunity("Explain the concept"))
        self.assertFalse(self.generator._contains_quiz_opportunity("This is a statement"))

    def test_extract_numerical_data(self):
        """Test numerical data extraction."""
        content = "Sales: Q1 25%, Q2 30%, Q3 35%, Q4 40%"
        result = self.generator._extract_numerical_data(content)

        self.assertIsNotNone(result)
        self.assertIn('labels', result)
        self.assertIn('values', result)
        self.assertEqual(len(result['labels']), 4)
        self.assertEqual(len(result['values']), 4)

    def test_parse_flowchart_nodes(self):
        """Test flowchart node parsing."""
        content = "1. Start\n2. Process Data\n3. Decision Point\n4. End"
        nodes = self.generator._parse_flowchart_nodes(content)

        self.assertEqual(len(nodes), 4)
        self.assertEqual(nodes[0]['title'], 'Start')
        self.assertEqual(nodes[2]['type'], 'diamond')  # Decision point

    def test_parse_flowchart_connections(self):
        """Test flowchart connection parsing."""
        content = "1. Step 1\n2. Step 2\n3. Step 3"
        connections = self.generator._parse_flowchart_connections(content)

        self.assertEqual(len(connections), 2)
        self.assertEqual(connections[0]['from'], 'node-0')
        self.assertEqual(connections[0]['to'], 'node-1')

    def test_color_schemes(self):
        """Test color scheme availability."""
        themes = ['business', 'technical', 'education', 'general']

        for theme in themes:
            self.assertIn(theme, self.generator.color_schemes)
            colors = self.generator.color_schemes[theme]
            self.assertEqual(len(colors), 5)
            self.assertTrue(all(color.startswith('#') for color in colors))

    def test_generate_visual_elements_for_content(self):
        """Test visual element generation based on content."""
        content = "Our sales grew by 25% to 30% over the last quarter"
        elements = self.generator.generate_visual_elements_for_content(content, 'business')

        self.assertIsInstance(elements, list)
        self.assertGreater(len(elements), 0)

    def test_generate_visual_enhancement_suggestions(self):
        """Test visual enhancement suggestions."""
        content = "Our process involves multiple steps and shows 25% growth"
        suggestions = self.generator.generate_visual_enhancement_suggestions(content, 'business')

        self.assertIsInstance(suggestions, list)
        self.assertGreater(len(suggestions), 0)

    def test_invalid_chart_type(self):
        """Test handling of invalid chart types."""
        result = self.generator.generate_chart_code('invalid', {}, 'Test')
        # Should fallback to bar chart
        self.assertIn('<BarChart', result)

    def test_invalid_diagram_type(self):
        """Test handling of invalid diagram types."""
        result = self.generator.generate_diagram_code('invalid', 'Test content', 'Test')
        # Should fallback to flowchart
        self.assertIn('<FlowChart', result)

    def test_invalid_interactive_type(self):
        """Test handling of invalid interactive types."""
        result = self.generator.generate_interactive_code('invalid', {}, 'Test')
        # Should fallback to quiz
        self.assertIn('<Quiz', result)

class TestChartGeneratorIntegration(unittest.TestCase):
    """Integration tests for ChartGenerator."""

    def setUp(self):
        """Set up test fixtures."""
        self.generator = ChartGenerator()

    def test_end_to_end_bar_chart(self):
        """Test complete bar chart generation workflow."""
        # Simulate real-world data
        data = {
            'labels': ['January', 'February', 'March', 'April'],
            'values': [12000, 15000, 18000, 22000],
            'subtitle': 'Monthly Revenue Growth',
            'maxValue': 25000,
            'showYAxis': True,
            'showXAxis': True
        }

        result = self.generator.generate_chart_code('bar', data, 'Revenue Report', 'business')

        # Verify all components are present
        self.assertIn('<BarChart', result)
        self.assertIn('title="Revenue Report"', result)
        self.assertIn('subtitle="Monthly Revenue Growth"', result)
        self.assertIn('January', result)
        self.assertIn('12000', result)
        self.assertIn(':maxValue="25000"', result)
        self.assertIn(':showYAxis="True"', result)

    def test_end_to_end_pie_chart(self):
        """Test complete pie chart generation workflow."""
        data = {
            'labels': ['Desktop', 'Mobile', 'Tablet', 'Other'],
            'values': [45, 35, 15, 5],
            'subtitle': 'Device Usage Distribution',
            'donut': True,
            'showLegend': True
        }

        result = self.generator.generate_chart_code('pie', data, 'Usage Statistics', 'technical')

        # Verify all components are present
        self.assertIn('<PieChart', result)
        self.assertIn('title="Usage Statistics"', result)
        self.assertIn('subtitle="Device Usage Distribution"', result)
        self.assertIn(':donut="True"', result)
        self.assertIn(':showLegend="True"', result)

    def test_end_to_end_flowchart(self):
        """Test complete flowchart generation workflow."""
        content = """
        1. User Registration
        2. Email Verification
        3. Profile Setup
        4. Account Activation
        """

        result = self.generator.generate_diagram_code('flowchart', content, 'User Onboarding', 'vertical')

        # Verify all components are present
        self.assertIn('<FlowChart', result)
        self.assertIn('title="User Onboarding"', result)
        self.assertIn('User Registration', result)
        self.assertIn('type: \'vertical\'', result)
        self.assertIn(':width="800"', result)
        self.assertIn(':height="400"', result)

    def test_end_to_end_quiz(self):
        """Test complete quiz generation workflow."""
        content = {
            'subtitle': 'Test your knowledge of web development',
            'questions': [
                {
                    'text': 'What does HTML stand for?',
                    'options': [
                        'Hyper Text Markup Language',
                        'High Tech Modern Language',
                        'Home Tool Markup Language',
                        'Hyperlinks and Text Markup Language'
                    ],
                    'correctAnswer': 0,
                    'explanation': 'HTML stands for Hyper Text Markup Language and is used to create web pages.',
                    'hint': 'Think about what you use to structure web content'
                },
                {
                    'text': 'Which CSS property is used to change text color?',
                    'options': ['text-color', 'color', 'font-color', 'text-style'],
                    'correctAnswer': 1,
                    'explanation': 'The color property in CSS is used to set the text color.'
                }
            ]
        }

        result = self.generator.generate_interactive_code('quiz', content, 'Web Development Quiz')

        # Verify all components are present
        self.assertIn('<Quiz', result)
        self.assertIn('title="Web Development Quiz"', result)
        self.assertIn('subtitle="Test your knowledge of web development"', result)
        self.assertIn('What does HTML stand for?', result)
        self.assertIn('Hyper Text Markup Language', result)
        self.assertIn(':correctAnswer: 0', result)
        self.assertIn(':showProgress="true"', result)
        self.assertIn(':allowRetry="true"', result)

    def test_content_analysis_workflow(self):
        """Test content analysis and visual element suggestions."""
        # Test content with numerical data
        content_with_data = """
        Our Q1 performance shows 25% growth in user acquisition,
        reaching 10,000 active users. Revenue increased by 30% to $50,000.
        """

        elements = self.generator.generate_visual_elements_for_content(content_with_data, 'business')
        suggestions = self.generator.generate_visual_enhancement_suggestions(content_with_data, 'business')

        # Should detect numerical data and suggest charts
        self.assertGreater(len(elements), 0)
        self.assertGreater(len(suggestions), 0)

        # Test content with process description
        content_with_process = """
        Our workflow follows these steps:
        1. Initial consultation
        2. Requirements analysis
        3. Solution design
        4. Implementation
        5. Testing and validation
        6. Deployment
        """

        elements = self.generator.generate_visual_elements_for_content(content_with_process, 'technical')
        suggestions = self.generator.generate_visual_enhancement_suggestions(content_with_process, 'technical')

        # Should detect process and suggest diagrams
        self.assertGreater(len(elements), 0)
        self.assertGreater(len(suggestions), 0)

    def test_theme_consistency(self):
        """Test color theme consistency across components."""
        data = {'labels': ['A', 'B'], 'values': [10, 20]}

        # Test different themes
        themes = ['business', 'technical', 'education', 'general']

        for theme in themes:
            with self.subTest(theme=theme):
                result = self.generator.generate_chart_code('bar', data, 'Test', theme)

                # Should use theme colors
                colors = self.generator.color_schemes[theme]
                for color in colors[:2]:  # Check first two colors
                    self.assertIn(color, result)

if __name__ == '__main__':
    # Create test suite
    suite = unittest.TestSuite()

    # Add test cases
    suite.addTest(unittest.makeSuite(TestChartGenerator))
    suite.addTest(unittest.makeSuite(TestChartGeneratorIntegration))

    # Run tests
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)

    # Exit with appropriate code
    sys.exit(0 if result.wasSuccessful() else 1)