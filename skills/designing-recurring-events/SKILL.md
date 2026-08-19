---
name: designing-recurring-events
description: Use when users create or modify repeating events and the interface must express recurrence rule, exceptions, series vs occurrence editing, timezone behavior and end conditions without reducing recurrence to a vague repeat toggle.
---

# Designing Recurring Events

## Parent Contract
**Required parent:** `designing-calendar-interfaces`.

This faculty owns recurrence authoring and occurrence/series editing semantics. Timezone conversion is delegated to `designing-timezone-aware-scheduling`.

## Decision Boundary
Represent recurrence as a rule plus exceptions, not a copied set of future events in the UI. Common rule dimensions include frequency, interval, weekdays/day-of-month, positional rules such as “third Tuesday,” start, end by date/count/never, and an authoritative timezone/wall-clock interpretation. Only expose complexity supported by the scheduling engine.

Summarize the rule in plain, locale-aware language before save: “Every 2 weeks on Tuesday and Thursday until 30 November 2026.” The summary must be generated from the same rule model, not handwritten copy that can drift from controls.

Editing requires scope: this occurrence, this and following, or entire series when the backend supports those semantics. Each option has different consequences for prior exceptions and future overrides. Do not show “all events” if it rewrites historical occurrences. An exception moved to another day remains part of the series unless policy says it becomes detached; expose identity accordingly.

Changing the recurrence rule can conflict with existing occurrence edits, attendees/resources or booked rooms. Preview which exceptions will be retained, migrated or discarded. Deleting one occurrence is not the same as ending the series.

DST behavior depends on temporal intent. A weekly 09:00 local meeting should usually remain at 09:00 local if that is the rule, even when UTC offset changes.

## Failure Topology
- “Monthly” repeats on the 31st and silently skips/changes months without stating rule.
- Editing one occurrence accidentally changes the whole series.
- `This and following` appears although backend only supports all-or-one and simulates it destructively.
- Rule change silently deletes manually moved exceptions.
- Ending the series retroactively removes past history.
- Recurrence stores fixed UTC intervals and shifts local meeting time after DST.

## Falsification and Recovery
Falsify with monthly edge dates, weekday rules, count/date endings, moved/deleted exceptions, one/future/all edits, timezone/DST and resource conflicts. Expand sample occurrences from the rule engine and compare to the UI summary.

Recover by making rule/exception model explicit, generating summaries from authoritative structure, forcing edit-scope choice when ambiguous and previewing exception consequences before rule replacement.

## Output Contract
Return `recurring-event-contract` with recurrence rule schema, localized summary, end conditions, exception identity, occurrence/series edit scopes, rule-change exception policy, timezone semantics, resource conflict handoff and expansion tests.