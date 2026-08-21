---
name: designing-accessibility-evidence-packets
description: Use when an accessibility claim must be supported by a mixed packet of automated checks, semantic inspection, keyboard interaction, assistive technology testing, visual review, and documented manual judgment rather than a single scanner result.
---

# Designing Accessibility Evidence Packets

## Accessibility proof is heterogeneous
No single artifact proves accessible behavior. Automated engines catch some classes, accessibility trees expose semantics, keyboard traces show operability, screen-reader sessions reveal announcement and navigation behavior, and manual review covers meaning, cognitive clarity, target sizing, focus visibility, or context-sensitive requirements. This skill owns how those evidence types are assembled into one claim-bounded packet.

## Parent Contract
**Required parent:** `binding-ui-evidence`.

The parent establishes evidence lineage and claim discipline. This specialist begins when the claim is an accessibility obligation whose verification requires more than one evidence modality.

## Packet schema
A packet should name the obligation or criterion, applicable surface/state, normative source and version, test environment, automated findings, manual checks, assistive-technology observations where needed, unresolved questions, exceptions, and reviewer identity/role. The decision owner is which evidence combination is sufficient for the specific claim.

Do not claim complete conformance from scanner output. Automated results can establish certain detectable violations and provide regression value; they cannot certify every criterion. Conversely, manual opinion without reproducible setup is weak. Each evidence item should state what it proves and what remains outside its scope.

## State and environment coverage
Accessibility changes with state: validation errors, modal transitions, expanded menus, drag/drop alternatives, dynamic updates, timeout warnings, disabled controls, and generated content can each alter semantics or operability. Bind packet evidence to the state matrix. Where assistive technology behavior is platform-dependent, bind to browser/device environment evidence rather than generalizing one combination to all.

## Manual judgment contract
Manual checks need an explicit protocol: keyboard order and traps, visible focus, label purpose, error identification, reflow/zoom, color-independent meaning, target access, announcement behavior, or other applicable obligations. Record pass, fail, not applicable, or blocked with rationale. “Looks accessible” is not a valid status.

## Evidence freshness
Packets age when the relevant component, semantics, interaction flow, content, browser/AT stack, or design-system primitive changes. Track those dependencies. A visual-only token change may not invalidate every screen-reader result, while a DOM restructuring may invalidate nearly all semantic evidence. Freshness should be dependency-aware rather than date-only.

## Failure modes
Characteristic Failure includes scanner-only certification, one keyboard smoke test standing in for state coverage, undocumented assistive-technology setup, manual checks with no criterion mapping, suppressed “incomplete” automated results, and evidence copied forward after a semantic rewrite. Another failure is inaccessible evidence itself—for example screenshots or videos with no textual finding summary for reviewers who cannot consume them.

## Falsification
Inject a keyboard trap that scanners miss, remove an accessible name, change live-region timing, alter zoom/reflow behavior, and update the component DOM without refreshing the packet. The contract fails if the packet still claims the affected obligation is proven, if evidence cannot identify which state/environment was tested, or if unresolved manual checks are treated as passes.

## Recovery
Recompute packet applicability from current obligations, preserve historical artifacts with revision labels, rerun only evidence invalidated by changed dependencies, and mark unknowns explicitly. If a manual or assistive-technology check contradicts automated output, preserve the contradiction and investigate behavior rather than privileging the easier artifact.

## Output and Handoff
Output: `accessibility-evidence-packets-contract`, containing obligation mapping, evidence modalities, state/environment bindings, manual protocol, freshness dependencies, unresolved status, and reviewer trace. Handoff environment selection to browser/device evidence matrices and human-only judgments to manual-review evidence contracts.

## Sibling Boundary and delete-the-skill
Sibling component-state matrices decide which states need evidence; this skill decides how accessibility obligations are proven within them. Manual-review evidence contracts govern review procedure across UI qualities, not the accessibility-specific evidence composition. The delete-the-skill test passes because without it, teams commonly mistake automated detection for conformance or collect manual notes with no durable claim lineage.