#!/usr/bin/env python3
"""
Test runner for Slidev PPT Creator
Runs all tests and generates a comprehensive test report.
"""

import unittest
import sys
import os
import time
from io import StringIO

# Add the parent directory to sys.path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

def run_test_suite():
    """Run the complete test suite and generate report."""
    print("🧪 Running Slidev PPT Creator Test Suite")
    print("=" * 50)

    # Discover and run all tests
    loader = unittest.TestLoader()
    start_dir = os.path.dirname(__file__)
    suite = loader.discover(start_dir, pattern='test_*.py')

    # Create test runner with detailed output
    stream = StringIO()
    runner = unittest.TextTestRunner(
        stream=stream,
        verbosity=2,
        buffer=True,
        failfast=False
    )

    # Run tests
    start_time = time.time()
    result = runner.run(suite)
    end_time = time.time()

    # Get test output
    test_output = stream.getvalue()

    # Generate summary report
    print("\n📊 Test Results Summary")
    print("=" * 50)
    print(f"Tests run: {result.testsRun}")
    print(f"Failures: {len(result.failures)}")
    print(f"Errors: {len(result.errors)}")
    print(f"Skipped: {len(result.skipped) if hasattr(result, 'skipped') else 0}")
    print(f"Time taken: {end_time - start_time:.2f} seconds")

    if result.failures:
        print(f"\n❌ Failures ({len(result.failures)}):")
        for test, traceback in result.failures:
            print(f"  - {test}")
            # Print first line of error for quick overview
            first_line = traceback.split('\n')[1] if '\n' in traceback else traceback
            print(f"    {first_line.strip()}")

    if result.errors:
        print(f"\n🔥 Errors ({len(result.errors)}):")
        for test, traceback in result.errors:
            print(f"  - {test}")
            # Print first line of error for quick overview
            first_line = traceback.split('\n')[1] if '\n' in traceback else traceback
            print(f"    {first_line.strip()}")

    # Success status
    if result.wasSuccessful():
        print("\n✅ All tests passed!")
        return True
    else:
        print(f"\n❌ {len(result.failures) + len(result.errors)} test(s) failed!")
        return False

def run_individual_tests():
    """Run individual test modules."""
    test_modules = [
        'test_chart_generator',
        'test_template_generator'
    ]

    all_passed = True

    for module in test_modules:
        print(f"\n🔍 Running {module}...")
        try:
            # Import the test module
            test_module = __import__(module)

            # Create test suite
            loader = unittest.TestLoader()
            suite = loader.loadTestsFromModule(test_module)

            # Run tests
            runner = unittest.TextTestRunner(verbosity=1)
            result = runner.run(suite)

            if not result.wasSuccessful():
                all_passed = False
                print(f"❌ {module} had failures/errors")
            else:
                print(f"✅ {module} passed")

        except Exception as e:
            print(f"🔥 Error running {module}: {e}")
            all_passed = False

    return all_passed

def validate_skill_structure():
    """Validate the overall skill structure."""
    print("\n🏗️  Validating Skill Structure")
    print("=" * 50)

    base_dir = os.path.join(os.path.dirname(__file__), '..')
    required_structure = {
        'SKILL.md': 'file',
        'scripts': 'dir',
        'assets': 'dir',
        'references': 'dir',
        'examples': 'dir',
        'tests': 'dir'
    }

    required_assets = {
        'templates': 'dir',
        'components': 'dir'
    }

    required_templates = {
        'business': 'dir',
        'technical': 'dir',
        'education': 'dir',
        'general': 'dir'
    }

    required_components = {
        'charts': 'dir',
        'diagrams': 'dir',
        'interactive': 'dir'
    }

    required_scripts = [
        'content_analyzer.py',
        'template_generator.py',
        'chart_generator.py',
        'slides_validator.py',
        'create_presentation.py',
        'package_skill.py'
    ]

    validation_passed = True

    # Check top-level structure
    for item, item_type in required_structure.items():
        path = os.path.join(base_dir, item)
        if item_type == 'file' and os.path.isfile(path):
            print(f"✅ {item} exists")
        elif item_type == 'dir' and os.path.isdir(path):
            print(f"✅ {item}/ exists")
        else:
            print(f"❌ {item} missing")
            validation_passed = False

    # Check assets structure
    assets_dir = os.path.join(base_dir, 'assets')
    if os.path.isdir(assets_dir):
        for item, item_type in required_assets.items():
            path = os.path.join(assets_dir, item)
            if item_type == 'dir' and os.path.isdir(path):
                print(f"✅ assets/{item}/ exists")
            else:
                print(f"❌ assets/{item}/ missing")
                validation_passed = False

        # Check templates
        templates_dir = os.path.join(assets_dir, 'templates')
        if os.path.isdir(templates_dir):
            for template in required_templates:
                path = os.path.join(templates_dir, template)
                if os.path.isdir(path):
                    print(f"✅ assets/templates/{template}/ exists")
                else:
                    print(f"❌ assets/templates/{template}/ missing")
                    validation_passed = False

        # Check components
        components_dir = os.path.join(assets_dir, 'components')
        if os.path.isdir(components_dir):
            for component in required_components:
                path = os.path.join(components_dir, component)
                if os.path.isdir(path):
                    print(f"✅ assets/components/{component}/ exists")
                else:
                    print(f"❌ assets/components/{component}/ missing")
                    validation_passed = False

    # Check scripts
    scripts_dir = os.path.join(base_dir, 'scripts')
    if os.path.isdir(scripts_dir):
        for script in required_scripts:
            path = os.path.join(scripts_dir, script)
            if os.path.isfile(path):
                print(f"✅ scripts/{script} exists")
            else:
                print(f"❌ scripts/{script} missing")
                validation_passed = False

    return validation_passed

def check_dependencies():
    """Check if all required dependencies are available."""
    print("\n📦 Checking Dependencies")
    print("=" * 50)

    dependencies = [
        ('json', 'json'),
        ('re', 're'),
        ('typing', 'typing'),
        ('pathlib', 'pathlib'),
        ('unittest', 'unittest'),
        ('tempfile', 'tempfile'),
        ('shutil', 'shutil')
    ]

    all_available = True

    for module_name, import_name in dependencies:
        try:
            __import__(import_name)
            print(f"✅ {module_name} available")
        except ImportError:
            print(f"❌ {module_name} not available")
            all_available = False

    return all_available

def main():
    """Main test runner."""
    print("🎯 Slidev PPT Creator - Comprehensive Testing")
    print("=" * 60)

    # Run validation checks first
    structure_valid = validate_skill_structure()
    deps_available = check_dependencies()

    if not structure_valid or not deps_available:
        print("\n❌ Basic validation failed. Skipping tests.")
        return False

    # Run tests
    print("\n🚀 Starting Test Execution")
    success = run_test_suite()

    if success:
        print("\n🎉 All tests passed! The skill is ready for use.")
    else:
        print("\n🔧 Some tests failed. Please review the issues above.")

    return success

if __name__ == '__main__':
    success = main()
    sys.exit(0 if success else 1)