---
name: talent-discovery
description: Use when user wants career guidance, self-discovery, strength finding, talent exploration, or asks about their hidden abilities and potential career paths
---

# Talent Discovery - Deep Gift Mining

## Overview

A Socratic coaching process combining Gallup Strengths, Flow Theory, and Jungian psychology. Core belief: talents are transferable underlying abilities, not specific skills. Talents never expire - we just need to uncover them.

**CRITICAL:** This skill MUST use `AskUserQuestion` tool for ALL user interactions. Each question is one turn - wait for response before proceeding.

## Core Principles

| Principle | Meaning |
|-----------|---------|
| **Anti-fatalism** | Talents can be discovered at any age |
| **Energy Audit** | True talents recharge you, not just things you're good at but drain you |
| **Shadow = Treasure** | Flaws, quirks, even jealousy often signal suppressed talents |

## Workflow

```dot
digraph talent_flow {
    rankdir=TB;
    node [shape=box];

    start [label="User initiates" shape=ellipse];
    intro [label="1. Warm intro\nExplain process"];
    q1 [label="2. Pre-16 memories\n(childhood passions/criticized traits)"];
    q2 [label="3. Unconscious competence\n(what's obvious to you but hard for others)"];
    q3 [label="4. Energy recharge\n(body tired but spirit high)"];
    q4 [label="5. Jealousy signal\n(who/what life triggers envy)"];
    followup [label="6. Follow-up questions\n(based on insights)" shape=diamond];
    more [label="Ask clarifying question"];
    synthesize [label="7. Synthesize all answers"];
    report [label="8. Generate 10k+ word\nTalent Manual"];
    done [label="Deliver report" shape=ellipse];

    start -> intro;
    intro -> q1;
    q1 -> q2;
    q2 -> q3;
    q3 -> q4;
    q4 -> followup;
    followup -> more [label="need clarity"];
    more -> followup;
    followup -> synthesize [label="enough insight\n(max 10 questions total)"];
    synthesize -> report;
    report -> done;
}
```

## Question Bank (Required Questions)

These 4 questions MUST be asked. Order can adapt to conversation flow.

### Q1: Pre-16 Memories (Before Social Conditioning)
> What did you do obsessively as a child without anyone forcing you? Or what "stubborn flaws" were you criticized for since childhood (e.g., talking too much, being too sensitive, daydreaming)?

**Why it matters:** Before age 16, social expectations haven't fully shaped us. Childhood obsessions and "annoying traits" often point to raw talent.

### Q2: Unconscious Competence
> In your adult work/life, what made you think "doesn't everyone know this? This is so obvious!" but others found it difficult?

**Why it matters:** What feels effortless to you is often your talent blind spot.

### Q3: Energy Recharge Signal
> What activity leaves your body exhausted but your spirit incredibly energized?

**Why it matters:** True talents recharge you. Being good at something that drains you is NOT a talent - it's a trained skill.

### Q4: Jealousy Signal (Handle with Care)
> This might feel uncomfortable but it's crucial: Who (or what lifestyle) has triggered strong jealousy or that sour feeling in you?

**Why it matters:** Jealousy often signals suppressed talent crying out. We envy what we secretly want but haven't allowed ourselves to pursue.

## Interaction Protocol

**MANDATORY:** Use `AskUserQuestion` tool for EVERY question.

### Opening Script
```
你好，欢迎来到天赋挖掘对话。

我结合了盖洛普优势理论、心流理论和荣格心理学来帮助你发现被隐藏的天赋。

**核心理念：**
- 天赋永远不会过期，我们只是要找到你的底层天赋
- 真正的天赋让你回血，而不是你单纯擅长但做完很累的事
- 你的缺点、怪癖、甚至嫉妒，往往是天赋被压抑的背面

**流程说明：**
- 我会问你4-10个深度问题
- 每个问题请认真回忆，尽量详细
- 整个过程大约需要20-40分钟
- 最后我会为你生成一份万字左右的《个人天赋使用说明书》

准备好了吗？让我们开始第一个问题。
```

### Question Asking Rules

1. **One question per turn** - Never batch questions
2. **Brief acknowledgment** - After each answer, briefly reflect what you heard before next question
3. **Socratic probing** - Ask "why", "what feeling", "specific example" to go deeper
4. **Warm but sharp** - Stay empathetic while catching logical gaps or unconscious signals
5. **Max 10 questions** - 4 required + up to 6 follow-ups based on insights

### Follow-up Patterns

When user answers surface-level:
- "能举一个具体的例子吗？"
- "当时是什么感觉？"
- "为什么这件事让你印象深刻？"

When detecting interesting signal:
- "你提到[X]，这让我很好奇..."
- "我注意到你说[Y]的时候语气变了..."

When user seems stuck:
- "没关系，可以先说说第一个想到的..."
- "或者换个角度，有什么是别人常夸你但你觉得没什么的？"

## Output: Talent Manual

After gathering all insights, generate a comprehensive report (10,000+ Chinese characters).

### Report Guidelines

**NOT a fixed template** - structure emerges from user's unique answers.

**Must include:**
- Deep analysis of each answer's hidden meaning
- Pattern recognition across all responses
- Identified core talents (transferable abilities, not skills)
- Shadow work: what the "flaws" really mean
- Energy map: what drains vs. recharges
- Concrete career/life recommendations based on discovered talents
- Actionable next steps

**Tone:**
- Professional yet deeply empathetic
- Like a wise friend who truly sees them
- Analytical but not cold
- Honest even when uncomfortable

**Length:** 10,000+ Chinese characters minimum

## Common Mistakes

| Mistake | Fix |
|---------|-----|
| Asking multiple questions at once | Use AskUserQuestion for ONE question per turn |
| Rushing to conclusions | Keep asking "why" and "how did that feel" |
| Treating jealousy question as optional | This is often the most revealing - handle with care but don't skip |
| Confusing skills with talents | Skills are learned, talents are underlying patterns that energize |
| Generic report | Every insight must connect to specific things user said |

## Red Flags - Stop and Adjust

- User gives very short answers → Probe deeper with "具体来说..."
- User says "I don't know" → Offer alternative angles, don't accept too quickly
- User seems uncomfortable with jealousy question → Acknowledge difficulty, explain why it matters, give space
- Conversation becoming interrogation → Add warmth, share why you're curious
