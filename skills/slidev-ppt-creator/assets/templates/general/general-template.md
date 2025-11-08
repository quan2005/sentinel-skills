---
theme: seriph
background: https://source.unsplash.com/collection/94734566/1920x1080
class: text-center
highlighter: shiki
lineNumbers: false
info: |
  ## General Presentation Template
  A versatile template suitable for various presentation types.
  Clean, professional, and adaptable to different content needs.
---

# Presentation Title

<div class="pt-12">
  <span class="px-2 py-1 rounded bg-blue-500 text-white">General Purpose</span>
</div>

<div class="pt-2">
  <span v-click>Subtitle or Tagline</span>
</div>

<div class="abs-br m-6 flex gap-2">
  <span v-click class="text-xl">📊 Professional Content</span>
</div>

---
layout: section
---

# Introduction

<div class="text-center">
  <div class="text-6xl mb-4">👋</div>
  <div class="text-xl">Setting the Stage</div>
</div>

---
layout: default
---

# About This Presentation

<div class="grid grid-cols-1 gap-6">
  <div class="bg-blue-50 border-l-4 border-blue-500 p-6 rounded">
    <div class="flex items-center mb-3">
      <span class="text-2xl mr-3">🎯</span>
      <div class="font-semibold text-lg">Purpose</div>
    </div>
    <div class="text-gray-700">{{ presentationPurpose }}</div>
  </div>

  <div class="bg-green-50 border-l-4 border-green-500 p-6 rounded">
    <div class="flex items-center mb-3">
      <span class="text-2xl mr-3">👥</span>
      <div class="font-semibold text-lg">Audience</div>
    </div>
    <div class="text-gray-700">{{ targetAudience }}</div>
  </div>

  <div class="bg-purple-50 border-l-4 border-purple-500 p-6 rounded">
    <div class="flex items-center mb-3">
      <span class="text-2xl mr-3">⏱️</span>
      <div class="font-semibold text-lg">Duration</div>
    </div>
    <div class="text-gray-700">{{ presentationDuration }}</div>
  </div>
</div>

---
layout: default
---

# Agenda

<div class="space-y-4">
  <div v-for="(item, index) in agenda" v-click class="flex items-center bg-gray-50 p-4 rounded-lg">
    <div class="bg-blue-500 text-white rounded-full w-8 h-8 flex items-center justify-center font-bold mr-4">
      {{ index + 1 }}
    </div>
    <div>
      <div class="font-semibold">{{ item.title }}</div>
      <div class="text-sm text-gray-600">{{ item.duration }} - {{ item.description }}</div>
    </div>
  </div>
</div>

---
layout: two-cols
---

# Key Topics

<div class="space-y-4">
  <div v-for="topic in keyTopics" v-click class="bg-white border p-4 rounded-lg shadow">
    <div class="flex items-center mb-2">
      <span class="text-xl mr-2">{{ topic.icon }}</span>
      <span class="font-semibold">{{ topic.title }}</span>
    </div>
    <div class="text-sm text-gray-600">{{ topic.description }}</div>
  </div>
</div>

# Visual Overview

<div class="bg-gradient-to-br from-blue-50 to-purple-50 p-6 rounded-lg">
  <div class="font-semibold text-lg mb-4">📊 Topic Distribution</div>

  <div class="space-y-3">
    <div v-for="section in topicDistribution" class="flex items-center">
      <span class="w-24 text-sm">{{ section.name }}</span>
      <div class="flex-grow bg-gray-200 rounded-full h-6 mr-3">
        <div :style="`width: ${section.percentage}%`" class="bg-blue-500 h-6 rounded-full flex items-center justify-center text-xs text-white">
          {{ section.percentage }}%
        </div>
      </div>
    </div>
  </div>
</div>

---
layout: section
---

# Main Content

<div class="text-center">
  <div class="text-6xl mb-4">📋</div>
  <div class="text-xl">Core Information</div>
</div>

---
layout: default
---

# Topic 1: [Main Subject]

<div class="bg-white border p-6 rounded-lg shadow-lg">
  <div class="grid grid-cols-2 gap-6">
    <div>
      <div class="font-semibold text-lg mb-4">🔍 Overview</div>
      <div class="text-gray-700">{{ topicOverview }}</div>
    </div>

    <div>
      <div class="font-semibold text-lg mb-4">💡 Key Points</div>
      <ul class="list-disc list-inside space-y-2">
        <li v-for="point in keyPoints">{{ point }}</li>
      </ul>
    </div>
  </div>
</div>

<div v-click class="mt-6 bg-yellow-50 border-l-4 border-yellow-500 p-4 rounded">
  <div class="font-semibold">🎯 Important Note</div>
  <div>{{ importantNote }}</div>
