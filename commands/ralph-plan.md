---
name: Ralph Plan (rplan)
description: Collaborative requirements refinement using product philosophy, then generates Ralph Wiggum loop commands with completion criteria and iteration parameters
---

# Ralph Plan (rplan) - 需求梳理 + Ralph 命令生成

**rplan = Ralph Plan**：用产品哲学梳理需求，然后生成 Ralph Wiggum Loop 命令

## 核心：产品哲学对话 → Ralph Loop 命令

## Phase 1: 产品哲学对话（需求梳理）

### 核心原则

| 哲学 | 应用 |
|------|------|
| **80/20 法则** | 追问"核心意图是什么？"，区分核心 vs 边缘 |
| **意图即产品** | 聚焦"用户想要什么"，而非"做什么功能" |
| **最小可行闭环** | 确保"意图→行动→反馈"完整 |
| **增量式演进** | 每次只解决一个核心问题 |
| **约束即赋能** | 将"限制"转化为"脚手架" |
| **知识显式化** | 记录"为什么"而非"是什么" |

### 对话流程（一次问一个问题）

**第 1 层：核心意图（80/20）**
- "核心意图是什么？"
- "用户最痛的是什么？"
- "80% 核心价值是什么？20% 边缘是什么（延后）？"
- "最小闭环是什么？"

**第 2 层：约束赋能**
- "有哪些约束？如何转化为脚手架？"
- "模块边界是什么？"

**第 3 层：增量规划**
- "第一步是什么？如何验证？"
- "能否拆分更小？"

**第 4 层：技术准备**
- "技术栈？现有模式？"
- "完成标准是什么？"

### 停止时机
- 核心意图清晰且聚焦
- 最小闭环完整可验证
- 增量规划清晰（第一步明确）
- 完成标准客观可衡量

---

## Phase 2: 生成 Ralph Loop 命令

### 命令格式

```bash
/ralph-loop:ralph-loop "<detailed_prompt>" --completion-promise "<promise>" --max-iterations <n>
```

### Prompt 结构

```
<detailed_task_description>

核心意图（Why）：
- <核心意图>

最小闭环（What）：
- <最简可实现方案>

要求（Requirements）：
- <核心要求1>（必须）
- <核心要求2>（必须）
- （边缘功能标注"延后"）

约束（Constraints）：
- <约束1>（已转化为脚手架）
- <约束2>（已转化为脚手架）

上下文（Context）：
- 项目使用 <TECH_STACK>
- 遵循的模式：<PATTERNS>

增量实现（Process）：
第1步：<步骤> - 验证：<标准>
第2步：<步骤> - 验证：<标准>

每一步：
  1. 理解当前状态
  2. 实现该步骤
  3. 验证是否满足标准
  4. 如果失败，修复并重试

完成标准（Completion Criteria）：
- <标准1>（量化、可验证）
- <标准2>（量化、可验证）

当所有标准满足时，输出：<promise>
```

### Prompt 编写最佳实践

| 原则 | 错误示例 ❌ | 正确示例 ✅ |
|------|-----------|-----------|
| **明确完成标准** | Build a todo API and make it good. | Build a REST API for todos.<br>When complete:<br>- All CRUD endpoints working<br>- Input validation in place<br>- Tests passing (coverage > 80%)<br>- README with API docs<br>- Output: <promise>COMPLETE</promise> |
| **逐步目标** | Create a complete e-commerce platform. | Phase 1: User authentication (JWT, tests)<br>Phase 2: Product catalog (list/search, tests)<br>Phase 3: Shopping cart (add/remove, tests)<br><br>Output <promise>COMPLETE</promise> when all phases done. |
| **自我纠正模式** | Write code for feature X. | Implement feature X following TDD:<br>1. Write failing tests<br>2. Implement feature<br>3. Run tests<br>4. If any fail, debug and fix<br>5. Refactor if needed<br>6. Repeat until all green<br>7. Output: <promise>COMPLETE</promise> |

### 参数设置

**`--completion-promise`**：
- 格式：`<TASK>_DONE` 或 `<TASK>_COMPLETE`
- 示例：`TODO_MVP_DONE`, `AUTH_LOOP_COMPLETE`

**`--max-iterations`**：
| 复杂度 | 迭代次数 | 80/20 比例 |
|--------|---------|-----------|
| 最小 MVP | 10-20 | 100% 核心 |
| 小功能 | 20-30 | 80% 核心 |
| 中功能 | 30-50 | 70% 核心 |
| 大功能 | 50-80 | 60% 核心 |
| Refactor | 30-50 | 100% 核心 |

---

## 即用型提示模板

### 模板 1: 功能实现

```bash
/ralph-loop:ralph-loop "Implement [FEATURE_NAME].

Requirements:
- [Requirement 1]
- [Requirement 2]
- [Requirement 3]

Success criteria:
- All requirements implemented
- Tests passing with >80% coverage
- No linter errors
- Documentation updated

Output <promise>COMPLETE</promise> when done." --max-iterations 30 --completion-promise "COMPLETE"
```

