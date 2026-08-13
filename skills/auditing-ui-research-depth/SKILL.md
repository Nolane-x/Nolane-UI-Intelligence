---
name: auditing-ui-research-depth
description: Use when acting as an independent critic whenever external research materially affects UI decisions; determines whether the agent actually inspected decision-relevant evidence or merely produced plausible-looking citations and summaries.
---

# Auditing UI Research Depth

## Parent Contract
**Required parent:** `critiquing-research-validity`.

Receive research claims, dossiers, source snapshots, decision outputs and the evidence ledger. The parent owns general research validity; this skill specializes that critique for artifact-level UI-source depth and material transfer claims.

## Decision Boundary
This is an **epistemic critic**, not another researcher. It owns the question: “Is the research deep enough that the claimed UI decision is warranted?” It does not reward volume, citation count, repository popularity, number of tabs opened, or prose sophistication. It attempts to falsify the research process and can downgrade PASS to UNKNOWN/BLOCKED.

## What depth means
Research is deep when the inspected evidence is capable of changing the decision. A five-file investigation can be deeper than fifty README pages if those five files contain the implementation, tests, demo context, accessibility behavior and dependency boundary that determine fitness. Conversely, a 10,000-word report can be shallow if every claim derives from marketing prose.

Audit against the v6 depth dimensions: ownership; inherited obligations; observation protocol; branch logic/tradeoffs; falsification; evidence; output semantics; failure topology; recovery; downstream verification. Do not use word/token/section count as a proxy.

## Audit procedure
1. Reconstruct the material decision from outputs without trusting the conclusion. What changed because of the research?
2. Trace each material claim backward to evidence. If a claim says “keyboard accessible,” find the inspected guidance/test/runtime artifact; if it says “lightweight,” find the dependency/performance evidence and target budget context.
3. Compare inspected artifacts with the role-specific plan. Missing artifact classes are not paperwork defects; state which uncertainty remains unresolved.
4. Test version coherence. Check that evidence belongs to a compatible snapshot/ref/release and that high-drift sources were reverified.
5. Inspect negative evidence. Research that reports only confirming facts is suspect. Look for contradictions, hazards, rejected alternatives, unread material and explicit uncertainty.
6. Audit transfer reasoning. Ensure the mechanism learned from a source is distinguished from copied style/code and reconciled to local semantics/tokens/accessibility/platform constraints.
7. Audit source diversity **by role**, not by count. Ten animated galleries can be one epistemic monoculture. A mature primitive, real product, design system, experimental gallery and empirical accessibility source can provide genuinely different evidence.
8. Audit stopping logic. Ask what unread fact could reverse the decision. If the researcher cannot answer, “stop_reason” is confidence theater.
9. Re-run one falsification probe when feasible: inspect a cited source path, compare a contrasting source, or remove the chosen mechanism and see whether the claimed product value remains.
10. Separate UNKNOWN from FAIL. Missing evidence means UNKNOWN/BLOCKED; contradictory evidence can mean FAIL. Never convert missing evidence into a low numeric confidence that still permits release.

## Adversarial probes
- Hide repository names/stars and re-evaluate the reasoning. Does authority collapse?
- Replace all aesthetic adjectives with blanks. Are causal mechanisms still described?
- Ask which exact artifact proves the strongest claim. If the answer is “README/docs generally,” trace deeper.
- Swap one source with another of the same visual trend. If conclusions remain identical, the research may be trend confirmation rather than product reasoning.
- Check whether a quoted source role is actually the role being used. A chart API is not statistical validation; a component demo is not user research; a design system is not a brand fit oracle.
- Inspect whether “current” means an actual retrieval date/ref or model memory.

## Falsification of the audit itself
This critic must also be falsifiable. If the researcher can produce missing artifact-level evidence, reconcile snapshot/version concerns, show the claimed mechanism in source/runtime, and explain why negative evidence does not overturn the decision, remove the finding. Do not preserve objections merely to appear rigorous.

## Output — `ui-research-depth-findings`
Emit finding IDs, affected source/decision, severity, epistemic state (`SUPPORTED | UNKNOWN | CONTRADICTED`), missing or contradictory evidence, artifact/claim trace, monoculture or version risks, falsification probe used, required recovery action, and what evidence would close the finding. Also emit an overall decision: `PASS | RESEARCH_MORE | RESELECT_SOURCE | BLOCKED`.

## Failure topology
- citation theater;
- README-only authorization;
- mixed-version evidence;
- source-role confusion;
- trend monoculture disguised as breadth;
- missing negative evidence;
- inaccessible/performance/license assumptions promoted to facts;
- mechanism claims without artifact paths;
- stop reasons that merely restate confidence;
- critic-generator correlation where the same context repeats its own unsupported assumptions.

## Recovery
For missing evidence, route back to `performing-ui-repository-archaeology` with exact artifact classes/questions. For source monoculture, route to ecosystem/visual-reference research with a contrasting source role. For role mismatch or disproven mechanism, reselect the source. For unresolved license/safety issues, block material use rather than suggesting stylistic workarounds.

## Hard gate
**Material external research cannot satisfy completion while a critical claim lacks decision-relevant artifact evidence, source versions are incoherent, the source role is being misused, or negative/falsifying evidence has not been represented. Research depth is judged by decision-changing evidence, never prose volume.**

## V6 Research Depth Critic Protocol
Perform **evidence-chain reconstruction** from each material design or implementation claim back to the exact source artifact, observation, and inference step. Map the **unread-risk surface**: files/docs/issues/tests/platform states not inspected that could plausibly overturn the claim.

Require **negative-evidence coverage**—known failures, limitations, contrary references, rejected alternatives, and unsupported contexts—not just confirming examples. Run a **stop-rule audit** to determine whether research stopped because marginal information gain became low or simply because the first attractive answer appeared. Issue an **epistemic-status verdict** per material claim: SUPPORTED, UNKNOWN, CONTRADICTED, or OUT-OF-SCOPE.

### Falsification
Ask an independent critic to trace one chosen mechanism and one rejected mechanism without using the author's summary. If the chain cannot be reconstructed or unread material could reverse the decision, depth is insufficient.

### Recovery
Reopen only the disputed evidence branch, inspect the missing primary artifacts, update contradictions/uncertainty, and block material influence until the verdict is supported.
