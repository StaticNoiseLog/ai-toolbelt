# Software Factory Building Blocks: State of the Art (July 2026)

**Research Question**: What are the best open-source building blocks for creating a "software factory" with cooperating AI agents, feedback loops, and hooks for external tools, supporting multiple LLM vendors (including OpenRouter and local AIs), with professional-grade performance and without enforcing specific workflows?

---

## Executive Summary

Based on research conducted in July 2026, the following frameworks emerge as the **top candidates** for building your software factory, ranked by alignment with your requirements:

### 🥇 **Tier 1: Best Overall Fits**


| Framework                                                   | Language  | Multi-Agent     | LLM Agnostic    | Performance | Workflow Flexibility | MCP Support | Production Ready |
| ----------------------------------------------------------- | --------- | --------------- | --------------- | ----------- | -------------------- | ----------- | ---------------- |
| **[Rig](https://rig.rs/)**                                  | Rust      | ✅ Yes           | ✅ 20+ providers | ⭐⭐⭐⭐⭐       | ⭐⭐⭐⭐⭐                | ✅ Yes       | ✅ Enterprise     |
| **[rs-graph-llm](https://github.com/a-agmon/rs-graph-llm)** | Rust      | ✅ Graph-based   | ✅ Via Rig       | ⭐⭐⭐⭐⭐       | ⭐⭐⭐⭐⭐                | ✅ Yes       | ✅ 99.99% uptime  |
| **[LangGraph](https://www.langchain.com/langgraph)**        | Python/JS | ✅ Cyclic graphs | ✅ Via LangChain | ⭐⭐⭐⭐        | ⭐⭐⭐⭐⭐                | ✅ Yes       | ✅ Production     |


### 🥈 **Tier 2: Strong Contenders with Trade-offs**


| Framework                                             | Language | Multi-Agent   | LLM Agnostic     | Performance | Workflow Flexibility | MCP Support | Production Ready |
| ----------------------------------------------------- | -------- | ------------- | ---------------- | ----------- | -------------------- | ----------- | ---------------- |
| **[ADK-Rust](https://github.com/zavora-ai/adk-rust)** | Rust     | ✅ Modular     | ✅ Model-agnostic | ⭐⭐⭐⭐⭐       | ⭐⭐⭐⭐⭐                | ✅ Yes       | ✅ Production     |
| **[CrewAI](https://www.crewai.com/)** + AMP           | Python   | ✅ Role-based  | ✅ Multiple       | ⭐⭐⭐         | ⭐⭐⭐⭐                 | ✅ Yes       | ✅ With AMP       |
| **[Agno](https://github.com/agnostack/agno)**         | Python   | ✅ Coordinator | ✅ Yes            | ⭐⭐⭐⭐⭐       | ⭐⭐⭐⭐                 | Limited     | ✅ Production     |


### 🥉 **Tier 3: Specialized Components**

- **Model Context Protocol (MCP)**: Universal connector for external tools (⭐⭐⭐⭐⭐)
- **Microsoft Agent Framework**: Merged AutoGen + Semantic Kernel (Enterprise focus)

---

## 🎯 **Recommendation Matrix**

### For Your Specific Requirements:


| Requirement                      | Best Match                                     | Why                                            |
| -------------------------------- | ---------------------------------------------- | ---------------------------------------------- |
| **Rust-based, high performance** | Rig, rs-graph-llm, ADK-Rust                    | Native Rust, memory safety, production-grade   |
| **Multi-LLM vendor support**     | Rig (20+ providers), LangGraph (via LangChain) | Unified APIs, easy switching                   |
| **Feedback loops & iterations**  | LangGraph, rs-graph-llm                        | Native cyclic graph support, state persistence |
| **External tool hooks**          | All Tier 1 + MCP                               | MCP provides standardized integration          |
| **No enforced workflow**         | Rig, rs-graph-llm, ADK-Rust                    | Minimal opinions, maximum flexibility          |
| **AI-to-AI review cycles**       | LangGraph, CrewAI                              | Built-in multi-agent coordination              |


**Primary Recommendation**: **Start with Rig + rs-graph-llm** for the Rust foundation, then integrate LangGraph for complex orchestration patterns. Use MCP for all external tool integrations.

---

## Detailed Framework Analysis

### 🏆 **Rig (0xPlaygrounds/rig)**

**⭐⭐⭐⭐⭐ Best for: High-performance Rust foundation**

- **Language**: Rust
- **Stars**: ~6,700 (July 2026)
- **License**: Open source
- **Key Features**:
    - Unified API across **20+ LLM providers** (OpenAI, Anthropic, OpenRouter, local models via OpenRouter, etc.)
    - Type-safe tools and structured output
    - Multi-agent workflows with multi-turn streaming
    - **MCP server support** built-in
    - OpenTelemetry observability
    - 10+ vector store integrations
    - Production deployments at Cloudflare, Neon, Nethermind, St.
- **Performance**: ~10MB memory, ~4MB binary, ~50ms cold start
- **Workflow Control**: Full flexibility - you define the orchestration logic
- **Feedback Loops**: Can be implemented via state management and custom logic
- **External Hooks**: Native support for MCP servers, tools, vector stores

**Pros**:

- Professional Rust quality with memory safety guarantees
- No enforced workflow - complete control
- Excellent multi-provider support
- Production-ready with enterprise adopters
- Small binary size, fast startup

**Cons**:

- Requires Rust knowledge
- Multi-agent orchestration requires more manual setup than dedicated frameworks

**Verdict**: **Primary foundation** for your software factory. Combines Rust performance with LLM agnosticism and MCP support.

---

### 🏆 **rs-graph-llm (a-agmon/rs-graph-llm)**

**⭐⭐⭐⭐⭐ Best for: Graph-based multi-agent orchestration in Rust**

- **Language**: Rust
- **Version**: v1.4.2 (July 2026)
- **License**: MIT
- **Key Features**:
    - Graph execution library for **complex, stateful workflows**
    - Type-safe and flexible framework
    - **Distributed execution** with reported 99.99% uptime in logistics deployments
    - Integrates with Rig crate for LLM capabilities
    - Supports cyclic graphs for feedback loops
    - Built from ground up in Rust (not a Python port)
- **Architecture**: graph-flow (core execution) + Rig (LLM integration)

**Pros**:

- Native Rust performance and safety
- Explicit support for cyclic workflows (feedback loops)
- Production-proven reliability
- Type-safe agent orchestration
- Seamless integration with Rig

**Cons**:

- Smaller community than Python alternatives
- Requires understanding of graph-based orchestration

**Verdict**: **Perfect complement to Rig** for implementing your feedback loops and multi-agent coordination. Together they provide a complete Rust-based solution.

---

### 🏆 **LangGraph**

**⭐⭐⭐⭐⭐ Best for: Stateful, cyclic multi-agent workflows**

- **Language**: Python, JavaScript
- **Stars**: 126,000+ (April 2026)
- **Version**: 1.1.6 (April 2026)
- **License**: Apache 2.0
- **Key Features**:
    - **Graph-based orchestration** with native cycle support
    - **Persistent state** management (SQLite, PostgreSQL, in-memory)
    - **Human-in-the-loop** controls with interrupt_before/after
    - **Cyclic reasoning loops**: reason → act → observe → repeat
    - **Multi-agent coordination**: Supervisor patterns with specialist agents
    - **Durable execution**: Survives crashes, pause/resume
    - Built on LangChain (inherits 1,000+ integrations)
    - **MCP support** via LangChain
- **Production**: 90M+ monthly downloads, used by Uber, JP Morgan, BlackRock, Cisco, LinkedIn, Klarna

**Pros**:

- Most mature multi-agent orchestration framework
- Native support for feedback loops and iterations
- Excellent state management
- Human review integration points
- Large ecosystem and community

**Cons**:

- Python-based (not Rust)
- Can be complex for simple use cases

**Verdict**: **Best for orchestration layer** if you need the most mature multi-agent system. Can be used alongside Rust frameworks via MCP or API.

---

### 🥈 **ADK-Rust (Agent Development Kit)**

**⭐⭐⭐⭐ Strong contender: Modular Rust framework**

- **Language**: Rust
- **License**: Open source
- **Key Features**:
    - Model-agnostic, deployment-agnostic
    - Modular components for models, tools, memory, real-time voice
    - **Template system**: tools, rag, api, openai, a2a, graph, realtime, sequential, parallel, loop
    - **Addons**: telemetry, auth, sessions, memory, mcp, guardrails, eval, browser, server
    - Optimized for frontier AI models
    - Production-ready with 70+ example agents
- **2026 Roadmap**: Active development with community input

**Pros**:

- Extremely modular and flexible
- Excellent addon ecosystem
- Production-focused
- Model-agnostic by design

**Cons**:

- Newer than Rig (less battle-tested)
- Smaller community

**Verdict**: **Excellent alternative to Rig** if you prefer a more modular, addon-based approach.

---

### 🥈 **CrewAI + AMP**

**⭐⭐⭐⭐ Strong contender: Role-based orchestration**

- **Language**: Python
- **Stars**: 52,800+ (2026)
- **License**: MIT
- **Key Features**:
    - **Role-based agent definition**: Define agents as team members with distinct roles, goals, tools
    - **Collaborative task execution**: Agents work together on complex tasks
    - **AMP (Agent Management Platform)**: Production deployment and management
    - Streaming tool call events (added January 2026)
    - Simple implementation without complex dependencies
- **Use Case**: Natural mapping to team workflows

**Pros**:

- Intuitive role-based design
- Good for collaborative multi-agent scenarios
- AMP provides production features
- Large community

**Cons**:

- Python-based
- Less low-level control than graph-based frameworks
- AMP is paid for advanced features

**Verdict**: **Good choice** if you prefer role-based abstraction over explicit graph orchestration.

---

### 🥈 **Agno**

**⭐⭐⭐⭐ Strong contender: High-performance agents**

- **Language**: Python
- **Key Features**:
    - **Lightweight, high-performance**: Agents run in under 2 microseconds
    - Built-in memory (short-term and long-term via vector stores)
    - Structured tool definitions
    - Multimodal inputs (text, images, audio, video)
    - Reasoning layer for step-by-step thinking
    - **Coordinator pattern** for multi-agent teams
    - Minimal framework overhead

**Pros**:

- Exceptional performance
- Minimal overhead
- Good for production environments

**Cons**:

- Python-based
- Smaller community than LangGraph/CrewAI

**Verdict**: **Best for performance-critical Python deployments** where raw speed matters.

---

## 🔧 **Model Context Protocol (MCP)**

**⭐⭐⭐⭐⭐ Essential: Universal tool integration**

- **Status**: Open standard (Anthropic, Nov 2024)
- **Adoption**: OpenAI, Google DeepMind, Sourcegraph, Replit, Zed, and many others
- **Transport**: JSON-RPC 2.0
- **Architecture**:
    - **MCP Host**: AI agent that interacts with LLM
    - **MCP Clients**: Created by host for each server
    - **MCP Servers**: Provide tools/resources (local or remote)

**Key Features**:

- Standardized framework for integrating AI with external data/tools
- Model-agnostic universal interface
- Supports reading files, executing functions, processing context
- SDKs in Python, TypeScript, Java, C#, Rust (via Rig)
- **MCP Apps**: Extension for interactive UIs (dashboards, forms)

**For Your Software Factory**:

- **Create MCP servers** for your static analysis tools (detekt, ktlint, etc.)
- **Use MCP servers** for IDE integration, code repositories, databases
- **Rig already supports MCP** - seamless integration
- **LangChain supports MCP** - works with LangGraph

**Verdict**: **Mandatory component** for standardized external tool integration.

---

## 🏭 **Architecture Recommendations**

### Option 1: Pure Rust Stack (Recommended)

```
┌─────────────────────────────────────────────────────────────┐
│                    Your Software Factory                      │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  ┌─────────────┐    ┌─────────────┐    ┌─────────────────┐  │
│  │  Rig         │    │ rs-graph-llm│    │  Custom Agents  │  │
│  │  (LLM Core)  │◄──►│ (Orchestration) │◄──►│  (Your Playbooks)│  │
│  └─────────────┘    └─────────────┘    └─────────────────┘  │
│           ▲                  ▲                    ▲            │
│           │                  │                    │            │
│  ┌───────────────────────────────────────────────────────┐  │
│  │                 MCP Servers Layer                      │  │
│  │  ┌─────────┐  ┌─────────┐  ┌─────────┐  ┌─────────┐  │  │
│  │  │ Static   │  │  Code    │  │  Database│  │  Custom  │  │  │
│  │  │ Analysis │  │ Repos   │  │  Query   │  │  Tools   │  │  │
│  │  │ (detekt) │  │         │  │          │  │          │  │  │
│  │  └─────────┘  └─────────┘  └─────────┘  └─────────┘  │  │
│  └───────────────────────────────────────────────────────┘  │
│                                                             │
│  ┌───────────────────────────────────────────────────────┐  │
│  │              Feedback Loop Implementation                │  │
│  │                                                           │  │
│  │  Agent A ──► Review ──► Agent B ──► Review ──► Human   │  │
│  │                    ↓                    ↓               │  │
│  │                 [Iterate if needed]                    │  │
│  │                                                           │  │
│  └───────────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────────┘
```

**Components**:

- **Rig**: Core LLM integration with 20+ providers
- **rs-graph-llm**: Graph-based orchestration with cyclic support
- **Custom Agents**: Your playbook-based agents (requirements engineer, architect, developer)
- **MCP Servers**: Wrappers for static analysis tools, code repos, etc.
- **Feedback Loops**: Implemented as cyclic graphs in rs-graph-llm

**Advantages**:

- Pure Rust performance and safety
- No enforced workflow
- Full control over agent behavior
- Native MCP support
- Production-ready

---

### Option 2: Hybrid Rust + Python Stack

```
┌─────────────────────────────────────────────────────────────┐
│                    Your Software Factory                      │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  ┌─────────────┐    ┌─────────────┐    ┌─────────────────┐  │
│  │  Rig         │    │ LangGraph   │    │  Custom Agents  │  │
│  │  (Rust/LLM)  │◄──►│ (Orchestration) │◄──►│  (Your Playbooks)│  │
│  └─────────────┘    └─────────────┘    └─────────────────┘  │
│           ▲                  ▲                    ▲            │
│           │                  │                    │            │
│  ┌───────────────────────────────────────────────────────┐  │
│  │                 MCP Servers Layer                      │  │
│  │  (Shared between Rust and Python components)             │  │
│  └───────────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────────┘
```

**Components**:

- **Rig**: Rust-based LLM core for performance-critical operations
- **LangGraph**: Python-based orchestration for complex multi-agent workflows
- **Custom Agents**: Mixed Rust/Python agents
- **MCP**: Bridge between Rust and Python components

**Advantages**:

- Best of both worlds: Rust performance + Python ecosystem
- LangGraph has the most mature multi-agent orchestration
- MCP provides seamless integration

**Disadvantages**:

- More complex deployment
- Language boundary to manage

---

### Option 3: Python-Only Stack

```
┌─────────────────────────────────────────────────────────────┐
│                    Your Software Factory                      │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  ┌─────────────┐    ┌─────────────┐    ┌─────────────────┐  │
│  │ LangChain   │    │ LangGraph   │    │  Custom Agents  │  │
│  │ (LLM Core)  │◄──►│ (Orchestration) │◄──►│  (Your Playbooks)│  │
│  └─────────────┘    └─────────────┘    └─────────────────┘  │
│           ▲                  ▲                    ▲            │
│           │                  │                    │            │
│  ┌───────────────────────────────────────────────────────┐  │
│  │                 MCP Servers Layer                      │  │
│  └───────────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────────┘
```

**Components**:

- **LangChain**: LLM core with 1,000+ integrations
- **LangGraph**: Orchestration layer
- **Custom Agents**: Python-based agents
- **MCP**: External tool integration

**Advantages**:

- Largest ecosystem
- Most mature orchestration (LangGraph)
- Easiest to find resources and examples

**Disadvantages**:

- Python performance limitations
- Less control over low-level behavior

---

## 🔄 **Feedback Loop Implementation Strategies**

### Strategy 1: Graph-Based Cycles (Recommended)

Both **rs-graph-llm** and **LangGraph** support cyclic graphs natively:

```python
# LangGraph example - cyclic review loop
from langgraph.graph import StateGraph

class ReviewState:
    code: str
    reviews: list
    iterations: int
    approved: bool

def generate_code(state):
    # Agent generates code
    return {"code": generated_code, "iterations": state.iterations + 1}

def review_code(state):
    # Reviewer agent checks code
    reviews = [reviewer_agent.review(state.code) for reviewer_agent in reviewers]
    if all_approved(reviews):
        return {"approved": True, "reviews": reviews}
    return {"approved": False, "reviews": reviews}

def needs_revision(state):
    return not state.approved and state.iterations < MAX_ITERATIONS

workflow = StateGraph(ReviewState)
workflow.add_node("generate", generate_code)
workflow.add_node("review", review_code)
workflow.add_conditional_edges(
    "review",
    needs_revision,
    {"continue": "generate", "end": END}
)
```

### Strategy 2: Supervisor Pattern

**LangGraph** excels at supervisor patterns:

```python
# Supervisor delegates to specialist agents
supervisor = Agent(
    prompt="You are a supervisor. Delegate tasks to specialists.",
    tools=[delegate_to_requirements_engineer, delegate_to_architect, delegate_to_developer]
)

# Each specialist is a sub-graph with its own feedback loop
requirements_engineer = StateGraph(...)
architect = StateGraph(...)
developer = StateGraph(...)
```

### Strategy 3: Interrupt-Based Human Review

**LangGraph** provides built-in interruption points:

```python
# Pause for human review at critical points
workflow.add_node("human_review", human_approval_gate)
workflow.add_edge("review", "human_review")

# interrupt_before: Pause before tool execution
# interrupt_after: Pause after node completes for content review
```

---

## 🛠️ **External Tool Integration**

### MCP Server Implementation

Create MCP servers for your static analysis tools:

```rust
// Example: detekt MCP server in Rust
use rig::mcp::{McpServer, Tool};

struct DetektTool;

impl Tool for DetektTool {
    fn name(&self) -> &str { "run_detekt" }
    
    fn description(&self) -> &str { 
        "Run detekt static analysis on Kotlin code"
    }
    
    async fn execute(&self, params: serde_json::Value) -> Result<String> {
        // Execute detekt via shell
        let output = std::process::Command::new("detekt")
            .args(["--input", &params["path"], "--config", &params["config"]])
            .output()?;
        
        Ok(String::from_utf8(output.stdout)?)
    }
}

// Register with Rig's MCP server
let mcp_server = McpServer::new()
    .add_tool(DetektTool);
```

### Shell Script Wrapper Pattern

For tools that can't be easily integrated:

```bash
#!/bin/bash
# mcp-detekt-server.sh

# Read MCP request from stdin
# Execute detekt
# Return results as JSON

detekt --input "$1" --config "$2" --format json
```

Then create a simple MCP server that calls this script.

---

## 📊 **Comparison Matrix**

### Performance Comparison (2026 Study)


| Framework    | Memory Crashes | Latency   | Race Conditions | Binary Size |
| ------------ | -------------- | --------- | --------------- | ----------- |
| Rust-based   | 78% fewer      | 45% lower | 60% fewer       | ~4-10MB     |
| Python-based | Baseline       | Baseline  | Baseline        | ~50-100MB   |


*Source: dasroot.net Rust LLM Orchestration Study, 2026*

### Feature Comparison


| Feature              | Rig         | rs-graph-llm | LangGraph | ADK-Rust | CrewAI  | Agno |
| -------------------- | ----------- | ------------ | --------- | -------- | ------- | ---- |
| Multi-Agent          | ✅           | ✅            | ✅         | ✅        | ✅       | ✅    |
| Cyclic Workflows     | ⚠️ (Manual) | ✅            | ✅         | ✅        | ⚠️      | ⚠️   |
| LLM Agnostic         | ✅ 20+       | ✅            | ✅         | ✅        | ✅       | ✅    |
| MCP Support          | ✅           | ✅            | ✅         | ✅        | ✅       | ⚠️   |
| Rust-Based           | ✅           | ✅            | ❌         | ✅        | ❌       | ❌    |
| Type Safety          | ✅           | ✅            | ⚠️        | ✅        | ❌       | ⚠️   |
| Production Ready     | ✅           | ✅            | ✅         | ✅        | ✅ (AMP) | ✅    |
| Workflow Flexibility | ✅           | ✅            | ✅         | ✅        | ⚠️      | ✅    |
| Community Size       | ⭐⭐⭐         | ⭐⭐           | ⭐⭐⭐⭐⭐     | ⭐⭐       | ⭐⭐⭐⭐    | ⭐⭐⭐  |
| Learning Curve       | ⭐⭐⭐         | ⭐⭐⭐⭐         | ⭐⭐        | ⭐⭐⭐⭐     | ⭐       | ⭐⭐   |


---

## 🚀 **Getting Started Roadmap**

### Phase 1: Foundation (Weeks 1-2)

1. **Choose primary stack**: Rig + rs-graph-llm (Rust) or LangGraph (Python)
2. **Set up MCP infrastructure**:
- Install MCP SDK for your language
- Create MCP servers for your static analysis tools
- Test MCP integration with simple agents
3. **Implement first agent**:
- Start with your requirements engineer playbook
- Test LLM provider switching (OpenRouter, local models)

### Phase 2: Orchestration (Weeks 3-4)

1. **Add multi-agent coordination**:
- Implement cyclic feedback loops
- Set up agent-to-agent review system
- Configure iteration limits and quality gates
2. **Integrate external tools**:
- Connect static analysis MCP servers
- Add code repository access
- Set up build system hooks

### Phase 3: Productionization (Weeks 5-6)

1. **Implement human review gates**:
- Configure interruption points for final approval
- Set up notification system (email, Slack, etc.)
2. **Add observability**:
- OpenTelemetry integration (Rig has built-in support)
- Logging and metrics for agent performance
3. **Optimize performance**:
- Fine-tune agent configurations
- Optimize MCP server performance

### Phase 4: Scaling (Ongoing)

1. **Add more agents**: Solutions architect, software developer
2. **Expand tool integration**: More static analysis, security scanners, etc.
3. **Implement advanced patterns**: Supervisor agents, parallel execution

---

## 📚 **Key Resources**

### Official Documentation

- [Rig Documentation](https://rig.rs/)
- [rs-graph-llm GitHub](https://github.com/a-agmon/rs-graph-llm)
- [LangGraph Documentation](https://www.langchain.com/langgraph)
- [ADK-Rust GitHub](https://github.com/zavora-ai/adk-rust)
- [CrewAI Documentation](https://www.crewai.com/)
- [Agno GitHub](https://github.com/agnostack/agno)
- [Model Context Protocol](https://modelcontextprotocol.io/)

### Tutorials & Guides

- [LangGraph Tutorial 2026](https://www.metacto.com/blogs/a-developer-s-guide-to-langgraph-building-stateful-controllable-llm-applications)
- [Rust AI Agent Frameworks Research](https://zylos.ai/research/2026-03-31-rust-ai-agent-frameworks-infrastructure/)
- [Rust Libraries for LLM Orchestration 2026](https://dasroot.net/posts/2026/02/rust-libraries-llm-orchestration-2026/)
- [Building AI Agents from Scratch in Rust](https://rustify.rs/articles/rust-ai-agents-from-scratch-2026)

### Community & Support

- Rig Discord/Slack: Check GitHub README
- LangChain Discord: Large, active community
- MCP Discussion: [GitHub Discussions](https://github.com/modelcontextprotocol/specification/discussions)

---

## ⚖️ **Decision Factors**

### Choose **Rig + rs-graph-llm** if:

- ✅ You want **maximum performance and safety** (Rust)
- ✅ You need **full control** over workflows
- ✅ You're comfortable with **Rust development**
- ✅ You want **minimal runtime overhead**
- ✅ You need **production-grade reliability**

### Choose **LangGraph** if:

- ✅ You want the **most mature orchestration** framework
- ✅ You need **quick time-to-market** with large ecosystem
- ✅ You prefer **Python development**
- ✅ You want **built-in cyclic workflow** support
- ✅ You need **extensive examples and documentation**

### Choose **ADK-Rust** if:

- ✅ You want a **modular, addon-based** approach
- ✅ You need **real-time voice** capabilities
- ✅ You prefer **template-driven** development

### Choose **CrewAI** if:

- ✅ You want **role-based abstraction** (natural for team workflows)
- ✅ You need **production management** (AMP platform)
- ✅ You prefer **simplicity** over low-level control

---

## 🎯 **Final Recommendation**

**Start with: Rig + rs-graph-llm + MCP**

This combination gives you:

1. **Rust performance and safety** for your core infrastructure
2. **Graph-based orchestration** for complex feedback loops
3. **Multi-LLM vendor support** (20+ providers including OpenRouter)
4. **MCP integration** for all external tools
5. **Zero enforced workflow** - you control everything
6. **Production-ready** components with enterprise adoption

**Implementation Path**:

1. Build your agents using Rig's LLM core
2. Use rs-graph-llm for orchestration and feedback loops
3. Create MCP servers for static analysis tools (detekt, ktlint, etc.)
4. Implement your playbook-based agents with full control
5. Add human review gates at the final approval stage

**Alternative**: If Rust expertise is a constraint, use **LangGraph + MCP** as a Python-based alternative with similar capabilities.

---

## 📅 **Next Steps**

1. **Evaluate Rig**: Clone the repository, try the examples, verify OpenRouter integration
2. **Experiment with rs-graph-llm**: Build a simple cyclic workflow
3. **Create MCP server prototype**: Wrap one static analysis tool (e.g., detekt)
4. **Design your agent architecture**: Map your playbooks to the chosen framework
5. **Start small**: Implement one agent with a simple feedback loop first

---

*Research conducted: July 3, 2026*  
*Sources: GitHub, official documentation, technical blogs, research papers, and community discussions*