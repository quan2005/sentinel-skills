---
title: "紧凑演示文稿"
theme: "default"
background: "#0f172a"
colorSchema: "dark"
author: "Presenter"
date: "{{date}}"
info: |
  极致紧凑的专业演示文稿模板
  专为信息密集型技术演示设计
layout: intro
---

# {{title}}

## {{subtitle}}

<div class="grid grid-cols-4 gap-2 mt-8 text-xs">
<div class="p-2 bg-blue-900/30 rounded">
{{feature_1_title}}<br/>{{feature_1_desc}}
</div>
<div class="p-2 bg-green-900/30 rounded">
{{feature_2_title}}<br/>{{feature_2_desc}}
</div>
<div class="p-2 bg-purple-900/30 rounded">
{{feature_3_title}}<br/>{{feature_3_desc}}
</div>
<div class="p-2 bg-orange-900/30 rounded">
{{feature_4_title}}<br/>{{feature_4_desc}}
</div>
</div>

<div class="text-xs text-gray-400 mt-4">{{author}} • {{date}} • 极致紧凑版</div>

---

## 项目架构全景

<div class="grid grid-cols-3 gap-1">
<div class="col-span-2">
```mermaid
{{mermaid_diagram}}
```
</div>
<div class="space-y-2 text-xs">
{{architecture_cards}}
</div>
</div>

---

## 技术栈详解

<div class="grid grid-cols-4 gap-2 text-xs">
{{tech_stack_content}}
</div>

---

## 核心功能解析

<div class="grid grid-cols-3 gap-2 text-xs">
{{core_content_sections}}
</div>

---

## 代码示例展示

<div class="grid grid-cols-2 gap-2">
<div class="p-2 bg-gray-900/50 rounded">
<h4 class="text-sm font-bold mb-1 text-blue-300">🔧 核心实现</h4>
<pre class="text-[9px] bg-black/60 p-2 rounded overflow-auto max-h-48"><code>{{code_example_1}}</code></pre>
</div>
<div class="p-2 bg-gray-900/50 rounded">
<h4 class="text-sm font-bold mb-1 text-green-300">⚙️ 配置示例</h4>
<pre class="text-[9px] bg-black/60 p-2 rounded overflow-auto max-h-48"><code>{{code_example_2}}</code></pre>
</div>
</div>

---

## 性能测试数据

<div class="grid grid-cols-4 gap-2 text-xs">
<div class="space-y-2">
<div class="p-2 bg-blue-900/40 rounded text-center">
<div class="text-2xl font-bold text-blue-300">{{metric_1_value}}</div>
<div class="text-blue-200">{{metric_1_label}}</div>
<div class="text-gray-400">{{metric_1_desc}}</div>
</div>
<div class="p-2 bg-green-900/40 rounded text-center">
<div class="text-2xl font-bold text-green-300">{{metric_2_value}}</div>
<div class="text-green-200">{{metric_2_label}}</div>
<div class="text-gray-400">{{metric_2_desc}}</div>
</div>
</div>
<div class="space-y-2">
<div class="p-2 bg-purple-900/40 rounded text-center">
<div class="text-2xl font-bold text-purple-300">{{metric_3_value}}</div>
<div class="text-purple-200">{{metric_3_label}}</div>
<div class="text-gray-400">{{metric_3_desc}}</div>
</div>
<div class="p-2 bg-orange-900/40 rounded text-center">
<div class="text-2xl font-bold text-orange-300">{{metric_4_value}}</div>
<div class="text-orange-200">{{metric_4_label}}</div>
<div class="text-gray-400">{{metric_4_desc}}</div>
</div>
</div>
<div class="col-span-2 space-y-2">
<div class="p-2 bg-gray-900/50 rounded">
<h4 class="font-bold text-yellow-300 mb-1">⚡ 效率对比分析</h4>
{{comparison_data}}
</div>
<div class="p-2 bg-gray-900/50 rounded">
<h4 class="font-bold text-cyan-300 mb-1">🎯 质量指标</h4>
{{quality_metrics}}
</div>
</div>
</div>

---

## 开发工作流程

