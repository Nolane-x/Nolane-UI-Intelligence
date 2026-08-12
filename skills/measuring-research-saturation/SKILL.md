---
name: measuring-research-saturation
description: Use when a substantial UI research wave may be ready to stop, when someone claims broad industry coverage, or when currentness and diminishing returns need a falsifiable completion decision.
---

# Measuring Research Saturation

## Overview
Research cannot prove that no future knowledge exists. This skill makes the narrower claim that, for a dated scope and source set, further search is no longer producing material new UI mechanisms or uncovered mandatory domains.

## Parent Contract
**Required parent:** `researching-ui-frontiers`.

Do not invoke saturation before the atlas and source ledger have been updated with the current wave. “I have read enough” is not evidence.

## Decision Model
Evaluate five dimensions independently.

**Breadth:** every mandatory atlas cell has an owner, verifier, and at least one appropriate authority path. **Depth:** high-risk and high-drift domains have multiple independent primary sources when the ecosystem provides them, plus deeper mechanism extraction rather than duplicated summaries. **Contradictions:** conflicts are resolved by scope/authority or preserved explicitly as unresolved; silence is not resolution. **Novelty:** run a final adversarial search wave using adjacent terminology, competing platforms, and failure-oriented queries. Measure whether it produces a new decision rule, failure mode, measurement method, platform delta, or coverage class. **Freshness:** high-drift records have review timestamps and radar cadence.

SATURATED requires all five dimensions to pass. A low novelty rate alone cannot compensate for an unowned medical, automotive, accessibility, or AI safety cell. Conversely, a field with hundreds of near-duplicate design-system pages does not need endless collection once mechanism novelty has collapsed.

Always attach reopen conditions. A platform release, regulatory update, new input modality, new AI UI standard, or contradictory evidence invalidates the old saturation decision for affected domains.

## Evidence
Use counts only as secondary evidence. Primary evidence is the mapping from search wave to unique mechanisms and atlas deltas. Record the final queries/source families, new mechanism count, duplicate/reconfirmation count, unresolved contradictions, stale sources, and uncovered cells. Never fabricate a percentage when the denominator is arbitrary.

## Output Contract
Return a `saturation-decision` with `wave_id`, `scope`, `as_of`, `breadth`, `depth`, `contradictions`, `novelty`, `freshness`, `decision: OPEN|SATURATED`, `blocking_gaps[]`, `final_wave_summary`, and `reopen_conditions[]`.

## Failure Traps
- Equating source count with coverage.
- Declaring “permanent” or “forever” saturation.
- Ignoring domains where primary guidance is paywalled or incomplete; mark the evidence boundary.
- Letting visual trend research stand in for safety, accessibility, modality, or research-method coverage.
- Stopping before an adversarial final wave.
- Continuing forever despite zero mechanism novelty solely to maximize link volume.

Stopping is justified only when the bounded claim can be falsified by the recorded evidence.