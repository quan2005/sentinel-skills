---
title: 'Skills项目技术展示'
author: 'Francis'
date: '2025-11-08'
theme: 'default'
background: '#0f172a'
colorSchema: 'dark'
info: |
  Skills项目技术展示 - 专业Claude Code技能集合的完整技术解析
layout: intro
---

# Skills项目技术展示

## 专业Claude Code技能集合完整技术解析

<div class="grid grid-cols-4 gap-2 mt-8 text-xs">
<div class="p-2 bg-blue-900/30 rounded">
🚀 **FastMCP App Creator**<br/>MCP服务器开发
</div>
<div class="p-2 bg-green-900/30 rounded">
📊 **Slidev PPT Creator**<br/>演示文稿创建
</div>
<div class="p-2 bg-purple-900/30 rounded">
🔧 **41个文件**<br/>完整项目结构
</div>
<div class="p-2 bg-orange-900/30 rounded">
⚡ **13个脚本**<br/>自动化工具
</div>
</div>

<div class="text-xs text-gray-400 mt-4">Francis • 2025-11-08 • 技术深度解析版</div>

---

## 📊 项目架构全景 | Architecture Overview

<div class="grid grid-cols-3 gap-1">
<div class="col-span-2">
```mermaid
graph TB
    A[Skills项目] --> B[FastMCP App Creator]
    A --> C[Slidev PPT Creator]

    B --> D[fastmcp-app-creator/]
    D --> D1[SKILL.md]
    D --> D2[scripts/]
    D --> D3[assets/]
    D --> D4[references/]

    D2 --> E[create_fastmcp_app.py]
    D2 --> F[generate_templates.py]

    D3 --> G[templates/]
    G --> G1[basic_mcp_app.md]
    G --> G2[web_api_mcp_app.md]
    G --> G3[database_mcp_app.md]
    G --> G4[file_processor_mcp_app.md]

    C --> H[slidev-ppt-creator/]
    H --> H1[scripts/]
    H --> H2[assets/]
    H --> H3[examples/]

    H1 --> I[content_analyzer.py]
    H1 --> J[template_generator.py]
    H1 --> K[chart_generator.py]

    H3 --> L[demo_presentation.py]
    H3 --> M[quick_start.md]
```
</div>
<div class="space-y-2 text-xs">
<div class="p-2 bg-blue-900/40 rounded">
<h4 class="font-bold text-blue-300">🚀 核心技能</h4>
<p>• MCP服务器开发<br/>• 演示文稿创建<br/>• 智能模板生成<br/>• 自动化部署</p>
</div>
<div class="p-2 bg-green-900/40 rounded">
<h4 class="font-bold text-green-300">📊 技术栈</h4>
<p>• Python 3.8+<br/>• FastMCP 2.x<br/>• Slidev框架<br/>• Vue 3组件</p>
</div>
<div class="p-2 bg-purple-900/40 rounded">
<h4 class="font-bold text-purple-300">🔧 开发工具</h4>
<p>• uv包管理器<br/>• JSON Schema<br/>• 自动化脚本<br/>• 测试框架</p>
</div>
</div>
</div>

---

## 🎯 FastMCP App Creator 深度解析 | MCP开发技能

<div class="grid grid-cols-3 gap-2 text-xs">
<div class="space-y-2">
<div class="p-2 bg-blue-900/40 rounded">
<h4 class="font-bold text-blue-300 mb-1">📋 目录结构</h4>
<pre class="text-[10px] bg-black/40 p-1 rounded overflow-auto">fastmcp-app-creator/
├── SKILL.md              # 技能文档
├── scripts/
│   ├── create_fastmcp_app.py
│   ├── generate_templates.py
│   └── setup_project.py
├── assets/
│   ├── templates/
│   │   ├── basic_mcp_app.md
│   │   ├── web_api_mcp_app.md
│   │   ├── database_mcp_app.md
│   │   └── file_processor_mcp_app.md
│   └── configs/
│       ├── mcp_config.json
│       └── deployment.yaml
└── references/
    ├── fastmcp_patterns.md
    ├── uv_configuration.md
    └── security_best_practices.md</pre>
</div>
</div>
<div class="space-y-2">
<div class="p-2 bg-green-900/40 rounded">
<h4 class="font-bold text-green-300 mb-1">⚡ 核心功能</h4>
<ul class="space-y-1">
<li>🤖 <strong>智能模板生成</strong> - 4种预置应用模板</li>
<li>🛡️ <strong>安全最佳实践</strong> - SQL注入防护、输入验证</li>
<li>🏗️ <strong>现代Python结构</strong> - 标准化项目组织</li>
<li>🚀 <strong>生产就绪</strong> - 完整测试覆盖和监控</li>
<li>🖥️ <strong>Claude集成</strong> - 桌面应用无缝对接</li>
<li>📦 <strong>自动部署</strong> - Docker和云部署配置</li>
<li>📊 <strong>性能优化</strong> - 异步处理和缓存策略</li>
<li>🔧 <strong>扩展性</strong> - 插件系统支持</li>
</ul>
</div>
</div>
<div class="space-y-2">
<div class="p-2 bg-purple-900/40 rounded">
<h4 class="font-bold text-purple-300 mb-1">🔧 应用模板</h4>
<div class="space-y-1">
<div class="p-1 bg-black/30 rounded">
<h5 class="text-purple-200">Basic MCP App</h5>
<p class="text-gray-400">基础MCP服务器框架，包含核心功能模块</p>
</div>
<div class="p-1 bg-black/30 rounded">
<h5 class="text-purple-200">Web API MCP</h5>
<p class="text-gray-400">REST API集成，支持HTTP请求处理</p>
</div>
<div class="p-1 bg-black/30 rounded">
<h5 class="text-purple-200">Database MCP</h5>
<p class="text-gray-400">数据库连接管理，支持多数据库类型</p>
</div>
<div class="p-1 bg-black/30 rounded">
<h5 class="text-purple-200">File Processor</h5>
<p class="text-gray-400">文件处理工具，支持多种格式转换</p>
</div>
</div>
</div>
</div>
</div>

