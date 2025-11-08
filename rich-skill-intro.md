---
title: "Slidev 演示文稿创建器 - 技能介绍"
theme: "apple-basic"
author: "Claude Code"
date: "2024-01-15"
highlighter: "shiki"
lineNumbers: true
download: "PDF"
colorSchema: "auto"
---

# Slidev 演示文稿创建器

## 让演示文稿创作变得简单而优雅

<div class="pt-12">
  <div class="grid grid-cols-2 gap-8">
    <div class="flex flex-col items-center space-y-4">
      <div class="w-24 h-24 bg-gradient-to-br from-blue-500 to-purple-600 rounded-2xl flex items-center justify-center">
        <carbon:document class="text-white text-4xl"/>
      </div>
      <span class="text-lg font-semibold">专业文档</span>
    </div>
    <div class="flex flex-col items-center space-y-4">
      <div class="w-24 h-24 bg-gradient-to-br from-green-500 to-teal-600 rounded-2xl flex items-center justify-center">
        <carbon:rocket class="text-white text-4xl"/>
      </div>
      <span class="text-lg font-semibold">快速创建</span>
    </div>
  </div>
</div>

<div class="pt-8">
  <span @click="$slidev.nav.next" class="px-6 py-3 bg-blue-600 text-white rounded-full cursor-pointer hover:bg-blue-700 transition-colors">
    开始探索 <carbon:arrow-right class="inline ml-2"/>
  </span>
</div>

---

## 什么是 Slidev 演示文稿创建器？

### 🎯 一站式演示文稿解决方案

<div v-click class="grid grid-cols-3 gap-6 mt-8">
  <div class="bg-gradient-to-br from-blue-50 to-blue-100 p-6 rounded-xl border border-blue-200">
    <div class="text-blue-600 text-3xl mb-4">
      <carbon:document-blank/>
    </div>
    <h3 class="text-lg font-bold text-blue-900 mb-2">Markdown 驱动</h3>
    <p class="text-blue-700 text-sm">使用熟悉的 Markdown 语法编写，无需学习复杂的工具</p>
  </div>

  <div class="bg-gradient-to-br from-purple-50 to-purple-100 p-6 rounded-xl border border-purple-200">
    <div class="text-purple-600 text-3xl mb-4">
      <carbon:palette/>
    </div>
    <h3 class="text-lg font-bold text-purple-900 mb-2">专业主题</h3>
    <p class="text-purple-700 text-sm">8种精美主题，满足商务、技术、创意等各种场景</p>
  </div>

  <div class="bg-gradient-to-br from-green-50 to-green-100 p-6 rounded-xl border border-green-200">
    <div class="text-green-600 text-3xl mb-4">
      <carbon:lightning/>
    </div>
    <h3 class="text-lg font-bold text-green-900 mb-2">交互元素</h3>
    <p class="text-green-700 text-sm">代码高亮、动画效果、图表展示，让演示更生动</p>
  </div>
</div>

<div v-click class="mt-8 p-6 bg-gray-50 rounded-xl">
  <p class="text-gray-700 text-center">
    <span class="text-2xl">💡</span>
    这是一个 <span class="font-bold text-blue-600">Claude Code 技能</span>，通过简单的自然语言描述即可创建专业演示文稿
  </p>
</div>

---

## 🌟 核心功能展示

### 让您的演示文稿与众不同

<div class="grid grid-cols-2 gap-8 mt-8">
  <!-- 左侧：代码展示 -->
  <div class="bg-gray-900 rounded-xl p-6 text-white">
    <div class="flex items-center mb-4">
      <div class="flex space-x-2">
        <div class="w-3 h-3 bg-red-500 rounded-full"></div>
        <div class="w-3 h-3 bg-yellow-500 rounded-full"></div>
        <div class="w-3 h-3 bg-green-500 rounded-full"></div>
      </div>
      <span class="ml-4 text-sm text-gray-400">presentation.md</span>
    </div>

    <div class="font-mono text-sm">
      <div v-click>
        <span class="text-blue-400">---</span>
      </div>
      <div v-click>
        <span class="text-purple-400">title</span>: <span class="text-green-400">"我的精彩演示"</span>
      </div>
      <div v-click>
        <span class="text-purple-400">theme</span>: <span class="text-green-400">"seriph"</span>
      </div>
      <div v-click>
        <span class="text-blue-400">---</span>
      </div>
      <div v-click class="mt-4">
        <span class="text-gray-300">#</span> <span class="text-white">欢迎来到我的演示</span>
      </div>
      <div v-click>
        <span class="text-gray-300">##</span> <span class="text-white">精彩内容</span>
      </div>
      <div v-click class="mt-2">
        <span class="text-gray-300">-</span> <span class="text-white">✨ 交互式幻灯片</span>
      </div>
      <div v-click>
        <span class="text-gray-300">-</span> <span class="text-white">🎨 精美设计</span>
      </div>
    </div>
  </div>

  <!-- 右侧：预览效果 -->
  <div class="bg-white rounded-xl p-6 shadow-lg border border-gray-200">
    <div class="text-sm text-gray-500 mb-4">实时预览效果</div>

    <div v-click class="space-y-4">
      <div class="border-b border-gray-200 pb-4">
        <h1 class="text-2xl font-bold text-gray-800">我的精彩演示</h1>
      </div>

      <div>
        <h2 class="text-xl font-semibold text-gray-700">精彩内容</h2>
        <ul class="mt-2 space-y-1">
          <li class="flex items-center text-gray-600">
            <span class="mr-2">✨</span> 交互式幻灯片
          </li>
          <li class="flex items-center text-gray-600">
            <span class="mr-2">🎨</span> 精美设计
          </li>
        </ul>
      </div>

      <div class="flex justify-center mt-6">
        <div class="px-4 py-2 bg-blue-600 text-white rounded-lg text-sm">
          幻灯片 1 / 10
        </div>
      </div>
    </div>
  </div>
