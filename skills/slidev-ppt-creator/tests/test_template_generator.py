#!/usr/bin/env python3
"""
Test suite for Template Generator
Tests template generation and customization functionality.
"""

import unittest
import sys
import os
import tempfile
import shutil

# Add the parent directory to sys.path to import the script
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from scripts.template_generator import TemplateGenerator

class TestTemplateGenerator(unittest.TestCase):
    """Test cases for TemplateGenerator class."""

    def setUp(self):
        """Set up test fixtures."""
        self.generator = TemplateGenerator()
        self.temp_dir = tempfile.mkdtemp()

    def tearDown(self):
        """Clean up test fixtures."""
        if os.path.exists(self.temp_dir):
            shutil.rmtree(self.temp_dir)

    def test_initialization(self):
        """Test TemplateGenerator initialization."""
        self.assertIsNotNone(self.generator.template_types)
        self.assertIn('business', self.generator.template_types)
        self.assertIn('technical', self.generator.template_types)
        self.assertIn('education', self.generator.template_types)
        self.assertIn('general', self.generator.template_types)

    def test_load_business_template(self):
        """Test loading business template."""
        template_path = os.path.join(
            os.path.dirname(__file__), '..', 'assets', 'templates', 'business', 'business-template.md'
        )

        if os.path.exists(template_path):
            content = self.generator.load_template('business')
            self.assertIsNotNone(content)
            self.assertIn('business', content.lower())
            self.assertIn('market', content.lower())
        else:
            # Skip test if template doesn't exist
            self.skipTest("Business template not found")

    def test_load_technical_template(self):
        """Test loading technical template."""
        template_path = os.path.join(
            os.path.dirname(__file__), '..', 'assets', 'templates', 'technical', 'technical-template.md'
        )

        if os.path.exists(template_path):
            content = self.generator.load_template('technical')
            self.assertIsNotNone(content)
            self.assertIn('technical', content.lower())
            self.assertIn('code', content.lower())
        else:
            # Skip test if template doesn't exist
            self.skipTest("Technical template not found")

    def test_load_education_template(self):
        """Test loading education template."""
        template_path = os.path.join(
            os.path.dirname(__file__), '..', 'assets', 'templates', 'education', 'education-template.md'
        )

        if os.path.exists(template_path):
            content = self.generator.load_template('education')
            self.assertIsNotNone(content)
            self.assertIn('education', content.lower())
            self.assertIn('learning', content.lower())
        else:
            # Skip test if template doesn't exist
            self.skipTest("Education template not found")

    def test_load_general_template(self):
        """Test loading general template."""
        template_path = os.path.join(
            os.path.dirname(__file__), '..', 'assets', 'templates', 'general', 'general-template.md'
        )

        if os.path.exists(template_path):
            content = self.generator.load_template('general')
            self.assertIsNotNone(content)
            self.assertIn('general', content.lower())
        else:
            # Skip test if template doesn't exist
            self.skipTest("General template not found")

    def test_load_invalid_template(self):
        """Test loading invalid template type."""
        content = self.generator.load_template('invalid')
        self.assertIsNone(content)

    def test_customize_template(self):
        """Test template customization."""
        template_content = """
---
title: Test Presentation
author: Test Author
---
# Test Title

## Content

This is test content with {{variable}} placeholder.
"""

        customizations = {
            'title': 'Custom Presentation',
            'author': 'Custom Author',
            'variable': 'custom value'
        }

        result = self.generator.customize_template(template_content, customizations)

        self.assertIn('Custom Presentation', result)
        self.assertIn('Custom Author', result)
        self.assertIn('custom value', result)
        self.assertNotIn('{{variable}}', result)

    def test_generate_presentation_metadata(self):
        """Test presentation metadata generation."""
        metadata = {
            'title': 'Test Presentation',
            'author': 'Test Author',
            'description': 'Test Description'
        }

        result = self.generator.generate_presentation_metadata(metadata)

        self.assertIn('title: Test Presentation', result)
        self.assertIn('author: Test Author', result)
        self.assertIn('description: Test Description', result)

    def test_select_template_based_on_content(self):
        """Test template selection based on content."""
        # Test business content
        business_content = "Our business strategy focuses on market growth and revenue optimization"
        template = self.generator.select_template_based_on_content(business_content)
        self.assertEqual(template, 'business')

        # Test technical content
        technical_content = "The system architecture uses microservices and API gateway patterns"
        template = self.generator.select_template_based_on_content(technical_content)
        self.assertEqual(template, 'technical')

        # Test educational content
        education_content = "This course teaches students about programming concepts and best practices"
        template = self.generator.select_template_based_on_content(education_content)
        self.assertEqual(template, 'education')

        # Test general content
        general_content = "This is a general presentation about various topics"
        template = self.generator.select_template_based_on_content(general_content)
        self.assertEqual(template, 'general')

    def test_create_presentation_structure(self):
        """Test presentation structure creation."""
        content = {
            'title': 'Test Presentation',
            'sections': [
                {'title': 'Introduction', 'content': 'Intro content'},
                {'title': 'Main Points', 'content': 'Main content'},
                {'title': 'Conclusion', 'content': 'Conclusion content'}
            ]
        }

        structure = self.generator.create_presentation_structure(content)

        self.assertIn('title', structure)
        self.assertIn('sections', structure)
        self.assertEqual(len(structure['sections']), 3)
        self.assertEqual(structure['sections'][0]['title'], 'Introduction')

    def test_validate_template_content(self):
        """Test template content validation."""
        # Valid template content
        valid_content = """
---
title: Test
---
# Slide 1

## Content

Slide content here.
"""

        result = self.generator.validate_template_content(valid_content)
        self.assertTrue(result['valid'])
        self.assertEqual(len(result['errors']), 0)

        # Invalid template content
        invalid_content = "Just some text without proper frontmatter"

        result = self.generator.validate_template_content(invalid_content)
        self.assertFalse(result['valid'])
        self.assertGreater(len(result['errors']), 0)

