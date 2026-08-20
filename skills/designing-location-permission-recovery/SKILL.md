---
name: designing-location-permission-recovery
description: Use when location is needed after a user denies, revokes, limits, or approximates permission and the product must explain degraded capability and route recovery to the correct OS/browser layer.
---

# Designing Location Permission Recovery

## Parent Contract
**Required parent:** `designing-device-integration-interfaces`.

This faculty owns recovery after location authorization is not in the expected state. It does not own the initial permission-onboarding rationale generally. It distinguishes denied, permanently denied, approximate-only, while-in-use, background restricted, service disabled, and unavailable fixes.

## Decision Boundary
Map each platform authorization state to what the current feature can still do. Approximate location may be sufficient for city-level discovery but not turn-by-turn navigation. Do not reprompt when the platform will no longer show a prompt; provide settings instructions/deep link where supported. Explain the feature consequence without coercive language or blocking unrelated product areas.

If device location services are globally disabled, app permission alone cannot recover. If browser/site permission differs from OS service state, tell users which layer to inspect. Provide manual location/search alternatives where task semantics allow them. Recovery should re-check state after users return from settings rather than requiring app restart.

## Failure Topology
- Denied permission triggers the same request prompt on every visit until users quit.
- UI says “Enable location” when OS location services are off but app permission is already granted.
- Approximate permission is treated as complete failure though the task needs only city accuracy.
- Settings instructions are copied from another platform/version and lead nowhere.
- Feature is completely blocked even though manual address entry would work.
- Returning from settings leaves stale Denied state until a full reload.

## Falsification and Recovery
Test first denial, permanent denial, approximate/precise changes, service disabled, browser versus OS permission, background restriction, settings return, and manual fallback. The design fails if it asks users to perform an action that cannot change the current authorization state.

Recover by mapping platform states precisely, limiting prompts, routing to correct settings layer, degrading to approximate/manual paths where valid, and re-observing permission after resume. Keep rationale factual and proportional to feature value.

## Output Contract
Return `location-permission-recovery-contract` with authorization-state matrix, feature degradation, reprompt eligibility, settings recovery, service-state distinction, manual fallback, resume recheck, and permission recovery verification cases.
