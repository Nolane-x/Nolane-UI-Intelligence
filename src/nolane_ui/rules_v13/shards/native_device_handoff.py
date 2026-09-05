"""V13 native-device rules for pairing, share results, handoff, modality, restoration, display, capability, and discovery truth."""
from __future__ import annotations

from ._capabilities import interaction_caps


NATIVE_DEVICE_HANDOFF_RULES_V13 = [
    {'rule_id': 'ui.native.bluetooth-pairing-target-identity-stable',
     'domain': 'native',
     'class': 'behavioral',
     'severity': 'major',
     'enforcement': 'block',
     'title': 'Bluetooth pairing must keep the selected physical target identity stable through discovery updates',
     'statement': 'Once a user chooses a nearby Bluetooth target to pair, discovery refreshes and device-list reordering '
                  'must not transfer that selection to another advertisement with a similar name or recycled row.',
     'intent': 'Keep pairing authority attached to the intended physical device rather than to a transient scan '
               'position.',
     'applies_when': ['A native application discovers multiple nearby Bluetooth devices whose names can duplicate, '
                      'change, or reorder as advertisements arrive.'],
     'does_not_apply_when': [],
     'failure_modes': ['The selected device is tracked by list index or display name and a refresh causes the pair '
                       'command to target a different device.'],
     'user_impacts': ['Users can connect to unintended hardware and may expose data or control to the wrong nearby '
                      'device.'],
     'observables': ['Discover several same-named devices, select one, force advertisement churn and reorder, then '
                     'compare pairing request identifier with the originally selected target.'],
     'falsifiers': ['The pair command uses the stable platform device identity chosen by the user and selection is '
                    'cleared rather than substituted if that target expires.'],
     'repairs': ['Capture the platform device identifier at selection and decouple selection state from scan ordering '
                 'and mutable display labels.'],
     'exceptions': [],
     'verification': ['Test duplicate names, signal-strength reorder, target disappearance, rediscovery, and permission '
                      'changes and verify pairing never jumps identities.'],
     'owner_hints': ['designing-bluetooth-device-pairing'],
     'verifier_hints': ['critiquing-security-and-privacy'],
     'capabilities': interaction_caps(),
     'provenance_ids': ['nui-native-device-owners-v13'],
     'status': 'active'},
    {'rule_id': 'ui.native.share-cancel-does-not-report-success',
     'domain': 'native',
     'class': 'behavioral',
     'severity': 'major',
     'enforcement': 'block',
     'title': 'Cancelling a native share sheet must not be reported as a successful share',
     'statement': 'When the platform share sheet or intent chooser closes without a completed share, the application '
                  'must not show sent or shared success solely because control returned from the system UI.',
     'intent': 'Keep platform handoff completion distinct from merely presenting or dismissing the share interface.',
     'applies_when': ['The application invokes a native share sheet, intent, activity view, or platform handoff whose '
                      'result can be cancelled or lack definitive delivery evidence.'],
     'does_not_apply_when': [],
     'failure_modes': ['Returning from the system share UI always triggers a success toast and updates share state even '
                       'when the user cancelled or the platform reports no completed activity.'],
     'user_impacts': ['Users can believe content was shared externally when no recipient or destination actually '
                      'received it.'],
     'observables': ['Open the share UI, cancel at different points, choose unsupported targets, and perform successful '
                     'supported shares while capturing platform completion signals.'],
     'falsifiers': ['Success is shown only when the platform provides evidence appropriate to the product claim; '
                    'cancellation and unknown delivery remain distinct states.'],
     'repairs': ['Map platform completion callbacks conservatively and phrase outcome according to the evidence level '
                 'rather than assuming presentation equals delivery.'],
     'exceptions': [],
     'verification': ['Test cancel, target selection, target failure, background return, and successful share on each '
                      'supported platform and verify result messaging matches platform evidence.'],
     'owner_hints': ['designing-native-share-sheet-intents'],
     'verifier_hints': ['critiquing-platform-fit'],
     'capabilities': interaction_caps(),
     'provenance_ids': ['nui-native-device-owners-v13'],
     'status': 'active'},
    {'rule_id': 'ui.native.handoff-confirms-target-account-and-device',
     'domain': 'native',
     'class': 'behavioral',
     'severity': 'major',
     'enforcement': 'block',
     'title': 'Cross-device handoff should confirm the target device and account context before transferring sensitive work',
     'statement': 'When a task, session, file, or control surface is handed to another device, the UI must make the '
                  'intended target and relevant account context explicit whenever multiple nearby devices or identities '
                  'could receive it.',
     'intent': 'Prevent convenient handoff from becoming an ambiguous transfer of sensitive state to the wrong hardware '
               'or signed-in identity.',
     'applies_when': ['The product can transfer active work to another device while more than one eligible device or '
                      'account context may be available.'],
     'does_not_apply_when': [],
     'failure_modes': ['A generic Continue on device action selects a target automatically or by mutable proximity '
                       'without showing which account and device will receive the state.'],
     'user_impacts': ['Users can expose sensitive work or move control to hardware owned by another person or signed '
                      'into another account.'],
     'observables': ['Prepare multiple eligible devices and accounts, trigger handoff under changing proximity and '
                     'availability, and compare visible target with the authoritative recipient.'],
     'falsifiers': ['The target device and account or workspace context are identifiable before transfer, and '
                    'unavailable targets fail closed rather than silently substituting another device.'],
     'repairs': ['Bind handoff to a stable target identity and require explicit target confirmation when ambiguity '
                 'exists or sensitivity warrants it.'],
     'exceptions': [],
     'verification': ['Test duplicate device names, shared devices, account switch, target disappearance, and retry and '
                      'verify the transfer never changes recipients implicitly.'],
     'owner_hints': ['designing-cross-device-session-handoffs'],
     'verifier_hints': ['critiquing-security-and-privacy'],
     'capabilities': interaction_caps(),
     'provenance_ids': ['nui-native-device-owners-v13'],
     'status': 'active'},
    {'rule_id': 'ui.native.input-prompt-switch-does-not-steal-active-operation',
     'domain': 'native',
     'class': 'behavioral',
     'severity': 'major',
     'enforcement': 'block',
     'title': 'Input-device prompt switching must not cancel or reinterpret an active operation',
     'statement': 'When the UI changes prompts between keyboard, gamepad, touch, stylus, remote, or another input mode, '
                  'the prompt update must not itself move focus, cancel a drag, submit a form, or reinterpret a held '
                  'control from the previous device.',
     'intent': 'Let input hints adapt dynamically without turning device detection into an unsolicited interaction '
               'event.',
     'applies_when': ['The product detects recent input modality and updates control prompts or navigation behavior '
                      'while users can be mid-operation.'],
     'does_not_apply_when': [],
     'failure_modes': ['A modality switch rerenders focus or control bindings in a way that cancels selection, submits '
                       'input, or treats an already-held button as a new command.'],
     'user_impacts': ['Users can lose work or trigger unintended actions merely by touching another input device.'],
     'observables': ['Hold and perform active operations while alternately sending keyboard, controller, touch, and '
                     'pointer events and inspect focus, operation state, and command dispatch.'],
     'falsifiers': ['Prompt visuals can update while the current operation retains its original interaction state until '
                    'a deliberate user action ends or transfers it.'],
     'repairs': ['Decouple modality detection from command dispatch and preserve active interaction ownership across '
                 'prompt-only rerenders.'],
     'exceptions': [],
     'verification': ['Test held keys, drag, text composition, gamepad hold, touch gesture, and rapid modality changes '
                      'and verify no prompt switch creates an extra action.'],
     'owner_hints': ['designing-input-device-prompt-switching'],
     'verifier_hints': ['critiquing-platform-fit'],
     'capabilities': interaction_caps(),
     'provenance_ids': ['nui-native-device-owners-v13'],
     'status': 'active'},
    {'rule_id': 'ui.native.navigation-restoration-preserves-task-state',
     'domain': 'native',
     'class': 'behavioral',
     'severity': 'major',
     'enforcement': 'block',
     'title': 'Native navigation restoration must preserve the task state associated with the restored route',
     'statement': 'When the operating system recreates an application after process death or background eviction, '
                  'restoring the visible navigation stack must also restore or safely invalidate the task state each '
                  'route depends on instead of showing stale screens with missing models.',
     'intent': 'Keep platform lifecycle restoration from producing a convincing shell around lost or mismatched '
               'application state.',
     'applies_when': ['A native application participates in OS state restoration and can be killed and recreated while a '
                      'multi-screen task is in progress.'],
     'does_not_apply_when': [],
     'failure_modes': ['The navigation stack returns to a deep screen but its record, draft, selection, or permission '
                       'context is missing or bound to a default replacement.'],
     'user_impacts': ['Users can edit the wrong object, lose input, or encounter controls that act on state different '
                      'from the restored screen.'],
     'observables': ['Kill the process at several deep routes, mutate underlying data before relaunch, and compare '
                     'restored route parameters, record identity, draft, and available actions.'],
     'falsifiers': ['Each restored route has the task state required to make it valid or redirects to a truthful '
                    'recovery boundary when that state cannot be restored.'],
     'repairs': ['Persist stable route arguments and recoverable task state together, then revalidate external records '
                 'and permissions during OS restoration.'],
     'exceptions': [],
     'verification': ['Test process death, app update, account change, expired deep record, and restored draft and '
                      'verify the recreated stack never outruns valid task state.'],
     'owner_hints': ['designing-native-navigation-stacks'],
     'verifier_hints': ['critiquing-platform-fit'],
     'capabilities': interaction_caps(),
     'provenance_ids': ['nui-native-device-owners-v13'],
     'status': 'active'},
    {'rule_id': 'ui.native.external-display-disconnect-restores-primary-controls',
     'domain': 'native',
     'class': 'behavioral',
     'severity': 'major',
     'enforcement': 'block',
     'title': 'Disconnecting an external display must return essential controls to an available primary surface',
     'statement': 'If essential controls move to or depend on an external display, disconnecting that display must '
                  'restore a usable control path on the remaining device instead of leaving the session running with '
                  'controls stranded offscreen.',
     'intent': 'Preserve task control continuity across display topology changes without assuming the external screen '
               'will remain available.',
     'applies_when': ['The application presents media, dashboards, presentation controls, editing tools, or other '
                      'essential interaction across an external display and primary device.'],
     'does_not_apply_when': [],
     'failure_modes': ['The external display disconnects and the application keeps focus or controls assigned to the '
                       'vanished surface with no primary replacement.'],
     'user_impacts': ['Users can become unable to stop, navigate, save, or recover the active session after a normal '
                      'hardware disconnect.'],
     'observables': ['Move essential controls to the external surface, disconnect at several workflow points, and '
                     'inspect focus, active window placement, and restored primary controls.'],
     'falsifiers': ['Essential controls and focus migrate to an available surface while nonessential presentation state '
                    'can degrade or close according to product policy.'],
     'repairs': ['Model display topology changes as layout-authority events and maintain a fallback control surface on '
                 'the primary device.'],
     'exceptions': [],
     'verification': ['Test cable removal, wireless disconnect, sleep, resolution change, and reconnect and verify '
                      'control continuity through every topology transition.'],
     'owner_hints': ['designing-external-display-handoffs'],
     'verifier_hints': ['critiquing-platform-fit'],
     'capabilities': interaction_caps(),
     'provenance_ids': ['nui-native-device-owners-v13'],
     'status': 'active'},
    {'rule_id': 'ui.native.capability-negotiation-does-not-offer-unsupported-action',
     'domain': 'native',
     'class': 'behavioral',
     'severity': 'major',
     'enforcement': 'block',
     'title': 'Cross-device capability negotiation must remove actions the chosen target cannot perform',
     'statement': 'After selecting a target device for handoff or remote control, the action surface must be derived '
                  "from that target's negotiated capabilities rather than from the source device's feature set.",
     'intent': 'Prevent cross-device flows from advertising controls that will predictably fail on the chosen '
               'destination.',
     'applies_when': ['The same task can move between devices with different sensors, permissions, codecs, input '
                      'methods, screen classes, or application capabilities.'],
     'does_not_apply_when': [],
     'failure_modes': ['The target UI still offers source-only actions because capability checks happened before target '
                       'selection or were cached from another device.'],
     'user_impacts': ['Users can enter dead-end flows or believe the destination supports hardware and operations it '
                      'cannot actually perform.'],
     'observables': ['Connect targets with intentionally different capabilities, switch between them, and compare '
                     'visible actions with the negotiated target capability packet.'],
     'falsifiers': ['Only supported actions are enabled or offered, and temporarily unknown capabilities remain '
                    'explicitly unavailable or pending rather than assumed supported.'],
     'repairs': ["Recompute action availability from the selected target's current capability contract and invalidate "
                 'cached assumptions on target or permission change.'],
     'exceptions': [],
     'verification': ['Test sensor absence, codec difference, permission denial, app-version mismatch, and target '
                      'reconnect and verify unsupported actions never remain falsely actionable.'],
     'owner_hints': ['designing-cross-device-capability-negotiation'],
     'verifier_hints': ['critiquing-functional-completeness'],
     'capabilities': interaction_caps(),
     'provenance_ids': ['nui-native-device-owners-v13'],
     'status': 'active'},
    {'rule_id': 'ui.native.device-discovery-expiry-removes-stale-target',
     'domain': 'native',
     'class': 'behavioral',
     'severity': 'major',
     'enforcement': 'block',
     'title': 'Nearby-device discovery must expire targets that are no longer currently discoverable',
     'statement': 'Device discovery lists must distinguish cached recent devices from targets that are presently '
                  'available, and a stale advertisement must not remain selectable as if the device were still in range '
                  'or ready.',
     'intent': 'Keep proximity and discovery state truthful so connection attempts are not launched against obsolete '
               'scan data.',
     'applies_when': ['The product discovers nearby devices through Bluetooth, local network, proximity, or another '
                      'ephemeral advertisement mechanism.'],
     'does_not_apply_when': [],
     'failure_modes': ['A target remains displayed as available indefinitely after advertisements stop and selecting it '
                       'begins a normal connection flow rather than a stale-target recovery.'],
     'user_impacts': ['Users can repeatedly attempt impossible connections or accidentally select a different '
                      'rediscovered device that reused the same display label.'],
     'observables': ['Stop advertisements at controlled times, advance discovery windows, and inspect target '
                     'availability, stale labeling, selection state, and connection attempts.'],
     'falsifiers': ['Expired targets leave the currently available set or become explicitly recent/offline entries, and '
                    'selection does not silently transfer to another discovered identity.'],
     'repairs': ['Attach freshness and stable identity to discovery records and expire active availability independently '
                 'from optional recent-device history.'],
     'exceptions': [],
     'verification': ['Test device disappearance, sleep, signal loss, rediscovery, duplicate names, and cached history '
                      'and verify only fresh targets are presented as currently connectable.'],
     'owner_hints': ['designing-nearby-device-discovery'],
     'verifier_hints': ['critiquing-functional-completeness'],
     'capabilities': interaction_caps(),
     'provenance_ids': ['nui-native-device-owners-v13'],
     'status': 'active'},
]

__all__ = ['NATIVE_DEVICE_HANDOFF_RULES_V13']
