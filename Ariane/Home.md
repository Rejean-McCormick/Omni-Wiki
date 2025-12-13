# Ariane

Ariane is a semantic infrastructure for treating user interfaces as data.

It defines a universal graph model of software UIs—screens, controls, and the actions that connect them—so that external systems (such as AI agents or automation tools) can query this graph and use it as a reference when guiding users through software.

Ariane itself is not a help overlay or assistant. It is the underlying map.

> **Core idea:** “UI as data” – represent any interface as a graph of states and transitions, independent of platform, styling, or branding.

---

## Objectives

- Model software user interfaces as a machine-readable graph.
- Make procedural knowledge (“how to do X in this tool”) accessible as data, not buried in tutorials.
- Provide a stable reference layer for agents and tools that need to act inside existing software.
- Support both **automated** and **human-guided** mapping of real applications.
- Remain platform-agnostic: web, desktop, mobile, and other environments.

---

## Components

Ariane is conceptually divided into two main components:

### Theseus (Exploration Engine)

Theseus is the exploratory engine that inspects real software and extracts a graph of:

- **States** – distinct UI configurations (screens, dialogs, menus, etc.).
- **Transitions** – user actions that move from one state to another (clicks, key presses, menu selections, etc.).

It operates through platform-specific drivers (for web, desktop, mobile, etc.) that normalize different accessibility and UI APIs into a common internal representation.

Theseus supports:

- **Automated exploration** where interfaces are accessible and safe to probe.
- **Human-guided recording** where a human operator performs actions and Theseus records the resulting states and transitions as data.

See:  
- [[Theseus]]  
- [[Theseus/Drivers]]  
- [[Theseus/State-Identification]]  
- [[Theseus/Exploration-Engine]]  
- [[Hybrid-Mapping-and-Human-Guided-Assistants]]

### Atlas (UI Graph and Ontology)

Atlas is the storage and semantic layer that persists the UI graph produced by Theseus.

It provides:

- A **graph model** (states and transitions).
- A **core schema** for representing UI elements, actions, and app metadata.
- An **ontology vocabulary** for common UI patterns and semantic intents (“Save”, “Export”, “Create”, etc.).
- Metadata fields to track provenance and quality:
  - e.g. `source = "auto" | "human"`, `review_status = "pending" | "verified"`.

External systems query Atlas to understand what actions are possible from a given state and which sequences achieve a given intent.

See:  
- [[Atlas]]  
- [[Atlas/Graph-Model]]  
- [[Atlas/Core-Schema]]  
- [[Atlas/Ontology-Vocabulary]]

---

## Intended Consumers

Ariane is designed as a data source. Typical consumers include:

- **AI agents** that need to plan and execute steps inside existing software.
- **Automation tools** that want a declarative description of UI workflows.
- **Analysis tools** that reason about UI complexity, accessibility, or consistency.
- **Human assistants / operator consoles** that provide step-by-step textual guidance to users or operators, using Atlas as the underlying reference graph. See [[Hybrid-Mapping-and-Human-Guided-Assistants]].

A future, optional overlay-style client could be built on top of Ariane as one specific consumer, but it is not part of the core scope.

See:  
- [[Consumers]]  
- [[Consumers/AI-Agent-Integration]]  
- [[Consumers/Future-Overlay-Client]]

---

## Conceptual Flow

1. **Exploration**  
   Theseus runs against a target application, observing the UI and exploring possible actions (either automatically, or with a human performing the actions).

2. **Extraction**  
   It identifies UI states, fingerprints them, and records transitions between them, annotating metadata such as source (`auto` / `human`) and optional intents.

3. **Storage**  
   The resulting graph (states + transitions + semantics) is written into Atlas using the defined schema and ontology.

4. **Consumption**  
   External systems query Atlas to:
   - Recognize where a user currently is (state identification).
   - Determine valid next actions (outgoing transitions).
   - Compute paths from a current state to a goal state (intent).
   - Generate step-by-step guidance for human operators.

---

## Navigation

- [[Background-UI-as-Data]] – context and motivation (“procedural knowledge gap”).  
- [[Theseus]] – exploration engine architecture and behavior.  
- [[Atlas]] – UI graph model and semantic schema.  
- [[Hybrid-Mapping-and-Human-Guided-Assistants]] – hybrid exploration and human-in-the-loop patterns.  
- [[Consumers]] – how external systems use Ariane’s data.  
- [[Glossary]] – definitions of key terms.
