---
name: using-nolane-ui
description: Use when a task materially designs, redesigns, audits, reproduces, implements, or verifies a user interface or user experience.
---

# Using Nolane UI

## Overview
This is the mandatory bootstrap for material UI/UX work. Its only job is to prevent the agent from collapsing product reasoning, visual design, implementation, and verification into one unstructured act.

**Core rule:** invoke `nolane-ui` before material design or implementation. A child skill may strengthen this protocol; it may not waive it.

## Materiality test
Treat the task as material when any of these are true: a new screen or flow is being created; navigation or information hierarchy changes; the visual language changes; a reusable component/system is introduced; a high-fidelity target must be reproduced; accessibility/interaction behavior is consequential; or the result will be shipped rather than used as disposable exploration.

A tiny, local change may take a reduced path only when `nolane-ui` records the scope and why omitted faculties cannot affect the result.

## Absolute constraints
- Build success is not design success.
- Visual attractiveness is not UX correctness.
- Automated accessibility output is evidence, not complete accessibility proof.
- A generator may not certify its own material completion.
- Missing evidence is `UNKNOWN` or `BLOCKED`, never `PASS`.
- User/product requirements outrank aesthetic heuristics.
- Do not load every NUI skill. Route first.

## Start
Hand the task to `nolane-ui` with the user request, known product context, available references, repository constraints, and runtime capabilities.

## Output: `bootstrap-directive`
Return the bootstrap directive that binds the task to `nolane-ui`, preserving the original request, known context, available references, runtime capabilities, materiality decision, and any justified reduced-scope boundary.

## Red flags
If you are thinking “the user said just code,” “I can infer the design while implementing,” “it compiles so the UI is done,” or “checking this would take too long,” you are at the exact trigger for this bootstrap. Do not bypass it.

## V6 Bootstrap Integrity Protocol
NUI itself can fail before design begins if the bootstrap silently drops facts while converting a request into a route. Build a **task-profile checksum** that restates, in compact structured form, the product surface, user/job, visual ambition, risk, modalities, platform, evidence capabilities, named sources, hard constraints, and unresolved facts. Compare that checksum with the raw request before loading specialist faculties; a mismatch is a routing defect, not an acceptable summary.

Maintain a **route-justification ledger**. Every activated owner records the observed trigger it answers; every plausible high-impact owner that remains inactive records why. This makes progressive disclosure auditable rather than a convenient excuse to omit expensive reasoning. Keep a **capability-evidence boundary** as well: the agent may only promise screenshot inspection, browser execution, repository archaeology, accessibility-tree inspection, performance tracing, or external research when those capabilities actually exist in the current runtime. Missing capability changes the evidence state to UNKNOWN; it never authorizes invented evidence.

For material tasks emit an **omission declaration** listing excluded domains or verification classes that could alter the answer. The declaration is especially important when context limits force a narrower route. If an omission is later discovered to affect product truth, safety, accessibility, or the selected aesthetic thesis, enter the **bootstrap recovery path**: invalidate downstream completion, repair the task profile, reroute from the earliest affected lifecycle state, and preserve already-valid evidence instead of restarting blindly.

### Falsification
Try to falsify the bootstrap by deleting one user constraint, changing one risk/modality field, and adding a named external source after routing. If the route and obligations do not materially react where they should, the bootstrap is under-sensitive. Conversely, inject an irrelevant domain and verify that the router can reject it with a reason rather than loading the entire graph.

### Recovery
When the task-profile checksum or route-justification ledger fails, stop implementation work. Reconstruct the profile from source language, mark uncertain inferences explicitly, rerun routing, and regenerate only artifacts whose parent obligations changed. A bootstrap defect cannot be waived by later visual quality.

## V10 Generation/Evaluation Isolation
Normal product generation and an **empirical-evaluation** experiment are different execution modes. In ordinary UI work, use NUI to design the product and produce task-specific evidence; do not load benchmark files simply because they exist. In empirical mode, the treatment manifest controls what NUI context is available and the generation side may receive **only** the public benchmark task plus treatment context.

The **hidden evaluator rubric** is evaluator-only material. Never add `benchmarks/v10/tasks-hidden.json`, its checklists, failure traps, hard blockers, contamination markers, or judge answers to a generator prompt, retrieval index, route packet, chain of source context, or NUI-full treatment. If the generator can retrieve the answer key while baseline cannot, the experiment measures leakage rather than design intelligence.

Before a benchmark run, create separate hashes for:
- public task material;
- routed treatment context;
- tool budget;
- exact NUI revision.