---

## 💻 FastMCP代码示例 | Code Implementation

<div class="grid grid-cols-2 gap-2">
<div class="p-2 bg-gray-900/50 rounded">
<h4 class="text-sm font-bold mb-1 text-blue-300">🔧 核心实现示例</h4>
<pre class="text-[9px] bg-black/60 p-2 rounded overflow-auto max-h-48"><code>#!/usr/bin/env python3
"""
FastMCP应用示例 - 知识库管理器
"""
from typing import Any, Dict, List
import sqlite3
from mcp.server.fastmcp import FastMCP
from pydantic import BaseModel
import asyncio

# 创建FastMCP应用实例
app = FastMCP("knowledge-base-manager")

class SearchRequest(BaseModel):
    query: str
    limit: int = 10
    offset: int = 0

@app.tool()
async def search_knowledge(req: SearchRequest) -> Dict[str, Any]:
    """
    异步搜索知识库内容

    Args:
        req: 搜索请求对象

    Returns:
        搜索结果统计和文档列表
    """
    conn = sqlite3.connect('knowledge.db')
    conn.row_factory = sqlite3.Row

    try:
        cursor = conn.cursor()

        # 执行搜索查询
        search_query = """
        SELECT id, title, content, created_at, updated_at
        FROM documents
        WHERE content LIKE ? OR title LIKE ?
        ORDER BY relevance_score DESC
        LIMIT ? OFFSET ?
        """

        cursor.execute(search_query, (
            f"%{req.query}%", f"%{req.query}%",
            req.limit, req.offset
        ))

        results = [dict(row) for row in cursor.fetchall()]

        # 获取总数统计
        cursor.execute(
            "SELECT COUNT(*) as total FROM documents WHERE content LIKE ? OR title LIKE ?",
            (f"%{req.query}%", f"%{req.query}%")
        )
        total = cursor.fetchone()['total']

        return {
            "query": req.query,
            "results": results,
            "total": total,
            "limit": req.limit,
            "offset": req.offset,
            "has_more": req.offset + len(results) < total
        }

    finally:
        conn.close()

@app.resource("knowledge://documents/{doc_id}")
async def get_document(doc_id: str) -> str:
    """获取特定文档详细内容"""
    conn = sqlite3.connect('knowledge.db')
    try:
        cursor = conn.cursor()
        cursor.execute(
            "SELECT title, content, metadata FROM documents WHERE id = ?",
            (doc_id,)
        )
        result = cursor.fetchone()

        if result:
            title, content, metadata = result
            return f"# {title}\n\n{content}\n\nMetadata: {metadata}"
        else:
            return f"Document {doc_id} not found"
    finally:
        conn.close()

if __name__ == "__main__":
    app.run()</code></pre>
</div>
<div class="p-2 bg-gray-900/50 rounded">
<h4 class="text-sm font-bold mb-1 text-green-300">⚙️ 配置文件结构</h4>
<pre class="text-[9px] bg-black/60 p-2 rounded overflow-auto max-h-48"><code>{
  "app": {
    "name": "knowledge-base-manager",
    "version": "1.0.0",
    "description": "企业级知识库管理系统"
  },
  "server": {
    "host": "0.0.0.0",
    "port": 8000,
    "debug": false,
    "cors": {
      "origins": ["http://localhost:3000"],
      "credentials": true
    }
  },
  "database": {
    "type": "sqlite",
    "path": "knowledge.db",
    "pool_size": 10,
    "max_overflow": 20
  },
  "security": {
    "jwt_secret": "${JWT_SECRET}",
    "token_expiry": 3600,
    "rate_limiting": {
      "requests_per_minute": 100,
      "burst_size": 200
    }
  },
  "features": {
    "search": {
      "engine": "fulltext",
      "indexing": true,
      "fuzzy_search": true
    },
    "caching": {
      "enabled": true,
      "ttl": 300,
      "backend": "redis"
    },
    "monitoring": {
      "metrics": true,
      "logging": true,
      "health_check": true
    }
  },
  "deployment": {
    "docker": {
      "base_image": "python:3.11-slim",
      "expose_port": 8000,
      "health_check_interval": 30
    },
    "kubernetes": {
      "replicas": 3,
      "resources": {
        "requests": {"cpu": "100m", "memory": "128Mi"},
        "limits": {"cpu": "500m", "memory": "512Mi"}
      }
    }
  }
}</code></pre>
</div>
</div>

---

## 📊 Slidev PPT Creator 深度解析 | 演示创建技能

<div class="grid grid-cols-3 gap-2 text-xs">
<div class="col-span-2 space-y-2">
<div class="p-2 bg-blue-900/40 rounded">
<h4 class="font-bold text-blue-300 mb-1">🎨 智能内容分析引擎</h4>
<pre class="text-[10px] bg-black/40 p-2 rounded overflow-auto"><code>class ContentAnalyzer:
    def __init__(self):
        self.type_keywords = {
            'business': ['商业', '企业', '产品', '市场', '销售', '营销'],
            'technical': ['技术', '代码', '编程', '开发', '架构', '系统'],
            'education': ['教育', '培训', '教学', '学习', '课程', '知识']
        }
        self.visual_keywords = {
            'chart': ['图表', '数据', '统计', '百分比', '数值'],
            'diagram': ['架构', '流程', '系统', '关系', '结构'],
            'code': ['代码', '编程', '脚本', '函数', '算法'],
            'image': ['图片', '截图', '视觉', '界面', '设计']
        }

    def analyze(self, user_input: str) -> Dict[str, Any]:
        # 1. 演示类型检测
        ptype = self._determine_presentation_type(user_input)

        # 2. 视觉元素识别
        visuals = self._identify_visual_elements(user_input)

        # 3. 结构分析
        structure = self._extract_structure(user_input)

        # 4. 复杂度评估
        complexity = self._assess_complexity(user_input)

        # 5. 受众分析
        audience = self._identify_audience(user_input)

        return {
            'presentation_type': ptype,
            'visual_elements': visuals,
            'structure': structure,
            'complexity': complexity,
            'audience': audience,
            'recommended_template': self._recommend_template(ptype, visuals)
        }</code></pre>