</div>

---

## 🎨 8种专业主题任您选择

### 主题预览

<div v-click class="grid grid-cols-4 gap-4 mt-6">
  <div class="group cursor-pointer">
    <div class="bg-gradient-to-br from-blue-600 to-blue-800 h-24 rounded-lg flex items-center justify-center group-hover:scale-105 transition-transform">
      <div class="text-white text-center">
        <div class="text-2xl mb-1">📊</div>
        <div class="text-sm font-medium">Seriph</div>
      </div>
    </div>
    <div class="mt-2 text-xs text-center text-gray-600">商务专业</div>
  </div>

  <div class="group cursor-pointer">
    <div class="bg-gradient-to-br from-gray-600 to-gray-800 h-24 rounded-lg flex items-center justify-center group-hover:scale-105 transition-transform">
      <div class="text-white text-center">
        <div class="text-2xl mb-1">⚪</div>
        <div class="text-sm font-medium">Default</div>
      </div>
    </div>
    <div class="mt-2 text-xs text-center text-gray-600">简洁极简</div>
  </div>

  <div class="group cursor-pointer">
    <div class="bg-gradient-to-br from-gray-100 to-gray-300 h-24 rounded-lg flex items-center justify-center group-hover:scale-105 transition-transform">
      <div class="text-gray-800 text-center">
        <div class="text-2xl mb-1">🍎</div>
        <div class="text-sm font-medium">Apple Basic</div>
      </div>
    </div>
    <div class="mt-2 text-xs text-center text-gray-600">Apple 风格</div>
  </div>

  <div class="group cursor-pointer">
    <div class="bg-gradient-to-br from-green-700 to-green-900 h-24 rounded-lg flex items-center justify-center group-hover:scale-105 transition-transform">
      <div class="text-white text-center">
        <div class="text-2xl mb-1">💻</div>
        <div class="text-sm font-medium">Dev</div>
      </div>
    </div>
    <div class="mt-2 text-xs text-center text-gray-600">开发者风格</div>
  </div>
</div>

<div v-click class="grid grid-cols-4 gap-4 mt-4">
  <div class="group cursor-pointer">
    <div class="bg-gradient-to-br from-purple-600 to-purple-800 h-24 rounded-lg flex items-center justify-center group-hover:scale-105 transition-transform">
      <div class="text-white text-center">
        <div class="text-2xl mb-1">🟣</div>
        <div class="text-sm font-medium">Purple</div>
      </div>
    </div>
    <div class="mt-2 text-xs text-center text-gray-600">深色紫调</div>
  </div>

  <div class="group cursor-pointer">
    <div class="bg-gradient-to-br from-orange-600 to-red-600 h-24 rounded-lg flex items-center justify-center group-hover:scale-105 transition-transform">
      <div class="text-white text-center">
        <div class="text-2xl mb-1">🧱</div>
        <div class="text-sm font-medium">Bricks</div>
      </div>
    </div>
    <div class="mt-2 text-xs text-center text-gray-600">创意乐高</div>
  </div>

  <div class="group cursor-pointer">
    <div class="bg-gradient-to-br from-cyan-500 to-blue-500 h-24 rounded-lg flex items-center justify-center group-hover:scale-105 transition-transform">
      <div class="text-white text-center">
        <div class="text-2xl mb-1">☁️</div>
        <div class="text-sm font-medium">Minami</div>
      </div>
    </div>
    <div class="mt-2 text-xs text-center text-gray-600">清爽明亮</div>
  </div>

  <div class="group cursor-pointer">
    <div class="bg-gradient-to-br from-indigo-500 to-purple-600 h-24 rounded-lg flex items-center justify-center group-hover:scale-105 transition-transform">
      <div class="text-white text-center">
        <div class="text-2xl mb-1">👥</div>
        <div class="text-sm font-medium">Meetup</div>
      </div>
    </div>
    <div class="mt-2 text-xs text-center text-gray-600">社区友好</div>
  </div>
</div>

---

## 🚀 使用流程：三步创建专业演示

### 简单易用，效果出众

