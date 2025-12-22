---
name: prompt-optimization
description: Use when optimizing system prompts, agent prompts, or any prompt requiring structural improvements for Claude or other LLMs
---

# System Prompt Optimization

## Overview

System prompts are the architectural foundation of AI behavior. Optimization requires **context engineering** (designing the full information environment) not just word-smithing.

**Core principle:** Claude 4.x follows instructions literally. Be explicit about what you want, not what you don't want.

## When to Use

**Use when:**
- Agent/system prompt produces inconsistent behavior
- Model undertriggers or overtriggers on tools
- Outputs lack desired format or verbosity
- Multi-step workflows fail mid-execution
- Behavioral steering isn't working

**Skip when:**
- Simple user-facing prompts working correctly
- One-time requests without reuse needs

## System Prompt Architecture

A well-structured system prompt has distinct sections:

```
┌─────────────────────────────────────┐
│ Identity & Role                     │ ← Who the agent is
├─────────────────────────────────────┤
│ Core Behaviors & Rules              │ ← Always/never constraints
├─────────────────────────────────────┤
│ Tool Definitions & Usage            │ ← When/how to use tools
├─────────────────────────────────────┤
│ Output Format & Style               │ ← How to respond
├─────────────────────────────────────┤
│ Domain Context                      │ ← Background knowledge
├─────────────────────────────────────┤
│ Examples (if needed)                │ ← Concrete patterns
└─────────────────────────────────────┘
```

## Claude 4.x Specific Techniques

### 1. Be Explicit, Not Implicit

Claude 4.x interprets literally. Request behaviors explicitly.

| ❌ Implicit | ✅ Explicit |
|-------------|-------------|
| "Help with code" | "Implement changes rather than only suggesting them" |
| "Be thorough" | "Read relevant files BEFORE proposing edits" |
| "Don't use markdown" | "Write in flowing prose paragraphs" |

### 2. Positive Framing Over Negation

Tell Claude what TO DO, not what NOT to do.

| ❌ Negation | ✅ Positive |
|-------------|-------------|
| "Don't be verbose" | "Be concise and direct" |
| "Don't hallucinate" | "Only reference code you have opened" |
| "Don't skip steps" | "Complete each step before proceeding" |

### 3. Use XML Structure

Claude is trained on structured prompts. XML tags improve parsing:

```xml
<role>You are a code reviewer...</role>
<rules>
- Always run tests before approving
- Check for security vulnerabilities
</rules>
<output_format>Respond in <review> tags</output_format>
```

### 4. Calibrate Tool Triggering

Claude 4.x responds strongly to system prompts. Adjust intensity:

| Undertriggering | Balanced | Overtriggering |
|-----------------|----------|----------------|
| "CRITICAL: You MUST use..." | "Use this tool when..." | (Dial back aggressive language) |

## Quick Reference

| Problem | Solution | Example |
|---------|----------|---------|
| Model suggests instead of acts | Add action bias | "By default, implement changes rather than suggesting" |
| Too verbose/terse | Explicit style guide | "Provide brief summaries after tool calls" |
| Skips verification | Mandate checkpoints | "Run tests before claiming completion" |
| Wrong format | Match prompt style | Remove markdown from prompt to reduce markdown in output |
| Ignores context | Add motivation | "This matters because X, so ensure Y" |
| Inconsistent behavior | Add red flags list | "STOP if you find yourself doing X" |

## Behavioral Steering Patterns

### Proactive vs Conservative Action

```
# Proactive (implements by default)
By default, implement changes rather than only suggesting them.
Infer user intent and proceed with the most useful action.

# Conservative (waits for explicit instruction)
Do not modify files unless explicitly instructed.
Default to providing information and recommendations.
```

### Verbosity Control

```
# More updates
After completing tool use, provide a quick summary.

# Less chatter
Skip verbal summaries; proceed directly to next action.
```

### Parallel vs Sequential Execution

```
# Maximize parallelism
Make all independent tool calls in parallel.
Never use placeholders or guess missing parameters.

# Sequential safety
Execute operations sequentially with pauses between steps.
```

## Multi-Context Workflows

For long-running agents:

1. **State persistence**: "Save progress to `progress.txt` before context refreshes"
2. **Verification tools**: "Run integration tests before new features"
3. **Incremental progress**: "Focus on completing one component fully before moving on"
4. **Git for state**: "Use git commits as checkpoints that can be restored"

## Common Mistakes

| Mistake | Impact | Fix |
|---------|--------|-----|
| Negative instructions only | Claude ignores or misinterprets | Reframe as positive actions |
| Generic "be helpful" | No behavioral change | Specify exact behaviors wanted |
| Conflicting instructions | Inconsistent behavior | Audit for contradictions |
| Missing format examples | Wrong output structure | Add concrete output samples |
| Over-engineering prompts | Token waste, confusion | Keep minimal and test often |

## Red Flags

- Using "CRITICAL/MUST/ALWAYS" excessively (causes overtriggering)
- Negative-only constraints without positive alternatives
- Long prompts without XML structure or clear sections
- Instructions that assume Claude will infer intent
- No examples for complex output formats

## Optimization Process

1. **Baseline**: Run current prompt, document failures verbatim
2. **Diagnose**: Categorize issues (format? action? tool use? verbosity?)
3. **Target one issue**: Fix one problem at a time
4. **Test**: Verify fix works AND didn't break other behaviors
5. **Iterate**: Repeat until stable

**Key insight:** Prompt optimization is iterative debugging, not one-shot perfection.