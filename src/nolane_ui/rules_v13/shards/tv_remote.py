"""V13 sixth-wave rules; all operational prose is independently authored."""
from __future__ import annotations

TV_REMOTE_RULES_V13 = [{'rule_id': 'ui.tv.focus-visible-at-viewing-distance',
  'domain': 'tv',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'TV focus indicators must remain unambiguous at normal viewing distance',
  'statement': 'A ten-foot interface controlled by directional focus must make the currently actionable element '
               'obvious without relying on subtle border, color, or shadow changes that disappear at viewing '
               'distance.',
  'intent': 'Keep remote-control navigation legible from the couch where pointer hover and close-up visual '
            'inspection are unavailable.',
  'applies_when': ['The primary input model is a TV remote, gamepad, or directional controller and users interact '
                   'from several feet or meters away.'],
  'does_not_apply_when': [],
  'failure_modes': ['The focused item differs from neighboring items only by a low-salience treatment that users '
                    'cannot reliably perceive at intended distance.'],
  'user_impacts': ['Users can activate the wrong item, lose orientation, or repeatedly move focus because they '
                   'cannot tell where navigation currently is.'],
  'observables': ['Navigate the interface from the product’s intended viewing distance across bright, dark, moving, '
                  'and dense backgrounds and inspect focus salience.'],
  'falsifiers': ['Focus remains visually and semantically distinct throughout navigation without requiring users to '
                 'infer position from previous key presses.'],
  'repairs': ['Use size, outline, elevation, motion, contrast, or other sufficiently salient focus treatment '
              'designed for the viewing distance and content background.'],
  'exceptions': [],
  'verification': ['Test representative displays, viewing distances, themes, and motion states and confirm every '
                   'reachable control has a consistently perceivable focus indicator.'],
  'owner_hints': ['designing-tv-ten-foot-interfaces'],
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
  'provenance_ids': ['nui-tv-remote-owners-v13'],
  'status': 'active'},
 {'rule_id': 'ui.tv.directional-navigation-no-focus-trap',
  'domain': 'tv',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Directional navigation graphs must not trap focus inside reachable TV regions',
  'statement': 'Every remote-navigable region must provide a predictable directional path to leave or return unless '
               'it is an intentional modal boundary with an explicit close or back action.',
  'intent': 'Prevent users from becoming stuck when focus movement depends on spatial graph relationships rather '
            'than tab order or pointer targeting.',
  'applies_when': ['Controls are navigated primarily with up, down, left, and right focus movement across rows, '
                   'grids, rails, dialogs, or overlays.'],
  'does_not_apply_when': [],
  'failure_modes': ['A reachable item has no directional route back to surrounding navigation even though the '
                    'surface is not intentionally modal.'],
  'user_impacts': ['Users can be forced to restart the screen or application because remote focus cannot escape the '
                   'region they entered.'],
  'observables': ['Traverse every reachable focus node and compute or exercise directional paths to major navigation '
                  'anchors and dismissal actions.'],
  'falsifiers': ['All non-modal nodes have a predictable escape path and modal regions expose a reliable close or '
                 'back route.'],
  'repairs': ['Model directional focus as an explicit graph and test connectivity instead of relying entirely on '
              'geometric nearest-neighbor heuristics.'],
  'exceptions': [],
  'verification': ['Run exhaustive remote navigation through grids, carousels, empty states, overlays, and edge '
                   'items and confirm no non-modal focus trap occurs.'],
  'owner_hints': ['designing-directional-focus-graphs'],
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
  'provenance_ids': ['nui-tv-remote-owners-v13'],
  'status': 'active'},
 {'rule_id': 'ui.tv.back-action-follows-navigation-hierarchy',
  'domain': 'tv',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Remote Back actions must unwind the active navigation hierarchy before exiting the task',
  'statement': 'The Back or equivalent remote action should dismiss the topmost transient layer or return to the '
               'prior meaningful screen before exiting the application or abandoning a deeper task state.',
  'intent': 'Match the strong hierarchical expectation of remote navigation where a single Back control substitutes '
            'for many pointer-visible close controls.',
  'applies_when': ['The TV interface uses a hardware or software Back action across nested screens, overlays, menus, '
                   'playback chrome, and modal states.'],
  'does_not_apply_when': [],
  'failure_modes': ['Pressing Back from an overlay or nested detail unexpectedly exits the application, discards the '
                    'task, or jumps to an unrelated root state.'],
  'user_impacts': ['Users can lose context or work because the primary recovery key does not reflect visible '
                   'navigation depth.'],
  'observables': ['Enter nested screens and overlays in varied orders, invoke Back once at each depth, and compare '
                  'the result with the visible topmost navigation layer.'],
  'falsifiers': ['Back predictably unwinds the active hierarchy or a deliberately exceptional action is clearly '
                 'communicated before abandoning state.'],
  'repairs': ['Maintain explicit navigation-layer state and route Back through the topmost dismissible context '
              'rather than a global exit handler.'],
  'exceptions': [],
  'verification': ['Exercise Back through search, details, playback controls, dialogs, side panels, and root screens '
                   'and confirm each step preserves expected hierarchy.'],
  'owner_hints': ['designing-remote-control-navigation'],
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
  'provenance_ids': ['nui-tv-remote-owners-v13'],
  'status': 'active'},
 {'rule_id': 'ui.tv.long-press-distinct-from-press',
  'domain': 'tv',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Remote long-press actions must not accidentally fire the short-press action first',
  'statement': 'When short press and long press on the same remote control have different meanings, the interaction '
               'must delay or reconcile dispatch so the long-press gesture does not also commit the short action.',
  'intent': 'Prevent one physical gesture from causing two commands when the input system emits down, repeat, and up '
            'events over time.',
  'applies_when': ['A remote or gamepad control maps short and long press to distinct commands such as open versus '
                   'options, skip versus seek, or select versus reorder.'],
  'does_not_apply_when': [],
  'failure_modes': ['Holding the key first executes the short-press action and then the long-press action, producing '
                    'an unintended compound result.'],
  'user_impacts': ['Users can navigate away, activate content, or mutate state before the intended long-press '
                   'command is recognized.'],
  'observables': ['Hold each dual-mapped key through the long-press threshold and record command dispatch timing and '
                  'side effects.'],
  'falsifiers': ['Exactly one semantic command commits for each completed gesture, with cancellation behavior '
                 'defined if the threshold is not reached.'],
  'repairs': ['Implement gesture arbitration around press duration rather than attaching independent side effects to '
              'key-down and repeat events.'],
  'exceptions': [],
  'verification': ['Test short, borderline, long, repeated, and released-outside timing cases on supported remote '
                   'hardware and confirm one command per gesture.'],
  'owner_hints': ['designing-remote-control-navigation'],
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
  'provenance_ids': ['nui-tv-remote-owners-v13'],
  'status': 'active'},
 {'rule_id': 'ui.tv.remote-disconnect-recovery-visible',
  'domain': 'tv',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Remote or controller disconnection must provide a visible recovery path without losing task state',
  'statement': 'When the active remote, controller, or input device disconnects, the interface should preserve the '
               'current task and expose how to reconnect or switch input rather than appearing frozen.',
  'intent': 'Make loss of the primary input channel diagnosable on a display where users may have no pointer or '
            'touch fallback.',
  'applies_when': ['The TV or large-screen experience depends on an external remote, gamepad, keyboard, or paired '
                   'controller that can disconnect at runtime.'],
  'does_not_apply_when': [],
  'failure_modes': ['Input stops responding with no visible indication that the controller disconnected and no '
                    'accessible route to pairing or alternate input.'],
  'user_impacts': ['Users can interpret the application as crashed and lose their current task while attempting to '
                   'recover control.'],
  'observables': ['Disconnect the active controller during navigation, text input, playback, and modal states and '
                  'inspect recovery messaging and task persistence.'],
  'falsifiers': ['The current task remains intact and the display communicates a reconnection or alternate-input '
                 'path appropriate to the platform.'],
  'repairs': ['Listen for controller connectivity state and overlay bounded recovery guidance without resetting '
              'navigation or application state.'],
  'exceptions': [],
  'verification': ['Exercise battery loss, Bluetooth disconnect, controller sleep, and replacement pairing and '
                   'confirm task state survives each recovery.'],
  'owner_hints': ['designing-remote-control-navigation'],
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
  'provenance_ids': ['nui-tv-remote-owners-v13'],
  'status': 'active'},
 {'rule_id': 'ui.tv.critical-controls-within-safe-area',
  'domain': 'tv',
  'class': 'behavioral',
  'severity': 'moderate',
  'enforcement': 'warn',
  'title': 'Critical TV controls must remain inside supported display safe areas',
  'statement': 'Essential navigation, confirmation, playback, and recovery controls must not rely on pixels near '
               'overscanned or platform-reserved edges where some televisions can crop or obscure them.',
  'intent': 'Preserve operability across real displays whose visible bounds differ from nominal framebuffer '
            'dimensions.',
  'applies_when': ['The interface targets televisions or display environments that may apply overscan, safe-area '
                   'insets, platform chrome, or device-specific edge cropping.'],
  'does_not_apply_when': [],
  'failure_modes': ['A critical focused action or status is positioned so close to the edge that supported display '
                    'configurations can partially or fully hide it.'],
  'user_impacts': ['Users can lose access to primary navigation or confirmation controls on otherwise supported '
                   'hardware.'],
  'observables': ['Render representative screens with configured safe-area insets and overscan simulations while '
                  'inspecting focusable and critical content bounds.'],
  'falsifiers': ['All essential controls and their focus treatments remain fully visible within the supported safe '
                 'region across target devices.'],
  'repairs': ['Apply platform safe-area constraints to critical layout and reserve edge placement for nonessential '
              'decorative or intentionally bleedable content.'],
  'exceptions': [],
  'verification': ['Test target resolutions, overscan settings, platform overlays, and focus scaling and confirm '
                   'critical controls never cross effective safe bounds.'],
  'owner_hints': ['designing-tv-ten-foot-interfaces'],
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
  'provenance_ids': ['nui-tv-remote-owners-v13'],
  'status': 'active'},
 {'rule_id': 'ui.tv.control-timeout-does-not-hide-focused-action',
  'domain': 'tv',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Auto-hiding TV controls must not disappear while a user is actively focused on them',
  'statement': 'Playback or ambient controls that time out must remain available while focus is inside the control '
               'surface or while the user is actively navigating, instead of hiding on an unrelated timer.',
  'intent': 'Prevent focus from becoming invisible or landing on hidden controls in remote-driven interfaces with '
            'auto-dismiss chrome.',
  'applies_when': ['A TV interface automatically hides playback controls, overlays, or navigation chrome after '
                   'inactivity while they can hold directional focus.'],
  'does_not_apply_when': [],
  'failure_modes': ['The auto-hide timer fires while focus is still on a control, leaving the user with an invisible '
                    'focused element or unexpected focus relocation.'],
  'user_impacts': ['Users can activate unseen actions or lose orientation because the interface changes under active '
                   'remote navigation.'],
  'observables': ['Place focus on each auto-hiding control, wait through the inactivity threshold, and inspect '
                  'visibility and logical focus ownership.'],
  'falsifiers': ['Active focus or navigation suspends auto-hide, or hiding deliberately moves focus to a visible '
                 'predictable target.'],
  'repairs': ['Include focus and recent directional activity in chrome visibility policy rather than using a '
              'wall-clock timer alone.'],
  'exceptions': [],
  'verification': ['Test idle timeout, held focus, repeated directional input, playback state changes, and '
                   'accessibility modes and confirm focus never becomes hidden.'],
  'owner_hints': ['designing-tv-ten-foot-interfaces'],
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
  'provenance_ids': ['nui-tv-remote-owners-v13'],
  'status': 'active'},
 {'rule_id': 'ui.tv.modal-close-restores-logical-focus',
  'domain': 'tv',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Closing a TV modal must restore focus to the action or item that opened it when still valid',
  'statement': 'After dismissing a remote-driven modal or overlay, focus should return to the invoking logical item '
               'or a predictable surviving neighbor rather than reset to an unrelated first control.',
  'intent': 'Preserve spatial orientation in large-screen interfaces where users navigate by relative focus movement '
            'and cannot simply point back to their previous item.',
  'applies_when': ['A focusable item opens a modal, details overlay, options sheet, or transient full-screen layer '
                   'that temporarily owns remote navigation.'],
  'does_not_apply_when': [],
  'failure_modes': ['Closing the layer sends focus to a distant default position even though the invoking item still '
                    'exists and remains actionable.'],
  'user_impacts': ['Users must reconstruct their place in a large rail or grid and can accidentally act on the wrong '
                   'content after dismissal.'],
  'observables': ['Open and close overlays from items deep in lists, grids, and carousels while tracking logical '
                  'focus identity and viewport position.'],
  'falsifiers': ['Focus returns to the invoking item when valid or to a documented nearby fallback when that item '
                 'was removed or disabled.'],
  'repairs': ['Store the logical focus return target with modal navigation state and restore by stable item identity '
              'rather than numeric index.'],
  'exceptions': [],
  'verification': ['Dismiss overlays after list reordering, item removal, data refresh, and viewport movement and '
                   'confirm focus restoration remains predictable.'],
  'owner_hints': ['designing-gamepad-remote-focus'],
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
  'provenance_ids': ['nui-tv-remote-owners-v13'],
  'status': 'active'}]

__all__ = ["TV_REMOTE_RULES_V13"]
