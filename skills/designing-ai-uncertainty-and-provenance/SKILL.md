---
name: designing-ai-uncertainty-and-provenance
description: Use when AI output may be wrong, incomplete, stale, synthesized from sources, mixed with human content, or used for decisions where origin, evidence, generated status, or calibrated uncertainty matters.
---

# Designing AI Uncertainty and Provenance

## Overview
Communicate what the system knows, where information came from, and what remains uncertain without inventing precision or burying users in model diagnostics.

## Parent Contract
**Required parent:** `routing-ui-work`.

Require output type, source availability, freshness, task consequence, whether uncertainty is calibrated, and how users can verify or correct the result. If no meaningful confidence estimate exists, never manufacture a percentage.

## Decision Model
Separate four concepts. **Identity:** human-authored, model-generated, model-edited, retrieved, calculated, or externally sourced. **Provenance:** source records and transformations that support the claim. **Freshness:** when source/model context was last valid. **Uncertainty:** what could be wrong and whether a calibrated estimate exists.

Choose presentation by decision value. Cite a source when it helps the user inspect evidence, not to decorate low-risk generated copy. For summaries, map claims to sources where feasible and distinguish unsupported synthesis. For calculations or tool outputs, identify the tool/data source separately from model narration.

Avoid false precision. “98% correct” is misleading without a validated calibration basis for that task population. Use qualitative uncertainty only when its categories have operational meaning. Sometimes the best communication is a limitation: “I could not verify the latest status” plus a path to verify.

Preserve provenance through editing. If a user changes generated text, the UI should not continue implying the entire result is model-authored or fully source-backed. In multi-agent work, attribution includes which agent/tool produced each material state.

## Evidence
Evidence includes source URLs/records, retrieval timestamps, tool logs, calibration studies where numeric confidence is shown, stale-data tests, citation correctness samples, user comprehension of provenance, and adversarial cases where fluent output lacks support.

## Output Contract
Return a `provenance-contract` with `content_origins[]`, `claim_source_map[]`, `freshness_rules[]`, `uncertainty_model`, `numeric_confidence_basis`, `generated_identity_rules`, `editing_attribution_rules`, `verification_actions[]`, `unsupported_claim_policy`, and `provenance_tests[]`.

## Failure Traps
- Confidence percentage copied from model token probability or intuition.
- Citation list that does not support individual claims.
- AI label disappearing after output becomes consequential.
- “Sources” that are actually model-generated references.
- Stale retrieved information presented with current tense.
- One global disclaimer users must remember for every output.
- Human-edited content still labeled as entirely AI-generated.

Provenance should help a person decide what to trust, inspect, or verify next.