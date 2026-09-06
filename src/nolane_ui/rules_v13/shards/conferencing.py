"""V13 eighth-wave independently authored rules for conferencing."""
from __future__ import annotations

from ._capabilities import interaction_caps


CONFERENCE_RULES_V13 = [{'rule_id': 'ui.conference.prejoin-device-selection-reflects-active-device',
  'domain': 'conference',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Prejoin device selection must reflect the device that will actually be used on join',
  'statement': 'Preview controls are misleading if the call engine opens a different camera, '
               'microphone, or speaker at join time.',
  'intent': 'Ensure users review the same hardware identity that becomes active in the call.',
  'applies_when': ['A prejoin screen lets users select media devices.'],
  'does_not_apply_when': [],
  'failure_modes': ['The preview shows USB microphone A, but joining silently falls back to laptop '
                    'microphone B.'],
  'user_impacts': ['Users can expose unintended audio/video or join with unusable hardware.'],
  'observables': ['Change default devices and disconnect selected hardware between preview and '
                  'join; inspect active devices after connection.'],
  'falsifiers': ['The joined call uses the reviewed device or clearly announces and obtains a '
                 'valid fallback choice.'],
  'repairs': ['Bind join configuration to stable device identities and surface any fallback before '
              'media starts.'],
  'exceptions': [],
  'verification': ['Disconnect/reconnect devices around join and verify active media identity '
                   'matches the final visible selection.'],
  'owner_hints': ['designing-call-join-device-checks'],
  'verifier_hints': ['critiquing-functional-completeness'],
  'capabilities': interaction_caps(),
  'provenance_ids': ['nui-conference-owners-v13'],
  'status': 'active'},
 {'rule_id': 'ui.conference.prejoin-mute-camera-state-preserved',
  'domain': 'conference',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Prejoin microphone and camera intent must be preserved through connection',
  'statement': 'A user’s explicit mute or camera-off choice is privacy-critical and should survive '
               'the transition from preview to joined call.',
  'intent': 'Prevent media from activating against the user’s reviewed prejoin state.',
  'applies_when': ['Users can configure mic/camera before entering a call.'],
  'does_not_apply_when': [],
  'failure_modes': ['A reconnect or permission retry causes the user to join with microphone on '
                    'despite selecting mute in prejoin.'],
  'user_impacts': ['Private audio or video can be transmitted unexpectedly.'],
  'observables': ['Join under permission prompts, device fallback, reconnect, and slow signaling '
                  'while observing published tracks.'],
  'falsifiers': ['No track is published contrary to the final prejoin mic/camera intent.'],
  'repairs': ['Carry explicit publish intent separately from device availability and apply it '
              'atomically at join.'],
  'exceptions': [],
  'verification': ['Exercise every prejoin state through retry and reconnect and verify initial '
                   'publication state is preserved.'],
  'owner_hints': ['designing-call-join-device-checks'],
  'verifier_hints': ['critiquing-functional-completeness'],
  'capabilities': interaction_caps(),
  'provenance_ids': ['nui-conference-owners-v13'],
  'status': 'active'},
 {'rule_id': 'ui.conference.participant-identity-distinguishable',
  'domain': 'conference',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Conference participants must remain distinguishable when display names collide or '
           'change',
  'statement': 'Tiles, chat, moderation, and participant controls require stable identity beyond '
               'mutable display names.',
  'intent': 'Prevent actions and attribution from targeting the wrong participant.',
  'applies_when': ['Calls may contain participants with duplicate or changing names.'],
  'does_not_apply_when': [],
  'failure_modes': ['Two people named Alex appear identical and a host removes the wrong '
                    'participant from the call.'],
  'user_impacts': ['Moderation, handoff, and conversation attribution can be incorrect.'],
  'observables': ['Join duplicate-name participants, rename profiles, and inspect tile controls, '
                  'chat, roster, and moderation actions.'],
  'falsifiers': ['Actions target stable participant/session identities and the UI provides enough '
                 'disambiguation when labels collide.'],
  'repairs': ['Use immutable participant/session IDs for controls and expose secondary identity '
              'context when needed.'],
  'exceptions': [],
  'verification': ['Create duplicate labels and verify every moderation or direct action affects '
                   'only the intended participant.'],
  'owner_hints': ['designing-call-participant-layouts'],
  'verifier_hints': ['critiquing-functional-completeness'],
  'capabilities': interaction_caps(),
  'provenance_ids': ['nui-conference-owners-v13'],
  'status': 'active'},
 {'rule_id': 'ui.conference.network-degradation-visible',
  'domain': 'conference',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Conference network degradation must be visible when it materially affects media or '
           'interactivity',
  'statement': 'A connected call can be severely degraded without being disconnected; users need '
               'evidence that missing audio/video is a network condition.',
  'intent': 'Make degraded-call behavior understandable and recoverable.',
  'applies_when': ['Calls adapt to packet loss, latency, or bandwidth constraints.'],
  'does_not_apply_when': [],
  'failure_modes': ['Remote video freezes and audio drops while the call still displays a normal '
                    '“connected” state.'],
  'user_impacts': ['Users may blame participants or repeatedly toggle devices instead of '
                   'addressing connectivity.'],
  'observables': ['Inject loss, jitter, and bandwidth reduction while monitoring media quality and '
                  'connection indicators.'],
  'falsifiers': ['Material degradation is surfaced and distinguished from local mute, remote mute, '
                 'and device failure.'],
  'repairs': ['Map call-quality telemetry to explicit degraded states and offer recovery guidance '
              'appropriate to the limiting condition.'],
  'exceptions': [],
  'verification': ['Simulate different impairment patterns and verify status and affected media '
                   'attribution are accurate.'],
  'owner_hints': ['designing-call-participant-layouts'],
  'verifier_hints': ['critiquing-functional-completeness'],
  'capabilities': interaction_caps(),
  'provenance_ids': ['nui-conference-owners-v13'],
  'status': 'active'},
 {'rule_id': 'ui.conference.screen-share-source-visible',
  'domain': 'conference',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Active screen sharing must identify the source surface currently being transmitted',
  'statement': 'Users can share a window, tab, screen, or device; source identity should remain '
               'visible as applications change.',
  'intent': 'Prevent accidental disclosure caused by losing track of the shared source.',
  'applies_when': ['A call supports screen or window sharing.'],
  'does_not_apply_when': [],
  'failure_modes': ['The presenter switches desktops and cannot tell that an entire screen rather '
                    'than one window is still being broadcast.'],
  'user_impacts': ['Sensitive content can be exposed unintentionally.'],
  'observables': ['Start each sharing mode, switch windows/desktops, minimize sources, and inspect '
                  'local share indicators.'],
  'falsifiers': ['The presenter can always identify the active share source and stop or change it '
                 'without ambiguity.'],
  'repairs': ['Persist sharing-source identity and present it independently from the current '
              'foreground application.'],
  'exceptions': [],
  'verification': ['Exercise source changes and multi-monitor setups and verify the indicator '
                   'tracks the actual transmitted surface.'],
  'owner_hints': ['designing-call-participant-layouts'],
  'verifier_hints': ['critiquing-functional-completeness'],
  'capabilities': interaction_caps(),
  'provenance_ids': ['nui-conference-owners-v13'],
  'status': 'active'},
 {'rule_id': 'ui.conference.host-cohost-authority-visible',
  'domain': 'conference',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Host and cohost authority must be visible where privileged meeting actions are offered',
  'statement': 'Meeting roles can change dynamically and privileged controls should reflect '
               'current server authority rather than stale local assumptions.',
  'intent': 'Prevent unauthorized or confusing moderation actions.',
  'applies_when': ['Calls support host/cohost roles and role transfer.'],
  'does_not_apply_when': [],
  'failure_modes': ['A promoted cohost receives controls but a demoted participant keeps “End '
                    'meeting” enabled until refresh.'],
  'user_impacts': ['Users can attempt invalid actions or misunderstand who controls the meeting.'],
  'observables': ['Transfer host/cohost roles during a call and inspect controls, confirmations, '
                  'and backend authorization.'],
  'falsifiers': ['Privileged controls converge promptly to authoritative role state and the acting '
                 'role is visible before destructive actions.'],
  'repairs': ['Drive control availability from current role authority and invalidate stale '
              'permissions on role events.'],
  'exceptions': [],
  'verification': ['Rapidly promote/demote roles and verify privileged actions are neither '
                   'retained nor withheld incorrectly.'],
  'owner_hints': ['designing-call-participant-layouts'],
  'verifier_hints': ['critiquing-functional-completeness'],
  'capabilities': interaction_caps(),
  'provenance_ids': ['nui-conference-owners-v13'],
  'status': 'active'},
 {'rule_id': 'ui.conference.leave-distinct-from-end-for-all',
  'domain': 'conference',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Leaving a conference must remain distinct from ending it for every participant',
  'statement': 'Personal departure and terminating the meeting are materially different '
               'destructive actions, especially for hosts.',
  'intent': 'Prevent hosts from ending a meeting when they intend only to leave.',
  'applies_when': ['Hosts can either leave or terminate the session.'],
  'does_not_apply_when': [],
  'failure_modes': ['The primary red button says “Leave” but ends the meeting for everyone because '
                    'host semantics are hidden.'],
  'user_impacts': ['All participants can be disconnected unexpectedly.'],
  'observables': ['Test host/cohost/participant exit flows with other people still present and '
                  'inspect session lifecycle.'],
  'falsifiers': ['Leave affects only the actor unless an explicit “end for all” action is '
                 'confirmed with scope.'],
  'repairs': ['Separate personal disconnect from session termination in both UI and API '
              'contracts.'],
  'exceptions': [],
  'verification': ['Exercise exit actions under each role and verify remaining participants stay '
                   'connected unless end-for-all was explicitly chosen.'],
  'owner_hints': ['designing-call-participant-layouts'],
  'verifier_hints': ['critiquing-functional-completeness'],
  'capabilities': interaction_caps(),
  'provenance_ids': ['nui-conference-owners-v13'],
  'status': 'active'},
 {'rule_id': 'ui.conference.recording-state-visible-to-participants',
  'domain': 'conference',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Conference recording state must be visible to affected participants while capture is '
           'active',
  'statement': 'Recording can begin, pause, resume, or fail independently of the call; '
               'participants need a trustworthy current capture state.',
  'intent': 'Prevent participants from being unaware of active recording or relying on a recording '
            'that failed.',
  'applies_when': ['The meeting supports server or local recording exposed as a shared call '
                   'feature.'],
  'does_not_apply_when': [],
  'failure_modes': ['A host starts recording but remote participants never see the recording '
                    'indicator; later a failure leaves the host indicator falsely active.'],
  'user_impacts': ['Privacy expectations and recordkeeping assumptions can be violated.'],
  'observables': ['Start, pause, resume, fail, and stop recording while observing all participant '
                  'roles and reconnects.'],
  'falsifiers': ['Affected participants receive a consistent recording state derived from '
                 'authoritative capture lifecycle.'],
  'repairs': ['Broadcast recording lifecycle events and reconcile indicators on join/reconnect '
              'rather than relying on local button state.'],
  'exceptions': [],
  'verification': ['Exercise recording transitions and participant reconnects and verify every '
                   'client converges to the same capture state.'],
  'owner_hints': ['designing-call-participant-layouts'],
  'verifier_hints': ['critiquing-functional-completeness'],
  'capabilities': interaction_caps(),
  'provenance_ids': ['nui-conference-owners-v13'],
  'status': 'active'}]

__all__ = ["CONFERENCE_RULES_V13"]
