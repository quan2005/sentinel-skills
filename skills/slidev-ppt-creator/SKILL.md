---
name: slidev-ppt-creator
description: This skill should be used when users need to create professional, feature-rich presentations using Slidev (sli.dev). It supports business presentations, technical sharing, educational training, and general presentation scenarios with automatic template recommendation, visual element generation (charts, diagrams, architecture diagrams, interactive quizzes), advanced theming, comprehensive error handling, and multiple input methods (simple description, structured input, interactive creation).
---

# Slidev PPT Creator Skill

## Purpose

This skill specializes in creating professional, feature-rich presentations using Slidev (sli.dev) framework. It transforms user requirements into structured, visually appealing presentations with automatic template selection, content organization, visual element enhancement, advanced theming options, and comprehensive validation.

## Core Capabilities

### 🎯 **Intelligent Content Analysis**
- Automatic presentation type detection (business, technical, educational, general)
- Content structure analysis and section organization
- Visual element requirement identification
- Target audience complexity assessment

### 🎨 **Advanced Theming System**
- 8 professional themes (Business, Technical, Education, General, Minimal, Creative, Medical, Academic)
- Intelligent theme selection based on content analysis
- Custom color scheme generation
- Typography and layout customization
- CSS variable generation for consistent styling

### 📊 **Rich Visual Elements**
- **Vue Component Charts**: Bar charts, pie charts, line graphs with customizable themes
- **Interactive Diagrams**: Flowcharts, architecture diagrams, process flows with dynamic layouts
- **Interactive Components**: Quizzes, polls, and engagement elements with real-time feedback
- **Theme-Aware Visualizations**: Color-coordinated charts and diagrams matching presentation themes

### 🛠️ **Comprehensive Toolset**
- Content analyzer with multi-language support (English/Chinese)
- Template generator with 4 complete template families
- Chart generator with Vue component integration
- Theme manager with customization capabilities
- Enhanced validator with accessibility checks
- Error handling with recovery strategies

### ✅ **Quality Assurance**
- Comprehensive Slidev syntax validation
- Component dependency verification
- Accessibility compliance checking
- Performance optimization suggestions
- Error recovery and fallback mechanisms

## When to Use

Use this skill when users request:
- Creation of any type of presentation (business, technical, educational, or general)
- Slidev-based presentation development with modern features
- Automatic template selection based on content analysis
- Integration of charts, diagrams, and interactive visual elements
- Custom theming and branding requirements
- Multi-format presentation exports (PDF, PPTX, PNG, web)
- Interactive elements like quizzes and polls
- Professional presentations with advanced styling

## Enhanced Usage Workflow

### 1. Content Analysis and Theme Selection

Execute `scripts/content_analyzer.py` to analyze user input and determine:
- Presentation type (business, technical, educational, general)
- Content structure and optimal section organization
- Required visual elements (charts, diagrams, interactive components)
- Complexity level and target audience assessment
- Recommended theme and customization options

**Theme Selection Process:**
```
User Input → Content Analysis → Theme Mapping → Customization Application
```

### 2. Template Generation and Customization

Use `scripts/template_generator.py` with `scripts/theme_manager.py` to:
- Select optimal template from `assets/templates/` (Business, Technical, Education, General)
- Apply intelligent theme matching based on content keywords
- Generate customized slides.md with theme-specific styling
- Configure appropriate layouts and component structures
- Set up CSS variables and custom styling

### 3. Visual Element Enhancement

Execute `scripts/chart_generator.py` to add rich visual elements:
- **Vue Component Charts**: Generate BarChart.vue and PieChart.vue components with theme colors
- **Interactive Diagrams**: Create FlowChart.vue components with dynamic layouts
- **Interactive Quizzes**: Build Quiz.vue components with progress tracking
- **Theme-Coordinated Styling**: Ensure all visual elements match selected theme

### 4. Comprehensive Validation

Run enhanced `scripts/slides_validator.py` to ensure:
- Proper Slidev syntax and frontmatter validation
- Vue component syntax and dependency checking
- Theme compatibility and CSS validation
- Accessibility compliance (WCAG guidelines)
- Performance optimization suggestions
- Export readiness verification

## Advanced Input Methods

### **Simple Description Method** (Enhanced)
Natural language processing with intelligent content analysis:
```
"Create a business proposal for an AI-powered healthcare platform targeting hospitals,
include market analysis showing 25% growth, competitor comparison with 3 key players,
and financial projections for 5 years. Use professional blue theme with charts."
```

### **Structured Input Method** (Enhanced)
Detailed requirements with theme and styling specifications:
```
{
  "title": "Microservices Architecture Guide",
  "type": "technical",
  "theme": "technical-dark",
  "audience": "senior developers",
  "customizations": {
    "primary_color": "#10B981",
    "font_family": "JetBrains Mono",
    "chart_style": "modern"
  },
  "sections": [
    {
      "title": "Architecture Overview",
      "visuals": ["architecture_diagram", "performance_chart"]
    }
  ]
}
```

