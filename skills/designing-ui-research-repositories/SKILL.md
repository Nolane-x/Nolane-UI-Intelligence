---
name: designing-ui-research-repositories
description: Design research repositories so findings are discoverable by problem, population, method, product surface, and decision without stripping away source context.
---

# Designing UI research repositories

Research repositories should reduce repeated studies and memory loss, not become a folder cemetery. Use this skill when teams need to store and retrieve studies, notes, clips, findings, artifacts, and decisions over time.

## Decision ownership

Own repository information architecture, metadata, search, access, study-to-finding relationships, sensitive-data handling, and archival policy. Decide what is indexed at study, session, observation, finding, or decision level.

## Inputs and evidence

Collect current research artifacts, naming conventions, product taxonomy, user segments, methods, access controls, retention requirements, researcher workflows, and common search questions. Identify findings trapped in slide decks or chat threads.

## Procedure

Model studies, participants/sessions, observations, findings, hypotheses, and decisions as related entities rather than flattening everything into documents. Provide metadata for product area, task, population, method, date, confidence, and status. Support full-text search plus faceted retrieval.

Preserve links to raw evidence where rights permit, but separate sensitive participant data from broadly accessible summaries. Make superseded or contradictory findings visible rather than deleting history. Create lightweight contribution rules so adding research is not more work than teams will sustain.

## Failure topology

Overly rigid taxonomies require constant cleanup and discourage contribution. Under-structured repositories cannot answer cross-study questions. Another failure is exposing participant-identifying media too broadly or retaining it beyond consent terms.

Findings can lose method/population context when copied into executive summaries.

## Falsification

Give users realistic retrieval tasks: find evidence about mobile onboarding among new users, identify studies that contradict a pattern, or locate the source clip for a finding. Measure search success and time. Test access boundaries with sensitive artifacts and archived studies.

## Output contract

Produce a `ui-research-repositories-contract` defining entity model, metadata, taxonomy governance, search/facets, source linkage, privacy/access, status/supersession, retention, and retrieval test scenarios.

## Handoffs

Use `engineering-ui-evidence-workflows` for evidence lifecycle, `designing-affinity-analysis-workflows` for synthesis artifacts, `designing-design-hypothesis-ledgers` for hypotheses, and privacy research practices for participant data.