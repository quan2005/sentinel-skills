#!/usr/bin/env python3
"""
Demo Presentation Generator for Slidev PPT Creator
Creates example presentations demonstrating all skill capabilities.
"""

import os
import sys
import json
import tempfile
import shutil
from pathlib import Path

# Add the parent directory to sys.path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from scripts.content_analyzer import ContentAnalyzer
from scripts.template_generator import TemplateGenerator
from scripts.chart_generator import ChartGenerator
from scripts.create_presentation import create_presentation
from scripts.slides_validator import SlidesValidator

class DemoGenerator:
    """Generates demo presentations showcasing skill capabilities."""

    def __init__(self):
        self.content_analyzer = ContentAnalyzer()
        self.template_generator = TemplateGenerator()
        self.chart_generator = ChartGenerator()
        self.slides_validator = SlidesValidator()

    def create_business_demo(self, output_dir):
        """Create a business presentation demo."""
        print("📊 Creating Business Presentation Demo...")

        # Sample business content
        content = """
        Create a business proposal presentation for an AI-powered customer service platform that helps companies reduce support costs by 60% while improving customer satisfaction. Include market analysis, product features, business model, competitive advantages, and investment opportunities. Target audience is potential investors and enterprise customers.
        """

        # Analyze content
        analysis = self.content_analyzer.analyze(content)
        print(f"   Analysis: {analysis['presentation_type']} presentation, {analysis['complexity']} complexity")

        # Create presentation
        presentation_data = {
            'title': 'AI Customer Service Platform - Investment Proposal',
            'type': analysis['presentation_type'],
            'content': content,
            'target_audience': 'potential investors and enterprise customers',
            'sections': [
                {
                    'title': 'Market Opportunity',
                    'content': 'The customer service market is $400B globally, growing at 15% annually. Current solutions are inefficient and costly.'
                },
                {
                    'title': 'Our Solution',
                    'content': 'AI-powered platform that reduces support costs by 60% while improving satisfaction scores by 40%.'
                },
                {
                    'title': 'Business Model',
                    'content': 'SaaS subscription model with tiered pricing based on volume and features.'
                },
                {
                    'title': 'Competitive Advantages',
                    'content': 'Proprietary AI technology, seamless integration, proven ROI.'
                },
                {
                    'title': 'Investment Opportunity',
                    'content': 'Seeking $5M Series A to scale operations and expand market reach.'
                }
            ]
        }

        # Generate charts
        charts = []
        market_data = {
            'labels': ['2023', '2024', '2025', '2026', '2027'],
            'values': [400, 460, 529, 608, 699],
            'subtitle': 'Market Size ($B)'
        }
        charts.append(self.chart_generator.generate_chart_code('bar', market_data, 'Market Growth', 'business'))

        roi_data = {
            'labels': ['Cost Reduction', 'Satisfaction Improvement', 'Efficiency Gain', 'Revenue Growth'],
            'values': [60, 40, 75, 25],
            'subtitle': 'Key Metrics (%)'
        }
        charts.append(self.chart_generator.generate_chart_code('pie', roi_data, 'ROI Metrics', 'business'))

        # Create presentation files
        result = create_presentation(
            presentation_data=presentation_data,
            template_type='business',
            charts=charts,
            output_dir=output_dir
        )

        # Validate presentation
        validation = self.slides_validator.validate_presentation(result['slides_path'])
        print(f"   Validation: {'✅ Passed' if validation['valid'] else '❌ Failed'}")

        return result

    def create_technical_demo(self, output_dir):
        """Create a technical presentation demo."""
        print("💻 Creating Technical Presentation Demo...")

        # Sample technical content
        content = """
        Create a technical sharing presentation about migrating from monolithic architecture to microservices. Include the challenges of monolithic systems, microservices design patterns, implementation strategies, database considerations, monitoring and observability, and lessons learned. Include code examples and architecture diagrams.
        """

        # Analyze content
        analysis = self.content_analyzer.analyze(content)
        print(f"   Analysis: {analysis['presentation_type']} presentation, {analysis['complexity']} complexity")

        # Create presentation
        presentation_data = {
            'title': 'Microservices Migration - A Technical Journey',
            'type': analysis['presentation_type'],
            'content': content,
            'target_audience': 'development team and technical leadership',
            'sections': [
                {
                    'title': 'Monolithic Challenges',
                    'content': 'Single codebase, tight coupling, deployment complexity, scaling limitations.'
                },
                {
                    'title': 'Microservices Design Patterns',
                    'content': 'Service discovery, circuit breakers, API gateways, event-driven architecture.'
                },
                {
                    'title': 'Implementation Strategy',
                    'content': 'Strangler fig pattern, database per service, gradual migration approach.'
                },
                {
                    'title': 'Architecture Diagram',
                    'content': 'API Gateway -> Service Registry -> Multiple Microservices -> Individual Databases'
                },
                {
                    'title': 'Code Example',
                    'content': 'Service implementation with Node.js, Express, and Docker.'
                }
            ]
        }

        # Generate diagrams and charts
        visual_elements = []

        # Architecture diagram
        arch_content = """
        1. API Gateway
        2. User Service (PostgreSQL)
        3. Order Service (MongoDB)
        4. Payment Service (PostgreSQL)
        5. Notification Service (Redis)
        """
        visual_elements.append(self.chart_generator.generate_diagram_code('architecture', arch_content, 'System Architecture'))

        # Performance metrics
        perf_data = {
            'labels': ['Response Time', 'Throughput', 'Availability', 'Error Rate'],
            'values': [85, 92, 99.9, 0.1],
            'subtitle': 'Performance Metrics (%)'
        }
        visual_elements.append(self.chart_generator.generate_chart_code('bar', perf_data, 'Performance Metrics', 'technical'))

        # Create presentation files
        result = create_presentation(
            presentation_data=presentation_data,
            template_type='technical',
            visual_elements=visual_elements,
            output_dir=output_dir
        )

        # Validate presentation
        validation = self.slides_validator.validate_presentation(result['slides_path'])
        print(f"   Validation: {'✅ Passed' if validation['valid'] else '❌ Failed'}")

        return result

    def create_education_demo(self, output_dir):
        """Create an education presentation demo."""
        print("🎓 Creating Education Presentation Demo...")

        # Sample education content
        content = """
        Create an educational presentation about React Hooks for frontend developers. Cover useState, useEffect, useContext, useReducer, and custom hooks. Include practical examples, common pitfalls, performance optimization techniques, and hands-on exercises. Make it interactive and engaging for learners.
        """

        # Analyze content
        analysis = self.content_analyzer.analyze(content)
        print(f"   Analysis: {analysis['presentation_type']} presentation, {analysis['complexity']} complexity")

        # Create presentation
        presentation_data = {
            'title': 'Mastering React Hooks - Complete Guide',
            'type': analysis['presentation_type'],
            'content': content,
            'target_audience': 'frontend developers',
            'sections': [
                {
                    'title': 'Learning Objectives',
                    'content': 'Understand React Hooks, master core hooks, create custom hooks, optimize performance.'
                },
                {
                    'title': 'Introduction to Hooks',
                    'content': 'What are Hooks, why they were introduced, benefits over class components.'
                },
                {
                    'title': 'useState Hook',
                    'content': 'State management in functional components, setter functions, best practices.'
                },
                {
                    'title': 'useEffect Hook',
                    'content': 'Side effects, lifecycle events, dependency array, cleanup functions.'
                },
                {
                    'title': 'useContext Hook',
                    'content': 'Context consumption, avoiding prop drilling, performance considerations.'
                },
                {
                    'title': 'Interactive Quiz',
                    'content': 'Test your knowledge of React Hooks concepts.'
                }
            ]
        }

        # Generate interactive elements and charts
        visual_elements = []

        # Learning progress chart
        progress_data = {
            'labels': ['useState', 'useEffect', 'useContext', 'useReducer', 'Custom Hooks'],
            'values': [90, 85, 75, 70, 60],
            'subtitle': 'Learning Progress (%)'
        }
        visual_elements.append(self.chart_generator.generate_chart_code('bar', progress_data, 'Hook Coverage', 'education'))

        # Interactive quiz
        quiz_content = {
            'questions': [
                {
                    'text': 'What Hook is used for managing state in functional components?',
                    'options': ['useEffect', 'useState', 'useContext', 'useReducer'],
                    'correctAnswer': 1,
                    'explanation': 'useState is the Hook used for managing state in functional components.'
                },
                {
                    'text': 'When does useEffect run by default?',
                    'options': ['Only once', 'Every render', 'Only when dependencies change', 'Never'],
                    'correctAnswer': 1,
                    'explanation': 'useEffect runs after every render by default, unless dependencies are specified.'
                }
            ]
        }
        visual_elements.append(self.chart_generator.generate_interactive_code('quiz', quiz_content, 'React Hooks Quiz'))

        # Create presentation files
        result = create_presentation(
            presentation_data=presentation_data,
            template_type='education',
            visual_elements=visual_elements,
            output_dir=output_dir
        )

        # Validate presentation
        validation = self.slides_validator.validate_presentation(result['slides_path'])
        print(f"   Validation: {'✅ Passed' if validation['valid'] else '❌ Failed'}")

        return result

    def create_general_demo(self, output_dir):
        """Create a general presentation demo."""
        print("📋 Creating General Presentation Demo...")

        # Sample general content
        content = """
        Create a product launch presentation for a new fitness tracking mobile app. Include market opportunity, app features and benefits, user interface design, technology stack, monetization strategy, marketing plan, and timeline. Show screenshots and user journey flows. Make it exciting and visually appealing.
        """

        # Analyze content
        analysis = self.content_analyzer.analyze(content)
        print(f"   Analysis: {analysis['presentation_type']} presentation, {analysis['complexity']} complexity")

        # Create presentation
        presentation_data = {
            'title': 'FitLife - Your Smart Fitness Companion',
            'type': analysis['presentation_type'],
            'content': content,
            'target_audience': 'potential users and investors',
            'sections': [
                {
                    'title': 'Market Opportunity',
                    'content': 'Fitness app market is $15B, growing 20% annually. Post-pandemic health consciousness surge.'
                },
                {
                    'title': 'Product Overview',
                    'content': 'AI-powered fitness tracking with personalized workouts and nutrition guidance.'
                },
                {
                    'title': 'Key Features',
                    'content': 'Activity tracking, workout planning, nutrition logging, social challenges, progress analytics.'
                },
                {
                    'title': 'User Interface',
                    'content': 'Clean, intuitive design with dark mode support and accessibility features.'
                },
                {
                    'title': 'Technology Stack',
                    'content': 'React Native, Node.js, MongoDB, TensorFlow for AI recommendations.'
                },
                {
                    'title': 'Monetization',
                    'content': 'Freemium model with premium features and personalized coaching.'
                }
            ]
        }

        # Generate charts and visual elements
        visual_elements = []

        # Market growth chart
        market_data = {
            'labels': ['2022', '2023', '2024', '2025', '2026'],
            'values': [12.5, 15.0, 18.0, 21.6, 25.9],
            'subtitle': 'Market Size ($B)'
        }
        visual_elements.append(self.chart_generator.generate_chart_code('line', market_data, 'Fitness App Market Growth', 'general'))

        # Feature adoption
        feature_data = {
            'labels': ['Activity Tracking', 'Workouts', 'Nutrition', 'Social', 'Analytics'],
            'values': [95, 85, 70, 60, 45],
            'subtitle': 'Feature Usage (%)'
        }
        visual_elements.append(self.chart_generator.generate_chart_code('pie', feature_data, 'Feature Adoption', 'general'))

        # Create presentation files
        result = create_presentation(
            presentation_data=presentation_data,
            template_type='general',
            visual_elements=visual_elements,
            output_dir=output_dir
        )

        # Validate presentation
        validation = self.slides_validator.validate_presentation(result['slides_path'])
        print(f"   Validation: {'✅ Passed' if validation['valid'] else '❌ Failed'}")

        return result

    def generate_demo_report(self, results, output_dir):
        """Generate a comprehensive demo report."""
        print("📄 Generating Demo Report...")

        report = {
            'generated_at': str(Path(__file__).stat().st_mtime),
            'presentations': {
                'business': {
                    'title': 'AI Customer Service Platform',
                    'slides': results['business'].get('slides_count', 0),
                    'charts': len(results['business'].get('charts', [])),
                    'validation': results['business'].get('validation', {}).get('valid', False)
                },
                'technical': {
                    'title': 'Microservices Migration',
                    'slides': results['technical'].get('slides_count', 0),
                    'diagrams': len(results['technical'].get('visual_elements', [])),
                    'validation': results['technical'].get('validation', {}).get('valid', False)
                },
                'education': {
                    'title': 'React Hooks Guide',
                    'slides': results['education'].get('slides_count', 0),
                    'interactive': len([e for e in results['education'].get('visual_elements', []) if 'Quiz' in e]),
                    'validation': results['education'].get('validation', {}).get('valid', False)
                },
                'general': {
                    'title': 'FitLife App Launch',
                    'slides': results['general'].get('slides_count', 0),
                    'visuals': len(results['general'].get('visual_elements', [])),
                    'validation': results['general'].get('validation', {}).get('valid', False)
                }
            },
            'features_demonstrated': [
                'Automatic template selection based on content',
                'Vue component integration (charts, diagrams)',
                'Interactive elements (quizzes)',
                'Multi-theme support (business, technical, education, general)',
                'Content analysis and structuring',
                'Slidev syntax validation',
                'Package.json generation',
                'Component bundling'
            ]
        }

        # Write report
        report_path = os.path.join(output_dir, 'demo_report.json')
        with open(report_path, 'w', encoding='utf-8') as f:
            json.dump(report, f, indent=2, ensure_ascii=False)

        # Write summary
        summary_path = os.path.join(output_dir, 'README.md')
        with open(summary_path, 'w', encoding='utf-8') as f:
            f.write("# Slidev PPT Creator - Demo Presentations\n\n")
            f.write("This directory contains example presentations demonstrating all capabilities of the Slidev PPT Creator skill.\n\n")
            f.write("## Generated Presentations\n\n")

            for key, data in report['presentations'].items():
                status = "✅" if data['validation'] else "❌"
                f.write(f"### {data['title']} ({key})\n")
                f.write(f"- Status: {status} {'Valid' if data['validation'] else 'Invalid'}\n")
                f.write(f"- Slides: {data['slides']}\n")
                if 'charts' in data:
                    f.write(f"- Charts: {data['charts']}\n")
                if 'diagrams' in data:
                    f.write(f"- Diagrams: {data['diagrams']}\n")
                if 'interactive' in data:
                    f.write(f"- Interactive Elements: {data['interactive']}\n")
                if 'visuals' in data:
                    f.write(f"- Visual Elements: {data['visuals']}\n")
                f.write("\n")

            f.write("## Features Demonstrated\n\n")
            for feature in report['features_demonstrated']:
                f.write(f"- {feature}\n")

        print(f"   Report saved to: {report_path}")
        print(f"   Summary saved to: {summary_path}")

    def run_all_demos(self, output_dir=None):
        """Run all demo presentations."""
        print("🎬 Running All Demo Presentations")
        print("=" * 50)

        # Create output directory
        if output_dir is None:
            output_dir = tempfile.mkdtemp(prefix='slidev_demo_')
        else:
            os.makedirs(output_dir, exist_ok=True)

        print(f"Output directory: {output_dir}")

        results = {}

        try:
            # Business demo
            results['business'] = self.create_business_demo(
                os.path.join(output_dir, 'business')
            )

            # Technical demo
            results['technical'] = self.create_technical_demo(
                os.path.join(output_dir, 'technical')
            )

            # Education demo
            results['education'] = self.create_education_demo(
                os.path.join(output_dir, 'education')
            )

            # General demo
            results['general'] = self.create_general_demo(
                os.path.join(output_dir, 'general')
            )

            # Generate report
            self.generate_demo_report(results, output_dir)

            print(f"\n🎉 All demos completed successfully!")
            print(f"📁 Output directory: {output_dir}")
            print("\nTo run the presentations:")
            for name in results.keys():
                demo_dir = os.path.join(output_dir, name)
                print(f"  cd {demo_dir} && npm install && npm run dev")

        except Exception as e:
            print(f"\n❌ Demo generation failed: {e}")
            import traceback
            traceback.print_exc()

        return output_dir, results

