---
name: designing-indeterminate-progress
description: Use when an operation is genuinely underway but reliable completion percentage is unavailable and the interface must communicate liveness, phase, timeout, and escape without fake precision.
---

# Designing Indeterminate Progress

## Parent Contract
**Required parent:** `designing-latency-and-progressive-feedback`.

This faculty owns waiting states where the system knows work is occurring but cannot honestly quantify remaining work. It does not license arbitrary spinners; the interface must distinguish active work from unknown, stalled, queued, or disconnected states.

## Decision Boundary
First ask whether any truthful progress proxy exists: named phases, item counts without total, queue position, bytes transferred, heartbeat, or observable completion milestones. Use those before a purely animated indicator. If no quantitative evidence exists, an indeterminate indicator should communicate activity plus the operation’s identity and expected user posture: wait, continue elsewhere, cancel, or retry later.

Time changes meaning. A spinner that is appropriate at 500 ms may become a failure at 30 seconds. Define thresholds for adding explanatory copy, surfacing cancellation, offering backgrounding, or declaring timeout based on backend/service expectations. Never loop an animation indefinitely after the request has already failed or lost connectivity.

Reduced-motion modes need an equivalent liveness signal that does not depend on rotation. Screen readers should hear meaningful status transitions, not continuous animation updates. Avoid blocking the entire interface if only one region is waiting.

## Failure Topology
- A fake progress bar advances deterministically despite no measurable work.
- Spinner continues after network disconnect, implying liveness that no longer exists.
- Whole page is disabled for a small region-level request.
- Long-running wait has no operation name, cancel path, or escalation.
- Reduced-motion users receive a static symbol with no textual liveness cue.
- Screen reader live region announces “loading” repeatedly on every animation frame.

## Falsification and Recovery
Falsify with a fast completion, a 30-second completion, server timeout, network drop, queue wait before work begins, phase transition without percentage, cancellation, reduced motion, and screen-reader operation. The design fails if users cannot distinguish working from stuck or if the UI communicates numeric certainty that the system does not possess.

Recover by using truthful phase/liveness evidence, defining elapsed-time escalation thresholds, separating local from global blocking, stopping indicators on authoritative failure/disconnect, and providing equivalent non-motion status.

## Output Contract
Return `indeterminate-progress-contract` with liveness evidence, indicator choice, phase messaging, elapsed-time thresholds, timeout/stall distinction, blocking scope, cancel/background options, reduced-motion treatment, accessibility announcements, and falsification cases.