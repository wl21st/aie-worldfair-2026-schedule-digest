# AI Engineer World Fair 2026 — Structured Session Analysis

**Event:** AI Engineer World Fair  
**Dates:** June 30 – July 2, 2026  
**Location:** San Francisco, CA  
**Format:** In-person + Livestream

---

# CROSS-CUTTING THEMES

| # | Theme | Sessions |
|---|---|---|
| 1 | **Harness engineering is the new bottleneck** — Models are capable; the constraint is scaffolding, controls, memory, and tooling around them | Multiple |
| 2 | **Cost as first-class constraint** — 75% of teams adjust usage based on cost; token allocation strategies show measurable gains | Bar Yaron survey, Sonar, Factory |
| 3 | **Evals remain the #1 unsolved challenge** — Vibe checks dominate; Agent-as-Judge and qualitative learning are emerging | Aparna, Nisham, DSPy session (Day 3) |
| 4 | **Agents are real and writing production data** — Write-enabled agents tripled YoY; guardrails still primitive | Bar Yaron survey, Daksh |
| 5 | **Specification over implementation** — As code generation is free, value moves to spec, requirements, and architecture | Resonate, Balash Ramad, Benoit |
| 6 | **Attention is the scarcest resource** — Human attention to steer agents, not model capability, is the bottleneck | Peter Steinberger, Tariq |
| 7 | **Test-time compute scaling** — More search/inference at test time, not bigger models, improves quality | Han Xiao, Factory routing |
| 8 | **Memory and context management are critical infrastructure** — Context rot, recall policies, and persistence determine long-horizon success | Stefania, Kevin, Factory |
| 9 | **Multi-agent architectures are the new default** — Manager/worker patterns, specialist teams, agent-to-agent communication | Peter, Tariq, Codex, Rushab |
| 10 | **Verification must be baked in, not bolted on** — Zero-trust multi-layered verification; guide-verify-solve cycle | Sonar, Amazon AGI Lab, Greptile |

---

# DAY 1 — June 30, 2026 (Software Factories Day)

---

## 1. Swix — Opening Keynote: Loopcraft & The Human Loop

| Field | Value |
|---|---|
| **Timestamp** | 09:11 – 09:18 |
| **Speaker** | Swix (Co-founder, AI Engineer / Editor, Leighton Space) |
| **Session Type** | Keynote / Opening Address |
| **Track** | Mainstage |

### Summary
Swix opened the World Fair by introducing the concept of "Loopcraft" — the core skill of an AI engineer being the ability to define, navigate, and abstract loops. He drew an analogy from human development: heartbeat (proof of life), talking, tool use, work, teams, and ultimately civilization-level collective intelligence. The key message was that AI engineers must be able to recurse up and down loops — going up for productivity/scaling inference, going down for reliability/debugging. He noted the conference has grown from 2,000 attendees in 2024 to 7,000 in 2026, reflecting the explosive growth of the field. He framed the World Fair as "the summit of summits" — the highest loop where humans come together to figure out what the next loop is. He introduced the theme of software factories and the need to understand what loops you're working in and whether that's the right level of abstraction. The talk set the philosophical tone for the entire event: AI is diffusing beyond coding into healthcare, finance, GTM, and every vertical. The "highest loop" is humans convening to decide what the next loop should be — a meta-generative process for generating loops.

### Keywords & Tags
`loopcraft`, `abstraction`, `software-factories`, `human-loop`, `collective-intelligence`, `conference-growth`, `vertical-ai`, `tiny-teams`

### Key Knowledge Points
- AI engineering is fundamentally about managing loops of abstraction
- Up a loop = productivity/scaling; down a loop = reliability/debugging
- The human analogy: heartbeat → talk → tools → work → teams → civilization
- Conference grew from 2K (2024) to 7K (2026), expo 4× larger
- AI is now diffusing beyond coding into healthcare, finance, GTM
- "Highest loop" is humans designing the next loop

### Follow-Up Items
- Read Swix's "Loopcraft" essay for deeper framework
- Evaluate personal workflow loops — identify which level you're blocked at
- Consider tiny teams concept for agent-heavy organizations

### Impact on Enterprise AI Software Development
Established a mental model where engineering leaders must think in terms of abstraction layers and loops. The framework helps enterprises diagnose whether they're blocked on reliability (need to go down a loop) or scaling (need to go up a loop). This directly affects how organizations structure AI teams, choose tooling, and prioritize investments.

### Major References
- Swix's "Loopcraft" essay
- Prior AI Engineer keynotes (2024, 2025)

### Single Sentence Taken Out
> "The highest loop of all is where humans come together to figure out what the next loop is — the loop that makes loops."

---

## 2. Pablo Castro (Microsoft) — AI & Knowledge: Intrinsic, Extrinsic, Learned

| Field | Value |
|---|---|
| **Timestamp** | 09:21 – 09:38 |
| **Speaker** | Pablo Castro (CVP & Distinguished Engineer, Microsoft) |
| **Session Type** | Keynote / Product Keynote |
| **Track** | Mainstage |

### Summary
Pablo Castro presented Microsoft's framework for thinking about knowledge in AI systems, dividing it into three categories: intrinsic (parametric knowledge in models), extrinsic (grounding via RAG and context engineering), and learned (continuous improvement through agent observation). He traced the exponential from IntelliSense (1996) to GitHub Copilot to today's agentic systems, arguing that intrinsic model knowledge sparked the exponential we're in. He then demonstrated Microsoft Ignite (AI Foundry) features: knowledge bases that automatically ground agents in SharePoint, emails, calendar, chat threads, and structured data (parquet tables, blob storage, web). Every knowledge base is also an MCP server — no glue code needed. He introduced the "Agent Optimizer" which performs hill-climbing over agent configurations (instructions, tools, skills) using traces from real user interactions. The optimizer uses a JEPA-style loop to evaluate baselines, generate candidates, and auto-deploy improvements. Satya Nadella's concept of "people and agents compounding" was referenced as the philosophical underpinning — every organization develops a unique, differentiated capability through these learning loops.

### Keywords & Tags
`knowledge-management`, `intrinsic-knowledge`, `extrinsic-knowledge`, `learned-knowledge`, `microsoft-foundry`, `mcp-server`, `agent-optimizer`, `context-engineering`, `rag-evolution`, `hill-climbing`

### Key Knowledge Points
- Three knowledge types: intrinsic (parametric), extrinsic (grounding/RAG), learned (continuous improvement)
- Context engineering has evolved from simple vector search to sophisticated agentic retrieval systems
- Microsoft Foundry knowledge bases auto-ground agents in company-wide ambient data
- Every knowledge base is an MCP server — zero glue code integration
- Agent Optimizer uses JEPA-style hill climbing over agent configurations
- Satya's vision: people and agents compound through learning loops
- Token efficiency measured as information density per token

### Follow-Up Items
- Try Microsoft Foundry knowledge base creation at ai.azure.com
- Evaluate Agent Optimizer for internal agent workflows
- Assess organizational readiness for "learned knowledge" loops

### Impact on Enterprise AI Software Development
Enterprises struggle with grounding agents in real organizational data. Microsoft's framework provides a concrete architecture: separate intrinsic knowledge (model), extrinsic knowledge (grounding/RAG), and learned knowledge (continuous optimization). The Agent Optimizer is a tangible tool for enterprises to auto-improve agent configuration without manual prompt engineering. The MCP-first design means knowledge bases are infrastructure, not point integrations.

### Major References
- Satya Nadella's writing on people-agent compounding
- Microsoft Foundry / AI Ignite product suite

### Single Sentence Taken Out
> "We can actually observe the processes and get better at them by reflecting and improving every step — that's the learning loop that captures what's unique about your organization."

---

## 3. Alexander Embirikos & Roman Hewitt (OpenAI) — Engineering Is Not Dead

| Field | Value |
|---|---|
| **Timestamp** | 09:38 – 09:58 |
| **Speakers** | Alexander Embirikos (Head of Enterprise Product, OpenAI) & Roman Hewitt (Head of Developer Experience, OpenAI) |
| **Session Type** | Keynote / Dual Keynote |
| **Track** | Mainstage |

### Summary
Alexander and Roman delivered a counter-narrative to "AI replaces engineers": engineering was never about writing code — it was about problem-solving, combining science with design, taste, judgment, and imagination. They framed AI engineers as the ones "eating the world" — the people pushing the frontier of what's possible. Key product announcements: GPT-5.6 series preview (launched the prior week), including 5.6 SOL (frontier intelligence running on Cerebras at "tokens per second" generating speed), 5.6 Terra (5.5-level intelligence at half cost), and Luna (cheapest frontier model at $1/M input tokens). They introduced "value maxing" as the successor to token maxing — the real measure of AI ROI. Cost efficiency, speed, and frontier intelligence are the three poles. GPT-5.3 Codex Spark demonstrated what speed unlocks. The talk featured Peter Steinberger (the "Claude father" now at OpenAI) who demonstrated his evolution from juggling terminals to managing a "manager of agents" — persistent context, delegation, and triggers forming the loop. His key insight: "I was orchestrating; really I was polling."

### Keywords & Tags
`gpt-5.6`, `value-maxing`, `agent-manager`, `openai-models`, `engineering-not-dead`, `cerebras`, `cost-efficiency`, `persistent-context`, `agent-delegation`

