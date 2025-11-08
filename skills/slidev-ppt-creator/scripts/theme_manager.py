#!/usr/bin/env python3
"""
Theme Manager for Slidev PPT Creator
Manages themes, color schemes, and customization options.
"""

import json
import os
from typing import Dict, Any, List, Optional
from pathlib import Path

# Import error handling
try:
    from .error_handler import (
        SlidevError, ThemeError, handle_slidev_errors,
        validate_file_path, validate_string_input, SafeFileOperations
    )
except ImportError:
    # Fallback if running as standalone script
    import sys
    sys.path.insert(0, os.path.dirname(__file__))
    from error_handler import (
        SlidevError, ThemeError, handle_slidev_errors,
        validate_file_path, validate_string_input, SafeFileOperations
    )

class ThemeManager:
    """Manages themes and customization for presentations."""

    def __init__(self):
        self.themes = {}
        self.theme_mappings = {}
        self.customization_options = {}
        self.current_theme = None

        # Load theme definitions
        self._load_themes()

    @handle_slidev_errors(fallback_result=False, context={'operation': 'load_themes'})
    def _load_themes(self):
        """Load theme definitions from themes.json file."""
        themes_file = os.path.join(
            os.path.dirname(__file__),
            '..', 'assets', 'styles', 'themes.json'
        )

        if not os.path.exists(themes_file):
            raise ThemeError(f"Themes file not found: {themes_file}")

        try:
            themes_data = SafeJSONOperations.load_json(themes_file)

            self.themes = themes_data.get('themes', {})
            self.theme_mappings = themes_data.get('theme_mappings', {})
            self.customization_options = themes_data.get('customization_options', {})

            if not self.themes:
                raise ThemeError("No themes found in themes file")

        except Exception as e:
            raise ThemeError(f"Failed to load themes: {e}")

    @handle_slidev_errors(fallback_result='general', context={'operation': 'select_theme'})
    def select_theme(self, content: str = None, content_type: str = None,
                    user_preference: str = None, keywords: List[str] = None) -> str:
        """
        Select appropriate theme based on content and preferences.

        Args:
            content: Content to analyze for theme selection
            content_type: Type of presentation (business, technical, education, general)
            user_preference: User-specified theme preference
            keywords: Additional keywords for theme selection

        Returns:
            Selected theme name
        """
        # Use user preference if specified and valid
        if user_preference and user_preference in self.themes:
            return user_preference

        # Use content type if specified
        if content_type and content_type in self.theme_mappings.get('presentation_types', {}):
            type_themes = self.theme_mappings['presentation_types'][content_type]
            if type_themes:
                return type_themes[0]  # Return first matching theme

        # Analyze content for keywords
        if content or keywords:
            content_lower = (content or '').lower()
            all_keywords = keywords or []

            # Extract keywords from content
            if content:
                content_words = content_lower.split()
                all_keywords.extend(content_words)

            # Check keyword mappings
            keyword_mappings = self.theme_mappings.get('content_keywords', {})
            for keyword in all_keywords:
                for mapped_keyword, theme in keyword_mappings.items():
                    if mapped_keyword in keyword:
                        if theme in self.themes:
                            return theme

        # Default fallback
        return 'general'

    @handle_slidev_errors(fallback_result={}, context={'operation': 'get_theme_config'})
    def get_theme_config(self, theme_name: str) -> Dict[str, Any]:
        """
        Get theme configuration.

        Args:
            theme_name: Name of the theme

        Returns:
            Theme configuration dictionary
        """
        if theme_name not in self.themes:
            raise ThemeError(f"Theme not found: {theme_name}")

        return self.themes[theme_name].copy()

    @handle_slidev_errors(fallback_result={}, context={'operation': 'apply_theme'})
    def apply_theme(self, theme_name: str, customizations: Dict[str, Any] = None) -> Dict[str, Any]:
        """
        Apply theme and customizations to generate theme configuration.

        Args:
            theme_name: Base theme name
            customizations: Custom theme customizations

        Returns:
            Complete theme configuration
        """
        base_theme = self.get_theme_config(theme_name)
        theme_config = base_theme.copy()

        # Apply customizations
        if customizations:
            theme_config = self._apply_customizations(theme_config, customizations)

        # Generate CSS variables
        theme_config['css_variables'] = self._generate_css_variables(theme_config)

        # Generate Slidev frontmatter
        theme_config['slidev_frontmatter'] = self._generate_slidev_frontmatter(theme_config)

        self.current_theme = theme_name
        return theme_config

    @handle_slidev_errors(fallback_result=[], context={'operation': 'list_themes'})
    def list_themes(self) -> List[Dict[str, str]]:
        """
        List all available themes.

        Returns:
            List of theme information dictionaries
        """
        themes_list = []
        for theme_name, theme_config in self.themes.items():
            themes_list.append({
                'name': theme_name,
                'display_name': theme_config.get('name', theme_name),
                'description': theme_config.get('description', ''),
                'primary_color': theme_config.get('primary', '#000000')
            })

        return themes_list

    @handle_slidev_errors(fallback_result=False, context={'operation': 'generate_theme_css'})
    def generate_theme_css(self, theme_name: str, customizations: Dict[str, Any] = None) -> str:
        """
        Generate CSS for a theme.

        Args:
            theme_name: Theme name
            customizations: Theme customizations

        Returns:
            CSS string for the theme
        """
        theme_config = self.apply_theme(theme_name, customizations)

        css = f"""
/* Theme: {theme_config.get('name', theme_name)} */

:root {{
{theme_config.get('css_variables', '')}
}}

/* Slidev theme overrides */
.slidev-layout {{
  font-family: {theme_config.get('typography', {}).get('font_family', 'system-ui')};
}}

h1, h2, h3, h4, h5, h6 {{
  font-weight: {theme_config.get('typography', {}).get('heading_weight', '700')}};
  color: {theme_config.get('primary', '#000000')};
}}

code {{
  color: {theme_config.get('code', '#374151')};
  font-family: {theme_config.get('typography', {}).get('mono_font', 'monospace')};
}}

/* Custom theme styles */
.theme-primary {{
  color: {theme_config.get('primary', '#000000')};
}}

.theme-secondary {{
  color: {theme_config.get('secondary', '#666666')};
}}

.theme-accent {{
  color: {theme_config.get('accent', '#888888')};
}}

.theme-background {{
  background-color: {theme_config.get('background', '#FFFFFF')};
}}

.theme-gradient {{
  background: {theme_config.get('gradient', 'linear-gradient(135deg, #000000 0%, #666666 100%)')};
}}

/* Chart colors */
.chart-colors {{
  --chart-color-1: {theme_config.get('colors', {}).get('chart', ['#000000'])[0] if theme_config.get('colors', {}).get('chart') else '#000000'};
  --chart-color-2: {theme_config.get('colors', {}).get('chart', ['#000000'])[1] if len(theme_config.get('colors', {}).get('chart', ['#000000'])) > 1 else '#666666'};
  --chart-color-3: {theme_config.get('colors', {}).get('chart', ['#000000'])[2] if len(theme_config.get('colors', {}).get('chart', ['#000000'])) > 2 else '#888888'};
  --chart-color-4: {theme_config.get('colors', {}).get('chart', ['#000000'])[3] if len(theme_config.get('colors', {}).get('chart', ['#000000'])) > 3 else '#AAAAAA'};
  --chart-color-5: {theme_config.get('colors', {}).get('chart', ['#000000'])[4] if len(theme_config.get('colors', {}).get('chart', ['#000000'])) > 4 else '#CCCCCC'};
}}

/* Semantic colors */
.semantic-success {{
  color: {theme_config.get('colors', {}).get('semantic', {}).get('success', '#059669')};
}}

.semantic-warning {{
  color: {theme_config.get('colors', {}).get('semantic', {}).get('warning', '#D97706')};
}}

.semantic-error {{
  color: {theme_config.get('colors', {}).get('semantic', {}).get('error', '#DC2626')};
}}

.semantic-info {{
  color: {theme_config.get('colors', {}).get('semantic', {}).get('info', '#0891B2')};
}}
"""

        return css

    def _apply_customizations(self, base_theme: Dict[str, Any],
                            customizations: Dict[str, Any]) -> Dict[str, Any]:
        """Apply customizations to base theme."""
        theme = base_theme.copy()

        # Color customizations
        color_overrides = {
            'primary_color': 'primary',
            'secondary_color': 'secondary',
            'accent_color': 'accent',
            'background_color': 'background',
            'text_color': 'text'
        }

        for custom_key, theme_key in color_overrides.items():
            if custom_key in customizations:
                theme[theme_key] = customizations[custom_key]

        # Typography customizations
        if 'typography_customization' in customizations:
            typo_custom = customizations['typography_customization']
            if 'typography' not in theme:
                theme['typography'] = {}

            typo_overrides = {
                'font_family': 'font_family',
                'heading_font': 'heading_font',
                'body_font': 'body_font',
                'mono_font': 'mono_font',
                'base_font_size': 'base_font_size',
                'heading_scale': 'heading_scale'
            }

            for custom_key, theme_key in typo_overrides.items():
                if custom_key in typo_custom:
                    theme['typography'][theme_key] = typo_custom[custom_key]

        # Update palette based on primary color change
        if 'primary' in theme and 'colors' in theme:
            theme['colors']['palette'][0] = theme['primary']
            theme['colors']['chart'][0] = theme['primary']

        return theme

    def _generate_css_variables(self, theme_config: Dict[str, Any]) -> str:
        """Generate CSS custom properties from theme config."""
        variables = []

        # Color variables
        color_vars = [
            ('primary', 'primary'),
            ('secondary', 'secondary'),
            ('accent', 'accent'),
            ('background', 'background'),
            ('text', 'text'),
            ('code', 'code')
        ]

        for css_var, theme_key in color_vars:
            if theme_key in theme_config:
                variables.append(f"  --theme-{css_var}: {theme_config[theme_key]};")

        # Typography variables
        if 'typography' in theme_config:
            typo = theme_config['typography']
            typo_vars = [
                ('font-family', 'font_family'),
                ('heading-weight', 'heading_weight'),
                ('body-weight', 'body_weight'),
                ('mono-font', 'mono_font')
            ]

            for css_var, theme_key in typo_vars:
                if theme_key in typo:
                    variables.append(f"  --theme-{css_var}: {typo[theme_key]};")

        return '\n'.join(variables)

    def _generate_slidev_frontmatter(self, theme_config: Dict[str, Any]) -> str:
        """Generate Slidev frontmatter configuration."""
        frontmatter = {}

        # Basic theme configuration
        if 'slidev_theme' in theme_config:
            frontmatter['theme'] = theme_config['slidev_theme']

        # Color configuration
        if 'primary' in theme_config:
            frontmatter['colorPrimary'] = theme_config['primary']

        # Font configuration
        if 'typography' in theme_config:
            typo = theme_config['typography']
            if 'font_family' in typo:
                frontmatter['fontFamily'] = typo['font_family']

        # Background configuration
        if 'background' in theme_config:
            frontmatter['background'] = theme_config['background']

        # Generate YAML frontmatter string
        yaml_lines = []
        for key, value in frontmatter.items():
            if isinstance(value, str):
                yaml_lines.append(f"{key}: {value}")
            else:
                yaml_lines.append(f"{key}: {json.dumps(value)}")

        return '\n'.join(yaml_lines)

    @handle_slidev_errors(fallback_result=False, context={'operation': 'create_custom_theme'})
    def create_custom_theme(self, theme_name: str, base_theme: str,
                          customizations: Dict[str, Any]) -> bool:
        """
        Create a custom theme based on an existing theme.

        Args:
            theme_name: Name for the new custom theme
            base_theme: Base theme to customize
            customizations: Customization options

        Returns:
            True if successful
        """
        if theme_name in self.themes:
            raise ThemeError(f"Theme already exists: {theme_name}")

        if base_theme not in self.themes:
            raise ThemeError(f"Base theme not found: {base_theme}")

        # Create custom theme
        custom_theme = self.apply_theme(base_theme, customizations)
        custom_theme['name'] = f"Custom {theme_name.title()}"
        custom_theme['description'] = f"Custom theme based on {base_theme}"
        custom_theme['base_theme'] = base_theme
        custom_theme['customizations'] = customizations

        # Add to themes
        self.themes[theme_name] = custom_theme

        return True

    def get_theme_recommendations(self, content: str, content_type: str = None) -> List[str]:
        """
        Get theme recommendations based on content analysis.

        Args:
            content: Content to analyze
            content_type: Type of presentation

        Returns:
            List of recommended theme names
        """
        recommendations = []

        # Base recommendation on content type
        if content_type and content_type in self.theme_mappings.get('presentation_types', {}):
            recommendations.extend(self.theme_mappings['presentation_types'][content_type])

        # Analyze content for theme-specific keywords
        content_lower = content.lower()
        keyword_mappings = self.theme_mappings.get('content_keywords', {})

        for keyword, theme in keyword_mappings.items():
            if keyword in content_lower and theme not in recommendations:
                recommendations.append(theme)

        # Add general themes if no specific recommendations
        if not recommendations:
            recommendations = ['general', 'minimal']

        return recommendations[:3]  # Return top 3 recommendations

