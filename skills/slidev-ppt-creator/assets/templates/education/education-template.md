---
theme: seriph
background: https://source.unsplash.com/collection/94734566/1920x1080
class: text-center
highlighter: shiki
lineNumbers: false
info: |
  ## Educational Presentation Template
  This template is designed for educational content and training sessions.
  Features interactive elements, clear learning objectives, and engaging layouts.
---

# Education Presentation Title

<div class="pt-12">
  <span class="px-2 py-1 rounded bg-teal-500 text-white">Educational Content</span>
</div>

<div class="pt-2">
  <span v-click>Course Name/Topic</span>
</div>

<div class="abs-br m-6 flex gap-2">
  <span v-click class="text-xl">🎯 Learning Focused</span>
</div>

---
layout: two-cols
---

# Learning Objectives

<div class="grid grid-cols-1 gap-4">
  <div v-click v-for="objective in objectives" class="bg-blue-50 border-l-4 border-blue-500 p-4 rounded">
    <div class="flex items-center">
      <span class="text-2xl mr-3">🎯</span>
      <div>
        <div class="font-semibold">{{ objective.title }}</div>
        <div class="text-sm text-gray-600">{{ objective.description }}</div>
      </div>
    </div>
  </div>
</div>

<style>
.objectives {
  display: grid;
  gap: 1rem;
}
</style>

# Target Audience

<div class="bg-purple-50 border-l-4 border-purple-500 p-6 rounded-lg">
  <div class="flex items-center mb-4">
    <span class="text-3xl mr-3">👥</span>
    <div class="font-semibold text-xl">Who This is For</div>
  </div>

  <div class="grid grid-cols-2 gap-4">
    <div v-for="audience in targetAudience" class="bg-white p-3 rounded border">
      <div class="font-medium">{{ audience.role }}</div>
      <div class="text-sm text-gray-600">{{ audience.background }}</div>
    </div>
  </div>
</div>

---
layout: two-cols
---

# Course Overview

<Timeline :events="courseTimeline" class="h-96" />

## Key Topics

<div v-click class="space-y-3">
  <div v-for="topic in keyTopics" class="flex items-start">
    <span class="text-xl mr-3 mt-1">{{ topic.icon }}</span>
    <div>
      <div class="font-semibold">{{ topic.title }}</div>
      <div class="text-sm text-gray-600">{{ topic.description }}</div>
      <div class="mt-1">
        <span v-for="tag in topic.tags" class="inline-block bg-gray-100 text-gray-700 px-2 py-1 rounded text-xs mr-1">
          {{ tag }}
        </span>
      </div>
    </div>
  </div>
</div>

---
layout: section
---

# Module 1: Introduction

<div class="text-center">
  <div class="text-6xl mb-4">📚</div>
  <div class="text-xl">Building the Foundation</div>
</div>

---
layout: default
---

# What is [Concept Name]?

<div class="grid grid-cols-2 gap-8">
  <div>
    <div class="bg-green-50 border-l-4 border-green-500 p-6 rounded">
      <div class="font-semibold text-lg mb-3">📖 Formal Definition</div>
      <div class="text-gray-700">{{ formalDefinition }}</div>
    </div>
  </div>

  <div>
    <div class="bg-yellow-50 border-l-4 border-yellow-500 p-6 rounded">
      <div class="font-semibold text-lg mb-3">💡 Simple Explanation</div>
      <div class="text-gray-700">{{ simpleExplanation }}</div>
    </div>
  </div>
</div>

<div v-click class="mt-6 bg-blue-50 p-6 rounded-lg">
  <div class="font-semibold text-lg mb-3">🎯 Why It Matters</div>
  <div class="text-gray-700">{{ importance }}</div>
</div>

---
layout: two-cols
---

# Key Concepts

<div class="space-y-4">
  <div v-for="concept in keyConcepts" v-click class="bg-gray-50 p-4 rounded-lg border">
    <div class="flex items-center mb-2">
      <span class="text-xl mr-2">{{ concept.icon }}</span>
      <span class="font-semibold">{{ concept.name }}</span>
    </div>
    <div class="text-sm text-gray-600">{{ concept.description }}</div>
  </div>
</div>

# Visual Representation