### Key Knowledge Points
- Engineering is problem-solving, not code-writing — AI engineers are more valuable than ever
- GPT-5.6 SOL: frontier intelligence on Cerebras at very high speed
- GPT-5.6 Terra: 5.5-level intelligence at half cost
- Luna: $1/M input tokens — cheapest frontier model
- "Value maxing" replaces "token maxing" as the ROI metric
- Model release cadence accelerated from "every few months" to ~every 6 weeks
- Peter Steinberger's evolution: pairing → managing terminals → managing a manager of agents
- Three enablers: server-side compaction, coordination, automation/triggers

### Follow-Up Items
- Evaluate GPT-5.6 Terra for cost-sensitive production workloads
- Implement "manager agent" pattern for long-running tasks
- Explore server-side compaction for reliable long-running agent sessions

### Impact on Enterprise AI Software Development
The "value maxing" frame shifts enterprise focus from "how many tokens can we consume" to "what business value are we generating per dollar." The accelerating model release cadence (every 6 weeks) means enterprises need eval infrastructure that can keep up. Peter's pattern of a "manager agent" that delegates to worker agents is a directly applicable architecture for enterprises scaling agent deployments.

### Major References
- Terminal Bench eval
- GPT-5.6 model family announcement

### Single Sentence Taken Out
> "Software ate the world, and then AI ate software, but now AI engineers are eating the world."

---

## 4. Peter Steinberger (OpenAI) — From Terminals to Loops

| Field | Value |
|---|---|
| **Timestamp** | 09:58 – 10:04 |
| **Speaker** | Peter Steinberger (OpenAI, formerly "Claude father") |
| **Session Type** | Live Demo / Keynote |
| **Track** | Mainstage |

### Summary
Peter Steinberger delivered a concise, powerful talk on his personal evolution as an AI engineer. He showed how he went from juggling 10+ terminal windows (thinking he was orchestrating but really polling) to now managing a long-running "manager" agent that delegates to worker agents. Three changes made this possible: (1) server-side compaction making long-running tasks reliable, (2) coordination allowing one thread to create and steer sub-projects, and (3) automation triggering the manager when something happens. He identified the moving bottleneck: first tokens, then compute (his MacBook sounded like a jet engine — now fixed with test boxes), and now attention. He argued the most important skill today is deciding where to spend attention — not watching agents generate code. He described his open-source workflow: a manager agent wakes up, reads issues against project goals, creates a worker, the worker investigates/implement/tests, another agent reviews, and he only reviews the final PR. Paul Salt's "chief of staff" agent was cited. His vision: agents should not be trapped inside apps — you should be able to text them, Slack them, or hear from anywhere. "The future is not terminals, it's better loops."

### Keywords & Tags
`manager-agent`, `bottleneck-moving`, `attention-bottleneck`, `server-side-compaction`, `agent-delegation`, `persistent-context`, `codex-agents`

### Key Knowledge Points
- Evolution: pairing with one agent → managing terminals → managing a manager of agents
- Three enablers: server-side compaction, coordination (one thread creates sub-projects), automation/triggers
- Bottleneck moved: tokens → compute (test boxes solved it) → attention
- Watching agents generate code is a waste of attention
- Open-source workflow: manager reads issue → creates worker → worker implements → reviewer agent → human reviews PR
- Paul Salt's "chief of staff" agent wakes up every N minutes to coordinate GitHub work
- Agents should be device-independent — textable, Slack-able, ambient

### Follow-Up Items
- Implement "manager agent" pattern for personal workflow
- Separate agent execution environment from local machine (test boxes)
- Design agent communication protocol for multi-agent coordination

### Impact on Enterprise AI Software Development
Peter's "attention bottleneck" diagnosis is critical for enterprises: the constraint isn't model capability but human attention to steer agents. The solution is hierarchical agent architectures (manager → workers) with human only at the outer loop. This pattern is directly deployable in enterprise settings where one senior engineer manages a "team" of agents.

### Major References
- Paul Salt's chief of staff agent implementation

### Single Sentence Taken Out
> "I thought I was orchestrating. Really, I was polling."

---

## 5. Zhuan Li (ZAI / GLM) — GLM 5.2 Open Weight Model & ZCode Harness

| Field | Value |
|---|---|
| **Timestamp** | 10:08 – 10:19 |
| **Speaker** | Zhuan Li (ZAI / GLM) |
| **Session Type** | Keynote (Remote) |
| **Track** | Mainstage |

### Summary
Zhuan Li introduced GLM 5.2, an open-weight model positioned between Opus 4.7 and 4.8 on terminal benchmarks. He clarified that "GLM" (General Language Model) is a legacy brand from the 2021 architecture paper, not the current architecture. GLM 5.2 adds a "high" thinking level for harder tasks, with the non-thinking model already outperforming the 5.1 thinking model. Benchmark results show it competitive with frontier models on Terminal Bench 2.0 and long-horizon tasks. He emphasized GLM is "more than a coding model" — strong on general chat, math, and role-play. The open-weight rationale: security/control for enterprises, building trust, enabling co-design of future architectures. He announced ZCode, an open-source agent harness built for GLM but supporting all frontier models (bring your own key). ZCode supports techniques like GO (goal-oriented) and compaction, similar to Codex and Claude Code.

### Keywords & Tags
`glm-5.2`, `open-weight`, `zcode`, `thinking-level`, `open-source-harness`, `terminal-bench`, `token-efficiency`, `sovereign-ai`

### Key Knowledge Points
- GLM 5.2 positioned between Opus 4.7 and 4.8 on Terminal Bench 2.0
- New "high" thinking level for hard tasks; non-thinking model beats 5.1 thinking model
- Strong across coding, math, general chat, role-play — not just a coding model
- Open weight for enterprise security, trust, and co-design
- ZCode: open-source harness supporting all frontier models (BYOK)
- Training pipeline and recipe shared publicly

### Follow-Up Items
- Evaluate GLM 5.2 on internal benchmarks vs Opus 4.8
- Try ZCode harness as an alternative to Codex/Claude Code
- Review GLM tech blog for training pipeline details

### Impact on Enterprise AI Software Development
Open-weight models like GLM 5.2 give enterprises an alternative to closed frontier models, especially for regulated industries needing data sovereignty. ZCode as an open-source harness means enterprises can standardize on one tool while switching models underneath. The model's competitive coding performance at lower cost pressures pricing across the industry.

### Major References
- GLM 2021 paper (auto-regressive blank filling)
- Terminal Bench 2.0 / 2.1

### Single Sentence Taken Out
> "We open the weights because there are users' needs and there are our needs — if we can meet their needs, it's okay for us to open the model."

---

## 6. Thomas Wolf (Hugging Face) & Olive (Minimax) — M3: Open Source Multimodal Model

| Field | Value |
|---|---|
| **Timestamp** | 10:21 – 10:41 |
| **Speakers** | Thomas Wolf (Co-founder & CSO, Hugging Face) & Olive (Minimax) |
| **Session Type** | Fireside Chat / Dual Keynote |
| **Track** | Mainstage |

### Summary
Thomas Wolf interviewed Olive about Minimax's M3 model, a ~200B parameter (46B active) open-weight multimodal model supporting text, image, video, and 1M token context. Key innovation: Minimax Sparse Attention (MSA), designed by an intern, that scales context length elegantly with an indexed branch (selects important blocks) and a sparse attention branch (calculates on selected blocks). The model was trained natively multimodal from the first step (not as an afterthought with adapters), solving the collapse problem that other labs face. Olive explained that native multimodal training produces better text performance and vision understanding simultaneously. Interleaved natural data (keeping images/videos in instead of masking) plus strong reward modeling prevented collapse. Minimax's unique organizational model: anyone can propose a project, others join, work for weeks/months, and shipped improvements go into the final model. M3 is also used internally for automated research workflows. Olive predicted multi-agent systems and model routing as the next frontier.

### Keywords & Tags
`minimax-m3`, `multimodal`, `sparse-attention`, `open-weight`, `native-multimodal`, `1m-context`, `intern-designed`, `open-source-business-model`

### Key Knowledge Points
- M3: ~200B total, 46B active parameters, open weight
- Native multimodal (text + image + video) trained from step 1 — avoids adapter compromise
- MSA (Minimax Sparse Attention): indexed branch selects important blocks + sparse attention calculates on them
- Designed by an intern — unique organizational openness
- 1M token context — critical for agentic tool-use and multi-round interactions
- Interleaved natural data training with strong reward modeling prevents collapse
- Autonomous multi-agent pipelines and model routing are next focus

### Follow-Up Items
- Evaluate M3 for multimodal agent workflows (video understanding + tool use)
- Study MSA architecture paper for long-context efficiency patterns
- Consider M3 for cost-sensitive production workloads vs frontier models

### Impact on Enterprise AI Software Development
M3 demonstrates that open-weight multimodal models at 1M context are production-ready. For enterprises, this means video/image understanding agents become feasible without depending solely on closed frontier APIs. The native multimodal approach (trained from step 1) produces better quality than adapter-based approaches — relevant for any enterprise building multimodal agents.

### Major References
- M3 model card on Hugging Face
- MSA architecture paper

### Single Sentence Taken Out
> "We realized that training vision after text pre-training would actually harm the text performance — so we decided to just train from the very first step."

---

## 7. Tisha & Sushin — Agent Debugging: You Can't Reproduce What You Can't Fix