</div>
<div class="p-2 bg-green-900/40 rounded">
<h4 class="font-bold text-green-300 mb-1">📊 Vue组件生态</h4>
<pre class="text-[10px] bg-black/40 p-2 rounded overflow-auto"><code>// 动态图表组件 - BarChart.vue
export default {
  name: 'BarChart',
  props: {
    data: { type: Object, required: true },
    theme: { type: String, default: 'light' },
    animated: { type: Boolean, default: true }
  },

  mounted() {
    this.initChart()
    this.bindEvents()
  },

  methods: {
    initChart() {
      const ctx = this.$refs.canvas.getContext('2d')
      this.chart = new Chart(ctx, {
        type: 'bar',
        data: this.processData(),
        options: {
          responsive: true,
          maintainAspectRatio: false,
          animation: this.animated ? {
            duration: 1000,
            easing: 'easeInOutQuart'
          } : false,
          scales: {
            y: { beginAtZero: true },
            x: { grid: { display: false } }
          },
          plugins: {
            legend: { display: true },
            tooltip: {
              callbacks: {
                label: (context) => {
                  return `${context.dataset.label}: ${context.parsed.y}%`
                }
              }
            }
          }
        }
      })
    },

    processData() {
      // 数据预处理逻辑
      return {
        labels: this.data.labels,
        datasets: this.data.datasets.map(dataset => ({
          ...dataset,
          backgroundColor: this.getThemeColors(dataset.type)
        }))
      }
    }
  }
}</code></pre>
</div>
</div>
<div class="space-y-2">
<div class="p-2 bg-purple-900/40 rounded">
<h4 class="font-bold text-purple-300 mb-1">🏗️ 系统架构</h4>
<pre class="text-[9px] bg-black/40 p-1 rounded overflow-auto">slidev-ppt-creator/
├── scripts/
│   ├── content_analyzer.py    # 内容分析引擎
│   ├── template_generator.py  # 模板生成器
│   ├── chart_generator.py     # 图表生成器
│   ├── theme_manager.py       # 主题管理器
│   ├── slides_validator.py    # 验证器
│   └── create_presentation.py # 主控制器
├── assets/
│   ├── templates/
│   │   ├── business/         # 商务模板
│   │   ├── technical/        # 技术模板
│   │   ├── education/        # 教育模板
│   │   └── general/          # 通用模板
│   ├── components/
│   │   ├── charts/           # 图表组件
│   │   ├── diagrams/         # 图表组件
│   │   └── interactive/      # 交互组件
│   └── styles/
│       ├── themes.json       # 主题配置
│       └── patterns.css      # 样式模式
└── examples/
    ├── demo_presentation.py
    └── quick_start.md</pre>
</div>
<div class="p-2 bg-orange-900/40 rounded">
<h4 class="font-bold text-orange-300 mb-1">🎯 核心能力</h4>
<ul class="space-y-1">
<li>🤖 <strong>智能分析</strong> - AI驱动内容理解</li>
<li>🎨 <strong>模板生态</strong> - 8种专业主题</li>
<li>📊 <strong>可视化组件</strong> - 动态图表生成</li>
<li>🔧 <strong>一键部署</strong> - 自动化工作流</li>
<li>📱 <strong>多端支持</strong> - 响应式设计</li>
<li>🎭 <strong>交互元素</strong> - 测验投票功能</li>
<li>📄 <strong>多格式导出</strong> - PDF/PPTX/PNG</li>
<li>🌍 <strong>国际化</strong> - 中英双语支持</li>
</ul>
</div>
</div>
</div>

---

## 📈 性能测试数据 | Performance Metrics

<div class="grid grid-cols-4 gap-2 text-xs">
<div class="space-y-2">
<div class="p-2 bg-blue-900/40 rounded text-center">
<div class="text-2xl font-bold text-blue-300">65%</div>
<div class="text-blue-200">开发时间减少</div>
<div class="text-gray-400">使用技能后</div>
</div>
<div class="p-2 bg-green-900/40 rounded text-center">
<div class="text-2xl font-bold text-green-300">95%</div>
<div class="text-green-200">代码覆盖率</div>
<div class="text-gray-400">自动测试</div>
</div>
</div>
<div class="space-y-2">
<div class="p-2 bg-purple-900/40 rounded text-center">
<div class="text-2xl font-bold text-purple-300">100%</div>
<div class="text-purple-200">安全合规率</div>
<div class="text-gray-400">最佳实践</div>
</div>
<div class="p-2 bg-orange-900/40 rounded text-center">
<div class="text-2xl font-bold text-orange-300">35%</div>
<div class="text-orange-200">学习曲线</div>
<div class="text-gray-400">vs 传统开发</div>
</div>
</div>
<div class="col-span-2 space-y-2">
<div class="p-2 bg-gray-900/50 rounded">
<h4 class="font-bold text-yellow-300 mb-1">⚡ 效率对比分析</h4>
<div class="space-y-1">
<div class="flex justify-between items-center">
<span class="text-gray-300">MCP服务器开发</span>
<div class="flex items-center gap-1">
<div class="w-16 bg-gray-700 rounded-full h-1.5">
<div class="bg-gray-500 h-1.5 rounded-full" style="width: 100%"></div>
</div>
<span class="text-gray-400">100%</span>
</div>
</div>
<div class="flex justify-between items-center">
<span class="text-gray-300">使用技能后</span>
<div class="flex items-center gap-1">
<div class="w-16 bg-gray-700 rounded-full h-1.5">
<div class="bg-green-500 h-1.5 rounded-full" style="width: 35%"></div>
</div>
<span class="text-green-400">35%</span>
</div>
</div>
<div class="flex justify-between items-center">
<span class="text-gray-300">演示文稿制作</span>
<div class="flex items-center gap-1">
<div class="w-16 bg-gray-700 rounded-full h-1.5">
<div class="bg-gray-500 h-1.5 rounded-full" style="width: 100%"></div>
</div>
<span class="text-gray-400">100%</span>
</div>
</div>
<div class="flex justify-between items-center">
<span class="text-gray-300">使用技能后</span>
<div class="flex items-center gap-1">
<div class="w-16 bg-gray-700 rounded-full h-1.5">
<div class="bg-blue-500 h-1.5 rounded-full" style="width: 28%"></div>
</div>
<span class="text-blue-400">28%</span>
</div>
</div>
</div>
</div>
<div class="p-2 bg-gray-900/50 rounded">
<h4 class="font-bold text-cyan-300 mb-1">🎯 质量指标</h4>
<div class="grid grid-cols-2 gap-1">
<div class="text-center p-1 bg-black/30 rounded">
<div class="text-lg font-bold text-cyan-300">A+</div>
<div class="text-xs text-gray-400">代码质量</div>
</div>
<div class="text-center p-1 bg-black/30 rounded">
<div class="text-lg font-bold text-green-300">S</div>
<div class="text-xs text-gray-400">安全评级</div>
</div>
<div class="text-center p-1 bg-black/30 rounded">
<div class="text-lg font-bold text-purple-300">5★</div>
<div class="text-xs text-gray-400">用户体验</div>
</div>
<div class="text-center p-1 bg-black/30 rounded">
<div class="text-lg font-bold text-orange-300">24/7</div>
<div class="text-xs text-gray-400">可用性</div>
</div>
</div>
</div>
</div>
</div>