</div>

---
layout: two-cols
---

# Supporting Details

<div class="space-y-4">
  <div v-for="detail in supportingDetails" v-click class="bg-gray-50 p-4 rounded-lg">
    <div class="font-medium mb-2">{{ detail.title }}</div>
    <div class="text-sm text-gray-600">{{ detail.content }}</div>

    <div v-if="detail.data" class="mt-2 bg-white p-3 rounded border">
      <div class="text-xs font-mono">{{ detail.data }}</div>
    </div>
  </div>
</div>

# Visual Elements

<div class="bg-purple-50 p-6 rounded-lg">
  <div class="font-semibold text-lg mb-4">📊 Supporting Visualization</div>

  <div class="bg-white p-4 rounded border">
    <ChartComponent :data="chartData" type="bar" />
  </div>

  <div v-click class="mt-4 text-sm text-gray-600 text-center">
    {{ chartCaption }}
  </div>
</div>

---
layout: default
---

# Case Study / Example

<div class="bg-gradient-to-r from-blue-50 to-green-50 p-6 rounded-lg">
  <div class="font-semibold text-lg mb-4">📌 Real-World Example</div>

  <div class="bg-white p-4 rounded border mb-4">
    <div class="font-medium mb-2">{{ caseStudyTitle }}</div>
    <div class="text-sm text-gray-600 mb-3">{{ caseStudyDescription }}</div>

    <div class="grid grid-cols-3 gap-3 text-sm">
      <div class="bg-gray-50 p-2 rounded">
        <div class="font-medium">Challenge</div>
        <div>{{ challenge }}</div>
      </div>
      <div class="bg-gray-50 p-2 rounded">
        <div class="font-medium">Solution</div>
        <div>{{ solution }}</div>
      </div>
      <div class="bg-gray-50 p-2 rounded">
        <div class="font-medium">Result</div>
        <div>{{ result }}</div>
      </div>
    </div>
  </div>

  <div v-click class="bg-blue-50 p-4 rounded">
    <div class="font-medium text-blue-800 mb-1">💡 Key Learning</div>
    <div class="text-sm">{{ keyLearning }}</div>
  </div>
</div>

---
layout: section
---

# Analysis & Insights

<div class="text-center">
  <div class="text-6xl mb-4">🔍</div>
  <div class="text-xl">Deep Dive</div>
</div>

---
layout: default
---

# Data & Metrics

<div class="grid grid-cols-2 gap-6">
  <div>
    <div class="font-semibold text-lg mb-4">📈 Performance Metrics</div>

    <div class="space-y-3">
      <div v-for="metric in metrics" class="bg-gray-50 p-3 rounded">
        <div class="flex justify-between items-center">
          <span class="font-medium">{{ metric.name }}</span>
          <span class="text-2xl font-bold text-blue-600">{{ metric.value }}</span>
        </div>
        <div class="text-sm text-gray-600 mt-1">{{ metric.description }}</div>
      </div>
    </div>
  </div>

  <div>
    <div class="font-semibold text-lg mb-4">📊 Visual Analysis</div>

    <div class="bg-white p-4 rounded border">
      <ChartComponent :data="analyticsData" type="line" />
    </div>
  </div>
</div>

---
layout: two-cols
---

# Key Findings

<div class="space-y-4">
  <div v-for="finding in findings" v-click class="bg-green-50 border-l-4 border-green-500 p-4 rounded">
    <div class="flex items-center mb-2">
      <span class="text-xl mr-2">✅</span>
      <span class="font-semibold">{{ finding.title }}</span>
    </div>
    <div class="text-sm text-gray-600">{{ finding.description }}</div>

    <div v-if="finding.impact" class="mt-2 text-xs bg-green-100 p-2 rounded">
      <strong>Impact:</strong> {{ finding.impact }}
    </div>
  </div>
</div>

# Comparative Analysis

<div class="bg-purple-50 p-6 rounded-lg">
  <div class="font-semibold text-lg mb-4">⚖️ Comparison</div>

  <table class="w-full text-sm">
    <thead>
      <tr class="bg-purple-100">
        <th class="p-2 text-left">Aspect</th>
        <th class="p-2 text-left">Option A</th>
        <th class="p-2 text-left">Option B</th>
      </tr>
    </thead>
    <tbody>
      <tr v-for="row in comparisonData" class="border-b">
        <td class="p-2 font-medium">{{ row.aspect }}</td>
        <td class="p-2">{{ row.optionA }}</td>
        <td class="p-2">{{ row.optionB }}</td>
      </tr>
    </tbody>
  </table>
</div>

---
layout: section
---

# Recommendations

<div class="text-center">
  <div class="text-6xl mb-4">💡</div>
  <div class="text-xl">Actionable Insights</div>