### **Interactive Creation Method** (Enhanced)
Guided creation with theme previews and customization:
1. Content analysis and automatic theme recommendation
2. Interactive theme selection with live preview options
3. Content structure optimization based on template type
4. Visual element suggestions with theme-coordinated styling
5. Real-time validation and optimization recommendations

## Enhanced Asset Structure

### **Templates** (`assets/templates/`)
- `business/business-template.md` - 387-line comprehensive business template
- `technical/technical-template.md` - 802-line detailed technical template
- `education/education-template.md` - Complete educational template with learning objectives
- `general/general-template.md` - Versatile general-purpose template

### **Components** (`assets/components/`)
- `charts/BarChart.vue` - Animated bar chart component with theme support
- `charts/PieChart.vue` - Interactive pie chart with donut mode and legends
- `diagrams/FlowChart.vue` - Dynamic flowchart with multiple layout options
- `interactive/Quiz.vue` - Complete quiz system with progress tracking

### **Styles** (`assets/styles/`)
- `themes.json` - 8 professional themes with customization options
- Theme-specific CSS files for each presentation type
- CSS variable generation for consistent theming

## Error Handling and Recovery

### **Robust Error Management**
- Centralized error handling with `scripts/error_handler.py`
- Automatic fallback strategies for common failures
- Recovery mechanisms for template, chart, and validation errors
- Comprehensive logging and error reporting

### **Validation Enhancements**
- Enhanced syntax validation with accessibility checking
- Component dependency verification
- Theme compatibility validation
- Performance optimization suggestions

## Reference Materials

Consult `references/` for detailed guidance:
- `slidev_syntax.md` - Complete Slidev syntax reference
- `template_patterns.md` - Advanced template structure patterns
- `theme_customization.md` - Theme customization and CSS variables
- `component_library.md` - Vue component usage and customization
- `best_practices.md` - Design, content, and accessibility guidelines

## Output Generation

Generate complete Slidev project including:
- `slides.md` - Main presentation content with frontmatter and components
- `package.json` - Project configuration with Slidev dependencies
- `style.css` - Custom styling with CSS variables and theme support
- `components/` - Custom Vue components (BarChart.vue, PieChart.vue, FlowChart.vue, Quiz.vue)
- `README.md` - Setup instructions and usage guidelines

### **Quality Assurance Features**
- Automatic validation of generated presentations
- Syntax checking and component verification
- Accessibility compliance validation
- Performance optimization recommendations

### **Export Capabilities**
Ensure all outputs are ready for:
- `npm run dev` - Development server with hot reload
- `npm run build` - Static site generation
- `npm run pdf` - PDF export with proper formatting
- `npm run pptx` - PowerPoint export compatibility

## Usage Examples

### **Business Presentation**
```
Input: "Create a Q4 business review with revenue growth 25%, market expansion to 3 territories,
       customer satisfaction 92%, and 2025 strategic plans"

Output: Professional business presentation with:
- Business template with blue theme
- Revenue growth bar chart
- Market expansion pie chart
- Competitive analysis tables
- Strategic timeline visualization
```

### **Technical Presentation**
```
Input: "Technical presentation about microservices migration including challenges,
       design patterns, implementation with code examples, and performance metrics"

Output: Technical presentation with:
- Technical template with dark theme
- Microservices architecture diagram
- Code examples with syntax highlighting
- Performance metrics charts
- Implementation timeline flowchart
```

### **Educational Presentation**
```
Input: "Educational presentation about React Hooks with learning objectives,
       practical examples, common pitfalls, and interactive quiz"

Output: Educational presentation with:
- Education template with fresh theme
- Learning objectives and progress tracking
- Code examples with explanations
- Interactive quiz component
- Knowledge check exercises
```

## Advanced Features

### **Theme Intelligence**
Automatic theme selection based on:
- Content keywords and terminology
- Presentation type analysis
- Industry-specific recommendations
- User preference learning

### **Interactive Elements**
- **Quizzes**: Multi-question assessments with immediate feedback
- **Polls**: Real-time audience engagement components
- **Progressive Disclosure**: Click-based content reveals
- **Animations**: Smooth transitions and element animations

### **Customization Options**
- **Color Customization**: Override theme colors with brand requirements
- **Typography Control**: Custom fonts and sizing
- **Layout Variations**: Different slide layouts and component arrangements
- **Component Styling**: Custom appearance for charts and diagrams

## Quality Standards

All generated presentations meet:
- ✅ Slidev syntax compliance
- ✅ Component integrity verification
- ✅ Theme consistency validation
- ✅ Accessibility WCAG compliance
- ✅ Performance optimization standards
- ✅ Cross-platform compatibility