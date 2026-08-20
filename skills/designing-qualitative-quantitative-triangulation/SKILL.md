---
name: designing-qualitative-quantitative-triangulation
description: Triangulate qualitative and quantitative UI evidence by comparing what each method can legitimately establish, rather than using one to decorate conclusions from the other.
---

# Designing qualitative quantitative triangulation

Analytics can show where behavior changes; qualitative research can reveal mechanisms, meanings, and unmet needs. Use this skill when teams need a combined conclusion from unlike evidence sources.

## Decision ownership

Own evidence-role mapping, convergence/divergence interpretation, population comparability, sequencing, and confidence updates. Decide when disagreement requires more research instead of choosing the method that supports the preferred story.

## Inputs and evidence

Collect study methods, samples/populations, time windows, metrics, interview or observation findings, product versions, and known biases. Check whether sources actually examine the same behavior and context.

## Procedure

State what each evidence source can answer. Use quantitative data for prevalence, trend, or causal effect when design supports it; use qualitative evidence for mechanism, comprehension, context, and discovery. Compare results at a shared hypothesis level.

When evidence converges, increase confidence only to the extent methods are independent. When it diverges, investigate sampling, instrumentation, context, timing, and construct differences. Preserve unresolved divergence visibly.

Use sequential designs deliberately: analytics may identify a drop-off to investigate qualitatively; qualitative findings may generate hypotheses to quantify.

## Failure topology

A quote can be used to “explain” a metric without evidence they share a cause. Small interview samples are sometimes converted into prevalence claims. Another failure is treating massive telemetry as inherently superior even when the metric does not measure the construct of interest.

## Falsification

Try to construct alternative explanations consistent with one data source but not the other. Compare populations and product versions. Remove one source and see what claims become unsupported. Ask whether convergence results from shared instrumentation or shared bias.

## Output contract

Produce a `qualitative-quantitative-triangulation-contract` containing hypotheses, evidence-role table, source comparability, convergence/divergence, alternative explanations, confidence updates, and follow-up studies for unresolved conflict.

## Handoffs

Use interview/observation synthesis skills for qualitative sources, experiment interpretation for causal tests, `designing-design-hypothesis-ledgers` for hypothesis tracking, and `engineering-ui-evidence-workflows` for durable linkage.