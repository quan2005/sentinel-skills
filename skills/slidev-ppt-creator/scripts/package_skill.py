#!/usr/bin/env python3
"""
Package script for Slidev PPT Creator skill
Validates and packages the skill for distribution.
"""

import os
import sys
import json
import zipfile
from pathlib import Path
from typing import Dict, List, Any

class SkillValidator:
    def __init__(self, skill_path: str):
        self.skill_path = Path(skill_path)
        self.errors = []
        self.warnings = []

    def validate(self) -> Dict[str, Any]:
        """Validate the skill structure and content."""
        self.errors = []
        self.warnings = []

        # Check required files
        self._validate_required_files()

        # Check skill.md structure
        self._validate_skill_md()

        # Check directory structure
        self._validate_directory_structure()

        # Check scripts
        self._validate_scripts()

        # Check assets
        self._validate_assets()

        return {
            'valid': len(self.errors) == 0,
            'errors': self.errors,
            'warnings': self.warnings,
            'summary': self._generate_summary()
        }

    def _validate_required_files(self):
        """Validate required skill files."""
        skill_md_path = self.skill_path / 'SKILL.md'

        if not skill_md_path.exists():
            self.errors.append("Missing required file: SKILL.md")
            return

        # Check SKILL.md content
        with open(skill_md_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # Check YAML frontmatter
        if not content.startswith('---'):
            self.errors.append("SKILL.md must start with YAML frontmatter")
        else:
            # Extract frontmatter
            try:
                frontmatter_end = content.find('---', 3)
                if frontmatter_end == -1:
                    self.errors.append("SKILL.md frontmatter not properly closed")
                else:
                    frontmatter = content[3:frontmatter_end]
                    self._validate_frontmatter(frontmatter)
            except Exception as e:
                self.errors.append(f"Error parsing SKILL.md frontmatter: {e}")

    def _validate_frontmatter(self, frontmatter: str):
        """Validate YAML frontmatter content."""
        lines = frontmatter.strip().split('\n')
        required_fields = ['name', 'description']

        found_fields = []
        for line in lines:
            if ':' in line:
                field = line.split(':')[0].strip()
                found_fields.append(field)

        for field in required_fields:
            if field not in found_fields:
                self.errors.append(f"Missing required field in frontmatter: {field}")

        # Check field quality
        if 'name' in found_fields:
            name_line = next(line for line in lines if line.startswith('name:'))
            name = name_line.split(':', 1)[1].strip()
            if len(name) < 5:
                self.warnings.append("Skill name is very short")
            if not name.replace('-', '').replace('_', '').isalnum():
                self.warnings.append("Skill name contains special characters")

        if 'description' in found_fields:
            desc_line = next(line for line in lines if line.startswith('description:'))
            description = desc_line.split(':', 1)[1].strip()
            if len(description) < 20:
                self.warnings.append("Skill description is very short")
            if not any(phrase in description.lower() for phrase in ['when', 'use', 'should']):
                self.warnings.append("Description should clarify when to use the skill")

    def _validate_skill_md(self):
        """Validate SKILL.md body content."""
        skill_md_path = self.skill_path / 'SKILL.md'
        with open(skill_md_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # Check for sections
        required_sections = ['Purpose', 'When to Use', 'How to Use']
        found_sections = []

        for line in content.split('\n'):
            if line.startswith('#') and ':' in line:
                section = line[1:].strip()
                found_sections.append(section)

        for section in required_sections:
            if not any(section.lower() in found_section.lower() for found_section in found_sections):
                self.warnings.append(f"Consider adding a '{section}' section to SKILL.md")

    def _validate_directory_structure(self):
        """Validate skill directory structure."""
        required_dirs = ['scripts', 'references', 'assets']
        found_dirs = []

        for item in self.skill_path.iterdir():
            if item.is_dir():
                found_dirs.append(item.name)

        # Check recommended directories
        for dir_name in required_dirs:
            if dir_name not in found_dirs:
                self.warnings.append(f"Consider adding '{dir_name}' directory for better organization")

        # Check for unexpected files
        for item in self.skill_path.iterdir():
            if item.is_file() and item.suffix not in ['.md', '.py', '.json', '.txt', '.yml', '.yaml']:
                if item.name not in ['LICENSE', 'README', '.gitignore']:
                    self.warnings.append(f"Unexpected file type: {item.name}")

    def _validate_scripts(self):
        """Validate Python scripts."""
        scripts_dir = self.skill_path / 'scripts'
        if not scripts_dir.exists():
            return

        for script_file in scripts_dir.glob('*.py'):
            try:
                # Try to compile the script
                with open(script_file, 'r', encoding='utf-8') as f:
                    script_content = f.read()
                compile(script_content, str(script_file), 'exec')
            except SyntaxError as e:
                self.errors.append(f"Syntax error in {script_file.name}: {e}")
            except Exception as e:
                self.warnings.append(f"Error checking {script_file.name}: {e}")

    def _validate_assets(self):
        """Validate assets directory."""
        assets_dir = self.skill_path / 'assets'
        if not assets_dir.exists():
            return

        # Check for asset organization
        asset_types = ['templates', 'components', 'styles']
        found_types = []

        for item in assets_dir.iterdir():
            if item.is_dir():
                found_types.append(item.name)

        if found_types:
            self.warnings.append(f"Found asset directories: {', '.join(found_types)}")

    def _generate_summary(self) -> str:
        """Generate validation summary."""
        if len(self.errors) == 0 and len(self.warnings) == 0:
            return "✅ Skill validation passed with no issues found."
        elif len(self.errors) == 0:
            return f"⚠️  Skill validation passed with {len(self.warnings)} warning(s)."
        else:
            return f"❌ Skill validation failed with {len(self.errors)} error(s) and {len(self.warnings)} warning(s)."

class SkillPackager:
    def __init__(self, skill_path: str):
        self.skill_path = Path(skill_path)

    def package(self, output_dir: str = None) -> str:
        """Package the skill into a zip file."""
        skill_name = self._get_skill_name()
        output_path = Path(output_dir or '.') / f"{skill_name}.zip"

        # Validate before packaging
        validator = SkillValidator(str(self.skill_path))
        validation_result = validator.validate()

        if not validation_result['valid']:
            print("❌ Skill validation failed. Cannot package.")
            for error in validation_result['errors']:
                print(f"  ❌ {error}")
            for warning in validation_result['warnings']:
                print(f"  ⚠️  {warning}")
            return None

        print("✅ Skill validation passed. Creating package...")

        # Create zip file
        with zipfile.ZipFile(output_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
            for root, dirs, files in os.walk(self.skill_path):
                # Skip .git directories and other unnecessary files
                dirs[:] = [d for d in dirs if not d.startswith('.')]

                for file in files:
                    if file.startswith('.') or file in ['LICENSE', 'README.md']:
                        continue

                    file_path = Path(root) / file
                    arc_path = file_path.relative_to(self.skill_path)

                    zipf.write(file_path, arc_path)

        print(f"✅ Skill packaged successfully: {output_path}")
        print(f"📦 Package size: {self._get_file_size(output_path)}")

        return str(output_path)

    def _get_skill_name(self) -> str:
        """Extract skill name from SKILL.md."""
        skill_md_path = self.skill_path / 'SKILL.md'
        with open(skill_md_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # Extract name from frontmatter
        frontmatter_end = content.find('---', 3)
        if frontmatter_end != -1:
            frontmatter = content[3:frontmatter_end]
            for line in frontmatter.split('\n'):
                if line.startswith('name:'):
                    return line.split(':', 1)[1].strip().strip('"\'')

        # Fallback to directory name
        return self.skill_path.name

    def _get_file_size(self, file_path: Path) -> str:
        """Get human readable file size."""
        size_bytes = file_path.stat().st_size

        for unit in ['B', 'KB', 'MB', 'GB']:
            if size_bytes < 1024.0:
                return f"{size_bytes:.1f} {unit}"
            size_bytes /= 1024.0
        return f"{size_bytes:.1f} TB"

def main():
    """Command line interface."""
    import argparse

    parser = argparse.ArgumentParser(description='Package Slidev PPT Creator skill')
    parser.add_argument('skill_path', help='Path to skill directory')
    parser.add_argument('--output', help='Output directory', default='.')
    parser.add_argument('--validate-only', action='store_true', help='Only validate, do not package')

    args = parser.parse_args()

    # Validate skill
    validator = SkillValidator(args.skill_path)
    validation_result = validator.validate()

    print(validation_result['summary'])
    if validation_result['errors']:
        print("\nErrors:")
        for error in validation_result['errors']:
            print(f"  ❌ {error}")
    if validation_result['warnings']:
        print("\nWarnings:")
        for warning in validation_result['warnings']:
            print(f"  ⚠️  {warning}")

    if not validation_result['valid']:
        sys.exit(1)

    if args.validate_only:
        print("✅ Validation complete. No packaging performed.")
        sys.exit(0)

    # Package skill
    packager = SkillPackager(args.skill_path)
    package_path = packager.package(args.output)

    if package_path:
        print(f"\n🎉 Skill packaged successfully!")
        print(f"📁 Package location: {package_path}")
        print(f"📖 To install: Extract and follow the README instructions")
    else:
        sys.exit(1)

if __name__ == "__main__":
    main()