| Field | Value |
|---|---|
| **Timestamp** | 10:47 – 10:57 |
| **Speakers** | Tisha & Sushin |
| **Session Type** | Technical Talk |
| **Track** | Mainstage |

### Summary
Tisha and Sushin tackled one of the hardest problems in production agent systems: reproducibility. Using a stock-trading agent scenario (selling 1,000 shares instead of $1,000 worth — a $190K mistake), they showed how agent failures can be silent — API returns OK, dashboards show green, but the trade is catastrophically wrong. They debunked the common reflex to "set temperature to zero" for reproducibility, explaining four reasons why temperature zero doesn't guarantee determinism: (1) sampling determinism ≠ system determinism (argmax ≠ identical scores run-to-run); (2) floating-point math is not associative (order of operations changes results); (3) batch variance — a request gets grouped with whatever else hits the server that millisecond; (4) mixture-of-experts routing — expert capacity limits mean token routing depends on batch traffic. Their key insight: the right question isn't "how do I make the model deterministic" but "how do I debug and retest a run I can't reproduce." They distinguished bitwise determinism (same input → same output, not achievable from hosted APIs) from replayability (rebuilding a run well enough to debug it, which is observability).

### Keywords & Tags
`agent-reproducibility`, `non-determinism`, `temperature-zero-myth`, `agent-debugging`, `replayability`, `production-failures`, `silent-failures`, `observability`

### Key Knowledge Points
- Temperature zero ≠ determinism — same logical error repeated identically
- Four sources of non-determinism: sampling ≠ system determinism, floating-point non-associativity, batch variance, MoE routing
- Temperature zero on GPU: running same prompt 1K times can return dozens of different responses
- Wrong question: "make the model deterministic" → Right question: "how do I debug an unreproducible run"
- Bitwise determinism (controllability) ≠ replayability (observability)
- Silent failures: API returns OK, dashboards are green, but the action is wrong

### Follow-Up Items
- Audit agent systems for silent failure modes (APIs returning OK on wrong actions)
- Implement replayability infrastructure (trace capture + state reconstruction)
- Educate teams that temperature zero is not a fix for reproducibility

### Impact on Enterprise AI Software Development
This is a critical talk for any enterprise deploying agents that interact with real systems (finance, healthcare, e-commerce). The silent failure mode — where the API returns success but the action was wrong — is perhaps the most dangerous class of agent bug. Teams need observability infrastructure (traces, state capture) rather than chasing bitwise determinism. The distinction between determinism and replayability should inform how enterprises design agent evaluation and debugging pipelines.

### Major References
- Hacker News and Reddit engineering threads on GPU non-determinism
- MoE architecture characteristics

### Single Sentence Taken Out
> "We don't need the model to return the exact same token every time — we just need our system to execute the exact same state transition."

---

## 8. Kevin (Codex / OpenAI) — Codex Workflows: Pinned Threads, Heartbeats & Agent Teams

| Field | Value |
|---|---|
| **Timestamp** | 10:57 – 11:11 |
| **Speaker** | Kevin (Developer Experience, OpenAI / Codex) |
| **Session Type** | Demo / Technical Talk |
| **Track** | Mainstage |

### Summary
Kevin demonstrated advanced Codex workflows centered on three concepts: pinned threads (long-running sessions that persist across days), heartbeats/automations (agents that wake up on schedule), and inter-thread communication (threads talking to each other). He argued that the old ChatGPT habit of short, throwaway threads is obsolete — all his work now happens in pinned threads. He showed how he uses dictation (voice is 3× faster than typing) and "app shots" (screenshot + accessibility tree capture) to give agents context instantly. His personal "chief of staff" thread wakes up every N minutes, monitors Slack/Twitter, triages issues, spawns child threads for specific tasks, and those threads communicate back. He demonstrated agent-to-agent workflows: a monitor thread detects an issue, creates a triage thread, which creates a comms thread — all without human intervention. Key plugins: Slack, Gmail, Calendar, Notion, Linear, Obsidian. His memory system is an Obsidian vault (people dir, projects dir, agent notes) shared via a template repo. He predicted voice-driven development will become the norm by end of year — "you're going to feel like Tony Stark."

### Keywords & Tags
`codex-workflows`, `pinned-threads`, `agent-heartbeats`, `agent-to-agent`, `voice-driven-dev`, `app-shots`, `memory-vault`, `chief-of-staff-agent`

### Key Knowledge Points
- Three acts: bring context in → work on pinned thread → computer acts/writes back to world
- Pinned threads replace short-lived chat sessions — they persist, named, with automations
- Heartbeats: agents wake up on schedule (e.g., every N minutes) to monitor and act
- Threads can talk to each other — enabling manager/sub-agent patterns
- App shots: press both command keys → captures screenshot + accessibility tree → instant agent context
- Memory vault: structured Obsidian (people, projects, agent notes) — template available
- Voice + dictation is 3× faster than typing; foot pedal for hands-free control
- Agent can spawn agents via API: "create a workspace for me, make all buttons blue"

### Follow-Up Items
- Try app shots workflow for daily triage
- Set up a pinned thread with heartbeat for monitoring project changes
- Download and set up Kevin's Obsidian memory vault template
- Experiment with voice dictation for agent prompts

### Impact on Enterprise AI Software Development
Kevin's workflow is a blueprint for how individuals and small teams can scale with agents. The "chief of staff" agent pattern — a persistent, scheduled agent that monitors channels, triages, and spawns sub-agents — is directly applicable to enterprise settings. The memory vault concept (structured markdown as a personal knowledge base) and inter-thread communication (agents talking to agents) are architectures that enterprises can adopt today.

### Major References
- Codex product documentation
- Kevin's Obsidian vault template (QR code shared)

### Single Sentence Taken Out
> "The same plugins that can read context can also draft — every email I ever have, when I review it, there's already a draft."

---

## 9. Teresa (Factory) — Building a Software Factory: Agnostic, Autonomous, Always Improving

| Field | Value |
|---|---|
| **Timestamp** | 11:20 – 11:42 |
| **Speaker** | Teresa (Factory) |
| **Session Type** | Technical Keynote |
| **Track** | Mainstage |

### Summary
Teresa defined a software factory as "the whole lifecycle of developing software with autonomy" — not just coding but collecting signals, reacting to feedback, prioritizing, orchestrating, executing, validating, testing in production, and iterating while continuously improving. She emphasized three pillars: agnostic (model-independent, environment-independent), autonomous (long-running missions lasting weeks, eventually years), and always improving (continuous learning and knowledge sharing). She demonstrated Factory's automatic model routing system that classifies task difficulty and selects the cheapest model above threshold — saving 25%+ on tokens while improving reliability. On autonomy, she showed Factory's architecture: orchestrator agent → workers in sequence (not swarm — fresh context per worker, like human handoffs) → validators (scrutiny validator checks code quality; user testing validator clicks through the app in a virtual machine). Missions run for weeks. She warned about the "power law" of AI adoption: if your codebase isn't ready, AI adoption can make it worse — the gap between prepared and unprepared teams grows. She presented the "deferred context engine" that saves 50%+ tokens by progressively disclosing tools only when needed.

### Keywords & Tags
`software-factory`, `model-routing`, `agnostic-autonomous-improving`, `orchestrator-worker-validator`, `deferred-context`, `long-running-missions`, `user-testing-validator`, `AI-adoption-power-law`

### Key Knowledge Points
- Software factory = whole lifecycle with autonomy, not just code generation
- Three pillars: agnostic (model/workflow independent), autonomous (week-long missions), always improving (continuous learning)
- Automatic model routing: classify task difficulty → select cheapest model above threshold → 25%+ savings
- Orchestrator → workers (in sequence, fresh context per handoff) → validators (scrutiny + user testing)
- User testing validator clicks through app in virtual machine — verifies it's actually interactive
- Deferred context engine: hide tools until needed, progressively disclose — saves 50%+ tokens
- AI adoption power law: unprepared codebases get worse with AI; gap between leaders and laggards grows
- Humans move up: from computers → programmers → agent managers → deciding what to build, not how

### Follow-Up Items
- Evaluate automatic model routing for internal agent workflows
- Assess codebase readiness ("agent readiness framework") before scaling AI adoption
- Consider deferred context engine pattern for complex multi-tool agents

### Impact on Enterprise AI Software Development
Factory's architecture is one of the most concrete software factory implementations shown. The three-pillar framework (agnostic, autonomous, improving) gives enterprises a blueprint. The model routing system is immediately practical — most enterprises overspend by defaulting to frontier models. The warning about the AI adoption power law is critical: enterprises must prepare codebases (structure, documentation, clean architecture) before scaling autonomous agents, or risk technical debt compounding faster than productivity gains.

### Major References
- Carnegie Mellon study on AI productivity dissipation
- Stanford study on code quality with AI

### Single Sentence Taken Out
> "If your codebase is not ready, adopting AI can actually make you end up worse — and there is a big and growing gap in productivity between those who just adopted AI versus those who actually thought about it."

---

## 10. Daksh (Greptile) — One Million AI-Generated PRs: What the Data Says

| Field | Value |
|---|---|
| **Timestamp** | 12:15 – 12:27 |
| **Speaker** | Daksh (Co-founder, Greptile) |
| **Session Type** | Data-Driven Keynote |
| **Track** | Mainstage |

