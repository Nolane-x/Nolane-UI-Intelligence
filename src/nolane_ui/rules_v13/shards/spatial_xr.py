"""V13 sixth-wave rules; all operational prose is independently authored."""
from __future__ import annotations

SPATIAL_XR_RULES_V13 = [{'rule_id': 'ui.spatial.recenter-preserves-world-target-meaning',
  'domain': 'spatial',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Recenter operations must preserve the semantic identity of world-anchored targets',
  'statement': 'When a user recenters or resets the XR origin, world-anchored content must either remain attached to '
               'its intended physical or logical target or clearly transition to a new coordinate basis.',
  'intent': 'Prevent origin recovery from silently moving content in a way that changes what object, place, or task '
            'step the content represents.',
  'applies_when': ['A spatial interface supports recentering, origin reset, guardian reset, seated/standing '
                   'transition, or coordinate-origin recovery while anchored content is present.'],
  'does_not_apply_when': [],
  'failure_modes': ['After recentering, a previously anchored annotation or control appears attached to a different '
                    'real-world target without any explicit re-anchoring decision.'],
  'user_impacts': ['Users can act on the wrong physical location or misinterpret spatial guidance because coordinate '
                   'recovery altered semantic attachment.'],
  'observables': ['Place anchors relative to known targets, perform each supported recenter path, and compare anchor '
                  'identifiers, transforms, and rendered target association.'],
  'falsifiers': ['Recenter changes the user reference frame without changing anchor meaning, or any required '
                 're-anchoring is explicit and reviewable before use resumes.'],
  'repairs': ['Separate user-origin transforms from persistent anchor identity and recalculate presentation from the '
              'new origin rather than rewriting target attachment implicitly.'],
  'exceptions': [],
  'verification': ['Exercise recenter, session resume, boundary reset, seated-to-standing transition, and tracking '
                   'recovery while confirming anchored content still refers to the same target.'],
  'owner_hints': ['designing-xr-recenter-and-origin-recovery'],
  'verifier_hints': ['critiquing-functional-completeness'],
  'capabilities': {'static': 'PARTIAL',
                   'dom': 'PARTIAL',
                   'computed-style': 'PARTIAL',
                   'browser-runtime': 'PARTIAL',
                   'interaction': 'REQUIRED',
                   'accessibility-tree': 'PARTIAL',
                   'visual-render': 'PARTIAL',
                   'semantic-product': 'REQUIRED',
                   'cross-generation': 'UNSUPPORTED',
                   'human-review': 'PARTIAL'},
  'provenance_ids': ['nui-spatial-xr-owners-v13'],
  'status': 'active'},
 {'rule_id': 'ui.spatial.safety-boundary-never-obscured',
  'domain': 'spatial',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Spatial safety boundaries must not be obscured by immersive application content',
  'statement': 'When the platform exposes a physical safety boundary, collision warning, or guardian cue, '
               'application overlays and effects must not intentionally hide or visually overpower it during '
               'locomotion or active interaction.',
  'intent': 'Preserve awareness of real-world movement limits when immersive content competes for the same field of '
            'view.',
  'applies_when': ['The experience operates in immersive or mixed reality where users can physically move and the '
                   'platform provides boundary or obstacle warnings.'],
  'does_not_apply_when': [],
  'failure_modes': ['A full-screen effect, modal, scene element, or custom overlay covers the platform safety cue or '
                    'leaves it too visually weak to notice during movement.'],
  'user_impacts': ['Users can collide with walls, furniture, people, or unsafe areas because application rendering '
                   'suppressed the available boundary signal.'],
  'observables': ['Approach the configured safety boundary during representative scenes and overlays while '
                  'inspecting whether the platform warning remains visible and perceivable.'],
  'falsifiers': ['Boundary cues remain perceivable above application content or the platform retains final '
                 'compositing authority that the application cannot suppress.'],
  'repairs': ['Reserve visual and interaction priority for platform safety layers and avoid effects or overlays that '
              'compete with the boundary in critical zones.'],
  'exceptions': [],
  'verification': ['Test high-contrast scenes, dialogs, dark environments, bright effects, and locomotion states '
                   'near the boundary and confirm safety cues remain perceivable.'],
  'owner_hints': ['designing-xr-safety-boundaries'],
  'verifier_hints': ['critiquing-human-factors-and-safety'],
  'capabilities': {'static': 'PARTIAL',
                   'dom': 'PARTIAL',
                   'computed-style': 'PARTIAL',
                   'browser-runtime': 'PARTIAL',
                   'interaction': 'REQUIRED',
                   'accessibility-tree': 'PARTIAL',
                   'visual-render': 'PARTIAL',
                   'semantic-product': 'REQUIRED',
                   'cross-generation': 'UNSUPPORTED',
                   'human-review': 'PARTIAL'},
  'provenance_ids': ['nui-spatial-xr-owners-v13'],
  'status': 'active'},
 {'rule_id': 'ui.spatial.anchor-loss-state-visible',
  'domain': 'spatial',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Loss of spatial anchor tracking must become a visible state rather than silent drift',
  'statement': 'If an anchor can no longer be localized reliably, content bound to that anchor must expose '
               'uncertainty, hide, freeze safely, or request recovery instead of continuing to drift as though the '
               'anchor remained authoritative.',
  'intent': 'Keep spatial content truth tied to actual tracking confidence when relocalization, mapping, or anchor '
            'services fail.',
  'applies_when': ['The interface relies on persistent or session anchors whose pose can become unavailable, '
                   'low-confidence, or invalid after occlusion, relaunch, or tracking loss.'],
  'does_not_apply_when': [],
  'failure_modes': ['Anchored content keeps moving with a stale or inferred pose while the system knows the anchor '
                    'is unresolved.'],
  'user_impacts': ['Users can treat visually precise content as physically accurate when the product no longer knows '
                   'where the referenced target is.'],
  'observables': ['Force anchor loss or failed relocalization and compare tracking state, confidence, rendered pose, '
                  'and any recovery affordance.'],
  'falsifiers': ['Unresolved anchors are represented as unavailable or uncertain and content becomes authoritative '
                 'again only after successful relocalization.'],
  'repairs': ['Propagate anchor tracking state into presentation and gate position-dependent actions until the '
              'anchor returns to a supported confidence state.'],
  'exceptions': [],
  'verification': ['Test occlusion, mapping reset, session restart, relocalization failure, and delayed recovery and '
                   'confirm anchored content never silently drifts through unknown state.'],
  'owner_hints': ['designing-spatial-anchor-persistence'],
  'verifier_hints': ['critiquing-functional-completeness'],
  'capabilities': {'static': 'PARTIAL',
                   'dom': 'PARTIAL',
                   'computed-style': 'PARTIAL',
                   'browser-runtime': 'PARTIAL',
                   'interaction': 'REQUIRED',
                   'accessibility-tree': 'PARTIAL',
                   'visual-render': 'PARTIAL',
                   'semantic-product': 'REQUIRED',
                   'cross-generation': 'UNSUPPORTED',
                   'human-review': 'PARTIAL'},
  'provenance_ids': ['nui-spatial-xr-owners-v13'],
  'status': 'active'},
 {'rule_id': 'ui.spatial.near-far-transfer-preserves-target',
  'domain': 'spatial',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Near-to-far interaction transfer must preserve the intended target across modality changes',
  'statement': 'When users transition from direct hand interaction to ray, gaze, controller, or other far '
               'interaction, the selected or grabbed object must not silently change because the targeting model '
               'switched.',
  'intent': 'Maintain task continuity when spatial distance or posture causes the interaction technique to change '
            'mid-action.',
  'applies_when': ['The experience supports both near direct manipulation and far pointing or selection for the same '
                   'set of spatial objects.'],
  'does_not_apply_when': [],
  'failure_modes': ['Crossing the near/far threshold retargets an in-progress selection, drag, or manipulation to a '
                    'neighboring object without explicit user intent.'],
  'user_impacts': ['Users can move, activate, or edit the wrong spatial object as the system changes input technique '
                   'underneath them.'],
  'observables': ['Begin interactions near the modality threshold, move across it while targets overlap, and trace '
                  'stable target identity through the handoff.'],
  'falsifiers': ['The active target remains bound to stable object identity for the duration of the gesture or the '
                 'current gesture ends before a new target can be acquired.'],
  'repairs': ['Separate target identity from the pointer technique and preserve capture until the gesture commits or '
              'cancels.'],
  'exceptions': [],
  'verification': ['Exercise grabs, selections, sliders, and object moves across near/far transitions with '
                   'overlapping targets and confirm no unintended retargeting.'],
  'owner_hints': ['designing-xr-near-far-interaction-transitions'],
  'verifier_hints': ['critiquing-input-modality'],
  'capabilities': {'static': 'PARTIAL',
                   'dom': 'PARTIAL',
                   'computed-style': 'PARTIAL',
                   'browser-runtime': 'PARTIAL',
                   'interaction': 'REQUIRED',
                   'accessibility-tree': 'PARTIAL',
                   'visual-render': 'PARTIAL',
                   'semantic-product': 'REQUIRED',
                   'cross-generation': 'UNSUPPORTED',
                   'human-review': 'PARTIAL'},
  'provenance_ids': ['nui-spatial-xr-owners-v13'],
  'status': 'active'},
 {'rule_id': 'ui.spatial.dom-overlay-input-ownership-explicit',
  'domain': 'spatial',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'XR DOM overlays must have explicit input ownership where spatial and screen controls overlap',
  'statement': 'When conventional DOM overlays coexist with immersive spatial input, hit testing and focus ownership '
               'must prevent one gesture from activating both the overlay and the world content behind it.',
  'intent': 'Avoid double activation and focus ambiguity at the boundary between browser-like controls and immersive '
            'scene interaction.',
  'applies_when': ['An immersive session renders interactive HTML or equivalent 2D overlay content in front of '
                   'spatial objects that also receive gaze, hand, ray, or controller input.'],
  'does_not_apply_when': [],
  'failure_modes': ['Selecting an overlay button also activates a world object behind it, or focus moves '
                    'unpredictably between overlay and scene because input ownership is undefined.'],
  'user_impacts': ['Users can trigger hidden spatial side effects while believing they interacted only with the '
                   'visible overlay.'],
  'observables': ['Place interactive scene targets behind overlay controls and exercise pointer, ray, gaze, and '
                  'keyboard focus while logging both event paths.'],
  'falsifiers': ['The active interaction layer consumes or transfers input according to a documented ownership model '
                 'and one user action maps to one intended target.'],
  'repairs': ['Implement explicit overlay hit-test priority, focus transfer, and event cancellation boundaries '
              'between DOM and immersive scene input systems.'],
  'exceptions': [],
  'verification': ['Test overlapping targets, overlay open/close transitions, keyboard focus, controller rays, and '
                   'gaze activation and confirm no gesture crosses layers unintentionally.'],
  'owner_hints': ['designing-xr-dom-overlay-coordination'],
  'verifier_hints': ['critiquing-input-modality'],
  'capabilities': {'static': 'PARTIAL',
                   'dom': 'PARTIAL',
                   'computed-style': 'PARTIAL',
                   'browser-runtime': 'PARTIAL',
                   'interaction': 'REQUIRED',
                   'accessibility-tree': 'PARTIAL',
                   'visual-render': 'PARTIAL',
                   'semantic-product': 'REQUIRED',
                   'cross-generation': 'UNSUPPORTED',
                   'human-review': 'PARTIAL'},
  'provenance_ids': ['nui-spatial-xr-owners-v13'],
  'status': 'active'},
 {'rule_id': 'ui.spatial.locomotion-mode-disclosed-before-motion',
  'domain': 'spatial',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Spatial locomotion mode must be clear before a movement command changes the viewpoint',
  'statement': 'Before activating teleport, smooth locomotion, snap turn, continuous turn, dash, or vehicle '
               'movement, users must be able to understand which movement mode is active when modes differ '
               'materially in motion and comfort.',
  'intent': 'Reduce disorientation and motion-sickness risk by making viewpoint movement predictable before it '
            'happens.',
  'applies_when': ['The experience supports multiple locomotion or turning modes or can change movement behavior '
                   'through settings, context, comfort profiles, or device capabilities.'],
  'does_not_apply_when': [],
  'failure_modes': ['The same input suddenly performs a different movement style because mode changed without a '
                    'visible or learnable indication.'],
  'user_impacts': ['Users can experience unexpected acceleration, rotation, displacement, or loss of spatial '
                   'orientation.'],
  'observables': ['Switch locomotion modes through settings and contextual transitions, then inspect active mode '
                  'cues before issuing movement input.'],
  'falsifiers': ['The active mode is stable and discoverable before use, and any automatic mode change is surfaced '
                 'before the next motion command.'],
  'repairs': ['Represent locomotion mode as explicit session state and expose it through control affordances or '
              'persistent comfort settings rather than hidden context.'],
  'exceptions': [],
  'verification': ['Exercise every locomotion mode, automatic fallback, device change, and session resume and '
                   'confirm users can predict the next viewpoint movement.'],
  'owner_hints': ['designing-xr-locomotion-controls'],
  'verifier_hints': ['critiquing-human-factors-and-safety'],
  'capabilities': {'static': 'PARTIAL',
                   'dom': 'PARTIAL',
                   'computed-style': 'PARTIAL',
                   'browser-runtime': 'PARTIAL',
                   'interaction': 'REQUIRED',
                   'accessibility-tree': 'PARTIAL',
                   'visual-render': 'PARTIAL',
                   'semantic-product': 'REQUIRED',
                   'cross-generation': 'UNSUPPORTED',
                   'human-review': 'PARTIAL'},
  'provenance_ids': ['nui-spatial-xr-owners-v13'],
  'status': 'active'},
 {'rule_id': 'ui.spatial.gaze-hand-ambiguity-requires-confirmation',
  'domain': 'spatial',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Ambiguous gaze and hand combinations must not commit high-consequence targets without disambiguation',
  'statement': 'When gaze suggests one target while hand pose, pinch, controller ray, or gesture geometry could '
               'plausibly indicate another, consequential actions must use an explicit target confirmation or stable '
               'acquisition model.',
  'intent': 'Prevent multimodal inference from inventing user intent when two input channels disagree about the '
            'target.',
  'applies_when': ['The spatial interaction model fuses gaze with hand, controller, voice, or gesture signals for '
                   'target selection or activation.'],
  'does_not_apply_when': [],
  'failure_modes': ['A destructive or consequential action commits to whichever target the fusion heuristic chose '
                    'even though gaze and gesture evidence pointed at different objects.'],
  'user_impacts': ['Users can delete, move, purchase, send, or control the wrong spatial object because the '
                   'interface hid target ambiguity.'],
  'observables': ['Create overlapping or closely spaced targets and deliberately diverge gaze from hand/ray '
                  'direction while invoking consequential actions.'],
  'falsifiers': ['The system has a stable acquisition rule users can perceive, or ambiguous high-consequence actions '
                 'pause for target confirmation before commit.'],
  'repairs': ['Expose acquired target feedback and require stronger multimodal agreement or confirmation when target '
              'confidence is insufficient for the action consequence.'],
  'exceptions': [],
  'verification': ['Test near-overlap, occlusion, moving targets, gaze drift, and hand jitter and confirm ambiguous '
                   'input never silently commits the wrong consequential target.'],
  'owner_hints': ['designing-gaze-hand-spatial-input'],
  'verifier_hints': ['critiquing-human-factors-and-safety'],
  'capabilities': {'static': 'PARTIAL',
                   'dom': 'PARTIAL',
                   'computed-style': 'PARTIAL',
                   'browser-runtime': 'PARTIAL',
                   'interaction': 'REQUIRED',
                   'accessibility-tree': 'PARTIAL',
                   'visual-render': 'PARTIAL',
                   'semantic-product': 'REQUIRED',
                   'cross-generation': 'UNSUPPORTED',
                   'human-review': 'PARTIAL'},
  'provenance_ids': ['nui-spatial-xr-owners-v13'],
  'status': 'active'},
 {'rule_id': 'ui.spatial.distance-scaling-preserves-legibility',
  'domain': 'spatial',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Spatial UI distance scaling must preserve readable text and targetability across supported depth',
  'statement': 'Controls and text that move through depth or attach to objects at varying distance must adapt size, '
               'layout, or placement so essential information and interaction targets remain usable throughout the '
               'supported range.',
  'intent': 'Prevent physically correct perspective scaling from making necessary UI unreadable or untargetable as '
            'content moves farther away.',
  'applies_when': ['A spatial interface places essential labels or controls on objects whose distance from the user '
                   'can vary materially during normal use.'],
  'does_not_apply_when': [],
  'failure_modes': ['A control remains technically present but becomes too small to read or acquire at an intended '
                    'working distance while the product still expects interaction.'],
  'user_impacts': ['Users can lose access to essential actions or misread labels solely because the spatial layout '
                   'allowed a supported target to recede beyond usable scale.'],
  'observables': ['Move representative UI-bearing objects across supported depth and measure apparent text size, '
                  'target acquisition, occlusion, and adaptive layout behavior.'],
  'falsifiers': ['Essential controls remain legible and targetable through adaptive scaling, billboarding, '
                 'relocation, zoom, or an alternate near-detail surface.'],
  'repairs': ['Define distance-aware presentation rules and switch to appropriate detail or scale treatments instead '
              'of applying raw world-scale uniformly.'],
  'exceptions': [],
  'verification': ['Test the near, nominal, and far supported distances with text expansion and multiple '
                   'field-of-view devices and confirm essential UI remains usable.'],
  'owner_hints': ['designing-spatial-ui-distance-scaling'],
  'verifier_hints': ['critiquing-accessibility'],
  'capabilities': {'static': 'PARTIAL',
                   'dom': 'PARTIAL',
                   'computed-style': 'PARTIAL',
                   'browser-runtime': 'PARTIAL',
                   'interaction': 'REQUIRED',
                   'accessibility-tree': 'PARTIAL',
                   'visual-render': 'PARTIAL',
                   'semantic-product': 'REQUIRED',
                   'cross-generation': 'UNSUPPORTED',
                   'human-review': 'PARTIAL'},
  'provenance_ids': ['nui-spatial-xr-owners-v13'],
  'status': 'active'}]

__all__ = ["SPATIAL_XR_RULES_V13"]
