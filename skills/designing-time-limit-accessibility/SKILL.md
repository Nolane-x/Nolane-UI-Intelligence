---
name: designing-time-limit-accessibility
description: Use when sessions, reservations, security windows, quizzes, transactions, or expiring tasks impose time limits and users need warning, extension, preservation, or recovery without losing essential work.
---

# Designing Time Limit Accessibility

## Parent Contract
**Required parent:** `designing-accessible-interfaces`.

This faculty owns user-facing time-limit behavior where elapsed time can terminate a task, invalidate data, or remove access. It does not decide business/security policy itself. It translates an authoritative timing constraint into warnings, extension opportunities, preservation semantics, and accessible recovery so people who need more time are not surprised by expiration.

## Decision Boundary
First distinguish essential timing from arbitrary inactivity timeout. Document the authority for limits that cannot be adjusted. For adjustable limits, define warning cadence, remaining-time representation, extension amount, number of extensions, and the last safe action point. Warnings must be perceivable without requiring constant visual attention and should not steal focus from ongoing input.

Preserve work whenever policy allows. Session expiration need not imply losing a drafted form. If reauthentication is required, maintain enough context to resume the task safely after identity is restored. Countdown interfaces should expose meaningful intervals rather than announcing every second. Do not make the extension control itself expire before users can reach it using keyboard or assistive technology.

## Failure Topology
- A user completes a long form and discovers expiration only after Submit.
- A countdown changes visually but is never announced nonvisually.
- Every countdown tick floods a live region with speech.
- The “extend session” control appears briefly and disappears before slow navigation reaches it.
- Security reauthentication discards unsaved work even though the task data could be retained safely.
- Time is shown only as a moving progress ring with no interpretable remaining duration.

## Falsification and Recovery
Test with delayed interaction, screen readers, keyboard-only operation, interrupted network, background tabs, reauthentication, and a task paused until shortly before expiration. The design fails if expiration can cause silent data loss, if extension is technically present but not reachable in time, or if the warning channel itself disrupts task completion.

Recover by warning earlier, making remaining time explicit, persisting drafts, separating session identity from task state, and providing an accessible extension/recovery path. Where a hard limit is essential, explain the consequence before the task begins and surface a safe restart path.

## Output Contract
Return `time-limit-accessibility-contract` with limit authority, adjustable/essential classification, warning schedule, remaining-time semantics, extension path, draft preservation, reauthentication/resume behavior, announcement policy, and expiration verification cases.
