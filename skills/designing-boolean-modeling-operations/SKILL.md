---
name: designing-boolean-modeling-operations
description: Own union, subtract, intersect, split, and related solid/mesh boolean workflows with operand identity, order, preview, validity, tolerance, source preservation, and failure diagnosis.
---
# Designing Boolean Modeling Operations

## Decision ownership

Own combination operations between geometric bodies. Decide boolean type, target/tool operand roles, order, source preservation, tolerance, live/modifier versus destructive result, preview, validity diagnostics, and recovery. Generic multi-object operations do not own topology-kernel failure semantics.

## Inputs and evidence

Require geometry/body types, manifold/solid status, operand count/order, boolean kernel capabilities, tolerance, coordinate units, source preservation policy, history/modifier model, and expected failure diagnostics. Identify coplanar, tiny-feature, self-intersection, and open-mesh cases.

## Procedure

Make target and tool operands unmistakable and preview the chosen union/subtract/intersect result. For non-destructive workflows, show source bodies and modifier ordering; for destructive workflows, state what will be consumed. Validate known preconditions and surface kernel warnings before or after computation with affected geometry focus. Tolerance changes need unit context and should not be a magical "fix" button. When a boolean fails, preserve inputs and offer diagnostic categories such as open body, coplanar ambiguity, self-intersection, or precision limitation rather than deleting geometry.

## Failure topology

Failures include subtract operands reversed, source body deleted unexpectedly, successful-looking operation yielding empty geometry, tolerance silently changed, modifier order altering result with no cue, and boolean failure destroying source inputs. Another failure is expensive recomputation freezing every transform of a live tool body.

## Falsification

Reject if operand roles cannot be confirmed before commit; if destructive source consumption is implicit; if a failed operation can remove sources; if tolerance lacks units; if empty/invalid result appears successful; if modifier order is hidden; or if live boolean latency exceeds the interaction budget with no deferred/preview strategy.

## Output contract

Return a `boolean-modeling-operations-contract` with: operation type; target/tool operands; order; destructive/non-destructive mode; source preservation; tolerance/unit; preconditions; preview; validity/result state; diagnostics; performance fallback; and recovery. Include one reversed-subtract and one open-mesh failure.

## Handoffs

Mesh/solid selection supplies operands, clash inspection may detect resulting interference, parametric/history owners govern non-destructive ordering, and manufacturing export validates final body suitability.