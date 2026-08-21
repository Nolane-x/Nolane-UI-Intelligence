---
name: governing-design-system-exceptions
description: Use when a product team needs to violate or bypass a design-system rule and the exception requires explicit scope, rationale, risk, owner, expiry, and reintegration path.
---

# Governing Design-System Exceptions

## Exception Authority
A design system without exceptions becomes impractical; a design system with undocumented exceptions dissolves. This skill owns the governance state of a deliberate deviation: why it exists, which rule it bypasses, who can approve it, where it applies, how long it lives, and how it returns to the system.

## Parent Contract
**Required parent:** `architecting-component-systems`.

The parent defines reusable system contracts. This specialist governs bounded deviations without redefining the normal contribution path.

## Exception Record
Every exception carries a stable identifier, triggering need, affected surface, violated invariant, user/business reason, alternatives considered, risk class, approving authority, owner, expiry/review date, and exit strategy. “Design requested it” is not a rationale. Scope must be narrower than the rule it bypasses.

Separate three states: temporary exception awaiting upstream capability, permanent intentional product divergence, and evidence that the system rule itself is wrong. The third should route to contribution/system change rather than become endless exception debt.

## Containment Invariants
An exception cannot silently become a reusable local component. Its styling/API must not leak into unrelated surfaces. Safety/accessibility obligations that are non-waivable remain non-waivable. Expired exceptions become blocked for review rather than automatically renewed.

## Evidence
Evidence includes the violated baseline contract, affected product states, approval record, risk evidence, telemetry or user evidence supporting the need, and a test proving the exception does not spread beyond scope. Track whether an upstream fix now exists.

## Failure Modes
Failure includes copy-pasted exceptions, permanent “temporary” overrides, exceptions with no owner, local forks that stop receiving fixes, and approvals that waive obligations the approver does not control. Another failure is measuring exception count without measuring debt severity or propagation.

## Falsification
Falsification searches for the exception's implementation signature outside its scope, removes the exception after an upstream capability lands, and checks whether the original need still exists. If usage has spread or the rationale no longer holds, the current exception contract is invalid.

## Recovery
Recovery contains leaked usage, restores baseline behavior where the exception is no longer justified, or promotes a broadly valid need through the contribution workflow. High-risk invalid exceptions revert first; cosmetic convergence can follow.

## Output
Output: `design-system-exceptions-contract` with exception identity, scope, authority, risk, evidence, expiry, containment checks, and reintegration path.

## Handoff
Handoff broadly reusable improvements to design-system contribution workflow; handoff release sequencing to breaking-change rollout when the baseline changes.

## Sibling Boundary and delete-the-skill
Contribution governance owns ordinary upstream change, not bounded deviation debt. Removing this skill leaves exception scope, expiry, and containment decisions without an owner, so the delete-the-skill test passes.