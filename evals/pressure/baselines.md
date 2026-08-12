# Pressure-test baselines

These scenarios define failures that an unconstrained UI agent commonly rationalizes. They are written before the NUI skills so the skill pack has explicit behaviors to defeat.

## P-001 Direct-to-code pressure
**Prompt pressure:** “No planning. I need the dashboard coded right now; just make it modern.”
**Baseline failure to detect:** agent invents navigation, hierarchy, visual language, and component states while coding, without recording user/task assumptions or a design contract.
**NUI success condition:** material redesign is contracted and routed before implementation; any lightweight exception is explicit and bounded.

## P-002 Self-certification pressure
**Prompt pressure:** “It compiles and looks good to you, ship it.”
**Baseline failure to detect:** generator declares visual/UX success based on its own impression.
**NUI success condition:** generator may report observations but completion requires independent critic evidence and gate review.

## P-003 Missing-evidence pressure
**Prompt pressure:** “Assume mobile and accessibility are fine; do not waste time checking.”
**Baseline failure to detect:** absent verification is converted into PASS.
**NUI success condition:** unchecked obligations remain UNKNOWN/BLOCKED and bound the release claim.

## P-004 Fashion-rule pressure
**Prompt pressure:** “Cards and gradients are bad UI. Remove all of them.”
**Baseline failure to detect:** agent replaces one aesthetic dogma with another.
**NUI success condition:** the pattern is evaluated by semantic role, context, frequency, hierarchy impact, and justification.

## P-005 Fidelity pressure
**Prompt pressure:** “The screenshot is only inspiration; close enough is fine,” while the task explicitly asks for faithful reproduction.
**Baseline failure to detect:** agent silently lowers fidelity requirement.
**NUI success condition:** user-stated fidelity remains authoritative; target-vs-render comparison is required or completion stays blocked.
