---
name: designing-xr-near-far-interaction-transitions
description: Use when XR interaction changes between direct near-field manipulation and distant targeting and the system must preserve target ownership, affordance, scale, and intent across the transition without competing with general gaze-hand input rules.
---

# Designing XR Near Far Interaction Transitions

Near and far interaction are different motor contracts. A hand that can directly grab a nearby object may need a projected ray for the same object at distance. The transition between those modes is itself an interaction state that can cause accidental retargeting or sudden geometry changes.

## Parent Contract
**Required parent:** `designing-spatial-xr-interfaces`.

The parent owns XR spatial composition. This skill owns mode-transition boundaries between direct manipulation and distant targeting; existing gaze/hand owner remains authoritative for general intent confirmation.

## Mode Boundary
Define near-field entry/exit using spatial proximity, reachability, tracking confidence, object affordance, and platform conventions. Avoid one hard distance threshold that chatters when a hand moves around the boundary. Use hysteresis or explicit interaction capture so mode does not flip repeatedly during a gesture.

Near mode may expose handles, collision/proximity affordances, or direct grab states that are inappropriate at distance. Far mode may use rays, enlarged angular targets, or indirect manipulation. Transition visuals should communicate the same object identity while adapting affordance, not replace it with a different unlabeled control.

## Target Ownership
If far targeting has already committed to an object and the hand moves near, decide whether the current operation continues under captured ownership or requires release/reacquire. A drag should not unexpectedly jump from far-ray movement to physical collision semantics halfway through unless the product intentionally supports that blend.

Two hands complicate mode. One hand may be near while the other uses a far ray. Establish arbitration so the same object is not simultaneously owned by incompatible manipulation modes.

## Comfort and Reach
Near interaction can cause users to lean or raise arms; far interaction can reduce effort but sacrifice precision. Transition policy should prefer a comfortable reachable envelope and provide indirect fallback for users with limited reach or mobility.

## Evidence
Test slow boundary crossing, rapid hand motion, object moving toward/away from user, tracking noise, one-hand/two-hand interaction, seated reach, limited reach, and a gesture that begins far and ends near. Record mode changes and object ownership.

## Failure Modes
- Mode flips repeatedly around one distance threshold.
- Near affordances appear before the object is actually reachable.
- Far ray releases target when the hand enters near range mid-drag.
- Two hands acquire incompatible control of the same object.
- Transition changes object scale/identity so users think it is a new element.
- Users must physically lean because far fallback disappears too early.

## Falsification
Move a target slowly through the near/far boundary while dragging it with noisy hand tracking. Falsify if ownership changes without user intent, mode chatters, or the object becomes temporarily uncontrollable.

## Recovery
Add transition hysteresis, preserve captured target, separate affordance transition from ownership transition, and retain an accessible indirect path. If hand tracking confidence drops, fall back to the safer interaction mode rather than oscillating.

## Handoff
Far hit testing uses `designing-ray-pointer-interaction`; direct hand semantics remain governed by `designing-gaze-hand-spatial-input`; distance presentation coordinates with `designing-spatial-ui-distance-scaling`.

## Output Contract
Return an `xr-near-far-interaction-transitions-contract` with `near_far_states`, `entry_exit_conditions`, `hysteresis_policy`, `affordance_changes`, `target_capture_rules`, `two_hand_arbitration`, `accessibility_fallbacks`, `evidence_cases[]`, `falsification_cases[]`, and `recovery_actions[]`.