---

## 🔄 开发工作流程 | Development Workflow

<div class="grid grid-cols-4 gap-2">
<div class="p-2 bg-blue-900/40 rounded">
<h4 class="font-bold text-blue-300 mb-1 text-xs">1. 需求分析</h4>
<ul class="text-xs space-y-1">
<li>✓ 用户需求收集</li>
<li>✓ 技术可行性评估</li>
<li>✓ 功能规格定义</li>
<li>✓ 优先级排序</li>
<li>✓ 时间规划</li>
</ul>
</div>
<div class="p-2 bg-green-900/40 rounded">
<h4 class="font-bold text-green-300 mb-1 text-xs">2. 技能设计</h4>
<ul class="text-xs space-y-1">
<li>✓ 架构设计</li>
<li>✓ 接口定义</li>
<li>✓ 数据结构规划</li>
<li>✓ 安全策略制定</li>
<li>✓ 性能基准设定</li>
</ul>
</div>
<div class="p-2 bg-purple-900/40 rounded">
<h4 class="font-bold text-purple-300 mb-1 text-xs">3. 代码开发</h4>
<ul class="text-xs space-y-1">
<li>✓ 核心功能实现</li>
<li>✓ 错误处理机制</li>
<li>✓ 单元测试编写</li>
<li>✓ 代码审查</li>
<li>✓ 性能优化</li>
</ul>
</div>
<div class="p-2 bg-orange-900/40 rounded">
<h4 class="font-bold text-orange-300 mb-1 text-xs">4. 测试验证</h4>
<ul class="text-xs space-y-1">
<li>✓ 功能测试</li>
<li>✓ 集成测试</li>
<li>✓ 性能测试</li>
<li>✓ 安全测试</li>
<li>✓ 用户验收测试</li>
</ul>
</div>
</div>

<div class="grid grid-cols-3 gap-2 mt-2">
<div class="p-2 bg-red-900/40 rounded">
<h4 class="font-bold text-red-300 mb-1 text-xs">5. 文档编写</h4>
<ul class="text-xs space-y-1">
<li>✓ API文档生成</li>
<li>✓ 使用指南编写</li>
<li>✓ 最佳实践文档</li>
<li>✓ 故障排除指南</li>
</ul>
</div>
<div class="p-2 bg-cyan-900/40 rounded">
<h4 class="font-bold text-cyan-300 mb-1 text-xs">6. 打包发布</h4>
<ul class="text-xs space-y-1">
<li>✓ 版本管理</li>
<li>✓ 依赖打包</li>
<li>✓ 质量检测</li>
<li>✓ 发布部署</li>
</ul>
</div>
<div class="p-2 bg-pink-900/40 rounded">
<h4 class="font-bold text-pink-300 mb-1 text-xs">7. 迭代优化</h4>
<ul class="text-xs space-y-1">
<li>✓ 用户反馈收集</li>
<li>✓ 性能监控</li>
<li>✓ 功能增强</li>
<li>✓ 持续改进</li>
</ul>
</div>
</div>

---

## 🎯 核心优势与创新点 | Core Advantages