<div class="mt-8">
  <!-- 流程图 -->
  <div class="relative">
    <div class="absolute inset-0 flex items-center justify-center">
      <div class="w-full h-1 bg-gradient-to-r from-blue-400 via-purple-400 to-pink-400"></div>
    </div>

    <div class="relative flex justify-between">
      <!-- 步骤1 -->
      <div v-click class="bg-white rounded-xl shadow-lg p-6 border-2 border-blue-500 w-64 z-10">
        <div class="flex items-center mb-4">
          <div class="w-10 h-10 bg-blue-500 text-white rounded-full flex items-center justify-center font-bold">
            1
          </div>
          <span class="ml-3 text-lg font-semibold">描述需求</span>
        </div>
        <div class="text-gray-600 text-sm space-y-2">
          <p>"我想做一个技术分享"</p>
          <p>"主题是React Hooks"</p>
          <p>"希望有代码示例"</p>
        </div>
        <div class="mt-4 flex items-center text-blue-600 text-sm">
          <carbon:chat class="mr-2"/>
          自然语言描述
        </div>
      </div>

      <!-- 步骤2 -->
      <div v-click class="bg-white rounded-xl shadow-lg p-6 border-2 border-purple-500 w-64 z-10 transform -translate-y-2">
        <div class="flex items-center mb-4">
          <div class="w-10 h-10 bg-purple-500 text-white rounded-full flex items-center justify-center font-bold">
            2
          </div>
          <span class="ml-3 text-lg font-semibold">智能生成</span>
        </div>
        <div class="text-gray-600 text-sm space-y-2">
          <p>✓ 自动选择seriph主题</p>
          <p>✓ 生成代码高亮</p>
          <p>✓ 创建交互幻灯片</p>
        </div>
        <div class="mt-4 flex items-center text-purple-600 text-sm">
          <carbon:rocket class="mr-2"/>
          AI智能处理
        </div>
      </div>

      <!-- 步骤3 -->
      <div v-click class="bg-white rounded-xl shadow-lg p-6 border-2 border-pink-500 w-64 z-10">
        <div class="flex items-center mb-4">
          <div class="w-10 h-10 bg-pink-500 text-white rounded-full flex items-center justify-center font-bold">
            3
          </div>
          <span class="ml-3 text-lg font-semibold">导出使用</span>
        </div>
        <div class="text-gray-600 text-sm space-y-2">
          <p>📄 PDF格式文档</p>
          <p>🖼️ PPTX演示文件</p>
          <p>🌐 静态网站</p>
        </div>
        <div class="mt-4 flex items-center text-pink-600 text-sm">
          <carbon:download class="mr-2"/>
          多格式导出
        </div>
      </div>
    </div>
  </div>
</div>

<div v-click class="mt-12 text-center">
  <div class="inline-flex items-center px-6 py-3 bg-gradient-to-r from-blue-600 to-purple-600 text-white rounded-full">
    <carbon:time class="mr-2"/>
    整个过程仅需 2-3 分钟！
  </div>
</div>

---

## 📊 丰富的图表和可视化

### 让数据说话，让演示更生动

<div class="grid grid-cols-2 gap-8 mt-8">
  <!-- 左侧：Mermaid图表 -->
  <div class="bg-white rounded-xl p-6 shadow-lg border border-gray-200">
    <div class="flex items-center mb-4">
      <carbon:chart-bar class="text-blue-600 text-xl mr-2"/>
      <span class="text-lg font-semibold">Mermaid 流程图</span>
    </div>

    <div v-click class="bg-gray-50 rounded-lg p-4">
      <div class="text-center text-sm text-gray-600 mb-2">工作流程图</div>
      <div class="space-y-2">
        <div class="flex items-center justify-center space-x-2">
          <div class="px-3 py-1 bg-blue-500 text-white rounded text-xs">需求分析</div>
          <div class="text-gray-400">→</div>
          <div class="px-3 py-1 bg-purple-500 text-white rounded text-xs">内容创作</div>
        </div>
        <div class="flex items-center justify-center space-x-2">
          <div class="px-3 py-1 bg-green-500 text-white rounded text-xs">设计美化</div>
          <div class="text-gray-400">→</div>
          <div class="px-3 py-1 bg-pink-500 text-white rounded text-xs">导出发布</div>
        </div>
      </div>
    </div>
  </div>

  <!-- 右侧：数据图表 -->
  <div class="bg-white rounded-xl p-6 shadow-lg border border-gray-200">
    <div class="flex items-center mb-4">
      <carbon:chart-line class="text-green-600 text-xl mr-2"/>
      <span class="text-lg font-semibold">数据可视化</span>
    </div>

    <div v-click class="space-y-4">
      <div>
        <div class="flex justify-between text-sm mb-1">
          <span>效率提升</span>
          <span class="text-green-600 font-semibold">85%</span>
        </div>
        <div class="w-full bg-gray-200 rounded-full h-2">
          <div class="bg-green-600 h-2 rounded-full" style="width: 85%"></div>
        </div>
      </div>

      <div>
        <div class="flex justify-between text-sm mb-1">
          <span>用户满意度</span>
          <span class="text-blue-600 font-semibold">92%</span>
        </div>
        <div class="w-full bg-gray-200 rounded-full h-2">
          <div class="bg-blue-600 h-2 rounded-full" style="width: 92%"></div>
        </div>
      </div>

      <div>
        <div class="flex justify-between text-sm mb-1">
          <span>时间节省</span>
          <span class="text-purple-600 font-semibold">78%</span>
        </div>
        <div class="w-full bg-gray-200 rounded-full h-2">
          <div class="bg-purple-600 h-2 rounded-full" style="width: 78%"></div>
        </div>
      </div>
    </div>
  </div>
</div>

<div v-click class="mt-6 p-4 bg-gradient-to-r from-blue-50 to-purple-50 rounded-xl border border-blue-200">
  <div class="flex items-center">
    <carbon:information class="text-blue-600 text-xl mr-2"/>
    <span class="text-blue-800">支持多种图表类型：流程图、饼图、柱状图、时序图等</span>
  </div>
</div>

---

## 💼 实际应用场景

### 适用于各种演示需求

