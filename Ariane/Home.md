# Ariane

Ariane is a semantic infrastructure for treating user interfaces as data.

[cite_start]It defines a universal graph model of software UIs—screens, controls, and the actions that connect them—so that external systems (such as AI agents or automation tools) can query this graph and use it as a reference when guiding users through software. [cite: 506, 507]

Ariane itself is not a help overlay or assistant. [cite_start]It is the underlying map. [cite: 508]

> [cite_start]**Core idea:** “UI as data” – represent any interface as a graph of states and transitions, independent of platform, styling, or branding. [cite: 509]

---

## Objectives

- [cite_start]Model software user interfaces as a machine-readable graph. [cite: 510]
- [cite_start]Make procedural knowledge (“how to do X in this tool”) accessible as data, not buried in tutorials. [cite: 511]
- [cite_start]Provide a stable reference layer for agents and tools that need to act inside existing software. [cite: 512]
- [cite_start]Support both **automated** and **human-guided** mapping of real applications. [cite: 513]
- [cite_start]Remain platform-agnostic: web, desktop, mobile, and other environments. [cite: 513]

---

## Components

Ariane is conceptually divided into two main components:

### Theseus (Exploration Engine)

[cite_start]Theseus is the exploratory engine that inspects real software and extracts a graph of: [cite: 514]

- [cite_start]**States** – distinct UI configurations (screens, dialogs, menus, etc.). [cite: 514]
- [cite_start]**Transitions** – user actions that move from one state to another (clicks, key presses, menu selections, etc.). [cite: 515]

[cite_start]It operates through platform-specific drivers (for web, desktop, mobile, etc.) that normalize different accessibility and UI APIs into a common internal representation. [cite: 516]

Theseus supports:

- [cite_start]**Automated exploration** where interfaces are accessible and safe to probe. [cite: 517]
- [cite_start]**Human-guided recording** where a human operator performs actions and Theseus records the resulting states and transitions as data. [cite: 518]

See:
- [Theseus](Theseus.md)
- [Theseus/Drivers](Theseus-Drivers.md)
- [Theseus/State-Identification](Theseus-State-Identification.md)
- [Theseus/Exploration-Engine](Theseus-Exploration-Engine.md)
- [Hybrid-Mapping-and-Human-Guided-Assistants](Hybrid-Mapping-and-Human-Guided-Assistants.md)

### Atlas (UI Graph and Ontology)

[cite_start]Atlas is the storage and semantic layer that persists the UI graph produced by Theseus. [cite: 519]

It provides:

- [cite_start]A **graph model** (states and transitions). [cite: 520]
- [cite_start]A **core schema** for representing UI elements, actions, and app metadata. [cite: 520]
- [cite_start]An **ontology vocabulary** for common UI patterns and semantic intents (“Save”, “Export”, “Create”, etc.). [cite: 521]
- Metadata fields to track provenance and quality:
  - e.g. `source = "auto" | "human"`, `review_status = "pending" | [cite_start]"verified"`. [cite: 522]

[cite_start]External systems query Atlas to understand what actions are possible from a given state and which sequences achieve a given intent. [cite: 523]

See:
- [Atlas](Atlas.md)
- [Atlas/Graph-Model](Atlas-Graph-Model.md)
- [Atlas/Core-Schema](Atlas-Core-Schema.md)
- [Atlas/Ontology-Vocabulary](Atlas-Ontology-Vocabulary.md)

---

## Intended Consumers

Ariane is designed as a data source. [cite_start]Typical consumers include: [cite: 524]

- [cite_start]**AI agents** that need to plan and execute steps inside existing software. [cite: 525]
- [cite_start]**Automation tools** that want a declarative description of UI workflows. [cite: 526]
- [cite_start]**Analysis tools** that reason about UI complexity, accessibility, or consistency. [cite: 527]
- **Human assistants / operator consoles** that provide step-by-step textual guidance to users or operators, using Atlas as the underlying reference graph. [cite_start]See [Hybrid-Mapping-and-Human-Guided-Assistants](Hybrid-Mapping-and-Human-Guided-Assistants.md). [cite: 528]

[cite_start]A future, optional overlay-style client could be built on top of Ariane as one specific consumer, but it is not part of the core scope. [cite: 529]

See:
- [Consumers](Consumers.md)
- [Consumers/AI-Agent-Integration](Consumers-AI-Agent-Integration.md)
- [Consumers/Future-Overlay-Client](Consumers-Future-Overlay-Client.md)

---

## Conceptual Flow

1. **Exploration**
   [cite_start]Theseus runs against a target application, observing the UI and exploring possible actions (either automatically, or with a human performing the actions). [cite: 530]

2. **Extraction**
   [cite_start]It identifies UI states, fingerprints them, and records transitions between them, annotating metadata such as source (`auto` / `human`) and optional intents. [cite: 531]

3. **Storage**
   [cite_start]The resulting graph (states + transitions + semantics) is written into Atlas using the defined schema and ontology. [cite: 532]

4. **Consumption**
   [cite_start]External systems query Atlas to: [cite: 533]
   - Recognize where a user currently is (state identification).
   - Determine valid next actions (outgoing transitions).
   - Compute paths from a current state to a goal state (intent).
   - [cite_start]Generate step-by-step guidance for human operators. [cite: 534]

---

## Navigation

- [cite_start][Background-UI-as-Data](Background-UI-as-Data.md) – context and motivation (“procedural knowledge gap”). [cite: 535]
- [Theseus](Theseus.md) – exploration engine architecture and behavior.
- [cite_start][Atlas](Atlas.md) – UI graph model and semantic schema. [cite: 536]
- [Hybrid-Mapping-and-Human-Guided-Assistants](Hybrid-Mapping-and-Human-Guided-Assistants.md) – hybrid exploration and human-in-the-loop patterns.
- [cite_start][Consumers](Consumers.md) – how external systems use Ariane’s data. [cite: 537]
- [Glossary](Glossary.md) – definitions of key terms.