<div class="bg-purple-50 p-6 rounded-lg">
  <ConceptDiagram :concept="mainConcept" class="h-80" />
</div>

<div v-click class="mt-4 text-center">
  <div class="inline-block bg-blue-100 text-blue-800 px-4 py-2 rounded-full">
    💭 Think about how this relates to your experience
  </div>
</div>

---
layout: section
---

# Module 2: Core Concepts

<div class="text-center">
  <div class="text-6xl mb-4">🧩</div>
  <div class="text-xl">Understanding the Building Blocks</div>
</div>

---
layout: default
---

# Core Principle: [Principle Name]

<div class="grid grid-cols-3 gap-4 mb-6">
  <div class="bg-blue-100 p-4 rounded-lg text-center">
    <div class="text-2xl mb-2">🔍</div>
    <div class="font-semibold">Observe</div>
    <div class="text-sm">{{ observationStep }}</div>
  </div>

  <div class="bg-green-100 p-4 rounded-lg text-center">
    <div class="text-2xl mb-2">🤔</div>
    <div class="font-semibold">Analyze</div>
    <div class="text-sm">{{ analysisStep }}</div>
  </div>

  <div class="bg-purple-100 p-4 rounded-lg text-center">
    <div class="text-2xl mb-2">🛠️</div>
    <div class="font-semibold">Apply</div>
    <div class="text-sm">{{ applicationStep }}</div>
  </div>
</div>

<div v-click class="bg-yellow-50 border-l-4 border-yellow-500 p-4 rounded">
  <div class="font-semibold">💡 Key Insight</div>
  <div>{{ keyInsight }}</div>
</div>

---
layout: two-cols
---

# Real-World Examples

<div class="space-y-4">
  <div v-for="example in examples" v-click class="bg-white border p-4 rounded-lg shadow">
    <div class="font-semibold mb-2">📌 {{ example.title }}</div>
    <div class="text-sm text-gray-600 mb-2">{{ example.description }}</div>
    <div class="bg-gray-50 p-3 rounded text-xs">
      <strong>Key Takeaway:</strong> {{ example.takeaway }}
    </div>
  </div>
</div>

# Interactive Element

<div class="bg-indigo-50 p-6 rounded-lg">
  <div class="font-semibold text-lg mb-4">🎮 Quick Exercise</div>

  <div class="mb-4">{{ exerciseQuestion }}</div>

  <div v-click class="space-y-2">
    <div v-for="option in exerciseOptions" class="bg-white p-3 rounded border cursor-pointer hover:bg-blue-50">
      {{ option }}
    </div>
  </div>
</div>

---
layout: section
---

# Module 3: Practical Application

<div class="text-center">
  <div class="text-6xl mb-4">🛠️</div>
  <div class="text-xl">Hands-On Learning</div>
</div>

---
layout: default
---

# Step-by-Step Guide

<div class="space-y-6">
  <div v-for="(step, index) in steps" v-click class="flex items-start">
    <div class="bg-blue-500 text-white rounded-full w-8 h-8 flex items-center justify-center font-bold mr-4 flex-shrink-0">
      {{ index + 1 }}
    </div>
    <div class="flex-grow">
      <div class="bg-gray-50 p-4 rounded-lg">
        <div class="font-semibold mb-2">{{ step.title }}</div>
        <div class="text-sm text-gray-600 mb-2">{{ step.description }}</div>

        <div v-if="step.code" class="bg-gray-900 text-green-400 p-3 rounded text-sm font-mono">
          {{ step.code }}
        </div>

        <div v-if="step.tip" class="mt-2 bg-yellow-50 border-l-4 border-yellow-500 p-2 text-xs">
          💡 {{ step.tip }}
        </div>
      </div>
    </div>
  </div>
</div>

---
layout: default
---

# Common Pitfalls & Solutions

<div class="space-y-4">
  <div v-for="pitfall in pitfalls" v-click class="bg-red-50 border-l-4 border-red-500 p-4 rounded">
    <div class="flex items-center mb-2">
      <span class="text-xl mr-2">⚠️</span>
      <span class="font-semibold">Pitfall: {{ pitfall.problem }}</span>
    </div>

    <div class="text-sm text-gray-600 mb-2">{{ pitfall.description }}</div>

    <div class="bg-green-50 p-3 rounded">
      <div class="font-medium text-green-800 mb-1">✅ Solution:</div>
      <div class="text-sm">{{ pitfall.solution }}</div>
    </div>
  </div>