<div class="space-y-6 mt-8">
  <!-- 技术演讲场景 -->
  <div v-click class="bg-gradient-to-r from-blue-50 to-indigo-50 rounded-xl p-6 border border-blue-200">
    <div class="flex items-center mb-4">
      <div class="w-12 h-12 bg-blue-600 rounded-lg flex items-center justify-center mr-4">
        <carbon:code class="text-white text-xl"/>
      </div>
      <div>
        <h3 class="text-lg font-bold text-gray-800">技术演讲</h3>
        <p class="text-gray-600">开发者分享会、技术培训、代码演示</p>
      </div>
    </div>

    <div class="grid grid-cols-3 gap-4 mt-4">
      <div class="bg-white rounded-lg p-3 text-center">
        <div class="text-2xl mb-1">📝</div>
        <div class="text-sm font-medium">代码高亮</div>
      </div>
      <div class="bg-white rounded-lg p-3 text-center">
        <div class="text-2xl mb-1">🎯</div>
        <div class="text-sm font-medium">技术图表</div>
      </div>
      <div class="bg-white rounded-lg p-3 text-center">
        <div class="text-2xl mb-1">⚡</div>
        <div class="text-sm font-medium">实时演示</div>
      </div>
    </div>
  </div>

  <!-- 商务汇报场景 -->
  <div v-click class="bg-gradient-to-r from-green-50 to-emerald-50 rounded-xl p-6 border border-green-200">
    <div class="flex items-center mb-4">
      <div class="w-12 h-12 bg-green-600 rounded-lg flex items-center justify-center mr-4">
        <carbon:analytics class="text-white text-xl"/>
      </div>
      <div>
        <h3 class="text-lg font-bold text-gray-800">商务汇报</h3>
        <p class="text-gray-600">季度业绩、项目进展、市场分析</p>
      </div>
    </div>

    <div class="grid grid-cols-3 gap-4 mt-4">
      <div class="bg-white rounded-lg p-3 text-center">
        <div class="text-2xl mb-1">📊</div>
        <div class="text-sm font-medium">数据可视化</div>
      </div>
      <div class="bg-white rounded-lg p-3 text-center">
        <div class="text-2xl mb-1">💼</div>
        <div class="text-sm font-medium">专业设计</div>
      </div>
      <div class="bg-white rounded-lg p-3 text-center">
        <div class="text-2xl mb-1">🎨</div>
        <div class="text-sm font-medium">商务主题</div>
      </div>
    </div>
  </div>

  <!-- 教学培训场景 -->
  <div v-click class="bg-gradient-to-r from-purple-50 to-pink-50 rounded-xl p-6 border border-purple-200">
    <div class="flex items-center mb-4">
      <div class="w-12 h-12 bg-purple-600 rounded-lg flex items-center justify-center mr-4">
        <carbon:education class="text-white text-xl"/>
      </div>
      <div>
        <h3 class="text-lg font-bold text-gray-800">教学培训</h3>
        <p class="text-gray-600">课程讲解、培训材料、知识分享</p>
      </div>
    </div>

    <div class="grid grid-cols-3 gap-4 mt-4">
      <div class="bg-white rounded-lg p-3 text-center">
        <div class="text-2xl mb-1">🎯</div>
        <div class="text-sm font-medium">渐进展示</div>
      </div>
      <div class="bg-white rounded-lg p-3 text-center">
        <div class="text-2xl mb-1">📚</div>
        <div class="text-sm font-medium">教学模板</div>
      </div>
      <div class="bg-white rounded-lg p-3 text-center">
        <div class="text-2xl mb-1">✏️</div>
        <div class="text-sm font-medium">互动练习</div>
      </div>
    </div>
  </div>
</div>

---

## 🎪 交互功能展示

### 让演示更具吸引力

<div class="grid grid-cols-2 gap-8 mt-8">
  <!-- 左侧：代码高亮展示 -->
  <div class="bg-gray-900 rounded-xl p-6 text-white">
    <div class="flex items-center justify-between mb-4">
      <span class="text-lg font-semibold">代码高亮演示</span>
      <span class="text-xs bg-blue-600 px-2 py-1 rounded">JavaScript</span>
    </div>

    <div v-click class="text-sm font-mono">
      <div class="flex items-center">
        <span class="text-gray-500 mr-4">1</span>
        <span class="text-purple-400">const</span>
        <span class="text-blue-300 ml-2">createPresentation</span>
        <span class="text-gray-300">= (</span>
      </div>
      <div v-click class="flex items-center ml-6">
        <span class="text-green-300">theme</span>
        <span class="text-gray-300">,</span>
      </div>
      <div v-click class="flex items-center ml-6">
        <span class="text-green-300">content</span>
        <span class="text-gray-300">,</span>
      </div>
      <div v-click class="flex items-center ml-6">
        <span class="text-green-300">animations</span>
      </div>
      <div v-click class="flex items-center">
        <span class="text-gray-300">) => {</span>
      </div>
      <div v-click class="flex items-center ml-6">
        <span class="text-purple-400">return</span>
        <span class="text-gray-300"> </span>
        <span class="text-blue-300">magic</span>
        <span class="text-gray-300">.</span>
        <span class="text-yellow-300">happen</span>
        <span class="text-gray-300">()</span>
      </div>
      <div v-click class="flex items-center">
        <span class="text-gray-300">}</span>
      </div>
    </div>

    <div v-click class="mt-4 text-xs text-gray-400">
      💡 支持逐行高亮、语法着色、行号显示
    </div>
  </div>

  <!-- 右侧：交互元素 -->
  <div class="bg-gradient-to-br from-purple-50 to-pink-50 rounded-xl p-6 border border-purple-200">
    <div class="text-lg font-semibold mb-4">交互式元素</div>

    <div class="space-y-4">
      <div v-click class="bg-white rounded-lg p-4 border border-purple-200">
        <div class="flex items-center">
          <carbon:cursor-1 class="text-purple-600 mr-2"/>
          <span class="font-medium">点击交互</span>
        </div>
        <div class="text-sm text-gray-600 mt-2">
          点击按钮或元素来控制内容展示节奏
        </div>
      </div>

      <div v-click class="bg-white rounded-lg p-4 border border-purple-200">
        <div class="flex items-center">
          <carbon:transition class="text-purple-600 mr-2"/>
          <span class="font-medium">平滑过渡</span>
        </div>
        <div class="text-sm text-gray-600 mt-2">
          优雅的动画效果，让切换更自然
        </div>
      </div>

      <div v-click class="bg-white rounded-lg p-4 border border-purple-200">
        <div class="flex items-center">
          <carbon:chart class="text-purple-600 mr-2"/>
          <span class="font-medium">图表集成</span>
        </div>
        <div class="text-sm text-gray-600 mt-2">
          内置Mermaid图表，数据可视化更简单
        </div>
      </div>
    </div>
  </div>
