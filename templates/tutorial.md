---
title: "{{tutorial_title}}"
theme: "default"
highlighter: "shiki"
lineNumbers: true
author: "{{your_name}}"
date: "{{presentation_date}}"
---

# {{tutorial_title}}

## {{subtitle}}

---

## What is {{topic}}?

<div v-click>

{{topic}} is {{brief_description}}

</div>

<div v-click>

### Key Features
{{#each features}}
- ✅ {{this}}
{{/each}}
</div>

---

## Getting Started

```bash
# Installation command
{{install_command}}

# Verify installation
{{verify_command}}
```

---

## First Example

```{{language}} {{highlight_lines}}
{{first_example_code}}
```

---

## Next Steps

1. {{step_1}}
2. {{step_2}}
3. {{step_3}}

---

# Thank You!

Happy {{topic}} coding!

*Template variables to replace: {{tutorial_title}}, {{subtitle}}, {{topic}}, {{brief_description}}, {{features}}, {{install_command}}, {{verify_command}}, {{language}}, {{highlight_lines}}, {{first_example_code}}, {{step_1}}, {{step_2}}, {{step_3}}, {{your_name}}, {{presentation_date}}*