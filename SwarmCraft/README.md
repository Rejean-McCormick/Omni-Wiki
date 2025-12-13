# SwarmCraft: Deterministic Story Engine

> **Architectural Lineage:**
> [cite_start]SwarmCraft is an **architectural fork and deep rewrite** of the multi-agent swarm engine created by **[Mojomast](https://github.com/mojomast)** in `mojomast/swarmussy`[cite: 1, 36].
> [cite_start]Its deterministic layering is derived from the meta-structure of the **Abstract Wiki Architect**[cite: 2].

## [cite_start]**POWERED BY GROK** [cite: 3]

[cite_start]**SwarmCraft** is a deterministic, data-driven story engine designed to transform explicit project state into prose using a strict control loop[cite: 3, 4]. [cite_start]Unlike chat-based swarms, it separates **Brain** (LLM personas), **Logic** (orchestration), and **Memory** (explicit state) to ensure long-form narrative coherence[cite: 4].

-----

## 1\. Core Architecture

[cite_start]The system operates on a "Three-Layer Model" to prevent hallucinations and state drift[cite: 4]:

  * [cite_start]**Brain (Personas):** Stateless services (Architect, Narrator, Editor) that never own canonical state[cite: 5].
  * [cite_start]**Logic (Engine):** The runtime that handles the `SCAN → PLAN → EXECUTE` loop and tool execution[cite: 6].
  * [cite_start]**Memory (State):** All truth lives in the **Matrix** (runtime status), **Story Bible** (creative intent), and **RAG DB** (long-term continuity)[cite: 11].

### The Deterministic Pipeline

SwarmCraft replaces emergent coordination with a strict cycle:

1.  [cite_start]**SCAN:** Recompute reality from disk[cite: 7].
2.  [cite_start]**PLAN:** Select the next atomic **Part** to draft or revise[cite: 8].
3.  [cite_start]**EXECUTE:** Run one persona on that Part, then exit[cite: 9].

-----

## 2\. Documentation Modules

### Core Logic & Orchestration

  * **[Architecture Overview](https://www.google.com/search?q=Architecture-Overview.md)** – High-level diagram of the Brain/Logic/Memory separation.
  * **[Deterministic Pipeline](https://www.google.com/search?q=Deterministic-Pipeline-Scan-Plan-Execute.md)** – Detailed breakdown of the SCAN-PLAN-EXECUTE control loop.
  * [cite_start]**[Prompt Hydration](https://www.google.com/search?q=Orchestration-Slice-By-Slice-Prompt-Hydration.md)** – How the engine prevents "prompt sprawl" by injecting only the active Part slice[cite: 88].
  * [cite_start]**[Provider Adapter: Grok](https://www.google.com/search?q=Provider-Adapter-Grok.md)** – The normalization layer that keeps the engine model-agnostic[cite: 120].

### State & Schema (The Truth)

  * [cite_start]**[Central Matrix](https://www.google.com/search?q=Central-Matrix-Runtime-State.md)** – The machine-readable runtime state (`matrix.json`)[cite: 11].
  * [cite_start]**[Story Bible (Intent)](https://www.google.com/search?q=Story-Bible-Creative-Intent.md)** – Where characters, lore, and constraints live[cite: 19].
  * [cite_start]**[Story Scaffold](https://www.google.com/search?q=Story-Scaffold-Templates-Outline-Parts.md)** – The grid system combining Templates and Outlines[cite: 210].
  * [cite_start]**[Schema: Templates](https://www.google.com/search?q=Schema-Templates.md)** – Defining thread sets and pacing rules[cite: 187].
  * [cite_start]**[Schema: Outline](https://www.google.com/search?q=Schema-Outline.md)** – Defining chapters, parts, and beat contracts[cite: 163].

### Operations & Usage

  * [cite_start]**[Dashboard TUI](https://www.google.com/search?q=Dashboard-TUI-Reference.md)** – The "Mission Control" interface for observing the engine[cite: 48].
  * [cite_start]**[Multi-Project Management](https://www.google.com/search?q=Multi-Project-Management.md)** – Running isolated universes in a single runtime[cite: 77].
  * [cite_start]**[Outline Grid & CSV](https://www.google.com/search?q=Outline-Grid-CSV-Round-Trip.md)** – Round-tripping the story structure via spreadsheets[cite: 102].
  * [cite_start]**[RAG Memory System](https://www.google.com/search?q=RAG-Memory-System.md)** – Long-term retrieval for narrative continuity[cite: 135].

-----

## 3\. Key Concepts

### Parts, Not Chapters

The atomic unit of work is the **Part**. [cite_start]Chapters are simply rollups of 1–6 Parts[cite: 13]. This allows for small, stable prompt slices and targeted regeneration.

### Slice-by-Slice Hydration

[cite_start]The engine never dumps the whole Story Bible into the LLM[cite: 31]. [cite_start]It hydrates prompts with **only** the active Part's beats, contract, and relevant RAG evidence[cite: 88].

### Credits & Lineage

  * [cite_start]**Upstream Foundation:** Mojomast/swarmussy (Multi-agent patterns, TUI concepts)[cite: 39].
  * **Meta-Structure:** Abstract Wiki Architect (State separation).
  * **Full Credits:** **[Read the Credits & Lineage Page](https://www.google.com/search?q=Credits-And-Lineage.md)**.