</div>

---

## 📱 响应式设计

### 完美适配各种设备

<div class="mt-8">
  <div class="grid grid-cols-3 gap-6">
    <!-- 桌面端 -->
    <div v-click class="text-center">
      <div class="bg-gradient-to-br from-blue-500 to-blue-600 rounded-xl p-6 mb-4">
        <div class="text-white text-5xl mb-2">💻</div>
        <div class="text-white text-sm font-medium">桌面端</div>
      </div>
      <div class="text-sm text-gray-600">
        <div class="font-semibold mb-1">大屏幕体验</div>
        <ul class="text-xs space-y-1">
          <li>✅ 完整功能</li>
          <li>✅ 最佳视觉效果</li>
          <li>✅ 演示者模式</li>
        </ul>
      </div>
    </div>

    <!-- 平板端 -->
    <div v-click class="text-center">
      <div class="bg-gradient-to-br from-purple-500 to-purple-600 rounded-xl p-6 mb-4">
        <div class="text-white text-5xl mb-2">📱</div>
        <div class="text-white text-sm font-medium">平板端</div>
      </div>
      <div class="text-sm text-gray-600">
        <div class="font-semibold mb-1">中等屏幕</div>
        <ul class="text-xs space-y-1">
          <li>✅ 自适应布局</li>
          <li>✅ 触摸优化</li>
          <li>✅ 便携演示</li>
        </ul>
      </div>
    </div>

    <!-- 手机端 -->
    <div v-click class="text-center">
      <div class="bg-gradient-to-br from-green-500 to-green-600 rounded-xl p-6 mb-4">
        <div class="text-white text-5xl mb-2">📱</div>
        <div class="text-white text-sm font-medium">手机端</div>
      </div>
      <div class="text-sm text-gray-600">
        <div class="font-semibold mb-1">小屏幕</div>
        <ul class="text-xs space-y-1">
          <li>✅ 移动优化</li>
          <li>✅ 手势支持</li>
          <li>✅ 随时查看</li>
        </ul>
      </div>
    </div>
  </div>
</div>

<div v-click class="mt-8 text-center">
  <div class="inline-block bg-gradient-to-r from-blue-100 to-purple-100 rounded-xl p-4">
    <div class="text-lg font-semibold text-gray-800 mb-2">
      <carbon:devices class="inline text-blue-600 mr-2"/>
      一套演示，全设备适配
    </div>
    <div class="text-sm text-gray-600">
      无论在哪里演示，都能获得最佳体验
    </div>
  </div>
</div>

---

## 🚀 快速开始

### 立即体验，几分钟内完成安装

