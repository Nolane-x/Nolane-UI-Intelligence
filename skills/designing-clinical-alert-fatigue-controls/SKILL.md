---
name: designing-clinical-alert-fatigue-controls
description: Use when clinical warnings, reminders, contraindications, critical results, and workflow notifications compete for attention and the product must preserve high-value interruption while reducing low-value repetition and unsafe dismissal habits.
---

# Designing Clinical Alert Fatigue Controls

Clinical alert fatigue is not solved by making alerts quieter. The design problem is to route the right signal, at the right interruption level, to the right responsible person, with enough context to act and enough governance to avoid habituation.

## Parent Contract
**Required parent:** `designing-clinical-care-workflows`.

The parent owns clinical workflow safety. This skill owns interruption tiering, repetition, acknowledgement, suppression, escalation, and measurement of alert burden across clinically consequential signals.

## Alert Classification
Classify alerts by hazard, urgency, confidence, preventability, actionability, and required response. A critical result requiring immediate escalation is not the same interaction as a duplicate-therapy advisory or a routine preventive reminder. Encode tiers behaviorally, not merely with color.

Define the recipient model. Some alerts belong to the ordering clinician, some to the current care team, some to a service queue, and some require escalation when unacknowledged. Avoid broadcasting every signal to everyone because diffuse responsibility can reduce action rather than increase it.

## Repetition and Suppression
Repeat only when the underlying risk persists and the repeated interruption changes the probability of appropriate action. Track alert instance identity so refreshes or route changes do not re-fire the same warning as if new. Suppression, snooze, or override must capture scope, duration, actor, and rationale according to policy.

Do not let frequent low-value advisories train users to click through the same interaction used for rare high-severity blockers. Different classes need distinct action patterns and, where appropriate, different authority to override.

## Acknowledgement Versus Resolution
Acknowledgement means the signal was seen or accepted; resolution means the underlying clinical condition or workflow need changed. Keep those states separate. For critical alerts, expose what action was taken or which team owns follow-up when policy requires.

## Evidence
Measure alert burden in realistic sequences, not one-off usability tests: alerts per clinician/time period, repeat rate, override rate, action rate, time-to-action, escalation rate, and clinically reviewed appropriateness where available. Test alert storms, duplicate events, stale patient context, role changes, overnight handoff, and partial service outage.

## Failure Modes
- Every alert uses the same modal and severity styling.
- A dismissed advisory immediately reappears on every navigation event.
- Override reason is collected but never changes future repetition policy.
- Critical result acknowledgement is displayed as clinical resolution.
- Alerts reach users who cannot act while responsible users receive no escalation.
- Low-value volume hides a rare high-consequence signal.
- UI suppresses alerts based solely on annoyance without safety authority.

## Falsification
Run a scenario containing many repeated advisories plus one critical actionable event. Falsify if experienced users treat the critical alert with the same automatic dismissal pattern, if duplicate signals multiply without new evidence, or if the system cannot identify who is responsible after acknowledgement.

## Recovery
Reclassify by actionability and consequence, deduplicate by clinical event identity, separate acknowledgement from resolution, narrow recipient routing, and introduce governed suppression/override windows. Use outcome and burden evidence to tune policy; do not optimize only for fewer popups.

## Handoff
Medication safety warnings coordinate with medication entry/reconciliation; abnormal result escalation coordinates with `designing-clinical-result-abnormality`; general notification mechanics may reuse interruption infrastructure but cannot define clinical severity.

## Output Contract
Return a `clinical-alert-fatigue-controls-contract` with `alert_classes[]`, `interruption_tiers`, `recipient_routing`, `repeat_dedup_policy`, `suppression_override_rules`, `acknowledgement_vs_resolution`, `burden_metrics[]`, `safety_evidence[]`, `falsification_cases[]`, and `recovery_actions[]`.