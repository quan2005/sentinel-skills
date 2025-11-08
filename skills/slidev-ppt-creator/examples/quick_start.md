# Slidev PPT Creator - Quick Start Guide

This guide demonstrates how to use the Slidev PPT Creator skill to generate professional presentations.

## 🚀 Quick Start

### Basic Usage

1. **Simple Description Method**
   ```
   Create a business presentation about our Q4 sales performance and growth strategy
   ```

2. **Structured Input Method**
   ```
   Title: Annual Sales Review
   Type: Business Presentation
   Audience: Executive Team
   Sections:
   - Revenue Performance (25% growth)
   - Market Expansion (3 new territories)
   - Customer Success (92% satisfaction)
   - 2025 Strategic Plans
   ```

3. **Interactive Creation Method**
   ```
   Help me create a technical presentation about microservices architecture.
   I need to cover design patterns, implementation challenges, and best practices.
   Include code examples and diagrams for my development team.
   ```

## 📊 What the Skill Can Do

### ✨ Core Features
- **Automatic Template Selection**: Business, Technical, Education, or General templates
- **Content Analysis**: Structured presentation generation from natural language
- **Visual Elements**: Charts, diagrams, and interactive components
- **Slidev Integration**: Full compatibility with Slidev framework
- **Multi-format Export**: PDF, PPTX, PNG, web formats

### 🎨 Visual Components
- **Charts**: Bar charts, pie charts, line graphs with Vue components
- **Diagrams**: Flowcharts, architecture diagrams, process flows
- **Interactive Elements**: Quizzes, polls, engagement components
- **Themes**: Business, Technical, Education, General color schemes

### 📝 Template Types

#### Business Template
- Market analysis slides
- Financial projections
- Competitive landscape
- Investment opportunities
- Professional styling

#### Technical Template
- Code examples with syntax highlighting
- Architecture diagrams
- Implementation details
- Performance metrics
- Developer-focused layout

#### Education Template
- Learning objectives
- Interactive quizzes
- Step-by-step tutorials
- Progress tracking
- Engaging visuals

#### General Template
- Versatile layouts
- Flexible content structure
- Professional appearance
- Mixed content support

## 🛠️ Usage Examples

### Example 1: Business Presentation
```
Create a business proposal for a new SaaS product that helps small businesses
manage inventory. Include market size ($50B), target customers, revenue model,
competitive advantages, and funding requirements. The presentation should be
persuasive for potential investors.
```

**Generated Features:**
- Business template with professional styling
- Market size bar chart
- Revenue model pie chart
- Competitive analysis table
- Investment ask slide

### Example 2: Technical Presentation
```
I need to create a technical presentation about implementing CI/CD pipelines.
Include the current challenges, proposed solution with GitHub Actions,
deployment strategies, monitoring setup, and team training plan.
The audience is my development team.
```

**Generated Features:**
- Technical template with code highlighting
- CI/CD pipeline flowchart
- Deployment architecture diagram
- Performance metrics dashboard
- Implementation timeline

### Example 3: Educational Presentation
```
Create an educational presentation about machine learning basics for beginners.
Cover supervised vs unsupervised learning, common algorithms, practical
examples, and hands-on exercises. Make it interactive and engaging.
```

**Generated Features:**
- Education template with learning objectives
- Concept comparison charts
- Algorithm flow diagrams
- Interactive quiz components
- Practice exercises

### Example 4: General Presentation
```
Help me create a project kickoff presentation for a new mobile app.
Include project goals, team roles, timeline, milestones, and success metrics.
Make it motivating for the team.
```

**Generated Features:**
- General template with versatile layout
- Project timeline visualization
- Team structure chart
- Milestone tracking
- Success metrics dashboard

## 🎯 Advanced Features

### Data Visualization
```
Include charts showing: User growth (25% monthly), Revenue ($1M ARR),
Customer satisfaction (4.8/5), Market share (15%)
```

### Interactive Elements
```
Add a quiz to test understanding of the key concepts
Include a poll for audience feedback on preferred features
```

### Custom Styling
```
Use our company colors: blue (#1E40AF) and green (#059669)
Include our logo on each slide
Make it professional and modern
```

## 📋 Output Structure

Each generated presentation includes:

```
presentation-folder/
├── slides.md           # Main presentation content
├── package.json        # Dependencies and scripts
├── style.css          # Custom styling
├── components/        # Custom Vue components
│   ├── BarChart.vue   # Chart components
│   ├── PieChart.vue   # Visualization components
│   ├── FlowChart.vue  # Diagram components
│   └── Quiz.vue       # Interactive components
└── README.md          # Setup instructions
```

## 🚀 Running the Presentation

1. **Navigate to the presentation folder**
   ```bash
   cd presentation-folder
   ```

2. **Install dependencies**
   ```bash
   npm install
   ```

3. **Start development server**
   ```bash
   npm run dev
   ```

4. **Export to other formats**
   ```bash
   npm run build     # Build static site
   npm run pdf       # Export to PDF
   npm run pptx      # Export to PowerPoint
   ```

## 💡 Pro Tips

1. **Be Specific**: More detailed input generates better presentations
2. **Include Data**: Numbers and percentages enable automatic chart generation
3. **Specify Audience**: Tailors content complexity and examples
4. **Request Visuals**: Ask for charts, diagrams, or interactive elements
5. **Provide Context**: Background information improves relevance

## 🎨 Customization Options

### Themes
- `business` - Professional blue theme
- `technical` - Dark gray tech theme
- `education` - Green learning theme
- `general` - Purple versatile theme

### Layout Options
- Section dividers
- Two-column layouts
- Full-screen visuals
- Speaker notes
- Progress indicators

### Export Formats
- PDF (print-friendly)
- PPTX (PowerPoint compatible)
- PNG (image slides)
- HTML (web presentation)

## 🔧 Troubleshooting

### Common Issues

1. **Generated presentation too simple**
   - Add more specific details and data points
   - Specify the target audience and complexity level

2. **Missing visual elements**
   - Include numerical data for automatic chart generation
   - Request specific types of charts or diagrams

3. **Template not matching content**
   - Use keywords matching the desired template type
   - Specify the template explicitly in your request

### Getting Help

If you encounter issues:
1. Check that all required files are generated
2. Verify `npm install` completed successfully
3. Review the generated `slides.md` for syntax errors
4. Run the validator script to check for issues

## 📚 Additional Resources

- [Slidev Documentation](https://sli.dev/guide/)
- [Vue.js Components](https://vuejs.org/guide/components/overview.html)
- [Mermaid Diagrams](https://mermaid.js.org/)
- [Chart Examples](./examples/)

## 🎉 Next Steps

1. Try generating your first presentation
2. Experiment with different content types
3. Customize the generated templates
4. Add your own components and styles
5. Export and share your presentations

Ready to create your first presentation? Just describe what you need!