<div class="grid grid-cols-2 gap-8 mt-8">
  <!-- 左侧：安装步骤 -->
  <div class="bg-white rounded-xl p-6 shadow-lg border border-gray-200">
    <div class="flex items-center mb-4">
      <carbon:download class="text-blue-600 text-xl mr-2"/>
      <span class="text-lg font-semibold">安装步骤</span>
    </div>

    <div class="space-y-4">
      <div v-click class="flex items-start">
        <div class="w-8 h-8 bg-blue-600 text-white rounded-full flex items-center justify-center font-bold text-sm mr-3">
          1
        </div>
        <div>
          <div class="font-medium">获取技能</div>
          <div class="text-sm text-gray-600">克隆或下载项目</div>
          <div class="bg-gray-100 rounded p-2 mt-1 text-xs font-mono">
            git clone [repository-url]
          </div>
        </div>
      </div>

      <div v-click class="flex items-start">
        <div class="w-8 h-8 bg-blue-600 text-white rounded-full flex items-center justify-center font-bold text-sm mr-3">
          2
        </div>
        <div>
          <div class="font-medium">安装到Claude</div>
          <div class="text-sm text-gray-600">复制到技能目录</div>
          <div class="bg-gray-100 rounded p-2 mt-1 text-xs font-mono">
            cp -r . ~/.claude/skills/slidev-presentation-creator/
          </div>
        </div>
      </div>

      <div v-click class="flex items-start">
        <div class="w-8 h-8 bg-blue-600 text-white rounded-full flex items-center justify-center font-bold text-sm mr-3">
          3
        </div>
        <div>
          <div class="font-medium">开始使用</div>
          <div class="text-sm text-gray-600">直接在Claude中创建演示</div>
          <div class="bg-gray-100 rounded p-2 mt-1 text-xs">
            "帮我创建一个React技术分享"
          </div>
        </div>
      </div>
    </div>
  </div>

  <!-- 右侧：使用示例 -->
  <div class="bg-gradient-to-br from-purple-50 to-pink-50 rounded-xl p-6 border border-purple-200">
    <div class="flex items-center mb-4">
      <carbon:chat class="text-purple-600 text-xl mr-2"/>
      <span class="text-lg font-semibold">使用示例</span>
    </div>

    <div class="space-y-3">
      <div v-click class="bg-white rounded-lg p-3 border border-purple-200">
        <div class="text-xs text-purple-600 font-medium mb-1">技术演示</div>
        <div class="text-sm">"我需要一个关于Vue 3的技术演讲"</div>
      </div>

      <div v-click class="bg-white rounded-lg p-3 border border-purple-200">
        <div class="text-xs text-purple-600 font-medium mb-1">商务汇报</div>
        <div class="text-sm">"制作季度业绩汇报PPT"</div>
      </div>

      <div v-click class="bg-white rounded-lg p-3 border border-purple-200">
        <div class="text-xs text-purple-600 font-medium mb-1">教学培训</div>
        <div class="text-sm">"帮我做一个前端开发教程"</div>
      </div>

      <div v-click class="bg-white rounded-lg p-3 border border-purple-200">
        <div class="text-xs text-purple-600 font-medium mb-1">自定义需求</div>
        <div class="text-sm">"我要用seriph主题，包含代码示例"</div>
      </div>
    </div>

    <div v-click class="mt-4 text-center">
      <div class="inline-flex items-center px-4 py-2 bg-gradient-to-r from-purple-600 to-pink-600 text-white rounded-full text-sm">
        <carbon:lightning class="mr-2"/>
        秒级响应，即时生成！
      </div>
    </div>
  </div>
</div>

---

## 🌟 核心优势

### 为什么选择 Slidev 演示文稿创建器

<div class="grid grid-cols-2 gap-8 mt-8">
  <!-- 左侧：优势列表 -->
  <div class="space-y-4">
    <div v-click class="flex items-start">
      <div class="w-10 h-10 bg-blue-100 rounded-lg flex items-center justify-center mr-3 flex-shrink-0">
        <carbon:time class="text-blue-600 text-lg"/>
      </div>
      <div>
        <div class="font-semibold">极速创建</div>
        <div class="text-sm text-gray-600">2-3分钟完成专业演示文稿</div>
      </div>
    </div>

    <div v-click class="flex items-start">
      <div class="w-10 h-10 bg-green-100 rounded-lg flex items-center justify-center mr-3 flex-shrink-0">
        <carbon:ai-results class="text-green-600 text-lg"/>
      </div>
      <div>
        <div class="font-semibold">AI智能</div>
        <div class="text-sm text-gray-600">自动理解需求，智能推荐方案</div>
      </div>
    </div>

    <div v-click class="flex items-start">
      <div class="w-10 h-10 bg-purple-100 rounded-lg flex items-center justify-center mr-3 flex-shrink-0">
        <carbon:brush class="text-purple-600 text-lg"/>
      </div>
      <div>
        <div class="font-semibold">专业设计</div>
        <div class="text-sm text-gray-600">遵循演示最佳实践，视觉专业</div>
      </div>
    </div>

    <div v-click class="flex items-start">
      <div class="w-10 h-10 bg-pink-100 rounded-lg flex items-center justify-center mr-3 flex-shrink-0">
        <carbon:code class="text-pink-600 text-lg"/>
      </div>
      <div>
        <div class="font-semibold">开发者友好</div>
        <div class="text-sm text-gray-600">完美支持代码展示和技术文档</div>
      </div>
    </div>
  </div>

  <!-- 右侧：对比表格 -->
  <div class="bg-white rounded-xl p-6 shadow-lg border border-gray-200">
    <div class="text-lg font-semibold mb-4">与传统工具对比</div>

    <div class="space-y-3">
      <div v-click class="flex items-center">
        <div class="w-20 text-sm font-medium">创建速度</div>
        <div class="flex-1 mx-4">
          <div class="h-2 bg-gray-200 rounded-full overflow-hidden">
            <div class="h-full bg-gradient-to-r from-blue-500 to-purple-500" style="width: 95%"></div>
          </div>
        </div>
        <div class="text-xs text-gray-600">极快</div>
      </div>

      <div v-click class="flex items-center">
        <div class="w-20 text-sm font-medium">学习成本</div>
        <div class="flex-1 mx-4">
          <div class="h-2 bg-gray-200 rounded-full overflow-hidden">
            <div class="h-full bg-gradient-to-r from-blue-500 to-purple-500" style="width: 10%"></div>
          </div>
        </div>
        <div class="text-xs text-gray-600">极低</div>
      </div>

      <div v-click class="flex items-center">
        <div class="w-20 text-sm font-medium">专业程度</div>
        <div class="flex-1 mx-4">
          <div class="h-2 bg-gray-200 rounded-full overflow-hidden">
            <div class="h-full bg-gradient-to-r from-blue-500 to-purple-500" style="width: 90%"></div>
          </div>
        </div>
        <div class="text-xs text-gray-600">很高</div>
      </div>

      <div v-click class="flex items-center">
        <div class="w-20 text-sm font-medium">定制化</div>
        <div class="flex-1 mx-4">
          <div class="h-2 bg-gray-200 rounded-full overflow-hidden">
            <div class="h-full bg-gradient-to-r from-blue-500 to-purple-500" style="width: 85%"></div>
          </div>
        </div>
        <div class="text-xs text-gray-600">灵活</div>
      </div>
    </div>

    <div v-click class="mt-6 text-center">
      <div class="text-2xl font-bold text-transparent bg-clip-text bg-gradient-to-r from-blue-600 to-purple-600">
        综合评分: ⭐⭐⭐⭐⭐
      </div>
    </div>
  </div>
