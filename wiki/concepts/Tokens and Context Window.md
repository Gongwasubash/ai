---
tags:
  - concept
  - ai-fundamentals
created: 2026-09-02
sources:
  - "[[Google's 8 Hour AI Essentials Course]]"
---

# Tokens and Context Window

How LLMs actually process and remember information.

## Tokens

- AI doesn't understand words — it understands **tokens** (word fragments stored as numbers)
- Example: "strawberry" → "straw" + "berry" (two tokens with different meanings individually, combined = one concept)
- Tokens are stored in **vector databases** as numbers for calculation
- Both input (your message) and output (AI's response) are built token by token

## Context Window

- The AI's working memory — like a whiteboard
- Has a fixed size (varies by model: 4K, 8K, 128K, etc.)
- As conversation grows, older information gets dropped to make room
- This is why AI "forgets" mid-conversation — it's not forgetting, it's running out of space

## Why This Matters

- Longer conversations = more context needed = more tokens = more cost
- Important info should be provided early or re-stated
- Large documents may exceed context window and need chunking

## Source References

- [[Google's 8 Hour AI Essentials Course]] — tokens and context window section
