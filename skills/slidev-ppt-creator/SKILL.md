---
name: slidev-ppt-creator
description: This skill should be used when users need to create professional, feature-rich presentations using Slidev (sli.dev). It supports business presentations, technical sharing, educational training, and general presentation scenarios with automatic template recommendation, visual element generation (charts, diagrams, architecture diagrams), and multiple input methods (simple description, structured input, interactive creation).
---

# Slidev PPT Creator Skill

## Purpose

This skill specializes in creating professional, feature-rich presentations using Slidev (sli.dev) framework. It transforms user requirements into structured, visually appealing presentations with automatic template selection, content organization, and visual element enhancement.

## When to Use

Use this skill when users request:
- Creation of any type of presentation (business, technical, educational, or general)
- Slidev-based presentation development
- Automatic template generation based on content type
- Integration of charts, diagrams, and other visual elements
- Conversion of ideas or outlines into professional presentations
- Multi-format presentation exports (PDF, PPTX, PNG, web)

## How to Use

### 1. Analyze User Input

Execute `scripts/content_analyzer.py` to analyze user input and determine:
- Presentation type (business, technical, educational, general)
- Content structure and sections
- Required visual elements (charts, diagrams, code blocks)
- Complexity level and target audience
- Recommended template type

### 2. Generate Appropriate Template

Based on the analysis, use `scripts/template_generator.py` to:
- Select the most suitable template from `assets/templates/`
- Generate initial slides.md structure
- Configure appropriate theme and styling
- Set up necessary components and layouts

### 3. Enhance with Visual Elements

Execute `scripts/chart_generator.py` to add visual elements:
- Generate data charts for numerical information
- Create architecture diagrams for technical content
- Add flowcharts for process descriptions
- Include appropriate icons and visual indicators

### 4. Validate and Finalize

Run `scripts/slides_validator.py` to ensure:
- Proper Slidev syntax and formatting
- Correct component usage
- Theme compatibility
- Export readiness

## Input Methods

### Simple Description Method
When users provide natural language descriptions like:
- "Create a presentation about AI in healthcare"
- "I need a tech talk about microservices"
- "Make a business proposal for a new product"

### Structured Input Method
When users provide detailed requirements:
- Specific sections and content outlines
- Preferred templates or styling requirements
- Data that needs visualization
- Target audience specifications

### Interactive Creation Method
Guide users through a structured process:
1. Determine presentation purpose and audience
2. Collect content sections and key points
3. Identify visual element requirements
4. Select appropriate styling and theme
5. Generate and refine the presentation

## Asset Management

### Templates (`assets/templates/`)
- `business/` - Business presentation templates with professional styling
- `technical/` - Technical sharing templates with code highlighting
- `education/` - Educational templates with learning structures
- `general/` - General purpose templates for mixed content

### Components (`assets/components/`)
- `charts/` - Reusable chart components (bar, pie, line charts)
- `diagrams/` - Architecture diagram and flowchart components
- `interactive/` - Interactive elements for engagement

### Styles (`assets/styles/themes/`)
- Theme configuration files
- Custom CSS styling
- Typography and color schemes

## Reference Materials

Consult `references/` when needed:
- `slidev_syntax.md` - Slidev syntax and capabilities
- `template_patterns.md` - Common presentation structures
- `visualization_library.md` - Available visual components
- `best_practices.md` - Design and content guidelines

## Output Generation

Generate complete Slidev project including:
- `slides.md` - Main presentation content
- `package.json` - Project configuration and dependencies
- `style.css` - Custom styling
- `components/` - Custom Vue components
- `README.md` - Usage instructions

Ensure all outputs are valid Slidev projects that can be immediately used with `npm run dev`.