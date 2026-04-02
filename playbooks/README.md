Playbooks for AI Agents
=======================

Antigravity
-----------

As of 2026-04 I use workflows to load the playbooks in Antigravity. You can adapt the example below for each playbook.

The example lets you load solution_architecture_playbook.md with `/architecture` and you would use this loading command
at the start of each new conversation.

```aiignore
---
description: Initiates the solution-architecture-playbook
---

# Workflow: Solution Architecture
# Trigger: /architecture

## Context Initialization
- **Action**: Load the playbook from `$HOME/ai/solution_architecture_playbook.md`.
- **Instruction**: Prioritize this file as the primary source of truth for the session and follow all the rules, guidelines and processes that it describes.
```