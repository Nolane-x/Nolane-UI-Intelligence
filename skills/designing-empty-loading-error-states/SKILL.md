---
name: designing-empty-loading-error-states
description: Use when a UI can have no content, pending content, partial results, stale data, permission limits, unavailable services, validation failure, or recoverable and unrecoverable errors.
---

# Designing Empty, Loading, and Error States

## Overview
Resilience states are part of the product truth, not afterthought illustrations. They must preserve orientation and tell users what is known, unknown, and actionable.

## Parent Contract
**Required parent:** `routing-ui-work`.

Use product lifecycle, task flow, async states, permissions, and interface-copy rules.

## Empty-state taxonomy
Distinguish:
- first-use/no objects created
- legitimately empty after completion/archive
- filtered/search zero results
- no permission/hidden content
- data unavailable/not yet synchronized
- error masquerading as empty

These states require different copy/actions. Never show “Create your first project” when the user actually has projects hidden by a filter.

## Loading
Choose feedback by expected latency and context:
- immediate local optimistic/pressed state
- compact progress indicator for bounded region
- skeleton only when the future geometry is known enough that it reduces layout shift and helps orientation
- progress when meaningful progress exists
- background status for long jobs

Do not blank the whole screen if existing content remains valid while a small region refreshes.

## Skeleton discipline
Skeletons should approximate real structure, not decorative gray art. Avoid skeleton controls that appear interactive. For fast loads, a skeleton flash can be worse than no transition.

## Partial/stale data
Expose which parts are current, stale, failed, or still loading when the distinction changes decisions. A dashboard where one metric failed should not necessarily become a full-page error.

## Errors
Classify:
- field/local validation
- action failure
- partial batch failure
- authorization
- connectivity/timeout
- server/system unavailable
- not found/deleted
- conflict/stale data

For each state preserve unaffected work and provide a real recovery path: retry, edit, refresh, request permission, choose another object, inspect details, or contact support only when support is genuinely the next step.

## Unknown outcome
Network failure after commit can mean the effect succeeded but acknowledgement was lost. Do not say “failed” if state is unknown. Provide reconciliation/read-back before offering a potentially duplicate retry.

## Visual treatment
Severity should influence prominence. Do not use giant red full-page treatments for minor inline failures, or subtle gray text for a blocking error. Error styling must coexist with focus, selection, and validation cues.

## Output: `resilience-state-contract`
Return `empty_taxonomy`, `loading_strategy`, `partial_state`, `stale_state`, `error_taxonomy`, `unknown_outcome_policy`, `recovery_actions`, `copy_requirements`, `visual_severity`, and `verification_cases`.
