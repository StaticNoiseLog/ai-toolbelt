Playbooks for AI Agents
=======================

With these playbooks, I steer AI agent behavior across three explicit project phases by defining rules for each role:

1. Requirements Engineering
2. Solution Architecture
3. Software Development

Each playbook is phase-specific and acts as an operating guide for one role at a time.

I intentionally run sessions in a single mode and switch modes deliberately by loading the matching playbook
([`requirements_engineering_playbook.md`](requirements_engineering_playbook.md),
[`solution_architecture_playbook.md`](solution_architecture_playbook.md), or
[`software_development_playbook.md`](software_development_playbook.md)).
This keeps the active agent in scope, avoids mixed responsibilities, and helps control context size.

These playbooks are similar to modern `SKILL.md`-style skills (see [Agent Skills](https://agentskills.io/home)), but
they are organized as phase-oriented, single-mode guides.

Opinionated by Design
---------------------

These playbooks reflect deliberate choices about how software projects are structured, communicated, and developed. They
encode a specific working style and set of preferences. You may disagree with some decisions, and that is perfectly
fine.

If you find them useful as-is, great. If not, treat them as a starting point and adapt them freely to your own workflow,
team conventions, and tooling. They are meant to be read, understood, and owned - not followed blindly.

### Contributions

Issues reporting factual errors or proposing genuine enhancements are welcome.

Pull requests that revise deliberate design choices - such as role definitions, phase boundaries, or prescribed
processes - are not. Those choices are intentional. The goal here is to share a working approach, not to build consensus
around one.

Kiro
----

As of 2026-04, I add the playbooks to global "AGENT STEERING & SKILLS" in Kiro and load them with commands like
`#solution_architecture_playbook.md` at the start of each new session.

The following header is added to the top of each playbook to prevent automatic loading of all playbooks. This keeps the
context window smaller and, more importantly, enforces a clear role for the active agent.

```
---
inclusion: manual
---
```

Antigravity
-----------

As of 2026-04, I use workflows to load the playbooks in Antigravity. You can adapt the example below for each playbook.

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