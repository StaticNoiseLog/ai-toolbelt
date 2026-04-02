Playbooks for AI Agents
=======================

These playbooks define how I collaborate with coding LLMs across three explicit project phases: requirements
engineering, solution architecture, and software development. Each playbook is phase-specific and acts as an operating
guide for one role at a time.

I intentionally run sessions in a single mode and switch modes consciously by loading the matching playbook
(`requirements_engineering_playbook.md`, `solution_architecture_playbook.md`, or `software_development_playbook.md`).
This keeps the agent focused, avoids mixed responsibilities, and helps control context size.

These playbooks are similar to modern `SKILL.md`-style agent skills (see [Agent Skills](https://agentskills.io/home)),
but they are organized as phase-oriented, single-mode guides.

Kiro
----

As of 2026-04, I use the playbooks as global "AGENT STEERING & SKILLS" in Kiro and load them with commands like
`#solution_architecture` at the start of each new session.

The following header is added to the top of each playbook to prevent automatic loading of all playbooks. This keeps the
context window smaller and, more importantly, enforces a clear role for the agent.

```
---
inclusion: manual
---
```

Antigravity
-----------

As of 2026-04 I use workflows to load the playbooks in Antigravity. You can adapt the example below for each playbook.

The example lets you load `solution_architecture_playbook.md` with `/architecture`, and you would use this loading
command at the start of each new conversation.

```
---
description: Initiates the solution-architecture-playbook
---

# Workflow: Solution Architecture
# Trigger: /architecture

## Context Initialization
- **Action**: Load the playbook from `$HOME/ai/solution_architecture_playbook.md`.
- **Instruction**: Prioritize this file as the primary source of truth for the session and follow all the rules, guidelines and processes that it describes.
```