---
name: maintaining-project-design-memory
description: Use when a project is designed across multiple sessions or agents and accepted/rejected design knowledge must persist without turning temporary taste into permanent global rules.
---

# Maintaining Project Design Memory

## Parent Contract
**Required parent:** `routing-ui-work`.

Receive evidence-bearing design decisions from visual iteration, usability findings, product decisions, design-system governance, implementation audits, and authoritative stakeholder choices. This skill stores bounded project knowledge; it does not make new design decisions merely because memory exists.

## Decision Boundary
This faculty owns **longitudinal design memory**: what the project learned, where the learning applies, what evidence supports it, how confident it is, when it expires, what contradicts it, and which newer decision supersedes it. It is not a style guide, changelog, prompt history, or unfiltered archive of every model thought.

A memory item is actionable only when it can influence a future decision: “Dense operational tables perform better with border/spacing hierarchy than elevated cards in the admin workspace, supported by accepted iteration R14 and user review,” not “cards looked bad.” Scope is essential: the same project may use expressive motion on marketing surfaces and restrained motion in a high-frequency console.

## Product Truth
Without memory, agents repeat expensive mistakes. They reintroduce rejected gradients, re-open settled density debates, select the same external library that previously caused hydration problems, or start visual research from zero. With naïve memory, the opposite failure appears: one stakeholder preference becomes an eternal command and blocks necessary evolution.

Useful design intelligence therefore requires memory with provenance and decay. The system must distinguish product invariant, validated pattern, current preference, experiment result, unresolved hypothesis, and deprecated decision.

## Decision Model
1. **Admit only material knowledge.** Store decisions that are likely to recur or constrain future work: accepted visual mechanisms, rejected experiments with reasons, component behavior constraints, external library integration lessons, accessibility accommodations, platform exceptions, content/locale stress findings, and explicit stakeholder decisions.
2. **Classify memory type.** Use `invariant`, `validated-pattern`, `preference`, `negative-pattern`, `experiment-result`, `integration-lesson`, or `open-hypothesis`. Each class carries different authority.
3. **Scope precisely.** Attach surfaces, feature families, actor contexts, platforms, themes, density modes, content types, or interaction classes. “No gradients” globally is usually invalid; “do not use decorative gradient behind dense chart labels” may be useful.
4. **Bind evidence.** Reference render comparisons, usability sessions, product decisions, runtime failures, design-system decisions, or authoritative sources. Memory without evidence is low-confidence context, not a hard constraint.
5. **Record confidence and authority.** Distinguish user/stakeholder directive from agent inference. A preference can be high-authority but still scoped; an empirical finding can be strong evidence but may not generalize.
6. **Set freshness/expiry.** Technology/API/library lessons can drift quickly; brand and product invariants may remain stable longer. Use `review_after` or event-based reopen conditions.
7. **Model contradiction.** New evidence may conflict with old memory. Do not silently choose the newer item; link the contradiction and require a resolution decision if both affect the current task.
8. **Supersede, do not erase.** Keep historical records but mark which item replaces another. This prevents rediscovering why a rule changed.
9. **Retrieve minimally.** Router/task faculties should load only relevant memory by scope and decision class. Dumping the whole history into context increases anchoring and prompt dilution.
10. **Update after verification.** A promising experiment should not become a validated pattern until accepted evidence exists. Record rejected results too when they prevent likely repetition.

## Evidence
Memory entries cite durable project artifacts when possible: accepted design revisions, commits, test/eval evidence, stakeholder decisions, issue/PR discussion, visual iteration records, runtime audit results, or design-system governance records. A chat statement can be stored when it carries explicit authority, but the exact statement and date should be preserved rather than paraphrased into a stronger claim.

External-source knowledge belongs in the ecosystem/reference registry; project memory may store how that source behaved **in this project**, such as “library X caused unacceptable bundle cost in the marketing app at version Y.”

## Output Contract
Return `design-memory` with:
- `entries[] {id, type, statement, scope, authority, evidence_refs, confidence, created_at, review_after, reopen_conditions, status: active|contested|superseded|expired}`
- `contradictions[] {entry_ids, issue, required_owner}`
- `supersessions[] {old_id, new_id, reason}`
- `retrieval_tags[]`
- `recently_rejected[]`
- `open_hypotheses[]`
- `memory_health {stale_count, contested_count, uncited_count}`

A future agent may treat an active invariant as a constraint only within its scope and authority. Expired/contested memory must trigger re-evaluation rather than silent reuse.

## Failure Traps
- Storing every prompt, screenshot, or preference and calling it intelligence.
- Turning one successful landing-page style into a rule for the admin console.
- Recording “user likes X” without preserving exact authority/context.
- Deleting old decisions after supersession, losing rationale.
- Treating stale external-library API knowledge as current project truth.
- Promoting an agent aesthetic preference to an invariant.
- Loading all memory into every task and anchoring exploration prematurely.
- Storing only successes; repeated rejected experiments are valuable negative knowledge.
- Allowing a contested entry to silently win because it is newer.

**Hard gate:** memory may accelerate decisions but cannot overrule current product authority, fresh evidence, accessibility/safety obligations, or an explicit reopen condition.