### Summary
Daksh presented a statistical analysis of over 1 million AI-generated PRs from enterprise customers (NVIDIA, Coinbase, Scale, and others). He discovered that identifying "vibe-coded" PRs is surprisingly difficult — GitHub author fields are unreliable since developers often don't attribute commits to agents. He estimated that anywhere from 20% to 80% of code in some organizations is AI-generated. Surprising finding: 99th percentile developers using AI write ~1,000 commits/month vs median developers writing fewer than 5. At that scale, manual code review is completely infeasible. He argued code validation's goal is three questions: (1) Does this change do what it intended? (2) Does it not break anything? (3) Is it maintainable? Testing, review, and QA are just implementation details of these three questions. Autonomous agents are actually quite good in commercial settings — the trajectory is clear that agents are getting good enough for production enterprise code. The implication for code review: it must become autonomous too, focused on intent verification rather than line-by-line review.

### Keywords & Tags
`vibe-coding-data`, `ai-prs`, `code-review-automation`, `enterprise-agent-adoption`, `greptile`, `commit-frequency-distribution`, `code-validation`

### Key Knowledge Points
- Estimating AI-generated PRs is hard — GitHub author field tags are inconsistent
- 20–80% of code in some enterprises is AI-generated (estimated)
- 99th percentile devs: ~1,000 commits/month; median: <5 commits/month → manual review infeasible
- Code validation = 3 questions: does it work? does it not break? is it maintainable?
- Autonomous agents are working in real enterprise production settings (NVIDIA, Coinbase, Scale)
- Code review must become autonomous — focus on intent, not line-by-line reading

### Follow-Up Items
- Audit internal commit velocity — is the organization's review process keeping pace?
- Evaluate autonomous code validation tools for the three-question framework
- Review Greptile's approach to intent-based PR validation

### Impact on Enterprise AI Software Development
This talk provides the strongest empirical evidence that vibe-coding is real in the enterprise, not just indie hacker projects. The commit frequency distribution (99th percentile doing 1,000 commits/month) means traditional code review is dead at scale. Enterprises must pivot from line-by-line review to intent-based autonomous validation. The three-question framework (does it work? not break? maintainable?) is a concise way to redesign code review processes for the AI era.

### Major References
- Greptile internal data from NVIDIA, Coinbase, Scale customers
- GitHub API analysis methodology

### Single Sentence Taken Out
> "The median coder using Greptile writes fewer than 5 commits a month; the 99th percentile writes close to 1,000 — at that scale, manual code review is completely infeasible."

---

## 11. Conductor Co-founder — Orchestras, Not Factories

| Field | Value |
|---|---|
| **Timestamp** | 11:50 – 12:07 |
| **Speaker** | Conductor Co-founder |
| **Session Type** | Keynote / Philosophy Talk |
| **Track** | Mainstage |

### Summary
The Conductor co-founder presented six principles for being the fastest builder in your organization, encapsulated in the acronym "STICK FOE": Stay near the frontier (try latest models day one), don't Try to beat the market (don't "midwit meme" — optimize workflow only if you have real alpha), create slot-free Zones (focused time blocks without distractions), Feed the beast (CIA — centralized intelligence agent — puts everything in Postgres for SQL-accessible organizational memory), Free range agents (cloud sandboxes where agents persist beyond laptop closure, can spawn themselves via API, and collaborate), and Orchestras not Factories (future should feel like conducting an orchestra, not managing a factory line). He demonstrated a new collaboration feature: cloud sandboxes with real-time agent persistence, team workspaces, and cross-workspace visibility. He showed agents spawning other agents via API (his OpenClaude called "Lord Crandon" that can create new workspaces from Telegram). His core philosophical argument: "software factory" is the wrong metaphor — it implies automation and dehumanization; "orchestra" centers the human as conductor, zooming in/out, crafting, feeling in flow.

### Keywords & Tags
`stick-foe`, `orchestras-not-factories`, `free-range-agents`, `feed-the-beast`, `cloud-sandboxes`, `agent-spawning`, `midwit-meme`, `human-centered-ai`

### Key Knowledge Points
- STICK FOE: Stay near frontier, don'T beat market, slot-free zones, feed beast, free range agents, Orchestras not Factories
- "Don't beat the market" heuristic: if it should be the default workflow, wait for the platform to build it
- Feed the beast: CIA (Centralized Intelligence Agent) — all org data in Postgres with SQL access
- Free range agents: cloud sandboxes, agents persist beyond laptop, can spawn themselves via API
- Agent collaboration: real-time multi-agent workspaces with cross-team visibility
- Philosophical argument: "orchestra" over "factory" — human at center, in flow, crafting

### Follow-Up Items
- Audit personal workflow — are you "midwit memeing" on workflow optimization?
- Consider "feed the beast" pattern: funnel all organizational signals into a queryable database
- Evaluate cloud sandbox for persistent agent execution beyond laptop sessions

### Impact on Enterprise AI Software Development
"Orchestras, not Factories" is an important counterpoint to the dominant "software factory" narrative. For enterprise leaders, this reframes AI adoption as a human-empowerment initiative rather than an automation/cost-cutting initiative. The "feed the beast" pattern (centralized, SQL-accessible organizational memory) is a concrete, implementable architecture. The "don't beat the market" heuristic saves enterprises from over-investing in custom workflow optimization when platform defaults will soon catch up.

### Major References
- Efficient Market Hypothesis (analogy)
- Route loops, /goal commands (design patterns to wait for platform adoption)

### Single Sentence Taken Out
> "Don't be the person who has an amazing Emacs setup but doesn't actually get stuff done."

---

## 12. Rushab (Machine Craft) — The Factory That Taught Itself to Remember

| Field | Value |
|---|---|
| **Timestamp** | 12:10 – 12:15 |
| **Speaker** | Rushab (Machine Craft) |
| **Session Type** | Case Study / Storytelling Keynote |
| **Track** | Mainstage |

### Summary
Rushab told the story of Machine Craft, a 3-generation Indian manufacturing company making thermoforming machines, that built an AI agent running their entire go-to-market without any data science team or ML budget. The problem: all company knowledge lived in three brains (grandfather, father, now his). Every departing employee took a chunk of the company's brain. Instead of writing documentation nobody reads, they built "Era" — a biologically-inspired AI twin of the company. Era uses a graph-based knowledge structure (vectors for meaning + relationships between entities), senses to identify who it's talking to, a "gut" to digest documents into facts, memory, a dream cycle, and an "immune system" to fight bad information. Era is not one prompt — it's a pantheon of specialists: Athena (runs the room), Prometheus (owns the sale), Plutus (pricing), Hephaestus (machine specs), Vera (fact-checker), Memnon (guards corrections). They hold meetings, argue, and produce a single answer. The system handles 9 concrete daily jobs: outbound emails, account briefs, quotations, lead revival, inbound replies, and qualification.

### Keywords & Tags
`biologically-inspired-ai`, `multi-agent-specialist`, `knowledge-graph`, `manufacturing-ai`, `gtm-automation`, `small-team-ai`, `institutional-knowledge`

### Key Knowledge Points
- Company knowledge lived in 3 brains across 3 generations — existential risk of forgetting
- Era: biologically-inspired AI twin with senses, gut, memory, dream cycle, immune system
- Graph-based knowledge: vectors for meaning + relationships between entities
- Pantheon of specialists (6+ agents), not one mega-prompt — each has exactly one job
- Agents hold meetings, argue, produce unified answers — "boardroom that never sleeps"
- Handles full GTM: outbound, account briefs, quotations, lead revival, inbound
- Built without data science team or ML budget

### Follow-Up Items
- Evaluate specialist multi-agent pattern for complex domain workflows
- Consider biologically-inspired knowledge architecture (graph + vectors + immune system) for institutional memory
- Study how small teams can implement sophisticated AI without dedicated ML headcount

### Impact on Enterprise AI Software Development
Rushab's story is a powerful existence proof that sophisticated multi-agent AI is accessible to non-tech companies with zero ML budget. The "pantheon of specialists" pattern (many narrow agents, not one broad prompt) is directly applicable to enterprise settings. The biologically-inspired architecture (memory, dream cycle, immune system) offers a fresh design pattern for institutional knowledge management. The "company twin" concept — where organizational knowledge is the moat, not models — reframes how enterprises should think about AI differentiation.

### Major References
- Machine Craft's 3-generation business story
- Biology-inspired AI design patterns

### Single Sentence Taken Out
> "We weren't scared of the competitors — we were scared of forgetting."

---

## 13. Aurel Zion — 10× Mobile Dev: Reimagining the Workflow, Not Just the Tool

| Field | Value |
|---|---|
| **Timestamp** | 12:34 – 12:42 |
| **Speaker** | Aurel Zion (Mobile Software Engineer) |
| **Session Type** | Technical Keynote |
| **Track** | Mainstage |

### Summary
Aurel asked a provocative question: "AI promised us 10× productivity. Do you feel it?" His answer: we changed the engine but not the workflow. He drew the historical analogy of factories switching from steam to electric — initially no productivity gain because factories kept the same layout (organized around the central steam engine). The real gain came when electric engines were miniaturized and placed inside each machine, enabling workflow-driven factory layout. Similarly, AI replaces code writing but doesn't eliminate friction: iteration cycles, context switches, communication overhead. His vision: one tool, one codebase for designers, QA, PMs, and developers. Designers should design in code and send developers a PR. QA should iterate with agents via simulator links. He identified the mobile development-specific bottleneck: build times (2–10 minutes) prevent agents from iterating fast. His solution: cloud sandboxes for mobile development — remote simulators/emulators where agents can preview changes instantly without downloading Xcode/Android Studio. He announced a product concept for cloud-based mobile dev sandboxes enabling designers, QA, and PMs to collaborate with agents without local tooling.