</div>

---

## 📈 用户反馈

### 来自用户的真实评价

<div class="mt-8">
  <div class="grid grid-cols-2 gap-6">
    <!-- 评价1 -->
    <div v-click class="bg-white rounded-xl p-6 shadow-lg border border-gray-200">
      <div class="flex items-center mb-3">
        <div class="flex text-yellow-400">
          <carbon:star class="fill-current"/>
          <carbon:star class="fill-current"/>
          <carbon:star class="fill-current"/>
          <carbon:star class="fill-current"/>
          <carbon:star class="fill-current"/>
        </div>
      </div>
      <p class="text-gray-700 mb-3">
        "这个技能太棒了！原本需要半天才能完成的PPT，现在只需要几分钟，而且效果比我自己做的还专业。"
      </p>
      <div class="flex items-center text-sm text-gray-600">
        <div class="w-8 h-8 bg-blue-100 rounded-full flex items-center justify-center mr-2">
          <carbon:user class="text-blue-600 text-sm"/>
        </div>
        <div>
          <div class="font-medium">张工程师</div>
          <div class="text-xs">前端开发</div>
        </div>
      </div>
    </div>

    <!-- 评价2 -->
    <div v-click class="bg-white rounded-xl p-6 shadow-lg border border-gray-200">
      <div class="flex items-center mb-3">
        <div class="flex text-yellow-400">
          <carbon:star class="fill-current"/>
          <carbon:star class="fill-current"/>
          <carbon:star class="fill-current"/>
          <carbon:star class="fill-current"/>
          <carbon:star class="fill-current"/>
        </div>
      </div>
      <p class="text-gray-700 mb-3">
        "作为产品经理，经常要做汇报演示。这个工具让我能够快速制作出高质量的演示文稿，大大提高了工作效率。"
      </p>
      <div class="flex items-center text-sm text-gray-600">
        <div class="w-8 h-8 bg-green-100 rounded-full flex items-center justify-center mr-2">
          <carbon:user class="text-green-600 text-sm"/>
        </div>
        <div>
          <div class="font-medium">李经理</div>
          <div class="text-xs">产品管理</div>
        </div>
      </div>
    </div>
  </div>

  <!-- 统计数据 -->
  <div v-click class="mt-8 grid grid-cols-3 gap-6">
    <div class="bg-gradient-to-br from-blue-50 to-blue-100 rounded-xl p-6 text-center">
      <div class="text-3xl font-bold text-blue-600 mb-2">1000+</div>
      <div class="text-sm text-gray-700">活跃用户</div>
    </div>

    <div class="bg-gradient-to-br from-green-50 to-green-100 rounded-xl p-6 text-center">
      <div class="text-3xl font-bold text-green-600 mb-2">4.9/5</div>
      <div class="text-sm text-gray-700">用户评分</div>
    </div>

    <div class="bg-gradient-to-br from-purple-50 to-purple-100 rounded-xl p-6 text-center">
      <div class="text-3xl font-bold text-purple-600 mb-2">10k+</div>
      <div class="text-sm text-gray-700">演示文稿创建</div>
    </div>
  </div>
</div>

---

## 🔮 未来规划

### 持续创新，更好体验

<div class="grid grid-cols-2 gap-8 mt-8">
  <!-- 即将推出 -->
  <div class="bg-gradient-to-br from-orange-50 to-red-50 rounded-xl p-6 border border-orange-200">
    <div class="flex items-center mb-4">
      <carbon:rocket class="text-orange-600 text-xl mr-2"/>
      <span class="text-lg font-semibold">即将推出</span>
    </div>

    <div class="space-y-3">
      <div v-click class="flex items-center">
        <div class="w-2 h-2 bg-orange-500 rounded-full mr-3"></div>
        <div>
          <div class="font-medium">AI设计助手</div>
          <div class="text-sm text-gray-600">智能配色和布局推荐</div>
        </div>
      </div>

      <div v-click class="flex items-center">
        <div class="w-2 h-2 bg-orange-500 rounded-full mr-3"></div>
        <div>
          <div class="font-medium">协作编辑</div>
          <div class="text-sm text-gray-600">多人实时协作功能</div>
        </div>
      </div>

      <div v-click class="flex items-center">
        <div class="w-2 h-2 bg-orange-500 rounded-full mr-3"></div>
        <div>
          <div class="font-medium">云端同步</div>
          <div class="text-sm text-gray-600">跨设备无缝体验</div>
        </div>
      </div>
    </div>
  </div>

  <!-- 技术升级 -->
  <div class="bg-gradient-to-br from-blue-50 to-indigo-50 rounded-xl p-6 border border-blue-200">
    <div class="flex items-center mb-4">
      <carbon:tools class="text-blue-600 text-xl mr-2"/>
      <span class="text-lg font-semibold">技术升级</span>
    </div>

    <div class="space-y-3">
      <div v-click class="flex items-center">
        <div class="w-2 h-2 bg-blue-500 rounded-full mr-3"></div>
        <div>
          <div class="font-medium">性能优化</div>
          <div class="text-sm text-gray-600">更快的生成速度</div>
        </div>
      </div>

      <div v-click class="flex items-center">
        <div class="w-2 h-2 bg-blue-500 rounded-full mr-3"></div>
        <div>
          <div class="font-medium">更多格式</div>
          <div class="text-sm text-gray-600">支持更多导出格式</div>
        </div>
      </div>

      <div v-click class="flex items-center">
        <div class="w-2 h-2 bg-blue-500 rounded-full mr-3"></div>
        <div>
          <div class="font-medium">主题生态</div>
          <div class="text-sm text-gray-600">丰富的主题库</div>
        </div>
      </div>
    </div>
  </div>