def main():
    """Main demo runner."""
    import argparse

    parser = argparse.ArgumentParser(description='Generate demo presentations for Slidev PPT Creator')
    parser.add_argument('--output', '-o', help='Output directory for demos')
    parser.add_argument('--type', choices=['business', 'technical', 'education', 'general', 'all'],
                       default='all', help='Type of demo to generate')

    args = parser.parse_args()

    generator = DemoGenerator()

    if args.type == 'all':
        output_dir, results = generator.run_all_demos(args.output)
    else:
        # Create output directory
        if args.output:
            output_dir = args.output
            os.makedirs(output_dir, exist_ok=True)
        else:
            output_dir = tempfile.mkdtemp(prefix=f'slidev_demo_{args.type}_')

        print(f"🎬 Running {args.type} Demo")
        print("=" * 30)

        if args.type == 'business':
            results = {'business': generator.create_business_demo(output_dir)}
        elif args.type == 'technical':
            results = {'technical': generator.create_technical_demo(output_dir)}
        elif args.type == 'education':
            results = {'education': generator.create_education_demo(output_dir)}
        elif args.type == 'general':
            results = {'general': generator.create_general_demo(output_dir)}

        generator.generate_demo_report(results, output_dir)

        print(f"\n🎉 Demo completed successfully!")
        print(f"📁 Output directory: {output_dir}")
        demo_dir = os.path.join(output_dir, args.type)
        print(f"To run: cd {demo_dir} && npm install && npm run dev")

    return 0

if __name__ == '__main__':
    sys.exit(main())