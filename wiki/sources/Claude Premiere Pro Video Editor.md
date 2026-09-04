---
title: "I taught Claude how to use Premiere Pro and it's INSANE"
source_file: "Clippings/I taught Claude how to use Premiere Pro and it's INSANE.md"
date_ingested: 2026-09-03
tags:
  - "youtube"
  - "claude"
  - "video-editing"
  - "ai-automation"
  - "mcp"
  - "hyperframes"
---

# I taught Claude how to use Premiere Pro and it's INSANE

**Source:** [YouTube](https://www.youtube.com/watch?v=Ohyo6-VO1jY)
**Author:** Jason Cooperson
**Published:** 2026-07-24

## Summary

Jason Cooperson demonstrates a Claude-powered video editing system that autonomously edits videos inside Premiere Pro. Every cut, transition, and motion graphic in the demo video was edited by Claude.

## Core Architecture

### HyperFrames (Free, Open-Source)
- GitHub: https://github.com/heygen-com/hyperframes
- Generates motion graphics using HTML/CSS animations
- Claude builds a webpage → animates it → screen records → imports to Premiere
- Better than video gen models (Higgsfield) for motion graphics: cleaner, faster, free

### Premiere Pro MCP (Bridge)
- GitHub: https://github.com/hetpatel-11/Adobe_Premiere_Pro_MCP
- Lets Claude control Premiere Pro directly
- Can import footage, cut timeline, add transitions, apply effects
- Also works with DaVinci Resolve Studio and Final Cut Pro

### Whisper X (Transcription)
- Transcribes videos to know where to cut

## Demo Results

- **Rough Cut:** 10min raw footage → 4min rough cut in ~15 minutes
- **Motion Graphics:** Complex animated graphic created in ~17 minutes, first try
- Applied audio presets automatically (amplify + hard limiter)

## Key Insight

> "Claude video editor does not replace creativity. It's replacing the execution — the 1+1 technical aspects of video editing."

- AI replaces busy work, not ideas
- Content creators limited by creativity, not technical knowledge
- Software engineers better at vibe coding because they understand the craft
- Same applies to video editors using AI tools

## Links

- [Skool Community](https://www.skool.com/leveragelab/about)
- [HyperFrames](https://github.com/heygen-com/hyperframes)
- [Premiere Pro MCP](https://github.com/hetpatel-11/Adobe_Premiere_Pro_MCP)

## Related Pages

- [[Claude Code]]
- [[MCP (Model Context Protocol)]]
- [[AI Video Editing]]
- [[HyperFrames]]
- [[Premiere Pro MCP]]