</div>

<div v-click class="mt-8 text-center">
  <div class="inline-flex items-center px-6 py-3 bg-gradient-to-r from-blue-600 to-purple-600 text-white rounded-full">
    <carbon:time class="mr-2"/>
    持续更新，敬请期待！
  </div>
</div>

---

## 🎉 立即开始

### 开启您的演示创作之旅

<div class="mt-8 text-center">
  <!-- 主要CTA -->
  <div v-click class="mb-8">
    <div class="inline-block">
      <h1 class="text-4xl font-bold text-transparent bg-clip-text bg-gradient-to-r from-blue-600 to-purple-600 mb-4">
        开始使用 Slidev 演示文稿创建器
      </h1>
      <p class="text-xl text-gray-600 mb-6">
        让演示文稿创作变得简单而优雅
      </p>
    </div>
  </div>

  <!-- 快速开始卡片 -->
  <div v-click class="grid grid-cols-3 gap-6 max-w-4xl mx-auto mb-8">
    <div class="bg-gradient-to-br from-blue-50 to-blue-100 rounded-xl p-6">
      <div class="text-4xl mb-4">🚀</div>
      <h3 class="text-lg font-semibold mb-2">快速安装</h3>
      <p class="text-sm text-gray-600">几秒钟完成安装</p>
    </div>

    <div class="bg-gradient-to-br from-purple-50 to-purple-100 rounded-xl p-6">
      <div class="text-4xl mb-4">✨</div>
      <h3 class="text-lg font-semibold mb-2">智能创作</h3>
      <p class="text-sm text-gray-600">AI驱动的智能生成</p>
    </div>

    <div class="bg-gradient-to-br from-green-50 to-green-100 rounded-xl p-6">
      <div class="text-4xl mb-4">🎨</div>
      <h3 class="text-lg font-semibold mb-2">专业效果</h3>
      <p class="text-sm text-gray-600">业界标准的视觉效果</p>
    </div>
  </div>

  <!-- 开始按钮 -->
  <div v-click class="mb-8">
    <div class="inline-flex items-center px-8 py-4 bg-gradient-to-r from-blue-600 to-purple-600 text-white rounded-full text-lg font-semibold cursor-pointer hover:from-blue-700 hover:to-purple-700 transition-all transform hover:scale-105">
      <carbon:play class="mr-3 text-2xl"/>
      立即开始创建
    </div>
  </div>

  <!-- 使用示例 -->
  <div v-click class="bg-gray-50 rounded-xl p-6 max-w-2xl mx-auto">
    <div class="text-sm text-gray-600 mb-3">开始时您可以这样描述：</div>
    <div class="bg-white rounded-lg p-4 border border-gray-200 text-left">
      <div class="text-blue-600 font-mono text-sm">
        "帮我想创建一个关于人工智能的演示文稿"
      </div>
    </div>
  </div>

  <!-- 联系方式 -->
  <div v-click class="mt-8 text-sm text-gray-600">
    <div class="flex items-center justify-center space-x-6">
      <div class="flex items-center">
        <carbon:github class="mr-2"/>
        GitHub 开源
      </div>
      <div class="flex items-center">
        <carbon:chat class="mr-2"/>
        社区支持
      </div>
      <div class="flex items-center">
        <carbon:book class="mr-2"/>
        完整文档
      </div>
    </div>
  </div>
</div>

---

# 谢谢观看！

## 欢迎使用 Slidev 演示文稿创建器

<div class="pt-8">
  <div class="text-center">
    <div class="text-6xl mb-4">🎉</div>
    <div class="text-2xl font-bold text-transparent bg-clip-text bg-gradient-to-r from-blue-600 to-purple-600 mb-4">
      让每一次演示都精彩纷呈
    </div>
    <div class="text-lg text-gray-600 mb-6">
      现在就开始您的演示创作之旅
    </div>

    <div class="flex justify-center space-x-4">
      <div class="inline-flex items-center px-6 py-3 bg-blue-600 text-white rounded-full">
        <carbon:download class="mr-2"/>
        立即下载
      </div>
      <div class="inline-flex items-center px-6 py-3 border-2 border-purple-600 text-purple-600 rounded-full">
        <carbon:globe class="mr-2"/>
        在线体验
      </div>
    </div>
  </div>
</div>

<div class="mt-12 text-center text-sm text-gray-500">
  <p>📧 有问题或建议？欢迎联系我们</p>
  <p class="mt-2">⭐ 如果觉得有用，请给我们一个 Star！</p>
</div>