<div class="grid grid-cols-4 gap-2">
{{workflow_sections}}
</div>

---

## 核心优势与创新点

<div class="grid grid-cols-3 gap-2 text-xs">
{{advantages_sections}}
</div>

---

## 使用示例实战

<div class="grid grid-cols-2 gap-2 text-xs">
{{use_case_examples}}
</div>

---

## 社区生态建设

<div class="grid grid-cols-3 gap-2 text-xs">
{{community_content}}
</div>

---

## 技术栈总览

<div class="grid grid-cols-5 gap-1 text-xs text-center">
{{technology_stack}}
</div>

---

## 未来发展规划

<div class="grid grid-cols-4 gap-2 text-xs">
{{roadmap_content}}
</div>

---

## 核心收获总结

<div class="grid grid-cols-4 gap-2 text-xs">
{{takeaways_content}}
</div>

---

# 🎉 演示结束

<div class="grid grid-cols-3 gap-4 mt-8 text-xs">
{{closing_content}}
</div>

<div class="text-center mt-6 text-xs text-gray-400">
{{project_stats}}
</div>

<div class="text-center mt-4 text-xs text-gray-500">
{{footer_text}}
</div>

<style>
.slidev-layout {
  font-family: 'JetBrains Mono', 'Fira Code', monospace;
}

