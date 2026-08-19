---
name: designing-uncertainty-visualization
description: Use when estimates, forecasts, models or measurements carry uncertainty and the interface must communicate interval, distribution, confidence, sample support or provenance without false precision.
---

# Designing Uncertainty Visualization

## Parent Contract
**Required parent:** `designing-data-visualization`.

This faculty owns user-facing representation and interaction for uncertainty. It does not select the statistical model, certify confidence-interval validity or decide domain risk tolerance without specialist evidence.

## Decision Boundary
First identify **what kind of uncertainty exists**. It may be measurement error, confidence/credible interval, forecast band, distribution, model disagreement, sampling variability, missing-data uncertainty or categorical confidence. These are not interchangeable visual decorations. The legend, labels and interactions must use the terminology supplied by the statistical/domain authority.

Choose encoding based on task. Error bars can support point comparisons; bands work for time-series intervals; density/violin/quantile views expose distributions; ensembles can show model spread; opacity or fuzziness is often too ambiguous alone. Never use a generic gradient to mean “confidence” if users cannot recover its quantitative or ordinal meaning.

Point estimates should not visually overpower uncertainty in a way that encourages false precision. Conversely, do not erase the estimate when users need a decision target. Tooltips/details should expose interval bounds, units, confidence/credible level where meaningful, sample size/support and timestamp/provenance.

Interaction must preserve uncertainty under filtering and aggregation. Aggregating uncertain values is not achieved by simply averaging displayed interval widths; defer to the statistical engine and show pending/unavailable uncertainty when recomputation is not valid.

Accessibility requires redundant representation. Color/opacity-only uncertainty needs shape, line style, labels, summary text or data table alternatives. High-stakes contexts may require textual interpretation boundaries such as “estimate, not guarantee,” but avoid editorial conclusions unsupported by domain authority.

## Failure Topology
- A forecast band is labeled “95% confidence” although the model produces a prediction interval with different meaning.
- Opacity encodes confidence but users cannot map opacity to values.
- Filtering updates point estimates while uncertainty bands remain from the previous population.
- Error bars are so subtle that viewers read the chart as exact values.
- Tooltips round the estimate to two decimals but omit a much wider interval.
- Screen-reader/data-table alternative exposes only point estimates.

## Falsification and Recovery
Falsify with narrow/wide intervals, overlapping categories, changing sample sizes, filters, missing uncertainty, color-vision/high-contrast modes and screen-reader summaries. Ask whether a viewer could reasonably infer more certainty than the source supports. If yes, the encoding fails.

Recover by naming the uncertainty type, strengthening quantitative/structural cues, recomputing or withholding stale uncertainty, and pairing visual encodings with explicit interval/support text.

## Output Contract
Return `uncertainty-visualization-contract` with uncertainty type/authority, encoding choice, estimate-vs-uncertainty hierarchy, quantitative disclosure, filter/aggregation recomputation, provenance, accessible alternative and false-precision falsification cases.