# Nolane UI Intelligence Evaluations

NUI evals are pressure tests for agent behavior. They are not screenshots of one preferred aesthetic and they do not define a single house style.

## Two kinds of evaluation

### Deterministic repository evals
Executed by `unittest` and `scripts/nui-validate`. These verify graph integrity, skill discoverability/contracts, token/state invariants, adapter completeness, JSON validity, and completion-packet rules.

### Agent behavior evals
JSON cases describe tasks, required behaviors, forbidden shortcuts, and an oracle. These require an agent runtime (and sometimes browser/design tools) to execute. They must never be reported as passed merely because their files parse.

## Evaluation protocol

For a skill/behavior change:

1. Run the case without the changed guidance or with a baseline agent policy where practical.
2. Record the failure/rationalization that the case is designed to expose.
3. Run with NUI in a fresh context.
4. Score hard gates first. A failed hard gate cannot be compensated by visual-quality points.
5. Score applicable quality dimensions using artifact/evidence, not the agent's own explanation.
6. Repeat enough times to inspect variance before claiming a wording/routing improvement.
7. For aesthetic comparisons, randomize/blind the evaluator to system identity when practical.

## Score interpretation

A behavior run has three outputs:

- `gate_decision`: PASS/BLOCKED
- `quality_vector`: per-dimension score for applicable dimensions
- `variance_notes`: instability across repeated runs

NUI does not claim “best UI skill” from repository size. Comparative superiority requires head-to-head evaluation on the same prompts, tools, model/runtime budget, and independent judging.

## Case format

Each case includes:
- `id`
- `prompt`
- `must`: observable behaviors/artifacts required
- `must_not`: observable shortcuts/failures forbidden
- `oracle`: how an evaluator decides

Optional fields specify references, capability requirements, routes, stress states, or scoring dimensions.