### Keywords & Tags
`mobile-dev-workflow`, `steam-to-electric-analogy`, `cloud-sandboxes-mobile`, `10x-productivity`, `design-to-code`, `qa-automation`, `workflow-reimagining`

### Key Knowledge Points
- Steam-to-electric analogy: AI is the new engine, but workflow hasn't changed → no 10× yet
- Iteration friction (context switches, communication, sync) is the real bottleneck, not code generation
- Vision: one tool, one codebase for designers, QA, PMs, devs — all roles collaborate via agents
- Designers design in code → send PR; QA iterates with agents via simulator links
- Mobile-specific bottleneck: 2–10 min build times block agent iteration
- Solution: cloud sandboxes with remote simulators for instant agent preview

### Follow-Up Items
- Investigate cloud-based mobile development sandboxes for agent workflows
- Evaluate cross-functional role redesign (designers → code PR, QA → agent iteration)
- Measure actual productivity gains (not just code velocity) before/after AI adoption

### Impact on Enterprise AI Software Development
Aurel's talk is essential for any enterprise deploying AI in mobile development. The steam-to-electric analogy explains why many enterprises see disappointing productivity gains from AI: they replaced the engine but kept the old workflow. The insight that iteration friction (not code generation) is the bottleneck reframes where to invest. Cloud sandboxes for mobile development are a concrete infrastructure need that enterprises should plan for.

### Major References
- Historical factory electrification productivity studies
- Mobile development CI/CD constraints

### Single Sentence Taken Out
> "They changed the steam engine with the electric engine, but they didn't rearrange the factory. The real gain came when they realized they could put the engine inside each machine and reorganize by workflow."

---

## 14. Gargay (Pragmatic Engineer) & Simon Erickson (TurboPuffer) — Infrastructure Deep Dive: Databases, CPUs, and Building in Public

| Field | Value |
|---|---|
| **Timestamp** | 12:44 – 1:40 |
| **Speakers** | Gargay (Author, Pragmatic Engineer) & Simon Erickson (Founder/CEO, TurboPuffer) |
| **Session Type** | Fireside Chat / Interview |
| **Track** | Mainstage |

### Summary
Gargay interviewed Simon Erickson in a wide-ranging conversation covering Simon's journey from Denmark to Shopify (where he thought he was taking a "gap year" but stayed 8 years), to founding TurboPuffer. Simon revealed that TurboPuffer started as a personal project to solve a single problem: vectors on S3 were too expensive. His "Napkin Math" project — a table of infrastructure costs (DRAM bandwidth, S3 latency, SSD throughput) with Rust scripts and flashcards — became his secret weapon for calling out bad benchmarks at Shopify. TurboPuffer's origin: Simon's summer obsession, released as a single TMUX instance on GCP. Cursor became their first customer. Simon's venture capital philosophy is contrarian: six reasons to raise (R&D, growth, ego, employee liquidity, strategic partnership, M&A) — he raised only for R&D and employee liquidity, explicitly avoiding ego-driven fundraising. He met Jensen Huang, asked him "do you vape?" on stage, and couldn't stop talking about CPUs despite being told not to say "the C word." Key insight: CPU shortage is real — RL training and agent execution are CPU-hungry, and the big labs are consuming massive CPU allocations.

### Keywords & Tags
`turbopuffer`, `napkin-math`, `databases`, `vector-search`, `cpu-shortage`, `venture-capital-philosophy`, `shopify-infrastructure`, `cursor-case-study`

### Key Knowledge Points
- Napkin Math: table of infrastructure costs (DRAM, SSD, network) — flash cards for every cell
- TurboPuffer started as one TMUX instance on GCP, released as MVP — "the simplest version of what it could be"
- Cursor was first customer; TurboPuffer reduced their vector DB bill by 95%
- CPU shortage is real and growing: RL training and agent execution both consume massive CPU
- "If you shut down all VMs, no data is lost" — S3-based durability as core invariant
- Six reasons to raise VC: R&D, growth, ego (dangerous), employee liquidity, strategic, M&A
- "Campfires" model: remote-first but with voluntary, periodic in-person gatherings
- Jensen Huang interaction: Simon couldn't stop talking about CPUs despite being told not to

### Follow-Up Items
- Review TurboPuffer as an alternative to in-memory vector databases
- Study Napkin Math methodology for infrastructure cost modeling
- Evaluate CPU allocation strategy for agent-heavy workloads
- Assess "campfires" remote culture model for distributed AI teams

### Impact on Enterprise AI Software Development
Simon's insight about CPU shortage is a critical, underappreciated infrastructure constraint for enterprise AI. As agent workloads grow (especially RL training and inference), CPU availability will become a bottleneck alongside GPU scarcity. TurboPuffer's S3-native architecture (vectors on object storage with caching) is a reference architecture for cost-efficient AI infrastructure — most enterprises are over-investing in DRAM-based vector stores. The Napkin Math approach is a powerful methodology for infrastructure engineers to validate vendor claims.

### Major References
- Napkin Math project (GitHub)
- TurboPuffer architecture blog posts

### Single Sentence Taken Out
> "If someone goes to prod, I'll set it up properly — but let's see if anyone cares first. It was the MVP of MVPs."

---

# DAY 2 — July 1, 2026 (Frontier Models & Agent Reliability Day)

---

## 15. Tariq Shihab-Eldin (Anthropic) — How to Work with Frontier Models (Claude Fable)

| Field | Value |
|---|---|
| **Timestamp** | 00:16:50 – 00:33:01 |
| **Speaker** | Tariq Shihab-Eldin (MTS, Anthropic / Claude Code) |
| **Session Type** | Keynote / Technical Talk |
| **Track** | Mainstage |

### Summary
Tariq introduced the "Mythos class" of models (Fable) as an RPG-like open world — "the map is opening up." He presented a four-part field guide: (1) Unhobbling Claude — models are grown, not designed; capability overhang means the model can do much more than we constrain it to. He showed the Pokemon example (which Pokemon end in AW?) — a chat model can't answer, but Claude Code can (writes a script to fetch and filter). He revealed that Anthropic recently removed 80% of Claude Code's system prompt because the new class of models is more imaginative than the examples we give it. (2) Finding your unknowns — the map (prompt/spec) is not the territory (actual codebase). Fable's bottleneck is the human's ability to match map to territory. Framework: known knowns, known unknowns, unknown knowns, unknown unknowns. Tools: blind spot passes, brainstorms/prototypes, interviews, references, implementation notes, quizzes. (3) Dealing with grief — Fable brings both gain and loss. The joy of hand-coding and the pain of debugging coexisted; "how can you not laugh, but also how can you not cry?" (4) Being unreasonable — Anthropic's culture: trade-offs are not real. "Good, fast, cheap — now it's pick three." The best way to prove agents work is to do the best work of our lives faster than ever before.

### Keywords & Tags
`claude-fable`, `mythos-class`, `unhobbling`, `capability-overhang`, `unknown-unknowns`, `being-unreasonable`, `map-is-not-territory`, `system-prompt-evolution`

### Key Knowledge Points
- Fable is a Mythos-class model — "the map is opening up"
- Capability overhang: models can do more than we constrain them to
- Pokemon example: chat model fails; agent with tools succeeds — capability overhang in action
- 80% of Claude Code system prompt removed — examples constrain the new class
- Ask User Question tool evolved: barely callable (Opus 4) → 40 questions about spec (Opus 4.5) → HTML reports with embedded questions (Fable)
- Four-part framework: unhobble Claude, find unknowns, deal with grief, be unreasonable
- Unknown unknowns found via blind spot passes, interviews, prototypes, references
- Trade-offs are not real — Anthropic culture: "force reality to show you the trade-off"

### Follow-Up Items
- Audit system prompts — reduce examples, increase context for Fable-class models
- Implement "blind spot pass" workflow before starting agent tasks
- Try "interview mode": ask Claude to question you about the spec before building
- Evaluate if the team is over-constraining models with excessive prompt rules

### Impact on Enterprise AI Software Development
Tariq's "capability overhang" concept is crucial for enterprises: the model can likely do more than your prompts constrain it to. The 80% system prompt reduction is a striking data point — enterprises should audit their prompts and remove constraints that may be hobbling newer models. The "being unreasonable" philosophy is a cultural challenge for enterprise risk-aversion: "good, fast, cheap — pick three" changes with frontier models.

### Major References
- Anthropic "Biology of a Large Language Model" paper
- Pokemon end-in-AW demonstration

### Single Sentence Taken Out
> "The map is opening up — you've been on the tutorial, and now you get to the open world."

---

## 16. Tariq Shawqi (Sonar) — AI Reliability: Verification as the Critical Path

| Field | Value |
|---|---|
| **Timestamp** | 00:35:44 – 00:53:10 |
| **Speaker** | Tariq Shawqi (CEO, Sonar) |
| **Session Type** | Keynote / Technical Talk |
| **Track** | Mainstage |