### 模板 2: TDD 开发

```bash
/ralph-loop:ralph-loop "Implement [FEATURE] using TDD.

Process:
1. Write failing test for next requirement
2. Implement minimal code to pass
3. Run tests
4. If failing, fix and retry
5. Refactor if needed
6. Repeat for all requirements

Requirements: [LIST]

Output <promise>DONE</promise> when all tests green." --max-iterations 50 --completion-promise "DONE"
```

### 模板 3: Bug 修复

```bash
/ralph-loop:ralph-loop "Fix bug: [DESCRIPTION]

Steps:
1. Reproduce the bug
2. Identify root cause
3. Implement fix
4. Write regression test
5. Verify fix works
6. Check no new issues introduced

After 15 iterations if not fixed:
- Document blocking issues
- List attempted approaches
- Suggest alternatives

Output <promise>FIXED</promise> when resolved." --max-iterations 20 --completion-promise "FIXED"
```

### 模板 4: 重构

```bash
/ralph-loop:ralph-loop "Refactor [COMPONENT] for [GOAL].

Constraints:
- All existing tests must pass
- No behavior changes
- Incremental commits

Checklist:
- [ ] Tests passing before start
- [ ] Apply refactoring step
- [ ] Tests still passing
- [ ] Repeat until done

Output <promise>REFACTORED</promise> when complete." --max-iterations 25 --completion-promise "REFACTORED"
```

---

## 完整示例

### 用户："做一个 todo API"

**对话：**
- Q1: 核心意图？→ A: 追踪待办，不遗忘
- Q2: 80/20？→ A: 核心（增删查改），边缘（分类、截止日期→延后）
- Q3: 最小闭环？→ A: 添加→显示→标记完成
- Q4: 第一步？→ A: POST, GET, PATCH 端点
- Q5: 完成？→ A: 3个端点都能正常工作

**输出：**

```markdown
## Ralph Loop 命令

```bash
/ralph-loop:ralph-loop "Build a minimum viable todo API.

核心意图（Why）：
让用户快速添加和追踪待办事项，不遗忘重要事情。

最小闭环（What）：
用户添加 todo → 显示 todo → 标记完成 → 看到完成状态

要求（Requirements - 100% 核心）：
- POST /todos: 创建 todo（title 必需）
- GET /todos: 获取所有 todos
- PATCH /todos/:id/complete: 标记完成
- 数据模型：id, title, completed, created_at

延后处理（YAGNI）：
- 分类、标签、截止日期、优先级

约束（Constraints）：
- 项目使用 FastAPI + PostgreSQL
- 遵循现有 API 风格
- 最简单实现

上下文（Context）：
- 自动建表
- RESTful 风格
- HTTP 状态码：201, 200, 404

增量实现（Process）：
第1步：创建数据模型 - 验证：表结构建立
第2步：实现 POST /todos - 验证：能创建 todo
第3步：实现 GET /todos - 验证：能获取列表
第4步：实现 PATCH /todos/:id/complete - 验证：能标记完成

完成标准（Completion Criteria）：
- 所有 3 个端点返回 200/201（或 404 不存在）
- POST 创建成功返回 todo 对象
- GET 返回所有 todos（可能为空）
- PATCH 标记完成后，completed=true

当所有标准满足时，输出：<promise>TODO_MVP_DONE</promise>" --completion-promise "TODO_MVP_DONE" --max-iterations 20
```

## 参数说明
- `--completion-promise "TODO_MVP_DONE"`: 简洁明确，匹配核心任务
- `--max-iterations 20`: 最小 MVP，100% 核心，预期 4 步 × 4-5 次迭代/步

## 下一步
1. 复制命令
2. 运行: `/ralph-loop:ralph-loop "..." --completion-promise "TODO_MVP_DONE" --max-iterations 20`
3. 监控进度
4. 如需取消: `/ralph-loop:cancel-ralph`
```

---

## 使用流程

1. **用户提出想法**
2. **触发命令**：输入 `/ralph-plan` 或 `/rplan`
3. **Phase 1: 产品哲学对话**（逐个提问，梳理需求）
4. **Phase 2: 输出 Ralph 命令**（包含 prompt、参数、说明）
5. **用户复制运行**
6. **监控 + 取消**（如需）

## 关键点

### Phase 1 - 产品哲学对话
- **一次问一个问题**，优先选择题
- **明确 YAGNI**，边缘功能标注"延后"
- **核心意图 > 功能堆砌**
- **最小闭环 > 完美设计**
- **显式记录"为什么"**

### Phase 2 - Ralph 命令生成
- **明确完成标准**：量化、可验证（不要模糊描述）
- **逐步目标**：拆分为多个阶段，每阶段可验证
- **自我纠正模式**：测试 → 失败 → 修复 → 重复
- **始终设置 max-iterations**（安全）
- **参考模板**：4 个即用型模板（功能实现/TDD/Bug修复/重构）
