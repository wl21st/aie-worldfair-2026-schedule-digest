# Investigation Report: AI Engineer World's Fair 2026 Speaker Embeddings

## 1. Overview & Dataset Metadata

This report details the technical investigation, preprocessing, vector duplicate analysis, and cross-verification of the dataset stored in `raw/speakers-embeddings.json`.

* **Conference**: AI Engineer World's Fair 2026 (San Francisco, CA)
* **Embedding Model**: `gemini-embedding-2-preview`
* **Output Dimensions**: `128` (truncated using Matryoshka Representation Learning / MRL from native `3072` dimensions)
* **Total Speakers Embedded**: `550`
* **Source Files**: `raw/speakers-embeddings.json`, `raw/speakers.json`, `raw/sessions.json`

---

## 2. Technical Purpose & Constraints

### Why the Embedding Algorithm Is Required for Querying
Embedding vectors are non-interpretable positions in a high-dimensional vector space. Each model projects language into a unique coordinate system. To perform natural language searches (e.g. *"Find talks on LLM evals"*), incoming queries **must** be embedded using `gemini-embedding-2-preview` with 128 MRL dimensions. Querying with a different model produces random, unaligned vector dot products.

### Usability Without the Model
Even without generating new query embeddings, the pre-computed 128-dimensional vectors support in-memory processing:
1. **Item-to-Item Recommendations**: Computing cosine similarity between existing speakers to show "Related Speakers" or "Related Sessions".
2. **2D Visual Clustering**: Running UMAP or t-SNE to group 550 speakers into thematic tracks.
3. **Duplicate & Overlap Detection**: Uncovering identical speaker profiles or overlapping talk content.

---

## 3. Duplicate & Similarity Analysis

An in-memory matrix multiplication was conducted across all 150,975 pairwise speaker combinations ($\frac{550 \times 549}{2}$).

### A. Exact Duplicates ($\ge 0.9999$)
* **Count**: `0`
* **Result**: All 550 speaker IDs, names, and embedding vectors are unique and verified intact.

### B. Co-Speaker Same-Talk Clusters ($\ge 0.95$)
The highest similarity scores ($0.955 - 0.977$) correspond to **co-speakers presenting the exact same talk or workshop**:

| Cosine Similarity | Speaker A | Speaker B | Shared Talk / Workshop Title |
| :--- | :--- | :--- | :--- |
| **0.9767** | Qianru Lao *(OpenAI)* | Lu Zhang *(OpenAI)* | Routing LLM Inference in Production: From Engine Signals to Policy |
| **0.9732** | Nachiket Paranjape *(DoorDash)* | Swaroop Chitlur Haridas *(DoorDash)* | AI Evals Platform for Cross-Functional Teams at Scale |
| **0.9716** | Yubo Wang *(Together AI)* | Jue Wang *(Together AI)* | Open-Source Inference Engineering for the Agentic Era |
| **0.9689** | Khaled Alashmouny *(AIDAChip)* | Abduallah Mohamed *(AIDAChip)* | What If Your Chip Design Team Moved Like a Single Body? |
| **0.9665** | Vayum Arora *(Weco AI)* | Dhruv Srikanth *(Weco AI)* | Hands-on AutoResearch: Cracking OpenAI's Parameter Golf |
| **0.9658** | Akele Reed *(SonderMind)* | Dave Revere *(SonderMind)* | Evals Driven-Development: Engineering a Mental Health AI Coach Ethically & Safely |

---

## 4. Lowered Threshold Analysis ($\ge 0.85$)

When lowering the cosine similarity threshold to **0.85**:
* **Total Pairs $\ge 0.85$**: **107,158 pairs** ($\sim 71\%$ of all combinations)

### High Domain Baseline
Because all 550 abstracts belong to the narrow domain of *AI Engineering & LLM Infrastructure*, the embedding vectors cluster closely. Most unrelated AI talks score between **0.75 and 0.85**.

### Cross-Session Thematic Overlaps ($0.88 - 0.95$)
Lowering the threshold to $0.88 - 0.95$ surfaces **different talks addressing similar technical challenges**:

| Cosine Similarity | Speaker A & Talk | Speaker B & Talk | Revealed Theme |
| :--- | :--- | :--- | :--- |
| **0.9531** | Yunmo Koo *(FriendliAI)*<br>`Inference performance as a competitive advantage` | Byung-Gon Chun *(FriendliAI)*<br>`The Frontier AI Inference Cloud for Agents` | **Inference Engines & Cloud** |
| **0.9477** | Shruti Arora *(Amazon AGI Lab)*<br>`Build with Perception Agents` | Antje Barth *(Amazon AGI Lab)*<br>`Perception Agents` | **Multimodal Perception** |
| **0.9472** | Merve Noyan *(Hugging Face)*<br>`e2e vision apps on edge` | Asma Beevi *(NVIDIA)*<br>`Compression at the Edge` | **Edge Computing & Vision** |
| **0.9438** | Uday Kiran Medisetty *(Uber)*<br>`Agentic SDLC at Uber` | Ameya Ketkar *(Uber)*<br>`Scaling Code Quality: uReview Engine` | **Enterprise Agentic SDLC** |
| **0.9435** | Cornelia Davis *(Temporal)*<br>`MCP Tasks (async)` | Melanie Warrick *(Temporal)*<br>`The Human Is an Async API` | **Async Agent Orchestration** |
| **0.9400** | Omer Primor *(Bright Data)*<br>`Context-as-a-Service for Agentic AI` | Omri Bruchim *(Monday)*<br>`From Systems of Record to Systems of Context` | **Context Engineering & RAG** |

---

## 5. Verification & Video Evidence

Recorded sessions from the AI Engineer World's Fair are hosted on the official **[AI Engineer YouTube Channel](https://www.youtube.com/@ai-engineer-worldsfair)**.

Verified sessions with direct YouTube recordings in the repo:
- **Evals-Driven Development (SonderMind)**: [Watch Recording](https://www.youtube.com/watch?v=O72p-rBb2bA) *(Co-speakers: Akele Reed, Dave Revere, Doug Keller — Similarity 0.9658)*
- **In the Land of AI Agents, the Verifiers Are King**: [Watch Recording](https://www.youtube.com/watch?v=VrpEyglYgeU) *(Tariq Shaukat)*
- **Agentic Security**: [Watch Recording](https://www.youtube.com/watch?v=yWS0udrIOc8) *(Steve Yegge)*
- **What is an Inference Engine, Anyway?**: [Watch Recording](https://www.youtube.com/watch?v=DeFF3J8T5Pk) *(Charles Frye)*
- **Evals in AI: A Deep Dive**: [Watch Recording](https://www.youtube.com/watch?v=C_GG5g38vLU) *(Tejas Kumar)*
- **From fork() to Fleet: Designing an Agent Sandbox Cloud**: [Watch Recording](https://www.youtube.com/watch?v=OqM67QG_Ikk) *(Abhishek Bhardwaj)*

---

## 6. Recommendations for Preprocessing Thresholds

* **Exact Duplicate / Co-Speaker Detection**: Similarity $\ge 0.955$
* **"Related Sessions" / Content Recommendation**: Similarity between **0.90 and 0.94**
* **Noise Floor**: Similarity $< 0.85$ (Domain baseline for AI engineering topics)