class TestTemplateGeneratorIntegration(unittest.TestCase):
    """Integration tests for TemplateGenerator."""

    def setUp(self):
        """Set up test fixtures."""
        self.generator = TemplateGenerator()
        self.temp_dir = tempfile.mkdtemp()

    def tearDown(self):
        """Clean up test fixtures."""
        if os.path.exists(self.temp_dir):
            shutil.rmtree(self.temp_dir)

    def test_end_to_end_business_presentation(self):
        """Test complete business presentation generation."""
        content = {
            'title': 'Q4 Business Review',
            'author': 'Business Team',
            'description': 'Quarterly business performance review',
            'content': '''
            Our business achieved remarkable growth in Q4 with 25% revenue increase.
            Market expansion strategy resulted in 3 new territories.
            Customer satisfaction improved to 92%.
            ''',
            'sections': [
                {'title': 'Executive Summary', 'content': 'Key business metrics and achievements'},
                {'title': 'Financial Performance', 'content': 'Revenue, profit, and growth metrics'},
                {'title': 'Market Analysis', 'content': 'Market trends and competitive landscape'},
                {'title': 'Future Outlook', 'content': 'Strategic initiatives and growth plans'}
            ]
        }

        # Select template
        template_type = self.generator.select_template_based_on_content(content['content'])
        self.assertEqual(template_type, 'business')

        # Load template
        template_content = self.generator.load_template(template_type)
        if template_content:
            # Customize template
            customizations = {
                'title': content['title'],
                'author': content['author'],
                'description': content['description']
            }

            customized_content = self.generator.customize_template(template_content, customizations)

            # Validate result
            validation = self.generator.validate_template_content(customized_content)
            self.assertTrue(validation['valid'])

            # Verify customization worked
            self.assertIn(content['title'], customized_content)
            self.assertIn(content['author'], customized_content)

    def test_end_to_end_technical_presentation(self):
        """Test complete technical presentation generation."""
        content = {
            'title': 'Microservices Architecture',
            'author': 'Engineering Team',
            'description': 'Technical deep-dive into microservices implementation',
            'content': '''
            Our system uses microservices architecture with API gateway pattern.
            Each service is independently deployable and scalable.
            We use Docker containers and Kubernetes orchestration.
            ''',
            'sections': [
                {'title': 'Architecture Overview', 'content': 'System design and components'},
                {'title': 'Implementation Details', 'content': 'Technical implementation specifics'},
                {'title': 'Performance Optimization', 'content': 'Optimization techniques and results'},
                {'title': 'Monitoring & Observability', 'content': 'Logging, metrics, and alerting'}
            ]
        }

        # Select template
        template_type = self.generator.select_template_based_on_content(content['content'])
        self.assertEqual(template_type, 'technical')

        # Create presentation structure
        structure = self.generator.create_presentation_structure(content)

        self.assertEqual(structure['title'], content['title'])
        self.assertEqual(len(structure['sections']), 4)

    def test_end_to_end_education_presentation(self):
        """Test complete education presentation generation."""
        content = {
            'title': 'Introduction to React Hooks',
            'author': 'Education Team',
            'description': 'Comprehensive guide to React Hooks for beginners',
            'content': '''
            React Hooks revolutionized how we write React components.
            They allow functional components to have state and lifecycle features.
            Students will learn useState, useEffect, and custom hooks.
            ''',
            'sections': [
                {'title': 'Learning Objectives', 'content': 'What students will learn'},
                {'title': 'Introduction to Hooks', 'content': 'Basic concepts and motivation'},
                {'title': 'Core Hooks', 'content': 'useState and useEffect详解'},
                {'title': 'Practice Exercises', 'content': 'Hands-on coding exercises'},
                {'title': 'Assessment', 'content': 'Knowledge check and quiz'}
            ]
        }

        # Select template
        template_type = self.generator.select_template_based_on_content(content['content'])
        self.assertEqual(template_type, 'education')

        # Create presentation structure
        structure = self.generator.create_presentation_structure(content)

        self.assertEqual(structure['title'], content['title'])
        self.assertEqual(len(structure['sections']), 5)

    def test_template_customization_workflow(self):
        """Test complete template customization workflow."""
        # Base template
        base_template = """
---
title: {{title}}
author: {{author}}
date: {{date}}
theme: {{theme}}
---

# {{title}}

## Overview

{{overview}}

## Key Points

{{key_points}}

## Conclusion

{{conclusion}}
"""

        # Customization data
        customizations = {
            'title': 'Custom Presentation Title',
            'author': 'Custom Author Name',
            'date': '2024-01-15',
            'theme': 'seriph',
            'overview': 'This is a custom overview with specific details about the presentation content.',
            'key_points': '• First key point\n• Second key point\n• Third key point',
            'conclusion': 'Custom conclusion summarizing the main takeaways.'
        }

        # Apply customizations
        result = self.generator.customize_template(base_template, customizations)

        # Verify all placeholders were replaced
        self.assertNotIn('{{title}}', result)
        self.assertNotIn('{{author}}', result)
        self.assertNotIn('{{date}}', result)
        self.assertNotIn('{{theme}}', result)

        # Verify custom values were inserted
        self.assertIn('Custom Presentation Title', result)
        self.assertIn('Custom Author Name', result)
        self.assertIn('2024-01-15', result)
        self.assertIn('seriph', result)

    def test_content_analysis_and_template_selection(self):
        """Test content analysis for automatic template selection."""
        test_cases = [
            {
                'content': 'Our business strategy focuses on market penetration and revenue growth through strategic partnerships.',
                'expected_template': 'business'
            },
            {
                'content': 'The system architecture implements microservices with RESTful APIs and container orchestration.',
                'expected_template': 'technical'
            },
            {
                'content': 'Students will learn programming fundamentals through hands-on exercises and practical projects.',
                'expected_template': 'education'
            },
            {
                'content': 'This presentation covers various topics and general information for all audiences.',
                'expected_template': 'general'
            }
        ]

        for case in test_cases:
            with self.subTest(content=case['content']):
                template = self.generator.select_template_based_on_content(case['content'])
                self.assertEqual(template, case['expected_template'])

if __name__ == '__main__':
    # Create test suite
    suite = unittest.TestSuite()

    # Add test cases
    suite.addTest(unittest.makeSuite(TestTemplateGenerator))
    suite.addTest(unittest.makeSuite(TestTemplateGeneratorIntegration))

    # Run tests
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)

    # Exit with appropriate code
    sys.exit(0 if result.wasSuccessful() else 1)