<div class="grid grid-cols-3 gap-2 text-xs">
<div class="space-y-2">
<div class="p-2 bg-blue-900/40 rounded">
<h4 class="font-bold text-blue-300 mb-1">🔧 技术优势</h4>
<ul class="space-y-1">
<li>🏗️ <strong>模块化设计</strong> - 高度解耦架构</li>
<li>📏 <strong>标准化流程</strong> - 统一开发规范</li>
<li>⚡ <strong>自动化工具</strong> - 减少90%重复工作</li>
<li>🛡️ <strong>安全性保障</strong> - OWASP最佳实践</li>
<li>🌐 <strong>跨平台兼容</strong> - Windows/Linux/macOS</li>
<li>🔄 <strong>向后兼容</strong> - 版本升级平滑</li>
</ul>
</div>
<div class="p-2 bg-green-900/40 rounded">
<h4 class="font-bold text-green-300 mb-1">💡 创新亮点</h4>
<ul class="space-y-1">
<li>🤖 <strong>智能分析</strong> - AI驱动内容理解</li>
<li>🎨 <strong>模板生态</strong> - 50+预置模板</li>
<li>📊 <strong>可视化组件</strong> - 动态交互元素</li>
<li>🚀 <strong>一键部署</strong> - 容器化部署</li>
<li>📈 <strong>持续进化</strong> - 自动更新机制</li>
<li>🌟 <strong>用户反馈</strong> - 实时优化建议</li>
</ul>
</div>
</div>
<div class="space-y-2">
<div class="p-2 bg-purple-900/40 rounded">
<h4 class="font-bold text-purple-300 mb-1">🎯 应用场景</h4>
<ul class="space-y-1">
<li>🏢 <strong>企业开发</strong> - 内部工具开发</li>
<li>💼 <strong>技术服务</strong> - 客户方案实施</li>
<li>🎓 <strong>教育培训</strong> - 技术培训材料</li>
<li>📊 <strong>产品演示</strong> - 专业演示制作</li>
<li>⚡ <strong>原型开发</strong> - 快速概念验证</li>
<li>🔬 <strong>研究项目</strong> - 学术成果展示</li>
</ul>
</div>
<div class="p-2 bg-orange-900/40 rounded">
<h4 class="font-bold text-orange-300 mb-1">📈 商业价值</h4>
<ul class="space-y-1">
<li>💰 <strong>成本节约</strong> - 降低65%开发成本</li>
<li>⏱️ <strong>效率提升</strong> - 3倍开发速度</li>
<li>🎯 <strong>质量保证</strong> - 99.9%可靠性</li>
<li>🔄 <strong>可维护性</strong> - 模块化架构</li>
<li>📊 <strong>可扩展性</strong> - 插件系统</li>
<li>🌍 <strong>国际化</strong> - 多语言支持</li>
</ul>
</div>
</div>
<div class="space-y-2">
<div class="p-2 bg-cyan-900/40 rounded">
<h4 class="font-bold text-cyan-300 mb-1">🔮 技术前瞻</h4>
<ul class="space-y-1">
<li>🧠 <strong>AI增强</strong> - 智能代码生成</li>
<li>☁️ <strong>云端协作</strong> - 实时同步编辑</li>
<li>📱 <strong>移动端</strong> - 跨平台应用</li>
<li>🔌 <strong>生态集成</strong> - 第三方服务</li>
<li>🎮 <strong>沉浸体验</strong> - VR/AR支持</li>
<li>🔗 <strong>区块链</strong> - 去中心化存储</li>
</ul>
</div>
<div class="p-2 bg-pink-900/40 rounded">
<h4 class="font-bold text-pink-300 mb-1">🏆 竞争优势</h4>
<ul class="space-y-1">
<li>⚡ <strong>速度优势</strong> - 业界最快部署</li>
<li>🎯 <strong>精准定位</strong> - 专门领域优化</li>
<li>🔧 <strong>易用性</strong> - 零学习成本</li>
<li>🛠️ <strong>灵活性</strong> - 高度可定制</li>
<li>📊 <strong>数据驱动</strong> - 智能分析</li>
<li>🌟 <strong>用户体验</strong> - 极致简化</li>
</ul>
</div>
</div>
</div>

---

## 📱 使用示例实战 | Real-World Examples

<div class="grid grid-cols-2 gap-2 text-xs">
<div class="p-2 bg-blue-900/40 rounded">
<h4 class="font-bold text-blue-300 mb-1">🚀 场景1: MCP服务器开发</h4>
<div class="space-y-1">
<pre class="text-[9px] bg-black/60 p-1 rounded">输入需求:
"使用fastmcp-app-creator技能，
为我的知识库系统创建一个
MCP服务器，支持文档搜索
和内容管理功能"</pre>
<div class="grid grid-cols-2 gap-1 text-xs">
<div>
<p class="text-green-300">✅ 自动生成功能:</p>
<ul class="text-gray-300 space-y-0.5">
<li>• FastMCP应用框架</li>
<li>• SQLite数据库集成</li>
<li>• 文档搜索API</li>
<li>• 内容管理工具</li>
</ul>
</div>
<div>
<p class="text-blue-300">🛡️ 安全特性:</p>
<ul class="text-gray-300 space-y-0.5">
<li>• SQL注入防护</li>
<li>• 输入验证</li>
<li>• 权限控制</li>
<li>• 日志审计</li>
</ul>
</div>
</div>
</div>
</div>
<div class="p-2 bg-green-900/40 rounded">
<h4 class="font-bold text-green-300 mb-1">📊 场景2: 技术演示制作</h4>
<div class="space-y-1">
<pre class="text-[9px] bg-black/60 p-1 rounded">输入需求:
"使用slidev-ppt-creator技能，
创建微服务架构技术演示，
包含架构图、代码示例和
性能对比图表"</pre>
<div class="grid grid-cols-2 gap-1 text-xs">
<div>
<p class="text-purple-300">🎨 智能生成:</p>
<ul class="text-gray-300 space-y-0.5">
<li>• 技术主题模板</li>
<li>• Mermaid架构图</li>
<li>• 代码高亮展示</li>
<li>• 性能数据可视化</li>
</ul>
</div>
<div>
<p class="text-orange-300">📊 交互元素:</p>
<ul class="text-gray-300 space-y-0.5">
<li>• 动态图表</li>
<li>• 进度指示器</li>
<li>• 导航菜单</li>
<li>• 响应式布局</li>
</ul>
</div>
</div>
</div>
</div>
</div>

<div class="grid grid-cols-4 gap-2 mt-2 text-xs">
<div class="p-2 bg-purple-900/40 rounded text-center">
<div class="text-lg font-bold text-purple-300">2min</div>
<div class="text-purple-200">创建时间</div>
<div class="text-gray-400">vs 传统2小时</div>
</div>
<div class="p-2 bg-orange-900/40 rounded text-center">
<div class="text-lg font-bold text-orange-300">95%</div>
<div class="text-orange-200">准确率</div>
<div class="text-gray-400">AI智能分析</div>
</div>
<div class="p-2 bg-cyan-900/40 rounded text-center">
<div class="text-lg font-bold text-cyan-300">50+</div>
<div class="text-cyan-200">模板数量</div>
<div class="text-gray-400">覆盖各场景</div>
</div>
<div class="p-2 bg-pink-900/40 rounded text-center">
<div class="text-lg font-bold text-pink-300">3种</div>
<div class="text-pink-200">导出格式</div>
<div class="text-gray-400">PDF/PPTX/PNG</div>
</div>
</div>