### Summary
Tariq Shawqi presented the hard data on AI reliability in enterprise settings. While Mythos models achieve 16–18 hours of autonomous task completion at 50% success rate (METR benchmark), dialing accuracy to 80% drops capability to ~3.5 hours — and 80% accuracy is still not enterprise-grade ("I'd put someone who gave me 80% accurate information on a performance review"). Sonar's own benchmarks on 4,000+ problems show frontier models generate buggy, complex, and insecure code. He cited a Carnegie Mellon study showing AI productivity gains dissipate after 3 months due to accumulated technical debt (security issues, maintainability, complexity). His framework: the Agent-Centric Development Cycle (ACDC) with three loops — guide (context + constraints), verify (zero-trust multi-layered verification), and solve (code generation). Key data: multi-layered verification reduces AI-derived production outages by 44%. Context and constraints reduce token consumption by 30%+ (agents navigate better with architectural awareness). A large bank using cutting-edge agentic tools achieved 92% reduction in issues with guide-verify-solve approach.

### Keywords & Tags
`ai-reliability`, `verification`, `acdc`, `zero-trust-verification`, `guide-verify-solve`, `metr-benchmark`, `technical-debt-compounding`, `sonar-vortex`

### Key Knowledge Points
- Mythos models: 16–18 hours task duration at 50% success; 3.5 hours at 80% success
- 80% accuracy is not enterprise-grade — "put them on a performance review"
- Carnegie Mellon study: 3–5× initial productivity gain fully dissipates in 3 months due to technical debt
- Agent-Centric Development Cycle (ACDC): guide (context + constraints), verify (multi-layered), solve
- Multi-layered verification reduces AI-derived outages by 44%
- Context + constraints reduce token consumption by 30%+
- 92% issue reduction at large bank with guide-verify-solve approach
- Three loops: agentic (inner), CI verification, code maintenance; verification at center

### Follow-Up Items
- Assess if the organization is seeing productivity dissipation (Carnegie Mellon pattern)
- Implement Sonar's guide-verify-solve framework or equivalent
- Audit current verification practices — are they "afterthought" or baked into the loop?
- Evaluate Sonar Vortex for agentic code quality

### Impact on Enterprise AI Software Development
This is perhaps the most sobering and critical talk for enterprise leaders. The Carnegie Mellon data showing productivity gains dissipating in 3 months is a warning that must be taken seriously. Shawqi's framework (guide → verify → solve) provides a concrete architecture for sustainable AI adoption. The 44% reduction in outages with multi-layered verification is a compelling ROI case. The insight that context + constraints reduce tokens 30%+ is immediately actionable.

### Major References
- METR benchmark (Measuring Agent Capability)
- Carnegie Mellon University study on AI productivity (3-month dissipation)
- Sonar code verification benchmarks

### Single Sentence Taken Out
> "My response to 80% accuracy was: I would still put someone who gave me 80% accurate information on a performance review — this isn't enterprise grade."

---

## 17. Onno Faber (Amazon AGI Lab) — Perception Agents: Completing the Computer-Use Loop

| Field | Value |
|---|---|
| **Timestamp** | 00:54:31 – 01:14:17 |
| **Speaker** | Onno Faber (Technical Staff, Amazon AGI Lab) |
| **Session Type** | Keynote / Technical Demo |
| **Track** | Mainstage |

### Summary
Onno argued that clicking is the easy part — the hard problem is completing the full perceive-plan-act loop. Current agents fire actions and move on without watching the result. He compared to robotics: a robot perceives, plans, then acts. Agents need the same loop, starting with perception — not scraping code behind the page but reading the rendered screen (layout, state, what changed). He introduced "perception agents" that can read the rendered interface, confirm their own output, and receive visual input from humans (pointing, not describing). He open-sourced two tools: (1) Annotation — a Chrome extension to mark elements on screen and tell the agent what to change (select heading → "make it red"; agent captures location + styles precisely); (2) Verification — an agent reads a design spec (design.md), visually checks the rendered app against it (colors, layout, components), and walks through user flows automatically. He demonstrated a real-world scenario: wearing B (AI glasses) in a design meeting, the transcript is captured, sent to the agent, applied to the website, and verified — all from the conversation. The core insight: shared context between human and agent (seeing the same screen) dramatically reduces explanation needed.

### Keywords & Tags
`perception-agents`, `computer-use`, `perceive-plan-act`, `visual-annotation`, `design-verification`, `shared-context`, `amazon-agi-lab`, `human-agent-interaction`

### Key Knowledge Points
- Clicking is the easy part; the real work lives "in the seams" between applications
- Current agents fire actions and move on — they don't watch the result or recover
- Robotics-inspired loop: perceive → plan → act (on screen, not just code)
- Perception = reading rendered interface (not scraping), tracking state/change in real time
- Two open-source tools: Annotation (point-to-change) and Verification (design spec checking)
- Verification does visual checks (on-brand?) and user flow checks (click through as real user)
- B glasses demo: meeting transcript → agent applies changes → verification report — all from conversation
- Shared screen = dramatically less explanation needed; "agent sees what you see"

### Follow-Up Items
- Try the open-source annotation tool (Chrome extension) for web development
- Evaluate verification tool for automated visual regression testing
- Consider perception agent pattern for enterprise workflows spanning multiple applications
- Explore human-agent interaction patterns beyond chat (pointing, visual feedback)

### Impact on Enterprise AI Software Development
Onno's work addresses the critical gap between agents that can use tools and agents that can complete real work. The perception loop (see rendered interface → confirm → recover) is essential for autonomous enterprise workflows that span multiple applications. The annotation and verification tools are immediately useful for web development teams. The "shared context" insight (agent sees what you see) points toward a future where human-agent interaction is more like collaboration than delegation.

### Major References
- Danielle Persik's podcast on human-agent interaction (Amazon AGI Lab)
- Robotics perception-plan-act loop

### Single Sentence Taken Out
> "If the agent one in four times deletes a database, you will never touch that agent again."

---

## 18. Benoit Schillings (Google DeepMind) — The Future of SE with AI: From Code to Science

| Field | Value |
|---|---|
| **Timestamp** | 01:15:44 – 01:33:48 |
| **Speaker** | Benoit Schillings (VP of Research, Google DeepMind) |
| **Session Type** | Keynote / Vision Talk |
| **Track** | Mainstage |

### Summary
Benoit Schillings traced his 45-year journey from Apple II assembly language to today's AI-driven coding, arguing that the fundamental bottleneck has shifted from the machine (assembly era) to the human brain (7–9 items of context, which determined software engineering practices) to now the AI era where code writing is nearly free. He presented the evolution from Pitchfork (2018, Google X project on ML for code) to today's reality: "superhuman syntax generation" — he cannot remember the last time Gemini wrote a function he could improve on. The hard problems remaining: multi-step codebase engineering (35M lines of PHP), architecture (humans still needed for inductive thinking), and security. He warned that 80% of new code on GitHub is machine-generated → we're running out of human training data. The solution: self-play (like AlphaZero). Frontier models can now create their own challenges, judge answers, and iterate — hundreds of millions of hours of self-play will unlock the next layer. He called for new evaluation benchmarks focused on open-ended problems (like text compression — "write the best lossless compressor"), new languages designed for models (strongly typed, proof-oriented, not necessarily human-readable), and active guardrails for security. Beyond code, he sees AI transforming science (chemistry with 10,000+ atoms, biology documentation, "the gold we cannot see").

### Keywords & Tags
`self-play`, `superhuman-syntax`, `code-is-free`, `pitchfork`, `new-language-for-models`, `open-ended-benchmarks`, `inductive-architecture`, `science-automation`, `deepmind`

### Key Knowledge Points
- 45-year coding journey: assembly → C → Python → vibe coding; "old dogs can learn new tricks"
- Human brain bottleneck: 7–9 items of context — determined all software engineering practices (now obsolete)
- Superhuman syntax generation: "I cannot remember the last time Gemini wrote a function I could improve on"
- 80% of new code on GitHub is machine-generated — human training data is running out
- Self-play (AlphaZero pattern): models create challenges, judge answers, iterate — no human data needed
- Need: open-ended benchmarks (text compression), new model-native languages (strongly typed, provable)
- Active guardrails: "teach models to write correct things from the start" not just detect vulnerabilities
- Beyond code: chemistry (10K atoms = life-like molecules), biology (nature's terrible documentation), "gold we cannot see"

### Follow-Up Items
- Evaluate self-play approaches for internal code generation models
- Consider open-ended benchmarks (compression, novel algorithm discovery) for model evaluation
- Track progress on proof-oriented languages designed for AI
- Explore AI-for-science opportunities in internal R&D

### Impact on Enterprise AI Software Development
Schillings' talk reframes the entire trajectory: we are past the "code writing" inflection point. The enterprise question is no longer "can AI write code" but "how do we manage the explosion of free code?" The self-play paradigm means models will improve without human-generated training data — a fundamental shift. The call for new evaluation approaches (open-ended, not pass/fail) and new programming languages (model-native, not human-readable) points to a radically different software engineering discipline within 2–3 years.

### Major References
- AlphaZero (DeepMind self-play)
- Pitchfork project (Google X, 2018)
- SWE-bench (critique: limited to pass/fail functional correctness)

### Single Sentence Taken Out
> "Code is over, but there's plenty to do."

---

## 19. Aparna Dinakaran (Arize AI) — Evals for Long-Horizon Tasks: Agent as Judge

| Field | Value |
|---|---|
| **Timestamp** | 01:37:10 – 01:41:58 |
| **Speaker** | Aparna Dinakaran (Co-founder & CPO, Arize AI) |
| **Session Type** | Keynote / Technical Talk |
| **Track** | Mainstage (Evals Track) |

### Summary
Aparna presented the evolution of evaluation: from single-prompt eval (2023) → tool call + reasoning eval (2024) → long-horizon agent trajectory eval (today). She revealed Arize runs 100M+ evals per month; the average team runs 12 eval jobs, top teams run 3,800+ evaluators. The key insight: as systems grew more complex, so did their failure modes — agents forget context, get stuck in loops, create dynamic UIs every session. Classical "LLM as judge" with fixed rubrics can't catch these failures because every trajectory is different. Her solution: "Agent as Judge" — an agent that reads traces, discovers patterns, and identifies subtle failures (e.g., inefficient repeated tool calls, loops that don't terminate). She announced Signal, a long-running evaluation agent that reads traces, discovers patterns, identifies issues classical evals miss, and can even file PRs to fix them. She argued the future is three-tier: deterministic evals + LLM as judge (fixed rubric) + Agent as judge (adaptive, dynamic, pattern-finding).

