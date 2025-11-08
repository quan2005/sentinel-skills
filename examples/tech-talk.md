---
title: "Advanced JavaScript Patterns"
theme: "seriph"
author: "Tech Speaker"
date: "2024-01-15"
highlighter: "shiki"
lineNumbers: true
---

# Advanced JavaScript Patterns

<div class="pt-12">
  <span @click="$slidev.nav.next" class="px-2 py-1 rounded">
    Start Exploring <carbon:arrow-right class="inline"/>
  </span>
</div>

---

## Overview

1. Async/Await Patterns
2. Functional Programming
3. Performance Optimization
4. Modern ES6+ Features

---

# Async/Await

```js {1|2-4|5-7}
async function fetchUserData(userId) {
  try {
    const response = await fetch(`/api/users/${userId}`)
    const data = await response.json()
    return data
  } catch (error) {
    console.error('Error:', error)
  }
}
```

---

## Functional Programming

::left::

### Pure Functions
- No side effects
- Predictable output
- Easy to test

::right::

```js
const add = (a, b) => a + b
const multiply = (x) => x * 2

// Compose functions
const addAndMultiply = (a, b) =>
  multiply(add(a, b))
```

---

# Thank You!

🚀 Happy coding!