def main():
    """Command line interface for theme manager."""
    import argparse
    import json

    parser = argparse.ArgumentParser(description='Manage themes for Slidev presentations')
    parser.add_argument('action', choices=['list', 'get', 'apply', 'recommend', 'css'],
                       help='Action to perform')
    parser.add_argument('--theme', help='Theme name')
    parser.add_argument('--content', help='Content for theme analysis')
    parser.add_argument('--type', help='Presentation type')
    parser.add_argument('--customizations', help='JSON string of customizations')
    parser.add_argument('--output', '-o', help='Output file')

    args = parser.parse_args()

    manager = ThemeManager()

    try:
        if args.action == 'list':
            themes = manager.list_themes()
            output = json.dumps(themes, indent=2)

        elif args.action == 'get':
            if not args.theme:
                print("Error: --theme required for get action")
                return 1

            theme_config = manager.get_theme_config(args.theme)
            output = json.dumps(theme_config, indent=2)

        elif args.action == 'apply':
            if not args.theme:
                print("Error: --theme required for apply action")
                return 1

            customizations = json.loads(args.customizations) if args.customizations else {}
            theme_config = manager.apply_theme(args.theme, customizations)
            output = json.dumps(theme_config, indent=2)

        elif args.action == 'recommend':
            content = args.content or ""
            recommendations = manager.get_theme_recommendations(content, args.type)
            output = json.dumps(recommendations, indent=2)

        elif args.action == 'css':
            if not args.theme:
                print("Error: --theme required for css action")
                return 1

            customizations = json.loads(args.customizations) if args.customizations else {}
            css = manager.generate_theme_css(args.theme, customizations)
            output = css

        else:
            print(f"Error: Unknown action: {args.action}")
            return 1

        # Output result
        if args.output:
            with open(args.output, 'w', encoding='utf-8') as f:
                f.write(output)
            print(f"Output saved to: {args.output}")
        else:
            print(output)

        return 0

    except Exception as e:
        print(f"Error: {e}")
        return 1

if __name__ == "__main__":
    import sys
    sys.exit(main())