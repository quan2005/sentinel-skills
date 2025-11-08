# Slidev Configuration Reference

This reference document contains essential Slidev configuration options and templates for creating professional presentations.

## Frontmatter Configuration

### Basic Configuration
```yaml
---
theme: default          # Theme: default, apple, serif, etc.
title: "Presentation Title"
author: "Author Name"
date: "2024-01-01"
aspectRatio: "16:9"     # 16:9, 4:3, or custom
canvasWidth: 1280       # Canvas width in pixels
fonts:
  sans: "Inter"
  serif: "Inter Serif"
  mono: "Fira Code"
---

# Slide Content

Markdown content here...
```

### Theme Configuration
```yaml
---
theme: seriph
themeConfig:
  primary: '#213547'
  secondary: '#1e293b'
  accent: '#0ea5e9'
  info: '#3b82f6'
  success: '#10b981'
  warning: '#f59e0b'
  error: '#ef4444'
  code: '#e2e8f0'
  background: '#ffffff'
---

# Content with custom theme colors
```

### Advanced Configuration
```yaml
---
layout: cover           # Layout for this slide
level: 2               # Header level for this slide
drawings:
  persist: false       # Keep drawings when navigating
  enabled: true        # Enable drawings on this slide
transition: slide-left # Transition effect
export:
  format: pdf         # Export format: pdf, png, pptx
  withClicks: true    # Include click animations
  dark: false         # Dark mode export
---

# Slide with custom configuration
```

## Slide Layouts

### Cover Slide
```markdown
---
layout: cover
---

# Main Title

<div class="text-6xl font-bold text-blue-600">
  Eye-catching Subtitle
</div>

<div class="text-xl text-gray-600 mt-4">
  Supporting description text
</div>

<div class="mt-8 text-lg text-gray-500">
  Author Name · Date
</div>
```

### Two Column Layout
```markdown
---
layout: two-cols
---

# Two Column Layout

::left::

## Left Column

- Point one
- Point two
- Point three

::right::

## Right Column

<div class="bg-blue-50 rounded-lg p-4">
  Important information in a styled box
</div>

Additional content with **bold** and *italic* text.
```

### Image + Text Layout
```markdown
---
layout: image-right
image: ./path/to/image.jpg
---

# Title with Image

Content on the left side, image on the right.

## Key Points

- Visual support enhances understanding
- Images should be high quality
- Text complements visual elements
```

## Content Formatting

### Text Styling
```markdown
# Heading 1
## Heading 2
### Heading 3

**Bold text** and *italic text*

~~Strikethrough text~~

`Inline code`

> Blockquote for emphasis
```

### Lists
```markdown
## Unordered List
- Item one
- Item two
  - Nested item
  - Another nested item

## Ordered List
1. First step
2. Second step
3. Third step
```

### Tables
```markdown
## Data Comparison

| Feature | Basic | Pro | Enterprise |
|---------|-------|-----|------------|
| Users | 5 | 50 | Unlimited |
| Storage | 1GB | 10GB | 100GB |
| Support | Email | Priority | 24/7 Phone |
```

### Code Blocks
```markdown
## JavaScript Example

```js
function createPresentation(config) {
  const slides = generateSlides(config.content);
  return {
    theme: config.theme,
    slides
  };
}
```

## Styling with Tailwind CSS

### Common Classes
```markdown
<div class="bg-blue-50 border-l-4 border-blue-500 p-4 rounded">
  **Information:** Important highlight box
</div>

<div class="grid grid-cols-2 gap-6">
  <div class="bg-white rounded-lg shadow p-6">
    Card content
  </div>
  <div class="bg-white rounded-lg shadow p-6">
    Another card
  </div>
</div>

<div class="text-center space-y-4">
  <div class="text-4xl font-bold text-blue-600">
    Statistic Number
  </div>
  <div class="text-lg text-gray-600">
    Supporting description
  </div>
</div>
```

### Responsive Design
```markdown
<div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
  <!-- Responsive grid layout -->
  <div>Column 1</div>
  <div>Column 2</div>
  <div>Column 3</div>
</div>
```

## Data Visualization

### Progress Bars
```markdown
## Progress Indicators

<div class="space-y-4">
  <div>
    <div class="flex justify-between mb-1">
      <span>Progress Item 1</span>
      <span class="font-semibold">75%</span>
    </div>
    <div class="w-full bg-gray-200 rounded-full h-3">
      <div class="bg-blue-500 h-3 rounded-full" style="width: 75%"></div>
    </div>
  </div>
</div>
```

### Statistics Display
```markdown
## Key Metrics

<div class="grid grid-cols-3 gap-6 text-center">
  <div class="bg-blue-50 rounded-lg p-6">
    <div class="text-4xl font-bold text-blue-600">85%</div>
    <div class="text-gray-600">Success Rate</div>
  </div>
  <div class="bg-green-50 rounded-lg p-6">
    <div class="text-4xl font-bold text-green-600">1.2M</div>
    <div class="text-gray-600">Users</div>
  </div>
  <div class="bg-purple-50 rounded-lg p-6">
    <div class="text-4xl font-bold text-purple-600">24/7</div>
    <div class="text-gray-600">Support</div>
  </div>
</div>
```

## Interactive Elements

### Click Animations
```markdown
## Progressive Reveal

First point

<div v-click>

Second point revealed on click

</div>

<div v-click>

Third point revealed on another click

</div>
```

### Component Integration
```markdown
## Custom Components

<Tweet id="20" />

## Code with Output

<div class="grid grid-cols-2 gap-4">
<div>

```js
console.log("Hello World");
```

</div>
<div>

```
Hello World
```

</div>
</div>
```

## Export Configuration

### PDF Export
```bash
# Install dependencies
npm install @slidev/cli puppeteer

# Export to PDF
slidev export --format pdf

# Export with dark mode
slidev export --format pdf --dark

# Export with click animations
slidev export --format pdf --with-clicks
```

### Image Export
```bash
# Export to PNG
slidev export --format png

# Export specific slide range
slidev export --format png --range 1-5

# Export with custom resolution
slidev export --format png --width 1920 --height 1080
```

## Best Practices

1. **Keep slides focused** - One main idea per slide
2. **Use visual hierarchy** - Headings, subheadings, and body text
3. **Limit text density** - Avoid overcrowded slides
4. **Use consistent styling** - Maintain theme consistency
5. **Test readability** - Ensure text is visible from a distance
6. **Optimize images** - Use appropriate image sizes and formats
7. **Practice transitions** - Test slide transitions and animations