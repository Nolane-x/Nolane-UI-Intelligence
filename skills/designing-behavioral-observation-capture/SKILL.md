---
name: designing-behavioral-observation-capture
description: Capture user behavior during UI research as timestamped observations separated from interpretation, with enough context to support later synthesis and audit.
---

# Designing behavioral observation capture

Research notes become unreliable when “user was confused” replaces what actually happened. Use this skill when teams need consistent observation records from usability sessions, field studies, support review, or moderated prototypes.

## Decision ownership

Own observation granularity, timestamping, event vocabulary, context fields, interpretation separation, severity tagging, and media linkage. Decide what should be captured live versus coded after review.

## Inputs and evidence

Collect protocol tasks, recording capabilities, privacy/consent, moderator workflow, observer count, target behaviors, and synthesis needs. Inspect current notes for judgments that cannot be traced to observable events.

## Procedure

Record concrete behavior: action, visible system state, participant words when material, outcome, and timestamp. Keep inference in a separate field. Link observations to task, screen/version, and source recording where permitted.

Use lightweight tags for recurring event types—hesitation, wrong path, self-recovery, help request, error—not as substitutes for notes. Capture positive evidence too, such as fast correct comprehension, so synthesis is not biased toward problems.

Normalize observer conventions before multi-session studies.

## Failure topology

Interpretive notes create confirmation bias. Overly granular logging can distract moderators and produce noise. Another failure is collecting only failures, making frequency estimates and success understanding impossible.

Unlinked observations lose the exact prototype state that triggered them.

## Falsification

Have independent reviewers watch a sample and compare notes. Check whether another researcher can distinguish observation from interpretation and locate supporting video. Review positive and negative event coverage. Test the capture method during a real-paced session for burden.

## Output contract

Produce a `behavioral-observation-capture-contract` defining observation fields, interpretation separation, timestamp/media linkage, event tags, positive/negative coverage, privacy constraints, and inter-observer calibration examples.

## Handoffs

Use `designing-interview-note-synthesis` for qualitative statements, `designing-affinity-analysis-workflows` for clustering, `designing-task-success-measures` for coding outcomes, and `designing-ui-research-repositories` for storage.