### Keywords & Tags
`evals`, `agent-as-judge`, `long-horizon-tasks`, `trace-analysis`, `arize`, `signal`, `trajectory-evaluation`, `llm-as-judge-limitations`

### Key Knowledge Points
- Eval landscape: 2023 (prompt) → 2024 (tool+reasoning) → today (long-horizon trajectories)
- Arize runs 100M+ evals/month; average team: 12 eval jobs; top teams: 3,800+ evaluators
- LLM as judge fails on dynamic, non-deterministic trajectories (every session is unique)
- Agent as judge: adaptive, pattern-finding, reads traces to discover novel failure types
- Signal: long-running eval agent that discovers failure patterns and files PR fixes
- Three-tier eval future: deterministic + LLM as judge + Agent as judge

### Follow-Up Items
- Evaluate three-tier eval architecture for internal agent monitoring
- Try Arize's Agent as Judge / Signal for trace analysis
- Move beyond "vibe checks" to structured, automated eval pipelines

### Impact on Enterprise AI Software Development
Aparna's three-tier framework gives enterprises a roadmap for eval maturity. Most enterprises are stuck at LLM as judge (tier 2) but need Agent as judge (tier 3) for long-horizon, autonomous agents. The insight that classical evals miss novel failure patterns in dynamic trajectories is critical for any enterprise deploying agents that interact with users in unpredictable ways.

### Major References
- Gary Tan: "Evals are everything you need"
- Arrow benchmark

### Single Sentence Taken Out
> "What if the best way to evaluate an agent was actually with an agent?"

---

## 20. Nisham Gupta (Meta) — From Offline Benchmarks to Production Reliability

| Field | Value |
|---|---|
| **Timestamp** | 02:15:51 – 02:20:35 (Day 2) |
| **Speaker** | Nisham Gupta (Software Engineering TL, Meta) |
| **Session Type** | Technical Keynote |
| **Track** | Mainstage |

### Summary
Nisham argued that agentic systems have fundamentally changed what evaluation means — moving from "did the model produce the correct answer?" to "did the system behave correctly?" Offline benchmarks measure model capability; production measures system behavior. Benchmarks don't capture tool failures, API outages, context changes, user variability, or long-running workflows. He introduced a hierarchy of agent failure modes: foundation (memory, retrieval, safety) → reasoning (planning, tool execution) → coordination (multi-agent failures). The mindset shift: think like an SRE, not a researcher. Measure reliability, availability, latency, cost, recovery — not accuracy. His pyramid: benchmarks (bottom, useful but limited) → scenario-based evaluations (middle, simulate realistic workflows) → production telemetry (top, highest value). The surprising insight: the most evaluation data comes from real users interacting with real systems. Evaluation is an always-running service, not a testing phase. Continuous monitoring is essential because agent systems drift constantly (model changes every 6 weeks, prompt changes, tool changes, user behavior changes).

### Keywords & Tags
`production-evals`, `sre-mindset`, `failure-mode-hierarchy`, `scenario-driven-eval`, `production-telemetry`, `continuous-evaluation`, `agent-drift`, `meta`

### Key Knowledge Points
- Agent systems change eval from "did model answer correctly?" to "did system behave correctly?"
- Benchmarks measure model capability; production measures system behavior — growing gap
- Failure mode hierarchy: foundation (memory/retrieval/safety) → reasoning (planning/execution) → coordination (multi-agent)
- Think like SRE, not researcher: measure reliability/availability/latency/cost, not accuracy
- Eval pyramid: benchmarks (bottom) → scenario-based (middle) → production telemetry (top)
- Most eval data comes from real users in production
- Agent systems drift constantly: model updates (every 6 weeks), prompt changes, tool changes, behavior changes
- Evaluation is an always-running operational service, not a pre-deployment phase

### Follow-Up Items
- Shift from accuracy-focused to reliability-focused evaluation metrics
- Implement scenario-based evaluations (customer support workflow, code gen workflow, research workflow)
- Build production telemetry pipeline for continuous agent evaluation
- Design drift detection system for agent behavior changes

### Impact on Enterprise AI Software Development
Nisham's SRE mindset is a critical reframing for enterprise AI teams. The failure mode hierarchy gives teams a structured way to think about agent failures beyond "hallucinations." The insight that evaluation is an always-running service (not a phase) means enterprises must invest in eval infrastructure as a production system, not a QA gate. The drift problem (models changing every 6 weeks) is a particularly acute challenge for regulated industries.

### Major References
- SRE practices (Google SRE book)
- Meta's training/inference infrastructure

### Single Sentence Taken Out
> "The question is no longer 'did the model generate the right answer?' — the question is 'did the system behave correctly?'"

---

## 21. Han Xiao (Jina AI / Elastic) — Scaling Search Intelligence: Test-Time Compute for Retrieval

| Field | Value |
|---|---|
| **Timestamp** | 02:20:40 – 02:35:55 |
| **Speaker** | Han Xiao (Founder, Jina AI / Elastic) |
| **Session Type** | Technical Keynote / Research Talk |
| **Track** | Mainstage |

### Summary
Han Xiao investigated whether test-time compute scaling works for small embedding models (not just large reasoning models). Using auto-research (agents running overnight), he explored two versions: Version A — an agent writes programs over a single frozen 200M-parameter embedder (Jina V5 nano). Over 144 generations, the agent discovered embedding algebra operations (chunking, scoring, feedback) without any retraining, second model, or learned parameters. Key result: the "compute rubric" (rewarding more compute) produced beautiful scaling curves in-domain but flat transfer to held-out tasks. The "transfer rubric" (rewarding only validation improvements without rewarding compute) discovered cheap, elegant programs (1–1.5× compute) that generalized across 4 unseen encoder families and 19 held-out tasks, winning 83% of comparisons without a single loss. Version B: agentic search pipeline with three open-source tools — Data Room (token-budgeted web exploration → zip file distilled corpus), Search Box (air-gapped testbed for agentic search), and Knowledge Graph (longest-path multi-hop questions for evaluation). His conclusion: "Search is test-time compute — don't reach for a bigger model, do more search at inference instead."

### Keywords & Tags
`test-time-compute`, `embedding-models`, `search-intelligence`, `auto-research`, `embedding-algebra`, `transfer-rubric`, `data-room`, `search-box`, `knowledge-graph`, `jina-elastic`

### Key Knowledge Points
- Test-time compute: spend more inference compute instead of training bigger models
- Version A: frozen 200M embedder + agent-discovered programming = relevance improvement
- Compute rubric (reward compute): beautiful in-domain scaling, flat transfer to held-out tasks
- Transfer rubric (reward only validation): cheap programs (1–1.5× compute) generalize across 4 unseen encoder families
- Best program: simple recombination of existing vector geometry, no new models — "it's all recomputation"
- Version B: Data Room (distilled web corpus), Search Box (air-gapped agentic search testbed), Knowledge Graph (multi-hop eval)
- "Search is test-time compute" — assemble more search at inference, don't train bigger models

### Follow-Up Items
- Evaluate test-time compute strategies for internal retrieval pipelines
- Try Data Room + Search Box for agentic search experiments
- Apply auto-research methodology to discover embedding algebra improvements

### Impact on Enterprise AI Software Development
Han's work has profound implications for enterprise RAG/search infrastructure: you can improve retrieval quality without retraining or upgrading models — just "assemble more search at test time." The transfer rubric finding (cheap, simple programs that generalize) means enterprises can discover useful embedding transformations automatically via overnight auto-research. The three open-source tools (Data Room, Search Box, Knowledge Graph) provide a complete testbed for optimizing search pipelines.

### Major References
- Noam Brown (OpenAI) poker bot test-time compute results
- ColBERT late interaction model
- AlphaCodium / auto-research methodologies

### Single Sentence Taken Out
> "More compute did not transfer — the cheap structure did."

---

## 22. Dominique Torneau (Resonate) — Specification Over Implementation: Durable Execution

| Field | Value |
|---|---|
| **Timestamp** | 02:41:09 – 02:50:33 |
| **Speaker** | Dominique Torneau (Founder & CEO, Resonate) |
| **Session Type** | Technical Keynote |
| **Track** | Mainstage |