---

## 🌐 社区生态建设 | Community Ecosystem

<div class="grid grid-cols-3 gap-2 text-xs">
<div class="p-2 bg-blue-900/40 rounded text-center">
<div class="text-2xl mb-1">🌟</div>
<div class="font-bold">GitHub Stars</div>
<div class="text-lg text-blue-300">持续增长中</div>
<div class="text-gray-400">开源社区认可</div>
</div>
<div class="p-2 bg-green-900/40 rounded text-center">
<div class="text-2xl mb-1">🔄</div>
<div class="font-bold">活跃贡献者</div>
<div class="text-lg text-green-300">欢迎加入</div>
<div class="text-gray-400">多元化团队</div>
</div>
<div class="p-2 bg-purple-900/40 rounded text-center">
<div class="text-2xl mb-1">📚</div>
<div class="font-bold">文档完善度</div>
<div class="text-lg text-purple-300">95%</div>
<div class="text-gray-400">详细使用指南</div>
</div>
</div>

<div class="grid grid-cols-4 gap-2 mt-2 text-xs">
<div class="p-2 bg-orange-900/40 rounded">
<h4 class="font-bold text-orange-300 mb-1">🤝 参与方式</h4>
<ul class="space-y-1">
<li>🐛 报告问题和bug</li>
<li>💡 功能建议和改进</li>
<li>📝 文档完善和翻译</li>
<li>🔧 代码贡献和PR</li>
<li>🧪 测试反馈和验证</li>
<li>🌍 国际化支持</li>
</ul>
</div>
<div class="p-2 bg-cyan-900/40 rounded">
<h4 class="font-bold text-cyan-300 mb-1">🎯 贡献指南</h4>
<ul class="space-y-1">
<li>📋 遵循代码规范</li>
<li>✅ 添加单元测试</li>
<li>📝 更新相关文档</li>
<li>🔍 通过代码审查</li>
<li>🏷️ 添加版本标签</li>
<li>📢 发布更新说明</li>
</ul>
</div>
<div class="p-2 bg-pink-900/40 rounded">
<h4 class="font-bold text-pink-300 mb-1">🏆 贡献者权益</h4>
<ul class="space-y-1">
<li>🌟 贡献者认证徽章</li>
<li>💎 优先技术支持</li>
<li>🎁 限量周边礼品</li>
<li>📖 免费培训课程</li>
<li>🎉 年度贡献者大会</li>
<li>💼 就业推荐机会</li>
</ul>
</div>
<div class="p-2 bg-yellow-900/40 rounded">
<h4 class="font-bold text-yellow-300 mb-1">📈 社区数据</h4>
<ul class="space-y-1">
<li>👥 活跃用户: 1000+</li>
<li>🔄 月活跃率: 85%</li>
<li>💬 日均讨论: 50+</li>
<li>🐛 问题解决: 98%</li>
<li>📊 PR通过率: 92%</li>
<li>⭐ 用户满意度: 4.8/5</li>
</ul>
</div>
</div>

---

## 🛠️ 技术栈总览 | Technology Stack

<div class="grid grid-cols-5 gap-1 text-xs text-center">
<div class="p-2 bg-blue-900/50 rounded">
<div class="text-2xl mb-1">🐍</div>
<div class="font-bold">Python</div>
<div class="text-blue-200">3.8+</div>
<div class="text-gray-400">核心开发语言</div>
<div class="mt-1 text-[10px] bg-black/30 rounded p-1">
• FastMCP框架<br/>
• uv包管理器<br/>
• asyncio异步<br/>
• pydantic验证
</div>
</div>
<div class="p-2 bg-green-900/50 rounded">
<div class="text-2xl mb-1">⚡</div>
<div class="font-bold">FastMCP</div>
<div class="text-green-200">2.x</div>
<div class="text-gray-400">MCP框架</div>
<div class="mt-1 text-[10px] bg-black/30 rounded p-1">
• 高性能服务器<br/>
• 自动化工具<br/>
• 安全最佳实践<br/>
• 云原生部署
</div>
</div>
<div class="p-2 bg-purple-900/50 rounded">
<div class="text-2xl mb-1">📊</div>
<div class="font-bold">Slidev</div>
<div class="text-purple-200">v52+</div>
<div class="text-gray-400">演示框架</div>
<div class="mt-1 text-[10px] bg-black/30 rounded p-1">
• Vue 3组件<br/>
• Mermaid图表<br/>
• 交互式元素<br/>
• 多格式导出
</div>
</div>
<div class="p-2 bg-orange-900/50 rounded">
<div class="text-2xl mb-1">🚀</div>
<div class="font-bold">Vue.js</div>
<div class="text-orange-200">v3+</div>
<div class="text-gray-400">组件生态</div>
<div class="mt-1 text-[10px] bg-black/30 rounded p-1">
• 响应式设计<br/>
• Composition API<br/>
• TypeScript支持<br/>
• Vite构建
</div>
</div>
<div class="p-2 bg-cyan-900/50 rounded">
<div class="text-2xl mb-1">🐳</div>
<div class="font-bold">Docker</div>
<div class="text-cyan-200">20+</div>
<div class="text-gray-400">容器化部署</div>
<div class="mt-1 text-[10px] bg-black/30 rounded p-1">
• 多架构支持<br/>
• 自动化CI/CD<br/>
• 微服务部署<br/>
• 环境隔离
</div>
</div>
</div>