</div>

---
layout: section
---

# Module 4: Assessment

<div class="text-center">
  <div class="text-6xl mb-4">📝</div>
  <div class="text-xl">Testing Your Knowledge</div>
</div>

---
layout: default
---

# Knowledge Check

<div class="space-y-6">
  <div v-for="(question, qIndex) in questions" v-click class="bg-blue-50 p-6 rounded-lg">
    <div class="font-semibold mb-4">Question {{ qIndex + 1 }}: {{ question.text }}</div>

    <div class="space-y-2">
      <div v-for="(option, oIndex) in question.options" class="bg-white p-3 rounded border cursor-pointer hover:bg-gray-50">
        <div class="flex items-center">
          <span class="bg-gray-200 rounded-full w-6 h-6 flex items-center justify-center text-sm mr-3">
            {{ String.fromCharCode(65 + oIndex) }}
          </span>
          {{ option }}
        </div>
      </div>
    </div>
  </div>
</div>

---
layout: default
---

# Practical Exercise

<div class="bg-green-50 p-6 rounded-lg">
  <div class="font-semibold text-lg mb-4">🎯 Hands-On Challenge</div>

  <div class="mb-4">{{ exerciseDescription }}</div>

  <div class="bg-white p-4 rounded border">
    <div class="font-medium mb-2">Requirements:</div>
    <ul class="list-disc list-inside text-sm space-y-1">
      <li v-for="requirement in requirements">{{ requirement }}</li>
    </ul>
  </div>

  <div v-click class="mt-4 bg-blue-50 p-4 rounded">
    <div class="font-medium">💡 Hint:</div>
    <div class="text-sm">{{ hint }}</div>
  </div>
</div>

---
layout: section
---

# Summary & Next Steps

<div class="text-center">
  <div class="text-6xl mb-4">🎉</div>
  <div class="text-xl">Congratulations!</div>
</div>

---
layout: default
---

# What We've Learned

<div class="grid grid-cols-2 gap-6">
  <div>
    <div class="font-semibold text-lg mb-4">📚 Key Concepts</div>
    <div class="space-y-2">
      <div v-for="concept in learnedConcepts" v-click class="flex items-center">
        <span class="text-green-500 mr-2">✓</span>
        {{ concept }}
      </div>
    </div>
  </div>

  <div>
    <div class="font-semibold text-lg mb-4">🛠️ Skills Acquired</div>
    <div class="space-y-2">
      <div v-for="skill in acquiredSkills" v-click class="flex items-center">
        <span class="text-green-500 mr-2">✓</span>
        {{ skill }}
      </div>
    </div>
  </div>
</div>

---
layout: default
---

# Continue Your Learning Journey

<div class="bg-gradient-to-r from-blue-50 to-purple-50 p-6 rounded-lg">
  <div class="font-semibold text-lg mb-4">🚀 Where to Go From Here</div>

  <div class="grid grid-cols-3 gap-4">
    <div v-for="resource in nextSteps" class="bg-white p-4 rounded-lg text-center">
      <div class="text-2xl mb-2">{{ resource.icon }}</div>
      <div class="font-medium">{{ resource.title }}</div>
      <div class="text-sm text-gray-600">{{ resource.description }}</div>
    </div>
  </div>
</div>

<div class="mt-6 text-center">
  <div v-click class="inline-block bg-gradient-to-r from-blue-500 to-purple-500 text-white px-6 py-3 rounded-full">
    🎯 Ready for the next challenge!
  </div>
</div>

---
layout: end
---

# Thank You!

<div class="text-center">
  <div class="text-6xl mb-4">🙏</div>
  <div class="text-2xl mb-4">Questions & Discussion</div>

  <div class="text-gray-600">
    <div>📧 Email: instructor@example.com</div>
    <div>💬 Course Community: join.slack.com/learning</div>
    <div>📚 Resources: course.example.com/resources</div>
  </div>

  <div class="mt-8">
    <div v-click class="inline-block bg-blue-100 text-blue-800 px-4 py-2 rounded-full">
      📝 Don't forget to complete your feedback form!
    </div>
  </div>
</div>