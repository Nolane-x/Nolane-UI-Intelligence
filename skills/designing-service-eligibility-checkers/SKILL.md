---
name: designing-service-eligibility-checkers
description: Use when a public service needs to help people determine likely eligibility or route suitability before a full application while preserving policy nuance, uncertainty, exceptions, and next-step options.
---

# Designing Service Eligibility Checkers

An eligibility checker is a policy explanation instrument. It should reduce unnecessary applications and route people appropriately without pretending a lightweight questionnaire is a legally final decision when it is not.

## Parent Contract
**Required parent:** `designing-public-service-experiences`.

The parent owns the public-service journey. This skill owns pre-application policy questions, branching, uncertainty, explanation, and transition into the correct service route.

## Rule Boundary
Declare whether the checker is authoritative, indicative, or only a routing aid. If a final decision depends on evidence review or discretion, say so before the result. Never let a green result visually imply guaranteed entitlement when the checker can only establish basic conditions.

Translate policy rules into questions that users can answer from their own circumstances. Avoid exposing administrative terminology unless it is defined. Where a rule depends on dates, residence, income periods, household composition, or status categories, make the period and interpretation explicit rather than relying on colloquial meaning.

## Branching and Exceptions
Minimize irrelevant questions through branching, but keep enough traceability to explain the outcome. Complex exceptions should not be compressed into misleading yes/no logic merely to shorten the flow. If a case cannot be determined digitally, route to human assessment or the full application with the uncertainty preserved.

Support backtracking without erasing dependent answers invisibly. When changing an upstream answer invalidates later answers, explain which information is being cleared and why.

## Result Design
Results should state: the likely eligibility/routing conclusion, the key rules that drove it, any assumptions or unresolved conditions, and the next action. For ineligible outcomes, provide alternative services or review routes when known. Avoid blame-oriented wording when the user simply falls outside a policy condition.

## Evidence
Build boundary cases around threshold dates, income bands, household changes, uncertain immigration/residence evidence, and exceptions. Compare checker outputs with policy-authoritative examples or service-team validation. Test language expansion, screen readers, interrupted flows, browser back, and links into the full application.

## Failure Modes
- Indicative eligibility looks like a final legal determination.
- The checker asks for facts users cannot reasonably know without explanation.
- Edge cases are forced into a false yes/no result.
- Changing an early answer leaves stale downstream answers active.
- Result copy gives a conclusion without the policy reasons that produced it.
- “Not eligible” provides no route for exceptions or alternative support.

## Falsification
Choose cases immediately on both sides of a policy threshold plus one discretionary exception. Falsify if the UI produces the same confident result for the exception as for deterministic cases, or if changing a threshold-driving answer does not recompute dependent state transparently.

## Recovery
Expose the rule boundary, preserve uncertainty, clear invalid dependent answers explicitly, and route indeterminate cases to the correct assessment path. If the checker cannot cite a current policy rule for a branch, do not retain that branch as authoritative.

## Handoff
Full application structure belongs to `designing-government-application-journeys`; entitlement explanation after formal decision belongs to `designing-benefit-entitlement-explanations`; identity proof should not be introduced here unless eligibility genuinely requires it.

## Output Contract
Return a `service-eligibility-checkers-contract` with `authority_level`, `policy_questions[]`, `branch_rules`, `exception_states[]`, `dependency_reset_rules`, `result_explanations`, `alternative_routes[]`, `policy_evidence[]`, `boundary_tests[]`, `falsification_cases[]`, and `recovery_actions[]`.