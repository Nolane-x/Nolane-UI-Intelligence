---
name: designing-triage-surfaces
description: Use when users rapidly assess uncertain incoming items to classify, prioritize, route, escalate or dismiss them and the interface must optimize evidence comparison without collapsing preliminary judgment into final resolution.
---

# Designing Triage Surfaces

## Parent Contract
**Required parent:** `designing-task-flows`.

This faculty owns the rapid assessment phase before deeper handling. It does not own the downstream case workflow, queue ordering policy or domain-specific diagnostic judgment.

## Decision Boundary
Triage is a **decision under incomplete evidence**. Model the set of permitted dispositions—route, prioritize, assign, request information, merge duplicate, escalate, defer, dismiss, open case—along with required evidence and uncertainty. Avoid a single “Resolve” button that hides these distinct outcomes.

Layout should support fast comparison of the facts that change disposition. Surface source, recency, severity indicators, prior history, duplicates, key structured attributes and missing evidence. Secondary metadata can remain progressive. Do not let visually loud but low-authority signals dominate simply because they are easy to render.

Preliminary labels must remain preliminary. If an AI score, rule engine or junior operator assigns “high risk,” distinguish recommendation/confidence from confirmed classification. Preserve rationale/provenance where later reviewers need to audit why the item was routed.

Keyboard efficiency matters in high-volume triage, but shortcuts must not make irreversible actions too easy. Provide undo or confirmation proportionate to consequence. Batch triage is allowed only when evidence and disposition truly generalize across the selected set.

## Failure Topology
- Triage view shows a large severity color but hides the evidence used to compute it.
- “Dismiss” permanently closes a case with one shortcut even though triage is preliminary.
- AI recommendation visually looks like a confirmed diagnosis/fraud decision.
- Sorting by predicted risk makes low-confidence but severe items disappear from attention.
- Missing data is rendered as benign/zero.
- Operators batch-route heterogeneous items because the interface makes selection easier than inspection.

## Falsification and Recovery
Falsify with missing evidence, contradictory signals, low-confidence automated scores, duplicate items, changed priority, keyboard shortcuts, batch selection and later audit review. Ask whether the original evidence and disposition rationale can be reconstructed.

Recover by separating recommendation from decision, making missing/uncertain evidence explicit, limiting batch actions to compatible items and routing irreversible consequences to stronger confirmation/review stages.

## Output Contract
Return `triage-surface-contract` with disposition set, evidence hierarchy, uncertainty/provenance treatment, priority/routing actions, shortcut safety, batch eligibility, handoff to downstream workflow and auditability tests.