</div>

---
layout: default
---

# Strategic Recommendations

<div class="space-y-6">
  <div v-for="(rec, index) in recommendations" v-click class="bg-gradient-to-r from-blue-50 to-purple-50 p-6 rounded-lg">
    <div class="flex items-start">
      <div class="bg-blue-500 text-white rounded-full w-8 h-8 flex items-center justify-center font-bold mr-4">
        {{ index + 1 }}
      </div>
      <div class="flex-grow">
        <div class="font-semibold text-lg mb-2">{{ rec.title }}</div>
        <div class="text-gray-700 mb-3">{{ rec.description }}</div>

        <div class="grid grid-cols-3 gap-3 text-sm">
          <div class="bg-white p-3 rounded">
            <div class="font-medium text-green-600">Benefit</div>
            <div>{{ rec.benefit }}</div>
          </div>
          <div class="bg-white p-3 rounded">
            <div class="font-medium text-orange-600">Effort</div>
            <div>{{ rec.effort }}</div>
          </div>
          <div class="bg-white p-3 rounded">
            <div class="font-medium text-blue-600">Timeline</div>
            <div>{{ rec.timeline }}</div>
          </div>
        </div>
      </div>
    </div>
  </div>
</div>

---
layout: default
---

# Implementation Roadmap

<div class="bg-gradient-to-br from-green-50 to-blue-50 p-6 rounded-lg">
  <div class="font-semibold text-lg mb-4">🗺️ Next Steps</div>

  <div class="space-y-4">
    <div v-for="(phase, index) in roadmap" v-click class="flex items-center">
      <div class="bg-green-500 text-white rounded-full w-10 h-10 flex items-center justify-center font-bold mr-4">
        {{ index + 1 }}
      </div>
      <div class="flex-grow bg-white p-4 rounded-lg border">
        <div class="flex justify-between items-start">
          <div>
            <div class="font-semibold">{{ phase.name }}</div>
            <div class="text-sm text-gray-600">{{ phase.description }}</div>
          </div>
          <div class="bg-blue-100 text-blue-800 px-2 py-1 rounded text-xs">
            {{ phase.duration }}
          </div>
        </div>

        <div v-if="phase.deliverables" class="mt-2 text-xs">
          <strong>Deliverables:</strong> {{ phase.deliverables }}
        </div>
      </div>
    </div>
  </div>
</div>

---
layout: section
---

# Conclusion

<div class="text-center">
  <div class="text-6xl mb-4">🎯</div>
  <div class="text-xl">Key Takeaways</div>
</div>

---
layout: default
---

# Summary

<div class="grid grid-cols-1 gap-4">
  <div class="bg-blue-50 border-l-4 border-blue-500 p-6 rounded">
    <div class="font-semibold text-lg mb-3">📋 What We Covered</div>
    <ul class="space-y-2">
      <li v-for="item in summaryPoints" class="flex items-center">
        <span class="text-blue-500 mr-2">•</span>
        {{ item }}
      </li>
    </ul>
  </div>

  <div class="bg-green-50 border-l-4 border-green-500 p-6 rounded">
    <div class="font-semibold text-lg mb-3">🎯 Main Takeaways</div>
    <ul class="space-y-2">
      <li v-for="takeaway in mainTakeaways" class="flex items-center">
        <span class="text-green-500 mr-2">✓</span>
        {{ takeaway }}
      </li>
    </ul>
  </div>
</div>

---
layout: default
---

# Call to Action

<div class="bg-gradient-to-r from-purple-500 to-blue-500 text-white p-8 rounded-lg">
  <div class="text-center">
    <div class="text-3xl font-bold mb-4">{{ callToAction.title }}</div>
    <div class="text-xl mb-6">{{ callToAction.message }}</div>

    <div class="grid grid-cols-3 gap-4 mb-6">
      <div v-for="action in callToAction.actions" class="bg-white/20 backdrop-blur p-4 rounded-lg">
        <div class="text-2xl mb-2">{{ action.icon }}</div>
        <div class="font-medium">{{ action.title }}</div>
        <div class="text-sm">{{ action.description }}</div>
      </div>
    </div>

    <div v-click class="inline-block bg-white text-blue-600 px-8 py-3 rounded-full font-semibold">
      {{ callToAction.primaryButton }}
    </div>
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
    <div>📧 Email: contact@example.com</div>
    <div>🌐 Website: www.example.com</div>
    <div>💬 Social: @example</div>
  </div>

  <div class="mt-8">
    <div v-click class="inline-block bg-blue-100 text-blue-800 px-4 py-2 rounded-full">
      📊 Slides available at: slides.example.com/presentation
    </div>
  </div>
</div>