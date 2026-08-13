---
name: verifying-runtime-ui-behavior
description: Use when a material interface exists in an executable form and static source/spec evidence is insufficient to prove that actions, focus, navigation, async states, permissions, recovery, and alternate inputs actually work.
---

# Verifying Runtime UI Behavior

## Parent Contract
**Required parent:** `binding-ui-evidence`.

Receive the current artifact revision, canonical action registry, scenarios, reachability proof, implementation specification, and the exact completion claims that require runtime observation. This faculty binds observations to behavior; it does not redesign failed interactions while verifying them.

## Decision Boundary
This skill owns **runtime behavioral evidence**. It distinguishes “the code appears to contain a handler” from “a user can trigger the intended action and observe the specified result under the tested conditions.” It is not a unit-test strategy, a generic QA suite, or a visual screenshot comparison. It observes UI behavior at the action/state boundary.

A probe is anchored to a canonical action or scenario checkpoint. It records starting state, actor/profile, input modality, exact steps, observations, artifact revision, environment, result, and evidence. The same action may require several probes when platform, permission, viewport, connectivity, or modality changes materially alter behavior.

## Product Truth
Static correctness and behavioral correctness diverge easily. A button has an `onClick` but is covered by another layer. A menu item renders but disappears at mobile width. A modal closes yet focus returns to the document body rather than the triggering control. A “Save” handler fires twice under rapid activation. A drag interaction works with pointer but has no keyboard alternative. A network failure leaves optimistic data visible with no recovery. A permission error arrives after the UI already navigated away. A route exists but authentication redirects destroy the original destination.

Runtime verification exists to catch this gap without pretending that every behavior can be inferred from code.

## Decision Model
1. **Select required probes from claims.** Start with release-critical actions and scenarios. Add destructive, transactional, asynchronous, permission-sensitive, navigation, focus, gesture, responsive, offline, and recovery behavior that static evidence cannot close.
2. **Pin artifact and environment.** Record commit/build/revision, browser/native platform, viewport, input modality, feature flags, role, seed data, connectivity conditions, locale, and relevant assistive technology. Evidence without context is not reusable.
3. **Define start state and oracle.** Before execution, state what must be true initially and what user-observable result constitutes PASS. Avoid post-hoc success definitions.
4. **Execute the semantic action.** Use the intended binding rather than calling internal functions directly. When alternate modalities are required, trigger them separately: keyboard shortcut, touch, screen-reader activation, remote, gesture alternative, or native back.
5. **Observe intermediate states.** For async work, record pending/progress, duplicate activation behavior, cancellation, interruption, optimistic state, server confirmation, timeout, retry, and late failure where applicable.
6. **Observe focus and navigation.** Record destination, history/back behavior, scroll restoration if material, dialog focus entry/containment/return, and announcements. A visible transition can still be behaviorally wrong.
7. **Exercise negative authority.** Verify controls are appropriately absent/disabled/explained for unauthorized roles, and that permission changes do not leak stale operations.
8. **Exercise failure/recovery.** Inject or reproduce validation error, network loss, server rejection, conflict, canceled permission, or destructive undo where required. Confirm user work and system truth converge.
9. **Preserve failures.** A repair creates a new probe bound to the new revision. Do not replace the failed record; this maintains regression history and prevents evidence laundering.
10. **Scope PASS precisely.** Passing Chrome desktop pointer behavior does not prove Safari, touch, screen reader, or mobile. Declare only what was observed.

Automation is welcome when it activates the real UI and preserves semantic evidence. Browser tests, native UI tests, accessibility-tree queries, video/trace capture, screenshots at checkpoints, and deterministic state fixtures can strengthen the ledger. Manual probes remain valid when automation cannot observe the relevant quality, but must still be reproducible.

## Evidence
Strong evidence includes test traces tied to the exact revision, DOM/accessibility snapshots around state changes, screenshots/video with timestamps, native UI automation records, browser console/network observations when they explain failure, and human observation for qualities not exposed mechanically. Unit tests can support implementation logic but cannot alone prove operability of a user binding.

Every evidence reference names what it proves. “Playwright passed” is weaker than “probe `member.invite.keyboard` activated action `member.invite` via keyboard, focus entered confirmation dialog, success announcement occurred, and member row appeared after server confirmation.”

## Output Contract
Return `behavior-verification-ledger` with:
- `artifact_revision`
- `environment_profiles[]`
- `probes[] {id, action_id, scenario_id, start_state, profile, modality, steps, expected_observables, observed, evidence_refs, result: PASS|FAIL|UNKNOWN}`
- `required_action_coverage {action_id: probe_ids[]}`
- `focus_navigation_observations[]`
- `async_recovery_observations[]`
- `unverified_claims[]`
- `regressions[]`
- `status: PASS|FAIL|UNKNOWN`

Required actions cannot be marked verified unless at least one applicable runtime probe passes, and required multi-modality behavior needs the promised modality coverage.

## Failure Traps
- Calling internal handlers or APIs and claiming the UI action works.
- Recording only final screenshots for async interactions and missing double-submit, interruption, or failure behavior.
- Reusing evidence after a materially overlapping UI change.
- Treating one viewport/input method as proof of all profiles.
- Ignoring focus because the visible pixels look correct.
- Marking a test `PASS` when the expected result was changed after observing the implementation.
- Deleting failed evidence after a fix.
- Assuming an external component’s demo proves its integration inside this product.
- Letting browser automation bypass login/permission behavior that is part of the scenario.

**Hard gate:** source code, static specs, and component-library claims cannot substitute for runtime evidence when the completion claim is about behavior actually working.

## V6 Runtime Verification Protocol
Capture an **event-sequence capture** for critical interactions: input, state transitions, requests, optimistic updates, responses, focus, announcements, and final state. Preserve **browser-console evidence** for errors/warnings/network failures/hydration issues tied to the exact run.

Create a **focus-runtime trace** across keyboard navigation, overlays, async replacement, route changes, deletion, error, and restoration. Execute **async failure injection** for timeout, out-of-order response, duplicate event, partial dependency failure, reconnect, and cancellation. Perform **runtime-state reconciliation** against the canonical state/action contract rather than accepting “the page rendered.”

### Falsification
Inject one impossible/out-of-order runtime state and verify the checker blocks completion. A green render with wrong action/focus/state falsifies runtime verification.

### Recovery
Repair the responsible state/event/data boundary, rerun the exact captured sequence, and refresh evidence against the same revision/configuration.
