---
name: planning-usability-research
description: Use when a UI decision has material uncertainty that cannot be resolved by standards or deterministic inspection, especially for new workflows, high-risk tasks, accessibility, expert tools, or competing design hypotheses.
---

# Planning Usability Research

## Overview
Choose evidence that can actually change the decision. Research is not a ceremonial usability test after the design is finished; it is an uncertainty-reduction instrument with explicit questions, participants, tasks, measures, and stopping logic.

## Parent Contract
**Required parent:** `routing-ui-work`.

The router must identify a decision uncertainty or validation obligation. If the question is normative — for example a known accessibility requirement — research does not replace compliance.

## Decision Model
Write the decision first: “We need to choose X versus Y because outcome Z is uncertain.” Select a method based on the uncertainty. Exploratory interviews or contextual inquiry uncover work models and vocabulary. Moderated usability sessions expose comprehension, navigation, recovery, and high-risk decision errors. Unmoderated tests can scale narrow tasks. Diary/longitudinal methods suit repeated habits and delayed effects. Telemetry can reveal frequency and failure patterns but rarely explains intent by itself.

Recruit for the behavior and capability that matter, not generic demographics. Include expert/novice split, assistive technology, environmental constraints, or safety-relevant roles when those define the product. Design tasks around realistic goals with credible data; avoid wording that teaches the intended UI path.

Define observable measures before sessions: success, critical error, time where meaningful, recovery, assistance, comprehension, confidence calibration, resume performance, and qualitative evidence. For safety/high-stakes work, distinguish exploratory formative evidence from formal validation requirements.

Plan analysis and stopping. A tiny sample can reveal severe repeated failures, but cannot support broad population claims. State what result would reverse the design decision.

## Evidence
The plan itself must preserve hypotheses, participant criteria, protocol, task scripts, instrumentation, privacy/consent handling, and analysis method. Record exclusions and why they do not invalidate the decision scope.

## Output Contract
Return a `research-plan` with `decision_question`, `hypotheses[]`, `method`, `participants`, `environment`, `tasks[]`, `measures[]`, `critical_events[]`, `data_handling`, `analysis_plan`, `decision_thresholds`, `stopping_rule`, and `claim_bounds`.

## Failure Traps
- Asking users which visual option they “like” when task performance is the decision.
- Recruiting convenient colleagues for specialized workflows.
- Leading tasks that reveal labels or navigation paths.
- Measuring only completion while ignoring critical error and recovery.
- Using research to waive a standard.
- Turning five sessions into a percentage claim about all users.
- Testing only the polished happy path.

Good research can prove the design hypothesis wrong; if the protocol cannot, it is probably validation theater.