# AI Engineer World Fair 2026 — Day 3 (Day 4 of event)

## Quick Reference: Session Overview

| # | Speaker(s) | Organization | Topic | Focus Area |
|----|-----------|--------------|-------|-----------|
| 1 | Bar Yaron | Amplify | State of AI Engineering 2026 Survey | Industry Survey |
| 2 | John Ousterhout | Stanford | HOMA Network Protocol | Infrastructure |
| 3 | Maxime Rivest, Isaac Miller | DSPy | Task-Model Separation | Framework Design |
| 4 | Tariq Shihab-Eldin, others | Various | Fable & Future of Claude | Model Strategy |
| 5 | Sponsor | - | Ontology-Based Semantic Layers | Enterprise Systems |
| 6 | - | - | RL-Guided ETL Failure Remediation | Data Engineering |
| 7 | - | - | Token Allocation Strategies | Cost Optimization |
| 8 | - | - | Personal AI Research OS | Software Factories |
| 9 | - | - | MCP, CLI, Skills: Tooling Comparison | Agent Tooling |

**Track:** Harness Engineering & Software Factories  
**MC:** Ralph Chabri (Replit)  
**Date/Time:** ~09:50–14:30+

---

- [AI Engineer World Fair 2026 — Day 3 (Day 4 of event)](#ai-engineer-world-fair-2026--day-3-day-4-of-event)
  - [Session 1 — State of AI Engineering 2026 Survey](#session-1--state-of-ai-engineering-2026-survey)
    - [Summary](#summary)
    - [Highlights](#highlights)
    - [Follow-up Items](#follow-up-items)
    - [Important Questions](#important-questions)
  - [Session 2 — Latency Matters: HOMA Network Protocol for AI Workloads](#session-2--latency-matters-homa-network-protocol-for-ai-workloads)
    - [Summary](#summary-1)
    - [Highlights](#highlights-1)
    - [Follow-up Items](#follow-up-items-1)
    - [Important Questions](#important-questions-1)
  - [Session 3 — DSPy: The Unreasonable Effectiveness of Separating Task from Model](#session-3--dspy-the-unreasonable-effectiveness-of-separating-task-from-model)
    - [Summary](#summary-2)
    - [Highlights](#highlights-2)
    - [Follow-up Items](#follow-up-items-2)
    - [Important Questions](#important-questions-2)
  - [Session 4 — Fireside Chat: Building with Fable \& the Future of Claude](#session-4--fireside-chat-building-with-fable--the-future-of-claude)
    - [Summary](#summary-3)
    - [Highlights](#highlights-3)
    - [Follow-up Items](#follow-up-items-3)
    - [Important Questions](#important-questions-3)
  - [Session 5 — Ontology-Based Semantic Layers for Enterprise Agents (Sponsor Talk)](#session-5--ontology-based-semantic-layers-for-enterprise-agents-sponsor-talk)
    - [Summary](#summary-4)
    - [Highlights](#highlights-4)
    - [Follow-up Items](#follow-up-items-4)
    - [Important Questions](#important-questions-4)
  - [Session 6 — RL-Guided ETL Failure Remediation (Breakout/Lightning)](#session-6--rl-guided-etl-failure-remediation-breakoutlightning)
    - [Summary](#summary-5)
    - [Highlights](#highlights-5)
    - [Follow-up Items](#follow-up-items-5)
    - [Important Questions](#important-questions-5)
  - [Session 7 — Tokens Should Have Jobs: Token Allocation Strategies for Agents](#session-7--tokens-should-have-jobs-token-allocation-strategies-for-agents)
    - [Summary](#summary-6)
    - [Highlights](#highlights-6)
    - [Follow-up Items](#follow-up-items-6)
    - [Important Questions](#important-questions-6)
  - [Session 8 — Building a Personal AI Research OS (Software Factories Track)](#session-8--building-a-personal-ai-research-os-software-factories-track)
    - [Summary](#summary-7)
    - [Highlights](#highlights-7)
    - [Follow-up Items](#follow-up-items-7)
    - [Important Questions](#important-questions-7)
  - [Session 9 — MCP, CLI, and Skills: Choosing the Right Agent Tooling Layer (Software Factories Track)](#session-9--mcp-cli-and-skills-choosing-the-right-agent-tooling-layer-software-factories-track)
    - [Summary](#summary-8)
    - [Highlights](#highlights-8)
    - [Follow-up Items](#follow-up-items-8)
    - [Important Questions](#important-questions-8)
  - [Cross-Cutting Themes](#cross-cutting-themes)

**Theme: Harness Engineering & Software Factories**
**MC: Ralph Chabri** (Developer Relations Engineer, Replit)
**Date/Slot: ~09:50–14:30+**

---

## Session 1 — State of AI Engineering 2026 Survey

**Speaker:** Bar Yaron (Investment Partner, Amplify)
**Time:** ~00:16:18 – 00:35:44

### Summary

Bar presented the annual State of AI Engineering survey results based on 1,048 respondents. The field is characterized as a discipline rather than a job title, spanning senior engineers who are new to AI. Key findings: text modalities dominate, but audio has the highest adoption intent (56% plan to adopt, up from 37% last year). Image generation doubled in usage (18% → 36%) due to model improvements. Model choice is driven by quality, agentic capability, and cost — not open vs. closed status. 87% of teams use more than one model, and organizations are standardizing on platforms but staying flexible on models. Cost is now a first-class engineering constraint — 75% of respondents adjust usage based on cost. Agents went from 47% to 95% usage YoY, with write-enabled agents tripling. Agent control remains primitive (mostly human-in-the-loop + permission gating). Eval remains the top stack challenge for the third year running, but the margin is shrinking. 97% of builders report a net positive effect from AI, with the top benefit being cheaper experimentation. Negative effects include review burden and erosion of deep technical skills. 81% say AI is blurring lines between engineering, product, and marketing.

### Highlights

- Audio has the strongest intent-to-adopt: 56% of non-users plan to adopt
- Image generation doubled (18% → 36%) as models improved
- 94% use closed models, 45% use open-weight, but open-weight augments rather than replaces
- Cost regularly shapes how ambitiously 40% use AI; another 36% sometimes
- 95% of respondents use agents (doubled from last year); write-enabled agents tripled
- Agent guardrails still primitive: mostly human-in-the-loop and permission gating
- Evals remain #1 challenge; vibe-check reviews are still #1 evaluation method
- Non-developers shipping customer-facing features at 17% of teams
- 67% expect a leading lab to declare AGI in the next 5 years (question asks about press release, not achievement)

### Follow-up Items

- Full survey report linked during talk (amplify.com or similar)
- Check audio adoption data as a leading indicator for 2027

### Important Questions

- Will audio adoption gap close by 2027 as it did for image gen in 2026?
- How do we evolve agent control beyond "human in the loop and permission gating"?
- Is "software engineering as a solved problem" actually a meaningful question, or definition-dependent?

---

## Session 2 — Latency Matters: HOMA Network Protocol for AI Workloads

**Speaker:** John Ousterhout (Professor Emeritus, Stanford University)
**Time:** ~00:36:08 – 00:54:02

### Summary

Ousterhout argued that AI network workloads are shifting from large throughput-dominated transfers (training) toward small latency-sensitive messages (inference and agentic coordination). TCP and RDMA are poorly suited to mixed-message environments due to head-of-line blocking, sender-side congestion control instability, and stream-based data models that can't prioritize short messages. HOMA (a Stanford protocol) was designed from scratch for data centers: it is message/RPC-based (not stream-based), uses receiver-controlled congestion with grant packets, prioritizes shorter messages via SRPT (Shortest Remaining Processing Time), and takes advantage of priority queues in modern switches. Benchmark results show HOMA achieves ~13× lower P99 tail latency for short messages compared to TCP, and is nearly 2× faster even on long messages.

### Highlights

- Agentic workloads create millisecond-scale compute periods where even millisecond network synchronization delays waste significant GPU time
- TCP/RDMA congestion control is sender-side and fundamentally unstable — constant oscillation between too much and too little
- HOMA is message-based (not stream), receiver-controlled, uses SRPT, and leverages switch priority queues
- P99 short-message latency: TCP >1ms vs HOMA <100µs (~13× improvement)
- Long message latency also improved (~2×) via run-to-completion scheduling
- Available as a Linux kernel module on GitHub; Ousterhout personally works on upstreaming

### Follow-up Items

- Evaluate HOMA for inference/agentic infrastructure: <https://github.com> (search HomaModule)
- Contact John Ousterhout (<ouster@cs.stanford.edu>) if tail latency is limiting throughput
- Track kernel upstreaming progress for HOMA

### Important Questions

- At what scale does small-message tail latency become a bottleneck in agent swarms?
- How does HOMA interact with existing RDMA/RoCE deployments?
- Is receiver-side congestion control applicable in multi-tenant cloud environments?

---

## Session 3 — DSPy: The Unreasonable Effectiveness of Separating Task from Model

**Speakers:** Maxime Rivest & Isaac Miller (Core Contributor & Lead Maintainer, DSPy)
**Time:** ~00:54:21 – 01:12:21

### Summary

DSPy is an open-source Python framework that treats AI programs like software functions: reusable, composable, testable, and automatically optimizable. The core idea is separating the task specification from the implementation. A task is fully specified by three things: (1) **instructions** — what should happen (natural language + signatures); (2) **code constraints** — what must happen (hard programmatic rules); and (3) **examples/evals** — what good looks like. With this separation, developers can swap models, change prompting strategies (few-shot → chain-of-thought → agents → harness), and apply new optimization techniques without touching the external interface. DSPy 4 introduces **DSPy.flex** (learning a harness automatically for a function) and **qualitative learning** (automatically converting real-world feedback into evals). Enterprise case studies: Shopify achieved 550× cost reduction by switching to a cheaper model while retaining the same eval framework.

### Highlights

- AI programs should have fixed input/output contracts to enable internal implementation flexibility
- Three languages to specify a task: instructions (natural language), constraints (code), and evals (examples)
- DSPy can optimize prompts, few-shot examples, and now entire harnesses (DSPy.flex)
- Qualitative learning: models interpret textual production feedback and auto-update evals
- Shopify: 550× cost reduction through model swap enabled by fixed eval contracts
- Even with AGI, "last mile" domain learning remains necessary — intelligence ≠ domain knowledge
- Fully open source and open research; Discord community active

### Follow-up Items

- Explore DSPy 4 features: DSPy.flex for harness learning, qualitative learning
- Review case studies: Shopify, plus two other enterprise examples mentioned
- Check DSPy Discord for new contributed techniques (RLMs, JEPA, Better Together, GRPO)

### Important Questions

- When should you use DSPy vs hand-crafted prompt pipelines?
- How does qualitative learning handle adversarial or noisy production feedback?
- What is the latency/cost overhead of DSPy.flex at inference time?

---

## Session 4 — Fireside Chat: Building with Fable & the Future of Claude

**Speakers:** Mike Krieger (Co-founder of Instagram, Member of Technical Staff, Anthropic) interviewed by Ralph Chabri
**Time:** ~01:12:21 – 01:38:32

### Summary

Mike Krieger discussed his shift from Anthropic CPO to a hands-on builder role driven by FOMO as models improved. He described how Claude usage at Anthropic internally has evolved from task delegation to expressing end states and letting Claude work autonomously. The most notable example: porting an entire Python codebase to TypeScript over a weekend using a dynamic workflow. He introduced the "Tags" system (internal Anthropic tool now public) which enables multiplayer, async, proactive agent delegation in Slack — effectively assigning Claude ownership of code areas, monitoring channels, and proactively handling tasks. He discussed review bottlenecks (not just time but human ability to conceptualize large diffs) and how Claude Code Artifacts help by explaining intent and trade-offs. On Anthropic Labs: 2-week "persevere or pivot" review cadence, fluid pod structure, shutdowns are normal and expected. On Claude Design: next step is better integration across surfaces (chat, code, design) and blurring the line between designed artifacts and deployable apps. On mental health: take real time off; verbalize emotions; the AI field is unusually intense but it's still a long game.

### Highlights

- Fable is "way, way smarter" than Krieger — requires explaining decisions back to him
- Tags system: multiplayer async proactive Claude delegation in Slack; 60%+ of Anthropic's code written via tags
- Ported a full Python codebase to TypeScript over a weekend — "be unreasonable"
- Code review bottleneck is more conceptual than time-based; Claude Code Artifacts help communicate intent
- Labs cadence: 2-week persevere-or-pivot reviews; projects shut down regularly by design
- Product simplification opportunity: Claude Code / Cowork / Claude.ai surface distinctions confuse users
- Finance vertical: verifiability + audit logging + agentic flexibility is the key design tension
- Burnout advice: carve real time off; sports mindset (never as good as best game, never as bad as worst)

### Follow-up Items

- Try "Tags" for multiplayer async agent workflows in team Slack
- Claude Code Artifacts for PR communication — share intent and trade-offs, not just diffs
- Follow Claude Design roadmap for design-to-app pipeline
- Monitor Anthropic Labs bets: Claude Design, other surface integrations

### Important Questions

- When will Claude Code / Cowork / Claude.ai converge into fewer, more composable surfaces?
- How do you establish trust in autonomous code review without reading every line?
- What is the right "persevere or pivot" cadence for AI product teams outside Anthropic?

---

## Session 5 — Ontology-Based Semantic Layers for Enterprise Agents (Sponsor Talk)

**Speaker:** Emil Eifrem (CEO, Neo4j)
**Time:** ~01:39:57 – 01:51:00

### Summary

Eifrem introduced the problem of enterprise-scale agent data access: every agent team manually rediscovers data sources, violating DRY, with no cross-agent learning. The solution is a three-pillar ontology-based semantic layer: (1) **business ontology** — key domain concepts in human-readable form (customer, account, transaction); (2) **technical ontology** — metadata of all data assets (100 databases, Snowflake, S3, schemas); (3) **execution traces** — runtime signals from agent execution (what worked, success scores). These three pillars together create "thin agents on a smarter shared substrate": agents don't re-wire data sources; they query the ontology. Benefits: automatic data discovery, trustworthiness (top-down curated + bottom-up empirical), single governed mapping, and cross-agent self-learning. Neo4j claims deployments at a Fortune 20 global bank, a major Bay Area tech platform, and a leading fintech.

### Highlights

- Enterprise agent bottleneck: manually re-discovering and re-wiring data sources for every new agent
- Three pillars: business ontology → technical ontology → execution traces
- Agents leave traces → ontology learns which data paths succeed → agents get smarter over time
- Cross-agent learning: success patterns from one agent benefit all others
- "Thin agents on a smarter shared substrate" as the design pattern
- Markdown files alone are not sufficient (quoting Swix: "You can't vibe code with just markdown files")

### Follow-up Items

- Check Neo4j documentation on ontology-based semantic layer blueprint (QR code shared)
- Evaluate for SAP/enterprise multi-agent deployments
- Review graph + AI patterns at Neo4j booth P3 (10 patterns in graph track, Room 2005)

### Important Questions

- How does the business ontology stay in sync when domain concepts evolve?
- What tooling builds and maintains the technical ontology from heterogeneous enterprise sources?
- How is execution trace data governed and secured across multi-tenant environments?

---

## Session 6 — RL-Guided ETL Failure Remediation (Breakout/Lightning)

**Speaker:** Anna Marie Benzon
**Time:** ~01:51:00 – 01:56:54

### Summary

Benzon presented a capstone project: an AWS-based RL guidance system for automated ETL failure remediation. The system architecture uses AWS Glue → EventBridge → Lambda → CloudWatch + Glue Data Catalog. An RL policy (tabular Q-learning) selects from six bounded actions (retry, coerce schema, rollback, quarantine, escalate, log) based on a compact state vector (failure category, risk level, retry count, drift severity, data quality). A safety override layer sits outside the learned policy to force escalation on critical anomalies even if the policy proposes passive actions. The baseline manual recovery was ~2.5 working days; the system compresses this for routine, recognizable failures while escalating novel or high-risk cases. Deterministic rules handle observable facts; ML handles contextual selection within bounded choices; guardrails handle authority.

### Highlights

- Design thesis: rules for facts, learning for bounded choices, guardrails for authority
- Six action space: retry, coerce, rollback, quarantine, escalate, log
- Safety override: if anomaly is critical and policy proposes logging → override to escalate
- Deterministic anomaly detection deliberately chosen over ML for observable conditions (easier to audit)
- Tabular Q-learning chosen for small state/action space — every Q-value inspectable
- ~2.5 working days baseline → significantly compressed for routine failures

### Follow-up Items

- Pattern is relevant for any ETL/data pipeline with recurring failure types
- Public repo available with sanitized generalized deployment template

### Important Questions

- How does the Q-table generalize when new failure types appear that don't match training distribution?
- What's the escalation SLA? Does the system need a human acknowledgment path?
- How do execution traces feed back into policy updates over time?

---

## Session 7 — Tokens Should Have Jobs: Token Allocation Strategies for Agents

**Speakers:** Caitlin (Lead, Platform Engineering, Anthropic) & Angela (Lead, Platform Product, Anthropic)
**Time:** ~01:56:54 – 02:09:51

### Summary

The Anthropic platform team challenged the assumption that all tokens are fungible. Instead of simply increasing token budget for better outcomes, they propose assigning tokens different "jobs." Four strategies were experimentally compared on a financial analysis benchmark:

- **Execute**: baseline — agent just executes
- **Advise**: executor + advisor agent (executor calls advisor mid-task)
- **Grade**: executor + grader (rubric-based quality check, iterate until pass)
- **Dream**: executor + dreamer (dreamer reads transcripts, writes learnings to memory for next run)

Holding token budget constant, **advise** showed +13pp accuracy gain over execute at same cost. For high-stakes use cases requiring 100% accuracy (financial P&L), **advise** was the most token-efficient to reach a perfect answer (lower expected total tokens per passing run). **Grade/Dream** are better when maximizing the percentage of perfect runs is the priority. Claude Managed Agents (in Claude platform) provides dreaming and grading primitives out of the box.

### Highlights

- Tokens are not fungible: same budget with different job allocation produces different outcomes
- Advise strategy: execute + advisor results in 0.89 vs 0.76 accuracy at same token budget
- For 100% accuracy requirement: advise is most token-efficient; grade/dream maximize reliability
- Execute required 1.8M tokens to get one perfect answer; advise/grade meaningfully lower
- Dreaming writes learnings to memory — every run improves the next run
- Claude Managed Agents provides dreaming/grading out of the box
- "Give your tokens jobs" is the key mental model

### Follow-up Items

- Experiment with advise/grade/dream strategies on high-precision internal agent workflows
- Evaluate Claude Managed Agents platform features for dreaming and grading primitives
- Design custom token job strategies beyond the four presented

### Important Questions

- Does the advise advantage hold across domains (beyond financial analysis)?
- How do you define the rubric for grading in open-ended tasks?
- How is dreaming memory scoped — per-agent, per-task-type, or shared across agents?

---

## Session 8 — Building a Personal AI Research OS (Software Factories Track)

**Speakers:** Paul Justin (Founder/CEO, Decoding AI; Co-author, LM Engineers Handbook) & Louis-François Bouchard (Co-founder/CTO, Towards AI; Creator, What's AI YouTube; Author, Building LMs for Production)
**Time:** ~02:09:51 – 02:20:08

### Summary

Paul and Louis-François presented a personal AI Research OS built on plain markdown files to solve the "second brain problem" — 5,000+ notes in Obsidian/Readwise/Notion that are hard to leverage with agents. Key insight: the context window becomes the database, file system, memory, and reasoning space simultaneously — and it resets every session. The solution: a structured file-based memory that agents can read and write, bridging between ephemeral agent sessions and the persistent personal knowledge base. Decision tree for tool selection: quick question → Google/ChatGPT; single one-off task → Claude Code/Codex; long-term repeatable research → custom Research OS. The system is designed to be personalized, inspectable by hand, agent-native, and to compound over time. Code is open-source and shared via their respective platforms.

### Highlights

- Context window bottleneck: not what you give the model, but how you leverage it in the future
- Obsidian vault grows at ~250 files/month — agents lose all context on session end
- Markdown-file-based system is more inspectable and personalized than vector DB RAG for personal use
- Notebook LM limitations: not agent-native, can't own/personalize, weak for coding tasks
- System enables cross-project learning: new video doesn't duplicate previous videos
- Decision tree: Google → ChatGPT → Claude Code → Research OS (increasing depth/repeatability)
- Code repo shared; designed to be adapted for individual workflows

### Follow-up Items

- Review open-source Research OS repo (link from talk)
- Evaluate for personal knowledge management in AI engineering workflows
- Consider hybrid: markdown-based for personal use, vector DB for production

### Important Questions

- How does the Research OS handle contradictory or outdated notes over time?
- What is the optimal structure for markdown files to maximize agent retrieval quality?
- How do you prevent the system from becoming another graveyard like the reading list?

---

## Session 9 — MCP, CLI, and Skills: Choosing the Right Agent Tooling Layer (Software Factories Track)

**Speaker:** Nikita Kuthari (Senior MTS, Salesforce — AgentForce, Headless 360)
**Time:** ~02:20:08 – 02:32:06

### Summary

Kuthari presented a practical rubric for choosing between three agent tooling layers: CLI, MCP, and Skills. Three production problems motivated the framework: (1) **context explosion** — 50 MCP tools burn 15K–20K tokens before the task starts; (2) **invisible failures** — agent creates PR on wrong branch, confidence lost; (3) **security surface** — broad LLM access accidentally queries multi-tenant data (compliance nightmare). The three layers: CLI (screwdriver — direct execution, readable, reproducible, composable); MCP (USB-C hub — universal adapter for services, handles auth and tenant isolation); Skill (runbook — structured playbook wrapping tools, defines rigid orchestration, prevents context explosion). Decision rubric: who needs this (CLI = one agent; MCP = multiple agents; Skill = multiple workflows); what failure mode matters (CLI = transparency/reproducibility; MCP = validation/isolation; Skill = sequencing); is context tight (yes → Skill + on-demand MCP). Golden rule: enforce isolation in infrastructure, never in prompts.

### Highlights

- 50 MCP tools in context = 15K–20K tokens burned before task begins
- CLI: proven 50+ years, structured I/O, copy-paste reproducible at 2am incidents
- MCP: universal adapter, auth at server level, tenant isolation guaranteed by infrastructure
- Skill: structural playbook, reduces context, standardizes workflows, enables automation of known procedures
- "If an engineer can open a terminal and do this, the agent should too" — CLI heuristic
- Security golden rule: enforce isolation in infrastructure, never in prompts (prompts can be injected)
- Least privilege principle: give agents minimum permissions needed for the task

### Follow-up Items

- Audit current agent context loading — are all MCP tools active when only 2 are needed?
- Convert high-frequency workflows into Skills for context efficiency
- Review security model: tenant isolation at MCP server level, not prompt level

### Important Questions

- How do you discover and version-control Skills across a team?
- When MCP tools need to be dynamically discovered (unknown services), how do Skills help?
- How does MCP auth compose with enterprise SSO and fine-grained permission models?

---

## Cross-Cutting Themes

1. **Harness engineering is the new bottleneck** — Models are capable; the constraint is the scaffolding, controls, memory, and tooling around them.
2. **Cost as first-class constraint** — 75% of teams adjust usage based on cost; token job allocation strategies show measurable efficiency gains.
3. **Evals remain unsolved** — Still the #1 stack challenge; vibe checks dominate; qualitative learning (DSPy) and grading strategies (Anthropic) are emerging directions.
4. **Agents are real and writing data** — Write-enabled agents tripled YoY; guardrails are still primitive.
5. **Separation of concerns** — DSPy (task from model), ontology layers (business from technical), token jobs (execution from advising/grading/dreaming), tooling layers (CLI/MCP/Skill).
6. **Context window is the scarce resource** — Multiple sessions addressed managing it: token jobs, skill-based MCP scoping, markdown-based memory, HOMA for network.
7. **Be unreasonable** — Mike Krieger's theme: push models harder than feels natural; first-gen AI products over-constrained Claude.