.tech-highlight {
  background: linear-gradient(135deg, #7c3aed 0%, #a855f7 100%);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
  font-weight: 600;
}

.code-block {
  background: #0f172a;
  border-radius: 6px;
  padding: 12px;
  font-size: 11px;
  line-height: 1.4;
  overflow-x: auto;
  border: 1px solid #1e293b;
}

.diagram-container {
  margin: 12px 0;
  text-align: center;
}

.grid {
  display: grid;
  gap: 0.5rem;
}

.grid-cols-1 { grid-template-columns: repeat(1, minmax(0, 1fr)); }
.grid-cols-2 { grid-template-columns: repeat(2, minmax(0, 1fr)); }
.grid-cols-3 { grid-template-columns: repeat(3, minmax(0, 1fr)); }
.grid-cols-4 { grid-template-columns: repeat(4, minmax(0, 1fr)); }
.grid-cols-5 { grid-template-columns: repeat(5, minmax(0, 1fr)); }

.col-span-2 { grid-column: span 2 / span 2; }
.col-span-3 { grid-column: span 3 / span 3; }

.bg-blue-900\/30 { background-color: rgba(30, 58, 138, 0.3); }
.bg-blue-900\/40 { background-color: rgba(30, 58, 138, 0.4); }
.bg-blue-900\/50 { background-color: rgba(30, 58, 138, 0.5); }
.bg-green-900\/30 { background-color: rgba(20, 83, 45, 0.3); }
.bg-green-900\/40 { background-color: rgba(20, 83, 45, 0.4); }
.bg-green-900\/50 { background-color: rgba(20, 83, 45, 0.5); }
.bg-purple-900\/30 { background-color: rgba(91, 33, 182, 0.3); }
.bg-purple-900\/40 { background-color: rgba(91, 33, 182, 0.4); }
.bg-purple-900\/50 { background-color: rgba(91, 33, 182, 0.5); }
.bg-orange-900\/30 { background-color: rgba(154, 52, 18, 0.3); }
.bg-orange-900\/40 { background-color: rgba(154, 52, 18, 0.4); }
.bg-orange-900\/50 { background-color: rgba(154, 52, 18, 0.5); }
.bg-cyan-900\/40 { background-color: rgba(22, 78, 99, 0.4); }
.bg-cyan-900\/50 { background-color: rgba(22, 78, 99, 0.5); }
.bg-pink-900\/40 { background-color: rgba(131, 24, 67, 0.4); }
.bg-pink-900\/50 { background-color: rgba(131, 24, 67, 0.5); }
.bg-red-900\/40 { background-color: rgba(127, 29, 29, 0.4); }
.bg-yellow-900\/40 { background-color: rgba(146, 64, 14, 0.4); }

.bg-gray-900\/30 { background-color: rgba(17, 24, 39, 0.3); }
.bg-gray-900\/40 { background-color: rgba(17, 24, 39, 0.4); }
.bg-gray-900\/50 { background-color: rgba(17, 24, 39, 0.5); }
.bg-black\/30 { background-color: rgba(0, 0, 0, 0.3); }
.bg-black\/40 { background-color: rgba(0, 0, 0, 0.4); }
.bg-black\/60 { background-color: rgba(0, 0, 0, 0.6); }

.border-l-2 { border-left-width: 2px; }
.border-l-4 { border-left-width: 4px; }

.border-blue-400 { border-color: rgb(96, 165, 250); }
.border-green-400 { border-color: rgb(74, 222, 128); }
.border-purple-400 { border-color: rgb(196, 181, 253); }
.border-orange-400 { border-color: rgb(251, 146, 60); }

.rounded { border-radius: 0.375rem; }
.rounded-lg { border-radius: 0.5rem; }

.p-1 { padding: 0.25rem; }
.p-2 { padding: 0.5rem; }
.p-3 { padding: 0.75rem; }
.p-4 { padding: 1rem; }
.p-6 { padding: 1.5rem; }

.mt-1 { margin-top: 0.25rem; }
.mt-2 { margin-top: 0.5rem; }
.mt-4 { margin-top: 1rem; }
.mt-6 { margin-top: 1.5rem; }
.mt-8 { margin-top: 2rem; }

.mb-1 { margin-bottom: 0.25rem; }
.mb-2 { margin-bottom: 0.5rem; }

.space-y-1 > :not([hidden]) ~ :not([hidden]) { margin-top: 0.25rem; }
.space-y-2 > :not([hidden]) ~ :not([hidden]) { margin-top: 0.5rem; }

.gap-1 { gap: 0.25rem; }
.gap-2 { gap: 0.5rem; }
.gap-4 { gap: 1rem; }

.max-h-48 { max-height: 12rem; }
.max-w-2xl { max-width: 42rem; }

.overflow-auto { overflow: auto; }
.overflow-hidden { overflow: hidden; }

.text-xs { font-size: 0.75rem; line-height: 1rem; }
.text-sm { font-size: 0.875rem; line-height: 1.25rem; }
.text-lg { font-size: 1.125rem; line-height: 1.75rem; }
.text-xl { font-size: 1.25rem; line-height: 1.75rem; }
.text-2xl { font-size: 1.5rem; line-height: 2rem; }

.font-bold { font-weight: 700; }

.text-blue-200 { color: rgb(191, 219, 254); }
.text-blue-300 { color: rgb(147, 197, 253); }
.text-blue-400 { color: rgb(96, 165, 250); }
.text-green-200 { color: rgb(187, 247, 208); }
.text-green-300 { color: rgb(134, 239, 172); }
.text-green-400 { color: rgb(74, 222, 128); }
.text-purple-200 { color: rgb(216, 180, 254); }
.text-purple-300 { color: rgb(196, 181, 253); }
.text-purple-400 { color: rgb(167, 139, 250); }
.text-orange-200 { color: rgb(254, 215, 170); }
.text-orange-300 { color: rgb(253, 186, 116); }
.text-orange-400 { color: rgb(251, 146, 60); }
.text-cyan-200 { color: rgb(165, 243, 252); }
.text-cyan-300 { color: rgb(103, 232, 249); }
.text-cyan-400 { color: rgb(34, 211, 238); }
.text-pink-200 { color: rgb(251, 207, 232); }
.text-pink-300 { color: rgb(249, 168, 212); }
.text-pink-400 { color: rgb(244, 114, 182); }
.text-red-300 { color: rgb(252, 165, 165); }
.text-yellow-200 { color: rgb(254, 240, 138); }
.text-yellow-300 { color: rgb(253, 224, 71); }
.text-gray-300 { color: rgb(209, 213, 219); }
.text-gray-400 { color: rgb(156, 163, 175); }
.text-gray-500 { color: rgb(107, 114, 128); }

.text-center { text-align: center; }

.bg-transparent { background-color: transparent; }
</style>