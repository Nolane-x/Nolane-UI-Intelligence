---
name: compressing-ui-decisions-for-execution
description: Use when implementation is imminent and a large routed UI reasoning graph must become a compact action brief without dropping hard constraints, evidence handles, or conditions that require deeper reasoning.
---

# Compressing UI Decisions for Execution

## Parent Contract
**Required parent:** `compiling-ui-implementation-specifications`.

Receive resolved typed outputs, hard gates, concrete design packet, implementation authority plan, unresolved risks, acceptance hooks and the current build target. The parent contains full implementation detail; this skill creates a focused working set for the implementer.

## Decision Boundary
Own **lossless obligation compression**, not summarization for readability. A shorter brief is successful only when an implementation built from it still satisfies the same non-waivable obligations and knows when to reopen deeper context.

## Compression Model
Partition information into:
- `must_hold`: safety, semantics, accessibility, platform, product truth, user-requested constraints, release gates;
- `make_concrete`: selected layout/type/material/signature/motion decisions with rationale handles;
- `implementation_edges`: source/library ownership, APIs, state/event contracts and tests;
- `open_questions`: unresolved items that forbid guessing;
- `reference_handles`: pointers back to full artifacts.

Use **decision budget allocation** only for working-memory choices, never for obligations. Collapse redundant rationale after preserving one stable handle. Never compress contradictory evidence into a false consensus.

## Ambiguity Budget
Declare a small ambiguity budget for low-impact implementation freedom. Anything capable of altering task semantics, platform fit, accessibility, signature identity or high-ambition visual thesis is outside that budget. When the implementer encounters an out-of-budget decision, use a **re-expansion trigger** and reopen the owning artifact/skill instead of improvising.

## Fast Path Contract
The execution brief should make common work quick: exact component/primitive choices when justified, concrete type/surface/layout decisions, target viewports/states, and verification commands. Speed comes from resolved knowledge, not from bypassing research.

## Output — `ui-execution-brief`
Emit a **compression checksum** that becomes stale whenever a hard upstream obligation changes. Return `must_hold[]`, `concrete_decisions[]`, `implementation_edges[]`, `acceptance_hooks[]`, `open_questions[]`, `reference_handles[]`, `ambiguity_budget`, `re_expansion_triggers[]`, and `compression_checksum` over obligation identities.

## Falsification
Compare the brief against the upstream obligation ledger. Delete the full context and ask a fresh implementer what is forbidden, what is unresolved, and how each material decision will be verified. Missing answers reveal lossy compression. Mutate one hard obligation upstream; the checksum/brief must become stale.

## Recovery
Re-expand only the affected owner output, restore lost obligation IDs or evidence handles, reduce optional prose, and regenerate the brief. If the brief cannot stay small without dropping safety/semantic constraints, prefer a larger brief over false simplicity.

## Hard gate
**An execution brief cannot replace its source graph unless every hard obligation survives, concrete decisions retain rationale/provenance handles, unresolved decisions remain explicit, and re-expansion triggers protect choices outside the ambiguity budget.**