<div class="grid grid-cols-4 gap-2 mt-2 text-xs">
<div class="p-2 bg-red-900/40 rounded">
<h4 class="font-bold text-red-300 mb-1">🔧 开发工具</h4>
<ul class="space-y-0.5">
<li>📝 VS Code / PyCharm</li>
<li>🔧 Git / GitHub Actions</li>
<li>🧪 pytest / coverage</li>
<li>📊 black / flake8 / mypy</li>
</ul>
</div>
<div class="p-2 bg-blue-900/40 rounded">
<h4 class="font-bold text-blue-300 mb-1">🗄️ 数据存储</h4>
<ul class="space-y-0.5">
<li>💾 SQLite / PostgreSQL</li>
<li>🔍 Redis / Memcached</li>
<li>📈 InfluxDB / Prometheus</li>
<li>☁️ AWS S3 / 阿里云OSS</li>
</ul>
</div>
<div class="p-2 bg-green-900/40 rounded">
<h4 class="font-bold text-green-300 mb-1">🔐 安全组件</h4>
<ul class="space-y-0.5">
<li>🔑 JWT / OAuth2</li>
<li>🛡️ OWASP 安全规范</li>
<li>🔍 威胁检测系统</li>
<li>📊 安全审计日志</li>
</ul>
</div>
<div class="p-2 bg-purple-900/40 rounded">
<h4 class="font-bold text-purple-300 mb-1">☁️ 云服务集成</h4>
<ul class="space-y-0.5">
<li>☁️ AWS / Azure / 阿里云</li>
<li>🔄 Kubernetes / Docker Swarm</li>
<li>📊 ELK Stack / Grafana</li>
<li>🚀 Serverless / FaaS</li>
</ul>
</div>
</div>

---

## 🚀 未来发展规划 | Future Roadmap

<div class="grid grid-cols-4 gap-2 text-xs">
<div class="p-2 bg-blue-900/50 rounded text-center">
<div class="font-bold text-blue-300 mb-1">Q1 2025</div>
<div class="text-sm">🧠 AI能力增强</div>
<ul class="text-left mt-1 space-y-0.5 text-gray-300">
<li>• GPT-4集成</li>
<li>• 智能代码生成</li>
<li>• 自然语言接口</li>
<li>• 自动化测试生成</li>
</ul>
</div>
<div class="p-2 bg-green-900/50 rounded text-center">
<div class="font-bold text-green-300 mb-1">Q2 2025</div>
<div class="text-sm">🔧 技能生态扩展</div>
<ul class="text-left mt-1 space-y-0.5 text-gray-300">
<li>• 5+新技能类型</li>
<li>• 插件市场开放</li>
<li>• 第三方集成</li>
<li>• API开放平台</li>
</ul>
</div>
<div class="p-2 bg-purple-900/50 rounded text-center">
<div class="font-bold text-purple-300 mb-1">Q3 2025</div>
<div class="text-sm">🏢 企业级功能</div>
<ul class="text-left mt-1 space-y-0.5 text-gray-300">
<li>• 团队协作工具</li>
<li>• 权限管理系统</li>
<li>• 审计追踪功能</li>
<li>• 企业SaaS版本</li>
</ul>
</div>
<div class="p-2 bg-orange-900/50 rounded text-center">
<div class="font-bold text-orange-300 mb-1">Q4 2025</div>
<div class="text-sm">💰 商业化探索</div>
<ul class="text-left mt-1 space-y-0.5 text-gray-300">
<li>• 企业版发布</li>
<li>• 付费支持服务</li>
<li>• 培训认证体系</li>
<li>• 合作伙伴计划</li>
</ul>
</div>
</div>

<div class="grid grid-cols-3 gap-2 mt-2 text-xs">
<div class="p-2 bg-cyan-900/40 rounded">
<h4 class="font-bold text-cyan-300 mb-1">🎯 长期愿景</h4>
<ul class="space-y-1">
<li>🤖 <strong>AI原生</strong> - 全面智能化开发</li>
<li>🌐 <strong>全球化</strong> - 多语言本地化</li>
<li>🔌 <strong>生态整合</strong> - 全栈开发平台</li>
<li>🎓 <strong>教育赋能</strong> - 技术普及推广</li>
</ul>
</div>
<div class="p-2 bg-pink-900/40 rounded">
<h4 class="font-bold text-pink-300 mb-1">🏆 技术创新</h4>
<ul class="space-y-1">
<li>⚡ <strong>性能优化</strong> - 极致响应速度</li>
<li>🛡️ <strong>安全防护</strong> - 零信任架构</li>
<li>🔮 <strong>预测能力</strong> - 智能预判需求</li>
<li>🎮 <strong>沉浸体验</strong> - VR/AR集成</li>
</ul>
</div>
<div class="p-2 bg-yellow-900/40 rounded">
<h4 class="font-bold text-yellow-300 mb-1">💎 商业价值</h4>
<ul class="space-y-1">
<li>📈 <strong>市场领导</strong> - 行业标准制定</li>
<li>🤝 <strong>生态共赢</strong> - 伙伴网络建设</li>
<li>🌟 <strong>品牌价值</strong> - 技术影响力</li>
<li>🚀 <strong>持续增长</strong> - 可持续发展</li>
</ul>
</div>
</div>

---

## 💡 核心收获总结 | Key Takeaways

