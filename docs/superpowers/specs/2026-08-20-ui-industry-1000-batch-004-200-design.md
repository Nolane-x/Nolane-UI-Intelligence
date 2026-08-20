# UI Industry 1000 — Batch 004 (200 Skills) Design

## Goal

Extend the canonical NUI graph from 474 to exactly 674 skills by adding 200 independently authored specialist faculties without weakening routing, duplicating existing ownership, or using template/loop-generated prose.

## Non-negotiable authorship rules

1. Exactly 200 new canonical `skills/<slug>/SKILL.md` files.
2. Skill prose is individually authored. No loop, macro, prompt template, mass rename, or generated body scaffold may be used to create the substantive prose.
3. Shared headings are allowed only as corpus schema. Decision logic, failure topology, procedure, falsification criteria, and output contract must be materially different for each skill.
4. A skill is admitted only when removing it would leave a distinct consequential decision or failure class unowned by its parent or siblings.
5. Every skill receives one unique output contract and one explicit parent in the canonical graph.
6. Graph/documentation updates are bookkeeping and may be deterministic; prose generation may not.
7. Exact normalized duplicates and trivial-renaming near-duplicates are release blockers.
8. No completion claim is allowed without exact-head verification evidence.

## Stacking model

Batch 004 is developed on `build/ui-industry-1000-batch-004-200`, stacked from Batch 003 head `4642dea16d7155676ab47efb958645866958cdb4`. Its review base is the Batch 003 branch so the Batch 004 diff remains isolated from the still-open Batch 003 PR. The canonical target for this batch is therefore 474 + 200 = 674 skills.

## Admission test

For every candidate, ask: **If this specialist disappeared and only its parent/siblings remained, is there a material UI decision or failure mode that would no longer have a clear owner?** If no, reject the candidate.

## Court architecture

Batch 004 contains ten courts of exactly twenty skills each. Each court has one domain root and nineteen narrower owners.

### Court A — Diagramming and node-graph authoring

Own graph construction and graph-specific inspection mechanics that generic canvas/editor skills do not own: node creation, connectors, edge routing, layout, subgraphs, formal diagram semantics, large-graph navigation, validation, history, collaboration, presentation, and executable-graph debug overlays.

### Court B — Project and work management

Own planning/coordination semantics beyond generic task flows: boards, backlogs, sprints, roadmaps, milestones, dependency networks, workload, status protocols, recurring work, templates, bulk edits, views, project health, tracking, estimation, risks, portfolios, and closure.

### Court C — Incident response and reliability operations

Own time-critical operational coordination: alert triage, severity, incident chronology, responder roles, runbooks, service health, impact, escalation, communications, status publication, on-call handoff, command, mitigation, hypothesis/evidence, postmortems, maintenance, and guarded reliability experiments.

### Court D — Software delivery and release engineering

Own CI/CD and deployment decisions: pipeline stages, build artifacts, job logs, gates, deployment targets, rollout strategies, rollback, artifact promotion, release notes, environment diff, drift, locks, release trains, freezes, preview environments, supply-chain provenance, and deployment diagnosis.

### Court E — Scientific and engineering instrumentation

Own instrument and experiment interaction semantics: telemetry, experiment configuration/control, calibration, live signals, waveform/spectrum analysis, microscopy measurement, samples, plates, batch traceability, process trends, alarm thresholds, setpoints, provenance, comparison, sweeps, fitting, and safety interlocks.

### Court F — 3D/CAD authoring

Own spatial authoring mechanics beyond generic 2D canvas manipulation: scene trees, 3D viewport navigation, cameras, spatial snapping, layers/collections, mesh modes, modeling operations, dimensions, constraints, assemblies, materials, lighting, UV/texture mapping, annotation, sections, clash inspection, render preview, and manufacturing/export handoff.

### Court G — Nonlinear media editing

Own authoring rather than playback: ingest/bins, edit timelines, tracks/layers, trimming, split/razor, ripple-roll-slip-slide semantics, timeline snapping, transitions, keyframes, multicamera, mixing, audio automation, grading, scopes, subtitle authoring, relinking, proxies, markers/review notes, and render queues.

### Court H — Digital learning and assessment

Own pedagogical state and assessment semantics: course discovery, curriculum paths, lessons, progress, practice, quiz authoring/taking, timed assessment, question navigation, review/explanation, rubric grading, gradebooks, submissions, integrity review, spaced repetition, flashcards, completion credentials, cohort analytics, and accommodation controls.

### Court I — Financial operations

Own operational finance and market-workspace semantics beyond generic payment/transaction UX: ledgers, journals, reconciliation, payables/receivables, expenses, budgets, cash flow, statements, variance, chart of accounts, tax mapping, currency exposure, portfolio positions, trading order entry, watchlists, order books, trade blotters, and risk limits.

### Court J — Security operations

Own defensive SOC workflows beneath the existing security-center authority: alert triage, investigation chronology/entities, IOC search, event correlation, detection rules/testing, attack paths, vulnerability prioritization, patch exposure, endpoint isolation, network session investigation, auth/privilege anomalies, phishing, malware-result interpretation, case evidence, threat hunting, and handoff.

## Skill body contract

Every `SKILL.md` must include:

- YAML frontmatter with `name` exactly equal to its directory slug and a specific description.
- `## Decision ownership` — what this owner decides and what it explicitly does not own.
- `## Inputs and evidence` — minimum evidence needed before making the decision.
- `## Procedure` — a domain-specific decision procedure, not generic design advice.
- `## Failure topology` — named failure modes and why they matter.
- `## Falsification` — observations that disprove the current design or force escalation.
- `## Output contract` — structured fields that downstream owners can consume.
- `## Handoffs` — neighboring owners and the boundary between them.

Minimum body depth is enforced mechanically, but length is not a substitute for distinct ownership.

## Verification

`tests/test_ui_industry_batch_004.py` is committed before any new skill body and must initially fail. It locks the exact 200-slug inventory and metadata and verifies:

- exactly 200 unique slugs and ten 20-skill courts;
- file/frontmatter existence and depth signals;
- exact family/parent/output registration;
- unique outputs with no collision against the pre-Batch-004 graph;
- parent-chain reachability to `using-nolane-ui` with no cycles;
- exact final graph count 674;
- no normalized exact body duplicates;
- no pair above the trivial-rename similarity threshold;
- no placeholder corpus text.

The final exact head must also pass the repository-wide unit/contract suite, completion-packet generation, canonical validator, clean-delivery contract, and changed-file forensic check.

## Cleanup

Any temporary graph integration/finalization tooling used during construction must be removed before the final merge candidate. Canonical `Verify NUI` must end read-only. Batch 004 must not introduce a self-mutating verifier or leave temporary finalizers in the released tree.