---
name: designing-xr-locomotion-controls
description: Use when XR users navigate virtual space through teleport, smooth movement, snap or smooth turn, climbing, vehicle-like movement, or room-scale repositioning and the interface must balance intent, orientation, comfort, reachability, and recovery.
---

# Designing XR Locomotion Controls

Locomotion changes the user's spatial frame and can induce discomfort or disorientation. It is not equivalent to scrolling a camera. The interface must provide intentional movement, orientation cues, comfort alternatives, and clear invalid-destination feedback.

## Parent Contract
**Required parent:** `designing-spatial-xr-interfaces`.

The parent owns spatial XR experience. This skill owns virtual locomotion control and comfort; physical safety boundaries are governed separately by `designing-xr-safety-boundaries`.

## Locomotion Modes
Declare supported movement modes and their semantics: room-scale physical movement, teleport, smooth translation, snap turn, smooth turn, dash, climb, seated movement, or vehicle control. Users may need independent settings for translation and rotation. Avoid one comfort preset that hides which mechanisms change.

Teleport should show destination validity, landing orientation, floor height, collision, and accessibility constraints before commit. Smooth movement should expose direction basis—head, hand/controller, body, or vehicle—and keep that basis stable enough to predict motion.

## Comfort Envelope
Control acceleration, velocity, turn rate, vignette/tunneling, horizon stability, and field-of-view effects according to platform guidance and user preference. Reduced-motion needs are not solved merely by slowing animations; virtual camera motion itself may be the trigger. Provide a low-motion locomotion path when the product permits it.

## Orientation and Recovery
After teleport or large movement, preserve orientation to important task objects or make reorientation obvious. Avoid spawning users inside geometry, at unsafe heights, or facing away from essential controls. Provide a recentre/return option for disorientation and a known safe location for unrecoverable navigation states.

## Interaction During Motion
Decide whether menus, grabs, rays, and ongoing tasks persist through locomotion. High-precision manipulation may need motion to pause or target capture to remain stable. Prevent accidental teleport from competing with object selection on the same gesture without clear mode separation.

## Evidence
Test seated/standing, left/right-handed controls, teleport invalid surfaces, slopes/stairs, smooth movement at different rates, snap/smooth turn, low-motion settings, interaction while moving, tracking loss, and return to origin. Include longer sessions to expose discomfort.

## Failure Modes
- Teleport indicator marks unreachable or colliding destination as valid.
- Smooth movement direction basis changes unexpectedly.
- User exits locomotion facing away from the active task with no orientation cue.
- Reduced-motion mode still forces continuous camera translation.
- Teleport and object select compete on one ambiguous gesture.
- Recenter after locomotion moves anchored world content incorrectly.

## Falsification
Have users perform the same navigation route with teleport and smooth movement while interacting with objects at stops. Falsify if locomotion creates accidental selection, unsafe placement, or a comfort option that does not materially reduce virtual motion.

## Recovery
Disable invalid movement, move to a known safe pose, restore orientation cues, separate gesture modes, and offer a lower-motion alternative. If spatial collision or floor evidence is uncertain, block destination rather than guessing.

## Handoff
Physical guardian/safety uses `designing-xr-safety-boundaries`; origin repair uses `designing-xr-recenter-and-origin-recovery`; near/far interaction transitions coordinate with locomotion interruptions.

## Output Contract
Return an `xr-locomotion-controls-contract` with `locomotion_modes[]`, `direction_basis`, `destination_validation`, `comfort_parameters`, `low_motion_path`, `post_move_orientation`, `interaction_during_motion`, `safe_recovery_pose`, `evidence_cases[]`, and `recovery_actions[]`.