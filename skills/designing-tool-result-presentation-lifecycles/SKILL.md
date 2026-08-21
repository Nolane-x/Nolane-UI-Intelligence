---
name: designing-tool-result-presentation-lifecycles
description: Use when tool output arrives incrementally, changes shape over time, can be superseded, or needs to graduate from raw execution evidence into a stable user-facing result without losing provenance.
---

# Designing Tool-Result Presentation Lifecycles

## The presentation problem
Tool output has a different lifecycle from the tool call itself. A runtime can finish successfully while its result is still streaming, parsing, enriching, rendering, or being replaced by a more authoritative representation. This skill owns the decisions that transform runtime output into a user-facing result surface: when raw evidence is shown, when it is summarized, when a structured view becomes canonical, how superseded views remain inspectable, and how uncertainty is preserved.

## Parent Contract
**Required parent:** `designing-generative-ui`.

The parent owns the broader generative-UI runtime and how agent-produced interface fragments participate in the product. This specialist starts after a tool has produced or begun producing a result and focuses on the result’s presentation states rather than execution authority.

## Presentation phases
Model at least `raw_available`, `normalizing`, `partial_view`, `structured_view`, `enriched_view`, `superseded`, and `presentation_error`. A runtime success does not imply a structured renderer succeeded. If normalization fails, the interface should retain access to the raw result instead of converting a rendering defect into a fictitious tool failure.

The key decision is which representation is currently canonical for user action. A partial table may be useful for reading but unsafe for export; an enriched map may lag behind a text result; a summary may omit fields required for audit. Attach capability to representation state so controls such as copy, export, continue, compare, or act-on-result only appear when their prerequisites are met.

## Provenance must survive transformation
Every transformation should maintain a trace from visible fields back to the tool result, including transformations performed by the model. Generated labels, inferred categories, or synthesized summaries must not look like original source fields. If a later authoritative result supersedes a provisional one, the interface should update the canonical view while preserving enough history to explain the change.

For sensitive results, redaction may be part of presentation, but redaction is not deletion from provenance. The evidence ledger should record that a value existed and was withheld under policy without leaking the value itself.

## Failure classes
Characteristic Failure includes rendering a parser error as tool failure, hiding partial completeness, silently replacing a result after the user acted on it, presenting model-generated summaries as source data, and allowing controls that assume fields the current representation does not possess. Another failure occurs when the user can no longer inspect the raw evidence after a generative component has transformed it.

## Evidence and review
Evidence should pair tool-result identifiers with presentation revision identifiers. Capture raw payload metadata, schema recognition, transformation steps, renderer state, field provenance, and any user actions taken from each revision. Test results whose shape evolves mid-stream, results that violate the expected schema, results too large for the preferred renderer, and results later superseded by a stronger source.

## Falsification probes
Falsification should force malformed structured output, schema version drift, delayed enrichment, a renderer crash after tool success, and a corrected second result that contradicts the first. The contract fails if runtime truth is lost when presentation fails, if transformed information cannot be distinguished from source information, if stale controls remain active, or if a superseded representation continues to appear canonical.

## Recovery route
Recovery falls back one representation level at a time: enriched to structured, structured to normalized text, normalized text to safely rendered raw evidence. Preserve the tool result identity throughout. If a user already acted on a superseded result, surface that dependency and route the affected action to reconciliation rather than quietly swapping the underlying data.

## Output
Output: `tool-result-presentation-lifecycles-contract`, defining presentation states, canonical-view rules, provenance mappings, capability gates, fallback renderers, supersession behavior, and evidence requirements.

## Handoff, Sibling boundary, delete-the-skill
Handoff execution truth to `designing-agent-tool-call-lifecycles`; hand off generated-component trust decisions to `designing-agent-generated-component-authority`; hand off schema degradation to `designing-generative-ui-schema-fallbacks`.

Sibling boundary: the tool-call lifecycle says whether an operation succeeded, failed, or is unknown. This skill says how the returned evidence becomes a durable interface object. The delete-the-skill test passes because without it, products tend to collapse execution state and representation state, causing successful tools to appear failed when rendering breaks and generated summaries to masquerade as raw truth.