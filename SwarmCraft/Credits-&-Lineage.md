# Credits & Lineage

SwarmCraft is built on two explicit lineages:

1) **Swarm foundation (upstream):** the multi-agent swarm engine patterns created by **[Mojomast](https://github.com/mojomast)** in **[mojomast/swarmussy](https://github.com/mojomast/swarmussy)**.  
2) **Architect meta-structure (AWA):** the deterministic “Architect-style” separation of **Brain / Logic / Memory** and state-first orchestration derived from **Abstract Wiki Architect (AWA)**.

---

## 1) Upstream Credit: Mojomast / swarmussy

SwarmCraft is an **architectural fork and deep rewrite**. The upstream project established the original swarm runtime approach and core implementation patterns.

**All architectural credit** for the original **multi-agent swarm design**—including the chatroom runtime concepts, terminal dashboard pattern, and foundational orchestration/tooling modules—belongs to **Mojomast**:

- Upstream author: **[Mojomast](https://github.com/mojomast)**
- Upstream repository: **[mojomast/swarmussy](https://github.com/mojomast/swarmussy)**

### Upstream-derived core module lineage (examples)
SwarmCraft acknowledges lineage (conceptual and/or code-derived depending on file history) from swarmussy patterns around:

- Agent tooling gateway  
  - `core/agent_tools.py`
- Task planning / task routing  
  - `core/task_manager.py`
- Token usage tracking  
  - `core/token_tracker.py`
- Dashboard / mission control pattern (TUI)

If upstream code is present in this repository, upstream license notices must be preserved alongside the derived files.

---

## 2) What SwarmCraft Adds / Changes

SwarmCraft reuses and extends the swarm foundation while introducing deterministic, story-first architecture and structured narrative state.

### 2.1 Deterministic pipeline
SwarmCraft replaces chatroom-style emergent coordination with a strict loop:

**SCAN → PLAN → EXECUTE**

- SCAN: reconcile truth from disk and update runtime state
- PLAN: select the next target Part and action
- EXECUTE: run one persona on one Part using guarded tools

See: **[[Deterministic Pipeline (SCAN-PLAN-EXECUTE)]]**

### 2.2 State-first narrative architecture (Brain / Logic / Memory)
SwarmCraft formalizes narrative work into explicit layers:

- **Brain**: stateless LLM personas (Architect, Narrator, Editor)
- **Logic**: orchestrator + tools + validation
- **Memory**: Matrix + Story Bible + RAG index

See: **[[Architecture Overview]]**

### 2.3 Parts-based story execution
SwarmCraft treats a **Part** as the atomic unit of drafting/revision.
Chapters are rollups over Parts.

See:
- **[[Central Matrix (Runtime State)]]**
- **[[Orchestration Slice-by-Slice Prompt Hydration]]**

### 2.4 Story Scaffold (Templates + Outline + Grid)
SwarmCraft introduces a structured story scaffold designed for both humans and LLMs:

- Templates define threads + cadence + default parts/chapter
- Outline defines chapters→parts mapping + per-part thread beats + part contracts
- Grid view displays the outline as a spreadsheet-like matrix, with optional CSV round-trip

See:
- **[[Story Scaffold (Templates-Outline-Parts)]]**
- **[[Schema Templates]]**
- **[[Schema Outline]]**
- **[[Outline Grid CSV Round-Trip]]**

### 2.5 Multi-project isolation
Each project has isolated:
- Matrix
- Story Bible
- Memory DB (RAG)

See: **[[Multi-Project Management]]**

### 2.6 RAG long-term continuity
SwarmCraft integrates per-project retrieval memory to maintain coherence in long works.

See: **[[RAG Memory System]]**

---

## 3) Provider Layer (Powered by Grok)

SwarmCraft is **powered by Grok** via a provider adapter that keeps the engine provider-agnostic:
- normalized request/response
- normalized tool calling
- centralized retries and error handling

See: **[[Provider Adapter Grok]]**

---

## 4) Attribution Guidance for Derivative Works

If you build on SwarmCraft, you should preserve:
- this Credits & Lineage page (or an equivalent notice in your primary documentation)
- upstream references to Mojomast/swarmussy
- any third-party license notices for code you redistribute

This page is the canonical place for lineage statements to avoid repeating long credit blocks throughout the wiki.
