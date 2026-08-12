---
name: critiquing-functional-completeness
description: Use when a feature-rich UI claims completeness and needs an independent critic to challenge missing capabilities, unreachable destinations, ghost actions, state gaps, or cross-feature breakage.
---

# Critiquing Functional Completeness

## Parent Contract
**Required parent:** `challenging-ui-designs`.

Receive the product contract, capability ledger, action registry, reachability proof, scenario coverage, implementation specification, current render or prototype, and available runtime evidence. The generator that produced the design must not silently self-certify this court.

## Decision Boundary
This critic owns **falsification of completeness**, not aesthetic taste, usability preference, code quality, or generic accessibility review. Its job is to find one missing edge, control, state, role path, recovery path, or product obligation that invalidates a broad “the UI is complete” claim.

The critic assumes that locally beautiful screens can still form a globally broken product. It therefore reasons across artifacts and deliberately searches for contradictions: capability exists but no action; action exists but no binding; binding exists but hidden for required profile; surface exists but unreachable; path exists but dead-ends on permission denial; spec includes control but runtime does nothing; mobile drops a desktop capability; two labels collide; external component behavior bypasses canonical semantics.

## Product Truth
Completion failures are often tiny. A missing “Back to projects” path after deleting a project can strand a user. A settings subpage can exist in the router yet have no navigation entry. A context menu may expose rename on desktop but disappear on touch. A modal may close with pointer but trap keyboard focus. An async button can be clicked twice because the loading state was never specified. An admin-only control can leak to a viewer even though the backend rejects it.

Each defect may occupy one line of code. The critic treats these as first-class because product trust is accumulated from details.

## Decision Model
1. **Cross-account capabilities.** For every required capability, locate its action, surface, scenario, specification, and evidence references. Missing links are findings even when another artifact says `PASS`.
2. **Cross-account actions.** For every required action, find at least one valid binding for each required actor/modality/context. Flag ghost actions and bindings that invoke unknown actions.
3. **Attack reachability.** Start from legitimate entry points with least-privileged required roles. Attempt to find orphan destinations, secret-URL-only paths, overflow omissions, mobile losses, and permission-dependent dead ends.
4. **Attack state transitions.** Inspect empty, loading, partial, offline, error, validation, conflict, permission, destructive, async, and success states. Ask what the next valid action is and whether recovery preserves user work.
5. **Attack cross-feature handoffs.** Follow scenarios across search/detail/edit, notification/object, import/correction, creation/share, transaction/history, and other boundaries. Look for state/identity/context that one feature assumes but another does not preserve.
6. **Attack semantics.** Detect duplicate labels with different effects, inconsistent labels for same action when ambiguity matters, hidden destructive consequences, and component events that bypass the action registry.
7. **Attack responsive and modality parity.** Functional parity means required outcomes remain possible, not identical layouts. Verify keyboard, touch, remote, assistive technology, gesture alternatives, and constrained viewports where promised.
8. **Attack implementation specificity.** Compare design claims with `ui-specification`; flag controls, states, copy, focus, responsive transformations, or feedback that engineering would have to invent.
9. **Attack evidence.** Static existence cannot prove runtime behavior. A green unit test unrelated to the UI action cannot close an interaction obligation. Mark unsupported claims `UNKNOWN`.
10. **Calibrate severity.** `critical` for safety/security/irreversible catastrophic gaps; `major` for blocked core outcomes, authority errors, or product-wide closure failure; `minor` for bounded non-core gaps; `note` for improvement not needed to support the claim.

## Evidence
Every finding names the conflicting artifacts and the smallest reproducer or proof. Examples: capability ID with no action reference; surface node unreachable in the graph; screenshot/spec showing no required control; runtime probe with action failure; mobile viewport evidence where an overflow menu disappears. Do not produce vague findings such as “navigation could be clearer.”

The critic may request targeted evidence rather than speculate. Unknown is a valid result. When a finding is fixed, preserve the old finding and bind new evidence to a resolution; do not rewrite history.

## Output Contract
Return `functional-completeness-findings` with:
- `findings[] {id, severity, failure_class, claim, evidence_refs, affected_capabilities, affected_actions, affected_surfaces, reproduction, expected, observed_or_missing, required_resolution}`
- `artifact_crosswalk_gaps[]`
- `role_modality_gaps[]`
- `responsive_losses[]`
- `runtime_unknowns[]`
- `closure_verdict: PASS|FAIL|UNKNOWN`
- `bounds[]`

`PASS` means no unresolved material contradiction was found within the bounded scope; it does not mean zero defects or universal quality.

## Failure Traps
- Reviewing screenshots independently instead of cross-referencing product artifacts.
- Writing aesthetic comments in the functional court.
- Accepting “there is a route” as proof of discoverable reachability.
- Assuming a headless/accessibility component library closes product-specific keyboard and focus obligations automatically.
- Ignoring rare destructive/admin features because they are not part of the demo path.
- Downgrading a missing core action to minor because the visual design is excellent.
- Treating the backend’s permission rejection as adequate UI behavior.
- Marking runtime behavior PASS from static source inspection.
- Allowing the same generator to erase or soften findings to obtain completion.

**Hard gate:** visual quality, stakeholder enthusiasm, code compilation, or test volume cannot compensate for a `FAIL` or material `UNKNOWN` in product-wide functional closure.
