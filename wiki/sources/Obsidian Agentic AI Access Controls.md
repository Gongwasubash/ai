---
title: "Obsidian + Agentic AI — Full Hermes Obsidian Workflow & Wiki Prep"
source_file: "Clippings/Obsidian + Agentic AI — Full Hermes Obsidian Workflow & Wiki Prep.md"
date_ingested: 2026-09-04
tags:
  - obsidian
  - hermes
  - access-controls
  - docker
  - version-control
---

# Obsidian Agentic AI Access Controls

Source: [YouTube](https://www.youtube.com/watch?v=znj-WpMj1dI) by [[Wanderloots]]

## Summary

How to set up Obsidian with agentic AI using a three-tier access control system. One vault, two views: human & agent. The agent sees & touches only what you let it.

## Three Access Levels

1. **Private** — agent can't see it at all (Docker masks with empty folder)
2. **Read Only** — agent can read but not modify (Docker mount with `:ro`)
3. **Read + Write** — agent can do anything (default)

## Implementation Methods

### Skills (Soft Layer)
- Add access rules to the Obsidian skill markdown file
- Weak: agent might ignore rules, especially after context compression

### Docker Mount Controls (Recommended)
- `config.yml` → `mcpasshrough` section
- Mount host path to container path with mode: nothing, read-only, or read-write
- **Masking**: mount an empty folder over the private vault folder
- Stronger than skills — enforced at system level

### Host Computer Level
- OS-level commands to limit agent access
- Most secure but complex and OS-dependent

## Setup Steps

1. Create Obsidian vault in Hermes workspace
2. Create 3 folders: private/, readonly/, readwrite/
3. Set environment variable for vault path
4. If Docker: pass through vault path in config.yml
5. Add Docker volume mounts with appropriate modes
6. Initialize Git for version control (undo button)
7. Test access levels

## Version Control

- Initialize Git repo in vault root
- Make commits before/after big changes
- Roll back to any point if agent messes up

## Profile-Based Controls

- Different Hermes profiles can have different access levels
- Example: OpenAI profile = no vault access; local Gemma profile = full access

## Related

- [[Hermes Agent]]
- [[Obsidian Access Controls]]
- [[Wanderloots]]
- [[LLM Wiki]]
