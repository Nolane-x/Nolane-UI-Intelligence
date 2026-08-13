---
name: critiquing-performance-and-resilience
description: Use when UI behavior depends on latency, loading, streaming, realtime updates, offline mode, background work, network loss, service degradation, hardware dependencies, retries, or layout stability under dynamic state.
---

# Critiquing Performance and Resilience

## Overview
Independently verify that slow, partial, live, offline, and failed states remain understandable and safe. Performance defects become UX defects when feedback arrives too late, targets move, actions duplicate, or users cannot tell whether work committed.

## Parent Contract
**Required parent:** `challenging-ui-designs`.

**May modify:** false. Consume latency, degraded-mode, realtime, state, and transaction/agent contracts as applicable. Runtime evidence is mandatory for claims about actual responsiveness or failure behavior.

## Decision Model
Review **acknowledgement**, **stability**, **state truth**, **recovery**, and **persistence**. Acknowledgement: does input receive prompt visible/semantic response before users repeat it? Stability: do layout, focus, selection, and reading position remain controllable during load/update? State truth: can users distinguish queued, pending, complete, stale, failed, partial, unknown, and cancelled? Recovery: is retry safe, is state preserved, and can conflicts be resolved? Persistence: can long/background work survive navigation, restart, or reconnect where promised?

Stress temporal edges. Lose network immediately before/after commit. Double-click/tap during delay. Reorder live data while menu/focus is on an item. Background the app during AI/tool work. Reconnect after local edits conflict. Remove a kiosk peripheral. Test stale caches and expired permissions. A happy-path spinner is weak evidence.

Performance metrics support diagnosis but do not close state correctness. INP/field responsiveness can reveal sluggish interactions, while visual stability metrics reveal movement; neither tells whether a payment retry is safe or an offline merge preserves intent.

## Evidence
Use runtime traces, field/lab performance where applicable, network throttling, offline/service fault injection, duplicate-action tests, focus/layout observation, job persistence, realtime burst tests, and transaction/action logs. Record exact revision/environment.

## Output Contract
Return a `finding-set` with `may_modify:false`, `artifact_revision`, `findings[] {finding_id, severity, temporal_failure, evidence, state_ambiguity, user_impact, falsifier, recommended_repair, required_reverification}`, `duplicate_action_risks[]`, `unknown_outcomes[]`, `stability_defects[]`, and `release_recommendation`.

## Failure Traps
- Fast developer machine used as proof of responsiveness.
- Spinner considered sufficient for all latency.
- Retry offered after unknown external commit.
- Live UI passes screenshot review while rows move under pointer.
- Offline banner with no queue/conflict semantics.
- Performance score averaged with visual quality to hide critical state ambiguity.
- Reviewer infers backend idempotency from disabled UI control.

A resilient interface preserves truth and control when time and dependencies stop behaving ideally.

## V6 Performance and Resilience Critic
Compare actual interaction against an **interaction latency budget** for input feedback, navigation, search, drag, typing, and async acknowledgement. Exercise **long-task resilience** through backgrounding, reconnect, cancellation, device sleep, and app restart.

Induce **memory pressure failure** on large data/media/canvas surfaces and inspect whether state degrades predictably. Capture **rendering-jank evidence**—frame drops, long tasks, layout shift, animation contention—rather than subjective “feels fast.” Identify a **graceful degradation gap** where loss of GPU/network/API capability destroys core action instead of reducing fidelity.

### Falsification
Throttle CPU/network/GPU, increase data size, background/reopen, and stress memory. If product truth/state is lost, resilience fails regardless of average benchmark.

### Recovery
Reduce work, virtualize/cache safely, background durable tasks, simplify effects, and preserve the core semantic path under degraded capability.