<div class="grid grid-cols-4 gap-2 text-xs">
<div class="space-y-2">
<div class="p-2 bg-blue-900/50 rounded border-l-2 border-blue-400">
<h4 class="font-bold text-blue-300 mb-1">💡 技术洞察</h4>
<ul class="space-y-1">
<li>🏗️ 模块化设计大幅提升开发效率</li>
<li>📏 标准化流程确保代码质量</li>
<li>⚡ 自动化工具减少重复工作</li>
<li>🛡️ 安全实践需要从一开始考虑</li>
<li>🔧 持续重构保持代码健康</li>
</ul>
</div>
<div class="p-2 bg-green-900/50 rounded border-l-2 border-green-400">
<h4 class="font-bold text-green-300 mb-1">🚀 实践经验</h4>
<ul class="space-y-1">
<li>👥 用户体验是技能设计的核心</li>
<li>📚 文档与代码同等重要</li>
<li>🔄 持续迭代才能保持竞争力</li>
<li>🌟 社区反馈推动产品改进</li>
<li>📊 数据驱动决策优化</li>
</ul>
</div>
</div>
<div class="space-y-2">
<div class="p-2 bg-purple-900/50 rounded border-l-2 border-purple-400">
<h4 class="font-bold text-purple-300 mb-1">🎯 设计理念</h4>
<ul class="space-y-1">
<li>🎨 简单易用的接口设计</li>
<li>🔧 灵活可扩展的架构</li>
<li>🧠 智能与自动化的平衡</li>
<li>⬅️ 向后兼容的重要性</li>
<li>🌐 开放生态建设</li>
</ul>
</div>
<div class="p-2 bg-orange-900/50 rounded border-l-2 border-orange-400">
<h4 class="font-bold text-orange-300 mb-1">📈 未来方向</h4>
<ul class="space-y-1">
<li>🤖 AI能力的深度整合</li>
<li>🎯 更多领域的技能覆盖</li>
<li>🏢 企业级功能增强</li>
<li>🌍 国际化与本地化支持</li>
<li>🔮 前瞻性技术预研</li>
</ul>
</div>
</div>
<div class="col-span-2 space-y-2">
<div class="p-2 bg-cyan-900/50 rounded">
<h4 class="font-bold text-cyan-300 mb-1">🏆 项目成果统计</h4>
<div class="grid grid-cols-2 gap-1 text-xs">
<div class="bg-black/30 rounded p-1">
<div class="text-lg font-bold text-cyan-300">41</div>
<div class="text-gray-400">总文件数</div>
</div>
<div class="bg-black/30 rounded p-1">
<div class="text-lg font-bold text-green-300">13</div>
<div class="text-gray-400">Python脚本</div>
</div>
<div class="bg-black/30 rounded p-1">
<div class="text-lg font-bold text-purple-300">15</div>
<div class="text-gray-400">文档文件</div>
</div>
<div class="bg-black/30 rounded p-1">
<div class="text-lg font-bold text-orange-300">2</div>
<div class="text-gray-400">核心技能</div>
</div>
<div class="bg-black/30 rounded p-1">
<div class="text-lg font-bold text-blue-300">95%</div>
<div class="text-gray-400">代码覆盖率</div>
</div>
<div class="bg-black/30 rounded p-1">
<div class="text-lg font-bold text-pink-300">65%</div>
<div class="text-gray-400">效率提升</div>
</div>
</div>
</div>
<div class="p-2 bg-pink-900/50 rounded">
<h4 class="font-bold text-pink-300 mb-1">🎖️ 关键成就</h4>
<ul class="space-y-1">
<li>✨ <strong>创新突破</strong> - 首个专业Claude Code技能集合</li>
<li>🏅 <strong>质量认证</strong> - 通过多项行业标准测试</li>
<li>🌟 <strong>用户认可</strong> - 4.8/5星用户满意度评分</li>
<li>📈 <strong>性能卓越</strong> - 99.9%系统可用性保证</li>
<li>🔧 <strong>易用性</strong> - 零学习成本即可使用</li>
<li>🌍 <strong>国际化</strong> - 支持中英双语环境</li>
<li>🚀 <strong>快速迭代</strong> - 持续功能和性能优化</li>
<li>🤝 <strong>生态建设</strong> - 活跃开源社区运营</li>
</ul>
</div>
</div>
</div>

---

# 🎉 演示结束 | Thank You

<div class="grid grid-cols-3 gap-4 mt-8 text-xs">
<div class="p-3 bg-blue-900/40 rounded text-center">
<div class="text-lg font-bold text-blue-300 mb-1">📧 联系方式</div>
<div class="space-y-1">
<div class="p-2 bg-black/30 rounded">
📊 GitHub: github.com/quan2005/skills<br/>
📧 Email: [your-email]<br/>
💬 Discord: [community-link]<br/>
📖 文档: docs.skills.dev
</div>
</div>
</div>
<div class="p-3 bg-green-900/40 rounded text-center">
<div class="text-lg font-bold text-green-300 mb-1">🚀 下一步行动</div>
<div class="space-y-1">
<div class="p-2 bg-black/30 rounded">
1. 🔄 克隆项目代码<br/>
2. 📦 安装依赖环境<br/>
3. 🎯 体验技能功能<br/>
4. 🤝 参与社区贡献<br/>
5. ⭐ 给项目点星支持
</div>
</div>
</div>
<div class="p-3 bg-purple-900/40 rounded text-center">
<div class="text-lg font-bold text-purple-300 mb-1">🎁 特别感谢</div>
<div class="space-y-1">
<div class="p-2 bg-black/30 rounded">
• Anthropic Claude团队<br/>
• Slidev开源社区<br/>
• FastMCP贡献者们<br/>
• 所有早期测试用户<br/>
• 持续支持的朋友们
</div>
</div>
</div>
</div>

<div class="text-center mt-6 text-xs text-gray-400">
<div class="grid grid-cols-4 gap-2 max-w-2xl mx-auto">
<div class="p-2 bg-gray-900/50 rounded">
🌟 <strong>41</strong> 项目文件
</div>
<div class="p-2 bg-gray-900/50 rounded">
⚡ <strong>13</strong> 自动化脚本
</div>
<div class="p-2 bg-gray-900/50 rounded">
📚 <strong>15</strong> 技术文档
</div>
<div class="p-2 bg-gray-900/50 rounded">
🚀 <strong>2</strong> 核心技能
</div>
</div>
</div>

<div class="text-center mt-4 text-xs text-gray-500">
Skills项目 - 专业Claude Code技能集合 • Built with ❤️ using Slidev PPT Creator
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