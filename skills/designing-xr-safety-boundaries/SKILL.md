---
name: designing-xr-safety-boundaries
description: Use when XR experiences must keep users aware of physical play-space limits, nearby obstacles, passthrough safety, reach hazards, seated or room-scale constraints, and emergency exit while virtual content competes for attention.
---

# Designing XR Safety Boundaries

Physical safety outranks immersion. The interface must prevent virtual tasks from encouraging users to walk, reach, lean, or turn beyond a known safe envelope and must degrade conservatively when environment confidence is poor.

## Parent Contract
**Required parent:** `designing-spatial-xr-interfaces`.

The parent owns the XR scene. This skill owns safety-boundary presentation and behavior around real physical constraints; it does not define general locomotion comfort.

## Safety Envelope
Use platform guardian/play-space, seated radius, passthrough/depth information, or product-specific known zones as evidence. Distinguish known-safe, near-boundary, outside-boundary, environment-unknown, and temporarily tracking-lost states. Do not infer safety from the absence of detected geometry.

Virtual content placement must respect the envelope. Avoid placing required controls, rewards, or targets beyond safe reach. If content moves dynamically, re-evaluate safety rather than assuming the initial placement remains valid.

## Boundary Presentation
Escalate boundary cues with proximity and motion intent. Early cues can be subtle; imminent crossing should become unmistakable and should override decorative scene content. Use visual, audio, or haptic channels according to platform capability without making one sense the only safety carrier.

Passthrough can improve awareness but is not a universal guarantee. If camera/depth is unavailable, dark, occluded, or low confidence, fall back to conservative boundary behavior. Emergency exit/recenter/system menu should remain discoverable even when the user is disoriented.

## Reach and Body Motion
Safety includes upper-body reach and turning, not only head position. A user can remain inside a guardian while reaching into furniture. For high-reach interactions, position targets inside a comfortable envelope and provide indirect alternatives.

## Evidence
Test small room, seated mode, boundary approach at different speeds, obstacle near boundary, passthrough loss, tracking loss, required target near edge, long reach, child/short/tall body ranges where product audience warrants, and emergency exit.

## Failure Modes
- UI interprets “no obstacle detected” as “safe.”
- Required object appears outside the guardian.
- Boundary cue is hidden behind world-space UI.
- Passthrough failure leaves the user with no safety indication.
- Haptic-only warning excludes users who cannot perceive it or devices without haptics.
- Game/reward design encourages leaning beyond safe reach.

## Falsification
Place a required interaction just beyond the safe boundary and approach it under degraded environment sensing. Falsify if the system continues to reward/enable unsafe reach or if the boundary cue can be occluded by scene content.

## Recovery
Disable or relocate unsafe targets, elevate boundary cue above scene composition, switch to conservative mode when sensing is uncertain, and expose a safe recenter/exit route. Unknown environment state must never be presented as confirmed safe.

## Handoff
Locomotion behavior uses `designing-xr-locomotion-controls`; physical/world panel placement uses placement owners; origin loss uses `designing-xr-recenter-and-origin-recovery`.

## Output Contract
Return an `xr-safety-boundaries-contract` with `safety_states[]`, `evidence_sources[]`, `placement_constraints`, `proximity_escalation`, `multisensory_cues`, `passthrough_fallback`, `reach_envelope`, `emergency_routes`, `evidence_cases[]`, `falsification_cases[]`, and `recovery_actions[]`.