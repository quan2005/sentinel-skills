# Document Converter Skill

🚀 **一个强大的文档转换技能，可以将PDF、PPT、DOCX和网页转换为Markdown格式**

## 📋 技能概述

Document Converter技能提供了一个完整的解决方案，用于将各种文档格式和网页内容转换为结构化的Markdown格式。该技能基于高性能内容解析服务，支持智能内容提取、复杂页面处理和高级转换选项。

## ✨ 主要特性

### 🌐 多格式支持
- **网页转换**: 博客、新闻、在线文档、复杂单页应用
- **文档转换**: PDF、PPT/PowerPoint、DOCX/Word文档
- **智能提取**: 自动识别主体内容，过滤广告和无关元素

### 🎯 高级功能
- **CSS选择器**: 精确控制要提取的内容范围
- **iframe支持**: 处理嵌入第三方内容的页面
- **Shadow DOM解析**: 支持现代Web组件页面
- **图片处理**: 删除图片或使用AI描述图片
- **重定向跟踪**: 解析短链接到最终目标

### ⚡ 性能优化
- **智能缓存**: 重复请求自动缓存加速
- **超时控制**: 可配置的页面加载超时
- **代理支持**: 通过代理访问受限内容
- **快速模式**: PDF快速文本提取

## 🚀 快速开始

### 基本使用

```bash
# 转换网页
python scripts/converter.py "https://blog.samaltman.com"

# 转换本地文件
python scripts/converter.py "document.pdf" --output "converted.md"

# 高级选项
python scripts/converter.py "https://example.com" \
  --target-selector "article" \
  --remove-selector "nav,footer" \
  --remove-images \
  --timeout 45000
```

### 测试环境

```bash
# 使用测试环境
python scripts/converter.py "https://example.com" --test
```

## 📁 技能结构

```
document-converter/
├── SKILL.md                    # 技能主文档 (必需)
├── scripts/
│   └── converter.py           # 核心转换脚本
├── references/
│   ├── api_reference.md       # API接口文档
│   ├── conversion_options.md  # 转换选项详解
│   └── error_handling.md      # 错误处理指南
├── assets/
│   ├── example_urls.txt       # 测试URL集合
│   ├── usage_examples.md      # 详细使用示例
│   └── test_documents/        # 测试文档目录
│       └── README.md          # 测试文档说明
└── README.md                  # 本文件
```

## 🛠️ 核心组件

### Scripts
- **`converter.py`**: 主转换引擎，支持GET/POST请求、文件上传、高级选项配置

### References
- **`api_reference.md`**: 完整的API文档，包括端点、参数、响应格式
- **`conversion_options.md`**: 详细的转换选项说明和使用示例
- **`error_handling.md`**: 错误代码、故障排除和解决方案

### Assets
- **`example_urls.txt`**: 各类测试URL集合
- **`usage_examples.md`**: 实际使用场景和最佳实践
- **`test_documents/`**: 测试文件存放目录

## 🔧 支持的转换选项

### 内容处理
- `--remove-images`: 删除图片
- `--describe-images`: AI描述图片
- `--smart-selector`: 智能内容提取
- `--no-smart-selector`: 禁用智能提取

### CSS选择器
- `--target-selector`: 目标内容选择器
- `--remove-selector`: 移除元素选择器

### 高级选项
- `--with-iframe`: 解析iframe内容
- `--with-shadow-dom`: 解析Shadow DOM
- `--follow-redirects`: 跟踪重定向
- `--timeout`: 页面加载超时(毫秒)
- `--pdf-fast-parse`: PDF快速解析

### 服务选项
- `--test`: 使用测试环境
- `--proxy-url`: 代理服务器URL
- `--json`: JSON格式输出

## 📊 服务信息

- **生产环境**: https://reader-aigc.skyengine.com.cn
- **测试环境**: http://knowledge-reader.external.bdp-testing-streaming.k8s.skyengine.com.cn:8000
- **认证**: 当前版本无需Token
- **文件大小限制**: 建议<50MB
- **超时限制**: 默认30秒，最大60秒

## 🎯 使用场景

### 1. 学术研究
```bash
# 转换学术论文
python scripts/converter.py "https://arxiv.org/abs/2301.07041" \
  --target-selector ".ltx_page_main" \
  --describe-images
```

### 2. 文档备份
```bash
# 备份在线文档
python scripts/converter.py "https://docs.example.com/guide" \
  --target-selector ".markdown-body" \
  --output "docs_backup.md"
```

### 3. 内容分析
```bash
# 提取新闻文章内容
python scripts/converter.py "https://news.example.com/story" \
  --target-selector "article" \
  --remove-selector ".ads, .social" \
  --json
```

### 4. 文档格式转换
```bash
# PDF转Markdown
python scripts/converter.py "manual.pdf" \
  --pdf-fast-parse \
  --describe-images
```

## ⚠️ 错误处理

常见错误及解决方案：

| 错误代码 | 常见原因 | 解决方案 |
|---------|---------|---------|
| 400 | URL格式错误 | 检查URL编码 |
| 408 | 页面加载超时 | 增加`--timeout`值 |
| 413 | 文件过大 | 使用`--pdf-fast-parse` |
| 502 | 服务异常 | 稍后重试或使用`--test` |

详细错误处理指南请参考 `references/error_handling.md`

## 🏆 最佳实践

1. **由简入繁**: 先使用默认选项，再根据需要添加复杂配置
2. **精确选择**: 使用具体的CSS选择器获得更好的提取效果
3. **超时管理**: 根据页面复杂度设置合适的超时时间
4. **图片处理**: 平衡内容完整性和处理速度
5. **测试验证**: 使用JSON输出进行调试和验证
6. **错误处理**: 实现重试逻辑和降级策略

## 📦 技能包

该技能已打包为可分发的zip文件：
```
document-converter.zip (24.8KB)
```

包含所有必需文件和资源，可直接部署使用。

## 🤝 贡献指南

### 添加新功能
1. 在 `scripts/converter.py` 中实现新功能
2. 更新 `references/api_reference.md` 文档
3. 在 `assets/usage_examples.md` 中添加使用示例
4. 更新 `SKILL.md` 中的功能描述

### 报告问题
提供以下信息：
- 错误消息和状态码
- 使用的URL或文件
- 应用的选项参数
- 服务环境(生产/测试)

## 📄 许可证

本技能遵循技能创建器的开源许可证，可自由使用和分发。

## 📞 技术支持

如需技术支持，请联系：
- 服务维护团队: @许汝全 @张涛
- 技能问题: 通过GitHub Issues报告

---

**Document Converter Skill** - 让文档转换变得简单高效 🚀