The bootstrap must be reproducible from those inputs. Any unrecorded extra hint, manual coaching, hidden-reference injection, or condition-specific tool access invalidates a matched empirical comparison.

### V10 evidence-class declaration
At bootstrap, label the intended evidence class:
- `ARTIFACT_WORK` — design/implementation quality for the current product;
- `STRUCTURAL_EVAL` — testing the V10 harness or synthetic fixtures;
- `EMPIRICAL_EVAL` — matched real-model treatment comparison.

Do not let those classes inherit each other's claims. `ARTIFACT_WORK` may produce a beautiful verified UI without saying NUI caused it. `STRUCTURAL_EVAL` may prove benchmark machinery is sound enough to run without claiming empirical improvement. `EMPIRICAL_EVAL` is the only class that can proceed toward a bounded efficacy claim, and even then only after downstream blind judgment, ablation and statistical gates.

### V10 contamination recovery
If hidden evaluator material enters generation context, mark the affected run `protocol-violation`; do not rewrite the output and keep it as valid evidence. Rebuild the treatment context from public sources, rerun the affected cells, and retain the contaminated run in the audit trail. A benchmark that needs answer-key hints to make NUI look strong is evidence against the experiment, not evidence for NUI.

## V12 External UI Reference Persistence Gate

External UI implementation intelligence is a first-class bootstrap obligation. When the task intersects motion, microinteraction, icon state, accessible primitives, drag/drop, design systems, agent UI, editors, canvas/diagram, data visualization, spatial/3D, native UI, design tokens, styling or verification, resolve one or more task-specific packs from `knowledge/external-ui-reference-packs-v12.json` through `src/nolane_ui/external_ui_intelligence.py`. Do not wait until implementation to remember external references.

Use `knowledge/external-ui-intelligence-network-v12.json` as the manifest for the sharded source network. It extends rather than replaces `knowledge/ui-ecosystem-registry.json` and `knowledge/ui-source-intelligence-v6.json`; material influence still requires the existing role-specific archaeology, pinned snapshot where required, mechanism evidence, adaptation boundary and local runtime proof.

### Permissive-first selection

For candidates that are materially capable, prefer verified permissive code (`MIT`, `Apache-2.0`, `BSD-2-Clause`, `BSD-3-Clause`, `ISC`, `0BSD`, `CC0-1.0`) over copyleft, source-available, Commons-Clause-like, commercial, mixed, custom or unclear alternatives. A restrictive source may outrank GREEN only when it satisfies a materially unique requirement that available GREEN candidates do not. Popularity, stars, demo polish, familiarity, aesthetics or convenience never justify the override.

Before material reuse, re-check the exact canonical upstream terms and the exact artifact scope. Repository, package, component, example/template, asset, icon, font and trademark terms may differ. Never inherit a license claim from an awesome list, marketplace, registry or aggregator.

If the best necessary source is `consent`, `restricted` or `mixed`, explain the relevant restriction and the strongest GREEN fallback, then obtain explicit user consent before direct adoption. If the user declines, automatically select the strongest sufficiently capable GREEN fallback; if none exists, independently synthesize the mechanism and record the unmet requirement. `unverified` sources may guide research but cannot authorize direct adoption until reverified. `discovery-only` and `reference-only` sources never authorize direct code or asset reuse.

### Persistence contract

An active reference packet MUST survive these stages without silently disappearing:

1. `intent` — state why the pack is relevant;
2. `design` — name the mechanisms being considered, not merely repository names;
3. `implementation-selection` — resolve exact candidate/source/component and local adaptation boundary;
4. `license-gate` — verify exact current scope and prefer GREEN fallbacks;
5. `critique` — compare the implementation against the intended mechanisms without cloning trade dress;
6. `runtime-verification` — observe actual interaction, responsive, accessibility, reduced-motion and performance behavior as task-relevant;
7. `provenance` — record what influenced the result, what was directly adopted, what was independently synthesized, and what remains unverified.

Starting implementation does not discharge this obligation. Context pressure may reduce the packet to 3–12 most relevant sources, but it may not erase active source IDs, license state, learned mechanisms, fallbacks or unresolved verification obligations.

### Discovery radar

Awesome lists are discovery-only radars. They may nominate a repository; they cannot authorize influence or adoption. Resolve canonical upstream identity, current health, exact license scope, implementation evidence and source role before promotion into a material reference packet.

### V12 recovery

If a restrictive source was selected while a sufficiently capable GREEN alternative existed, if a license was inherited from an aggregator, or if active references vanished between design and verification, mark the source decision invalid. Re-run pack resolution from the earliest affected stage, preserve already-valid local work, and replace or independently re-synthesize the affected implementation before claiming completion.