### Summary
Dominique presented Resonate's working theory: general-purpose implementations will increasingly be replaced by bespoke implementations generated on demand from a specification. Reuse moves upstream — instead of reusing implementations, we reuse specifications. Using Resonate (a durable execution platform) with NATS.io as the case study, he showed the process: abstract specification → simulation implementation (executable design) → concrete specification → concrete implementation. The key finding: when agents jumped directly from abstract spec to concrete implementation (Rust on Postgres), they failed — the gap was too large (happy path worked, but broke on concurrency, process failure, network failure). Inserting a concrete specification layer (derived interactively with the agent but human-driven) made it work. The next step: agents moved further upstream by using a deterministic simulation environment to design the algorithm first, then write the concrete spec, then the implementation. Minimalism and simplicity are the finish line, not the starting point — three years of removing abstractions resulted in a tiny protocol centered on two objects (durable promise, durable task).

### Keywords & Tags
`specification-over-implementation`, `durable-execution`, `agent-upstream`, `concrete-specification`, `simulation-first`, `resonate`, `natsio`, `minimalism`

### Key Knowledge Points
- General-purpose implementations → bespoke implementations generated on demand from spec
- Reuse moves upstream: reuse specification, not implementation
- Resonate + NATS.io case study: abstract spec → simulation → concrete spec → implementation
- Direct jump from abstract spec to concrete implementation fails (happy path only)
- Concrete specification layer (human-driven) makes agent implementation succeed
- Next level: agents design via deterministic simulation before writing spec
- Minimalism is the finish line: 3 years of removing abstractions → 2 objects protocol

### Follow-Up Items
- Evaluate specification-first approach for enterprise agent architecture
- Consider deterministic simulation for agent design before production implementation
- Study Resonate's protocol as reference for minimal durable execution

### Impact on Enterprise AI Software Development
Dominique's "specification over implementation" thesis is a profound architectural insight for the AI era. Enterprises currently invest heavily in general-purpose implementations (libraries, frameworks, platforms). If implementations become cheap to generate, the value moves to the specification layer. This changes how enterprises should think about their intellectual property and architecture decisions. The simulation-first design pattern (agents test algorithms in simulation before writing production code) is a replicable methodology.

### Major References
- Resonate durable execution protocol
- NATS.io messaging system

### Single Sentence Taken Out
> "The product is no longer the implementation — the product is the specification, the protocol."

---

## 23. Unknown Speaker (Open-Ended Evolution / Recursive) — The Eureka Machine: RSI for Science

| Field | Value |
|---|---|
| **Timestamp** | 01:55:07 – 02:15:27 |
| **Speaker** | Unknown (Recursive / AIX Ventures) |
| **Session Type** | Keynote / Vision Talk |
| **Track** | Mainstage |

### Summary
The speaker presented a vision for the "Eureka Machine" — an automated scientific discovery engine inspired by evolution. Four pillars: (1) understand existing knowledge, (2) gather measurement data, (3) build simulations for unmeasurable phenomena, (4) physical lab for real experiments — all coordinated by an agent swarm. He argued that the exponential growth of science is hitting a "people bottleneck" (too many niche subfields, not enough scientists per field). The solution: recursive self-improvement (RSI) — AI that designs better AI. Three steps: ideation → implementation → validation. He demonstrated concrete proof points: NanoChat (training a small chat model in <5 minutes, beating the community record from 0.93 to 0.91 bits-per-byte by discovering novel ideas like hash bigrams and trigram embeddings), NanoGPT Speedrun (making training 2 seconds faster at 70 seconds, beating human+AI efforts over a year), and CUDA Kernel optimization (beating NVIDIA's benchmark leaderboard by a sizable margin across all kernel categories — without any CUDA kernel experts on the team). The key: RSI discovers truly novel ideas, not just hyperparameter tuning.

### Keywords & Tags
`eureka-machine`, `recursive-self-improvement`, `auto-research`, `nanochat`, `nanogpt-speedrun`, `cuda-kernels`, `scientific-discovery`, `open-ended-evolution`, `rsi`

### Key Knowledge Points
- Science hits a "people bottleneck" — too many subfields, not enough scientists per field
- Eureka Machine: knowledge → data → simulation → physical lab, coordinated by agent swarm
- Three-step RSI: ideation → implementation → validation; AI codes better AI
- NanoChat: discovered hash bigrams/trigrams, novel gating mechanisms — not just hyperparameter tuning
- NanoGPT speedrun: beating human+AI efforts of >1 year in days
- CUDA kernels: beating NVIDIA's own benchmark leaderboard without CUDA experts on team
- "When we take out a manual process and replace it with a learned system, improvements follow"
- Intelligence is multi-dimensional — we're still astronomically far from upper bounds

### Follow-Up Items
- Assess RSI-readiness of internal ML infrastructure
- Evaluate auto-research methodologies for optimization problems
- Track Recursive's open-source RSI tools and benchmarks

### Impact on Enterprise AI Software Development
The Eureka Machine vision represents the next frontier after coding agents: AI that does research. For enterprises, this means the R&D function itself may be automated sooner than expected. The proof points (NanoChat, kernel optimization) demonstrate that RSI is already producing novel discoveries, not just tuning. The "people bottleneck" of science is relevant for enterprise R&D — AI can explore far more hypotheses than human researchers.

### Major References
- AlphaZero / self-play (DeepMind)
- Karl Popper's philosophy of science (theory competition as evolution)
- Mark Andreessen's Techno-Optimist Manifesto
- NanoChat, NanoGPT speedrun, NVIDIA CUDA kernel benchmarks

### Single Sentence Taken Out
> "It may be true that we should fire all the AI engineers and have them mostly manage an actual AI engineer that is AI and works on AI."

---

## 24. Stefania Drug (Sakana AI) — Memory Harnesses for Long-Running Research Agents

| Field | Value |
|---|---|
| **Timestamp** | 02:50:44 – 03:01:49 |
| **Speaker** | Stefania Drug (Research Scientist, Sakana AI) |
| **Session Type** | Technical Talk |
| **Track** | Mainstage |

### Summary
Stefania tackled the problem of context rot in long-horizon agent tasks — where models contradict themselves, redo work, or drift from goals as context grows beyond the window. She noted that from METR projections, we're approaching a convergence where long-horizon tasks increase but model releases slow down, making memory management critical. She built a memory harness running on a local M3 Ultra (96GB, 28-core CPU) using DeepSeek V4 Flash and Qwen 27B. The harness design: research agents (zero durable memory) → core (always-shown traces) → recall block (tested modes: no memory, vector RAG, decisions ledger, oracle ground truth). Key finding: when tasks fit in context, memory adds cost without benefit. When context exceeds window, a ranked recall policy (decisions ledger prioritized by relevance) significantly outperforms no-memory baselines and naïve RAG. The oracle (ground truth memory) didn't hit max performance because the model can still choose to ignore it. A good structural recall policy saves tokens (bad memory is expensive — sends agent wrong direction). She open-sourced 30+ runnable memory cookbooks. Her broader point: sovereign AI — controlling the full stack (data, traces, evaluations) on local hardware — is increasingly important, especially for Japan's "sovereign AI" mission.

### Keywords & Tags
`memory-harness`, `context-rot`, `recall-policy`, `local-models`, `sovereign-ai`, `long-horizon-tasks`, `decisions-ledger`, `sakana-ai`

### Key Knowledge Points
- Context rot: models contradict themselves, redo work, drift from goals as context grows
- METR projection: long-horizon tasks rising + fewer model releases → memory becomes critical
- Harness design: research agents → core (traces) → recall block (policy modes)
- When task fits in context, memory adds cost without benefit
- Ranked decisions-ledger recall > no memory > vector RAG > oracle (can still be ignored)
- Good structural recall policy saves tokens; bad memory is expensive (sends agent wrong way)
- 30+ open-source memory cookbooks available
- Sovereign AI: controlling full stack on local hardware is strategically important

### Follow-Up Items
- Design recall policy as a first-class metric in agent systems
- Evaluate ranked decisions-ledger pattern for long-running enterprise agents
- Review open-source memory cookbooks for applicable techniques

### Impact on Enterprise AI Software Development
Stefania's findings are directly applicable to any enterprise running long-horizon agents. The key insight that memory helps only when context exceeds the window is a practical design heuristic. The ranked recall policy (decisions ledger prioritized by relevance) is a simple, implementable improvement over naïve RAG for agent memory. The "bad memory is expensive" finding has direct cost implications. The sovereign AI argument resonates with regulated industries that need full control over their AI stack.

### Major References
- METR projections on task horizon vs model release cadence
- Coinbase AI cost-reduction case study (transition to local models)
- X-Bench (long-horizon memory benchmark)

### Single Sentence Taken Out
> "Bad memory is expensive — it spends more tokens and can send the agent the wrong way."

---

## Methodology

This analysis was compiled from full transcript recordings of the AI Engineer World Fair 2026 mainstage sessions (June 30 – July 2, 2026). Sessions are grouped by speaker with verified timestamps. Each entry is self-contained to enable independent reading. Summaries are 200+ words covering context, problem, solution, and key results. Follow-up items are actionable. Impact assessments focus specifically on enterprise AI software development implications. All quotes are verbatim from transcripts.
