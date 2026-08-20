---
name: designing-timed-assessment-interfaces
description: Use when this specialist's decision ownership is materially in scope. Own assessment timing semantics including authoritative clock, start conditions, accommodations, pause policy, warnings, connectivity, server deadlines, auto-submit, and evidence around time expiration.
---
# Designing Timed Assessment Interfaces

## Parent Contract

**Required parent:** `designing-digital-learning-experiences`.

Inherit the broader routing and decision boundary from this canonical parent; this specialist remains accountable only for the narrower ownership, failure topology, falsification criteria, and output contract defined below.

## Decision ownership

Own time as a high-consequence part of an assessment attempt. Decide clock authority, effective duration, start, pause/resume if permitted, accommodation extensions, warning thresholds, deadline versus duration, network/disconnect treatment, auto-submit, and post-expiry state. This owner does not define question scoring.

## Inputs and evidence

Require assessment timing policy, server/client clock model, duration/deadline, time-zone display, accommodations, pause rules, late-start policy, disconnect rules, autosave/submission, grace period, and proctor/instructor override. Identify clock drift and suspended-device behavior.

## Procedure

Use an authoritative timing model and show remaining time plus enough deadline context to avoid ambiguity. Applied accommodations affect the learner's effective duration without exposing private reasons. Warnings should be perceptible without becoming constant anxiety or stealing focus. If pausing is allowed, show whether the clock actually stops and who authorized it. Network loss must not silently stop or extend time unless policy says so; display local estimate with authoritative-sync uncertainty. At expiry, freeze answer editing according to policy, complete pending saves, and clearly distinguish auto-submitting from submission failure.

## Failure topology

Failures include browser clock drift, timer resetting on refresh, accessibility extension not applied, hidden pause continuing to count down, network loss making learners think time stopped, modal warnings interrupting answer entry, and auto-submit racing unsaved responses. Another failure is deadline displayed in a confusing timezone.

## Falsification

Reject if timer authority is unclear; if refresh/resume changes effective remaining time unexpectedly; if accommodation duration cannot be verified by the authorized learner/staff; if disconnect behavior is unstated; if time warning traps focus; if expiry can lose saved responses due an avoidable race; or if deadline/timezone is ambiguous.

## Output contract

Return a `timed-assessment-interfaces-contract` with: clock authority; duration/deadline/timezone; start; pause policy; accommodation application; warning thresholds/modal behavior; reconnect synchronization; expiry state; autosave/auto-submit ordering; grace/override; and audit timestamps. Include one disconnect-near-expiry scenario.

## Handoffs

Quiz taking owns responses, question navigation owns movement, accommodations supplies authorized timing adjustments, and assessment integrity may consume timing anomalies without redefining the clock.