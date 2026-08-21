---
name: designing-manual-review-evidence-contracts
description: Use when important UI qualities cannot be fully automated and a human review must produce reproducible, bounded evidence with explicit questions, artifacts, verdicts, uncertainty, reviewer role, and escalation instead of informal approval comments.
---

# Designing Manual Review Evidence Contracts

## Manual review needs a test contract
Some UI claims require judgment: whether hierarchy makes a critical warning discoverable, whether copy communicates irreversible consequences, whether a focus indicator remains perceivable over real content, or whether a complex workflow is comprehensible. This skill owns how those judgments become evidence rather than unstructured opinion.

## Parent Contract
**Required parent:** `binding-ui-evidence`.

The parent defines claim/evidence lineage. This specialist activates when the claim cannot be sufficiently proven by deterministic automation and a human reviewer must make a bounded decision.

## Review question design
Write review questions so two qualified reviewers can examine the same artifact and understand what decision is being requested. Bind each question to a surface, state, environment, task, obligation, and artifact revision. The decision owner is the admissibility standard for a manual verdict—not the aesthetic preference of the reviewer.

Prefer questions such as “Can a keyboard-only user identify the focused destructive action in each modal state?” over “Does this feel accessible?” Prefer “Does the warning remain distinguishable from informational notices at normal and high-density states?” over “Is the visual hierarchy good?” Specific questions reduce retrospective rationalization.

## Reviewer role and independence
Record reviewer identity or stable role, relevant expertise, conflict or authorship relationship, and whether independent review is required. High-risk claims may need a reviewer other than the implementer. Manual review is not automatically stronger because a senior person performed it; expertise must match the question and evidence must remain inspectable.

## Verdict vocabulary
Use statuses such as `pass`, `fail`, `blocked`, `not_applicable`, and `inconclusive`. An inconclusive result is not a soft pass. Include rationale tied to observed evidence, not personal taste, and state any assumptions. When reviewers disagree, preserve both observations and route the conflict to a defined resolution path rather than averaging them into approval.

## Evidence package
Evidence may include annotated screenshots, short recordings, interaction traces, semantic trees, test data, task scripts, and reviewer notes. Make the package itself accessible and durable. A verbal meeting conclusion with no artifact identity cannot support later release claims.

## Failure modes
Characteristic Failure includes “LGTM” as the only record, review against an unpinned build, reviewers answering different implicit questions, authors self-certifying high-risk work with no independence rule, and blocked checks being omitted from the packet. Another failure is retroactive rubric creation after seeing the result, which converts review into justification rather than evaluation.

## Falsification
Give the same packet to another qualified reviewer, change the build revision while keeping screenshots, remove the review question, or inject an artifact that contradicts the written verdict. The contract fails if the verdict cannot be reproduced or challenged, if a reviewer cannot identify the exact tested state, or if uncertainty is silently interpreted as approval.

## Recovery
When review evidence is weak, retain the original verdict as historical record, define a precise review question, recapture current artifacts, and conduct a new review. If reviewers disagree, isolate the factual disagreement from preference and obtain stronger evidence or a designated authority decision. Do not overwrite dissenting evidence.

## Output and Handoff
Output: `manual-review-evidence-contracts-contract`, containing review questions, reviewer role, artifact identity, verdict vocabulary, rationale, uncertainty, independence rules, and conflict handling. Handoff accessibility-specific composition to accessibility evidence packets and baseline-change decisions to regression-baseline governance.

## Sibling Boundary and delete-the-skill
Sibling visual-diff triage helps reviewers decide whether image differences are noise or material; it does not define a general human-review protocol. The delete-the-skill test passes because without this owner, manual evidence remains informal and cannot reliably support an evidence-gated release.