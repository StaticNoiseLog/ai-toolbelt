Playbooks for AI Agents
=======================

These playbooks define how I collaborate with coding LLMs across three explicit project phases:
requirements engineering, solution architecture, and software development. Each playbook is
phase-specific and acts as an operating guide for one role at a time.

I intentionally run sessions in a single mode and switch modes consciously by loading the matching
playbook (`requirements_engineering_playbook.md`, `solution_architecture_playbook.md`, or
`software_development_playbook.md`). This keeps the agent focused, avoids mixed responsibilities,
and helps control context size. Conceptually, these playbooks are similar to modern agent skills
(`SKILL.md`-style guidance), but organized as phase-oriented playbooks.

Kiro
----

As of 2026-04 I add the playbooks as global "AGENT STEERING & SKILLS" in Kiro and load them with commands lik
`#solution_architecture` at the start of each new session.

The following header is added to the top of each playbook to prevent automatic loading of all playbooks. One hand this
keeps the context window smaller, but - more importantly - it enforces a clear role for the agents.

```
---
inclusion: manual
---
```

Antigravity
-----------

As of 2026-04 I use workflows to load the playbooks in Antigravity. You can adapt the example below for each playbook.

The example lets you load solution_architecture_playbook.md with `/architecture` and you would use this loading command
at the start of each new conversation.

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