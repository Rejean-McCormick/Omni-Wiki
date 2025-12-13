# 🐜 SwarmCraft Wiki (v3.0.0)

> **Architectural Lineage (Upstream Credit):**  
> SwarmCraft is an **architectural fork and deep rewrite** of the multi-agent swarm engine created by **[Mojomast](https://github.com/mojomast)** in **[mojomast/swarmussy](https://github.com/mojomast/swarmussy)**.  
> SwarmCraft’s deterministic “Architect-style” layering is also **derived from the meta-structure of Abstract Wiki Architect (AWA)**.  
> Full lineage details: **[[Credits & Lineage]]**

## **POWERED BY GROK** ⚡️

SwarmCraft is a **data-driven AI story engine** for long-form narrative generation: deterministic orchestration, multi-project isolation, RAG memory for continuity, and a structured story scaffold (templates + outline + parts).

---

## 🧭 Wiki Navigation (Architecture-First)

### Core Architecture
- **[[Architecture Overview]]**
- **[[Deterministic Pipeline (SCAN-PLAN-EXECUTE)]]**
- **[[Central Matrix (Runtime State)]]**
- **[[Story Bible (Creative Intent)]]**
- **[[Orchestration Slice-by-Slice Prompt Hydration]]**

### Story Scaffold (New)
- **[[Story Scaffold (Templates-Outline-Parts)]]**
- **[[Schema Templates]]**
- **[[Schema Outline]]**
- **[[Outline Grid CSV Round-Trip]]**

### Systems
- **[[RAG Memory System]]**
- **[[Multi-Project Management]]**
- **[[Dashboard TUI Reference]]**
- **[[Provider Adapter Grok]]**

---

## Status

| Component | Status | Note |
| :--- | :--- | :--- |
| **Version** | **3.0.0** | SwarmCraft (fork + deep rewrite) |
| **Architecture** | Active / Stable | Swarmussy foundation + AWA-derived deterministic layering |
| **Scaffold** | Active | Templates + Outline + Parts |
| **Memory** | Active | Per-project RAG |
| **Interface** | TUI | Real-time mission control |

---

## What’s New in SwarmCraft (v3.0)

- **AWA-derived deterministic architecture**: decouples **Brain / Logic / Memory** and enforces a strict pipeline.
- **Parts-based writing**: a *Part* is the atomic unit of drafting/revision; chapters are rollups.
- **Story Scaffold**: template-defined narrative threads + outline grid for human editing.
- **Slice-by-slice prompt hydration**: only the active Part slice is injected into the model to reduce repetition.
- **Multi-project isolation**: each universe has isolated state, configs, and memory.
- **RAG continuity**: long-term memory retrieval for consistency across 100k+ words.

---

## Quick Start (Engine + Monitor)

SwarmCraft runs in two terminals.

### Terminal 1: Engine (Moteur)
```bash
python main.py
````

### Terminal 2: Monitor (Moniteur)

```bash
python dashboard.py
```

---

## Notes

* Credits are centralized here: **[[Credits & Lineage]]**
* Grok configuration details: **[[Provider Adapter Grok]]**


