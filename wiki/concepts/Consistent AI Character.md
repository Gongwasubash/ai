---
tags:
  - concept
  - video
  - ai
created: 2026-09-06
sources:
  - "How to Make a REALISTIC AI Talking Head Avatar (Google Flow Tutorial)"
  - "How Google Flow Agent Turned a Storyboard into an AI UGC AD (Step-by-Step)"
---

# Consistent AI Character

A reusable AI persona whose face, voice, and behavior stay locked across every generated clip — the precondition for series content with AI presenters.

## Locking Mechanisms

1. **Defined look:** structured prompt (appearance + background scene reference, not subject)
2. **Face lock:** uploaded reference image tagged as scene; character object tagged as subject
3. **Voice lock:** preset or description-generated voice attached to the character
4. **Behavior lock:** personality line + per-clip bracket action cues (`[looks at her body]`)
5. **Loop discipline:** reuse-prompt arrow, one variable (dialogue line) changed per generation
6. **ID sheet (Klever Nuts):** multi-angle persona shots screenshotted into a single face-definition sheet fed back to the model — strongest consistency anchor
7. **Copyright-safe casting:** reference a real TikTok model, generate a *similar-but-different* face

## Related

- [[Google Flow]]
- [[AI Talking Head Avatars]]
- [[Viral Style Repurposing]]
