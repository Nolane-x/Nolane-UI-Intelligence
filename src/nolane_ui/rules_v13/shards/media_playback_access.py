"""V13 media playback and accessibility rules for track, timeline, remote-session, and error truth."""
from __future__ import annotations

from ._capabilities import interaction_caps


MEDIA_PLAYBACK_ACCESS_RULES_V13 = [
    {'rule_id': 'ui.media.captions-available-not-equal-enabled',
     'domain': 'media',
     'class': 'behavioral',
     'severity': 'major',
     'enforcement': 'block',
     'title': "Caption availability must be distinct from the user's current caption state",
     'statement': 'A media player must not treat the existence of caption tracks as proof that captions are currently '
                  'enabled, nor treat a user disabling captions as if the media has no captions available.',
     'intent': 'Keep track capability, selected language, and enabled presentation state separate so controls and '
               'accessibility status remain truthful.',
     'applies_when': ['Media can expose one or more caption or subtitle tracks and the user can turn caption rendering '
                      'on or off.'],
     'does_not_apply_when': [],
     'failure_modes': ['The captions control reports enabled merely because tracks exist, or reports unavailable after '
                       'the user turns presentation off.'],
     'user_impacts': ['Users can misunderstand whether accessible text is currently being shown and lose the ability to '
                      'restore the desired track.'],
     'observables': ['Load media with zero, one, and multiple tracks, toggle rendering, switch languages, and inspect '
                     'control state plus actual timed-text output.'],
     'falsifiers': ['Availability reflects track capability while enabled state reflects current presentation, with '
                    'selected track identity preserved independently.'],
     'repairs': ['Model caption capability, selected track, and rendering enabled state as separate values and derive '
                 'the control from all three.'],
     'exceptions': [],
     'verification': ['Test track discovery, off/on toggles, language changes, source switches, and persisted '
                      'preferences and verify each state remains distinct.'],
     'owner_hints': ['designing-caption-presentation'],
     'verifier_hints': ['critiquing-accessibility'],
     'capabilities': interaction_caps(**{'accessibility-tree': 'REQUIRED'}),
     'provenance_ids': ['w3c-media-accessibility-reqs-v13', 'w3c-wcag22-v13'],
     'status': 'active'},
    {'rule_id': 'ui.media.audio-description-track-state-visible',
     'domain': 'media',
     'class': 'behavioral',
     'severity': 'major',
     'enforcement': 'block',
     'title': 'Audio-description selection must be distinguishable from the primary audio track',
     'statement': 'When audio description is available as an alternate or supplemental audio track, the control surface '
                  'must expose whether description is selected without disguising it as an ordinary language change or '
                  'generic audio toggle.',
     'intent': 'Give users a stable way to understand and restore the accessibility track they intentionally chose.',
     'applies_when': ['Media offers audio description through an alternate audio track, mixed track, or '
                      'product-supported description mode.'],
     'does_not_apply_when': [],
     'failure_modes': ['The player switches into or out of description with no visible or programmatic state, or labels '
                       'the change only by language even when both tracks share a language.'],
     'user_impacts': ['Users can lose descriptions during source or device changes and cannot tell which audio '
                      'presentation is active.'],
     'observables': ['Load media with primary and described audio variants, switch tracks, cast or reload where '
                     'supported, and inspect selected-track semantics and audible output.'],
     'falsifiers': ['The chosen description mode is represented explicitly and maps to the actual active audio track or '
                    'mix.'],
     'repairs': ['Attach accessibility purpose metadata to audio-track selection and surface description state '
                 'separately from language and generic track index.'],
     'exceptions': [],
     'verification': ['Test description on/off, language changes, resume, cast, and playback-device changes and verify '
                      'visible state matches the active track.'],
     'owner_hints': ['designing-audio-description-access'],
     'verifier_hints': ['critiquing-accessibility'],
     'capabilities': interaction_caps(**{'accessibility-tree': 'REQUIRED'}),
     'provenance_ids': ['w3c-media-accessibility-reqs-v13', 'w3c-wcag22-v13'],
     'status': 'active'},
    {'rule_id': 'ui.media.playback-speed-preserves-caption-sync',
     'domain': 'media',
     'class': 'behavioral',
     'severity': 'major',
     'enforcement': 'block',
     'title': 'Playback-speed changes must keep timed text synchronized with the media timeline',
     'statement': 'Changing playback rate must not cause captions, subtitles, transcripts, or other time-coded '
                  'alternatives to drift onto a different logical media position even if rendering cadence changes.',
     'intent': 'Preserve the shared timeline relationship between primary media and accessibility alternatives across '
               'supported speed controls.',
     'applies_when': ['The player supports playback rates other than normal speed while presenting time-synchronized '
                      'text or description cues.'],
     'does_not_apply_when': [],
     'failure_modes': ['After speed changes or rapid toggling, timed cues render according to wall-clock delay rather '
                       'than media time and visibly lead or lag the content.'],
     'user_impacts': ['Users can no longer associate captions or transcript text with the speech and events they '
                      'describe.'],
     'observables': ['Play known cue boundaries at several rates, change rates around cue transitions, and compare '
                     'active cue timecodes with the authoritative media currentTime.'],
     'falsifiers': ['Timed alternatives remain keyed to media timeline position and recover synchronization after rate '
                    'changes, seeks, pauses, and resumes.'],
     'repairs': ['Schedule cue activation from media time and resynchronize pending cue work whenever playback rate or '
                 'seek position changes.'],
     'exceptions': [],
     'verification': ['Test slow, fast, repeated rate switching, pause, seek, and resume using timestamped cue fixtures '
                      'and verify cue selection tracks media time.'],
     'owner_hints': ['designing-playback-speed-control'],
     'verifier_hints': ['critiquing-accessibility'],
     'capabilities': interaction_caps(**{'accessibility-tree': 'REQUIRED'}),
     'provenance_ids': ['w3c-media-accessibility-reqs-v13'],
     'status': 'active'},
    {'rule_id': 'ui.media.seek-preview-not-committed-until-seek',
     'domain': 'media',
     'class': 'behavioral',
     'severity': 'moderate',
     'enforcement': 'warn',
     'title': 'Timeline preview movement must be distinct from an actual committed seek',
     'statement': 'Hovering, scrubbing, or dragging a seek preview may show a candidate timestamp or thumbnail, but the '
                  "player must not update committed playback position or history until the product's defined seek action "
                  'occurs.',
     'intent': 'Separate exploratory timeline inspection from playback authority so previewing content does not silently '
               'mutate watch position.',
     'applies_when': ['The media timeline supports hover thumbnails, drag previews, chapter inspection, or other '
                      'pre-seek interactions.'],
     'does_not_apply_when': [],
     'failure_modes': ['Moving the pointer or keyboard preview updates persisted progress, resume position, analytics '
                       'watch state, or the actual currentTime before the user commits the seek.'],
     'user_impacts': ['Users can lose their place or generate false viewing history merely by exploring the timeline.'],
     'observables': ['Preview multiple distant timestamps without committing, reload or inspect persisted progress, then '
                     'perform a real seek and compare the resulting state transitions.'],
     'falsifiers': ['Preview state can move independently while committed playback and persisted progress change only at '
                    'the documented seek boundary.'],
     'repairs': ['Maintain separate preview and committed timeline positions and route persistence or analytics through '
                 'committed playback events only.'],
     'exceptions': [],
     'verification': ['Test pointer hover, drag cancel, keyboard preview, touch scrub cancel, and committed seek and '
                      'verify only the final action mutates playback position.'],
     'owner_hints': ['designing-media-timeline-scrubbing'],
     'verifier_hints': ['critiquing-functional-completeness'],
     'capabilities': interaction_caps(),
     'provenance_ids': ['nui-media-playback-owners-v13'],
     'status': 'active'},
    {'rule_id': 'ui.media.live-edge-distinct-from-current-playback',
     'domain': 'media',
     'class': 'contextual',
     'severity': 'moderate',
     'enforcement': 'warn',
     'title': "Live-stream players must distinguish the live edge from the viewer's current playback point",
     'statement': 'When a live stream supports rewind or delayed playback, the UI must distinguish being at the current '
                  'live edge from merely playing a stream that is live as a source.',
     'intent': 'Prevent a generic LIVE label from hiding whether the viewer is seconds or minutes behind the current '
               'broadcast position.',
     'applies_when': ['A live or near-live stream exposes a sliding playback window where users can pause or seek behind '
                      'the latest available content.'],
     'does_not_apply_when': [],
     'failure_modes': ['The player shows a live-state indicator whenever the source is live even when current playback '
                       'is materially behind the live edge.'],
     'user_impacts': ['Users can believe they are watching events in real time and make decisions based on content that '
                      'is actually delayed.'],
     'observables': ['Pause and rewind within the live window, then compare live-edge timestamp, currentTime, badge '
                     'state, and jump-to-live control as the gap changes.'],
     'falsifiers': ['Live-source identity and at-live-edge state are represented separately, and the at-live state '
                    'changes only when playback reaches the product-defined edge tolerance.'],
     'repairs': ['Track the moving live edge independently from playback position and derive the live-edge indicator '
                 'from their distance rather than stream type alone.'],
     'exceptions': [],
     'verification': ['Test pause, rewind, variable latency, catch-up playback, reconnect, and jump-to-live and verify '
                      'the indicator follows actual edge position.'],
     'owner_hints': ['designing-media-playback-experiences'],
     'verifier_hints': ['critiquing-user-experience'],
     'capabilities': interaction_caps(),
     'provenance_ids': ['nui-media-playback-owners-v13'],
     'status': 'active'},
    {'rule_id': 'ui.media.cast-state-distinct-from-local-playback',
     'domain': 'media',
     'class': 'behavioral',
     'severity': 'major',
     'enforcement': 'block',
     'title': 'Casting must distinguish remote playback from local device playback state',
     'statement': 'When media is handed to a cast or external playback target, the controlling UI must make clear that '
                  'playback authority moved to another device and must not display local renderer state as if it were '
                  'the remote output.',
     'intent': 'Keep remote session authority legible so volume, pause, disconnect, and resume actions target the device '
               'the user actually controls.',
     'applies_when': ['The product supports casting, AirPlay-like handoff, or another external playback session while '
                      'retaining a local controller.'],
     'does_not_apply_when': [],
     'failure_modes': ['After connecting, the local player continues to present itself as the active renderer or uses '
                       'local buffering and volume state as the remote device status.'],
     'user_impacts': ['Users can mute or stop the wrong output, think playback ended when it continues remotely, or lose '
                      'control of the external session.'],
     'observables': ['Connect and disconnect external targets while changing remote and local playback independently, '
                     'then compare visible target identity and control results.'],
     'falsifiers': ['The active playback target is explicit and remote state is sourced from the external session, with '
                    'local fallback clearly separated.'],
     'repairs': ['Model external playback as its own session with target identity and authoritative transport state '
                 'rather than decorating the local player with a cast icon.'],
     'exceptions': [],
     'verification': ['Test target switch, network interruption, remote pause, local app backgrounding, and disconnect '
                      'and verify control authority always matches the shown target.'],
     'owner_hints': ['designing-casting-and-external-playback'],
     'verifier_hints': ['critiquing-functional-completeness'],
     'capabilities': interaction_caps(),
     'provenance_ids': ['nui-native-device-owners-v13'],
     'status': 'active'},
    {'rule_id': 'ui.media.picture-in-picture-return-preserves-state',
     'domain': 'media',
     'class': 'behavioral',
     'severity': 'moderate',
     'enforcement': 'warn',
     'title': 'Returning from picture-in-picture must preserve the active media session state',
     'statement': 'Exiting picture-in-picture back into the main application should preserve the same media item, '
                  'playback position, pause state, selected tracks, and relevant queue context rather than constructing '
                  'a fresh player with default state.',
     'intent': 'Make picture-in-picture a presentation-mode transition around one media session, not a destructive '
               'player replacement.',
     'applies_when': ['The platform supports picture-in-picture or a floating external player that can later return to '
                      'the main application surface.'],
     'does_not_apply_when': [],
     'failure_modes': ['Returning to the full player resets captions, track selection, queue position, playback time, or '
                       'pause state because the UI creates a new uncontrolled media instance.'],
     'user_impacts': ['Users lose context or accessibility preferences simply by using a platform playback mode intended '
                      'to preserve continuity.'],
     'observables': ['Enter picture-in-picture with non-default playback and track state, interact there, return, and '
                     'compare the restored player with the underlying session.'],
     'falsifiers': ['The same authoritative media session continues across the presentation transition, including '
                    'changes made while in picture-in-picture.'],
     'repairs': ['Separate media session state from presentation container lifecycle and rebind the main player to the '
                 'existing session on return.'],
     'exceptions': [],
     'verification': ['Test repeated enter/exit, source queue changes, captions, speed, pause, and app backgrounding and '
                      'verify continuity across every return.'],
     'owner_hints': ['designing-picture-in-picture-playback'],
     'verifier_hints': ['critiquing-platform-fit'],
     'capabilities': interaction_caps(),
     'provenance_ids': ['nui-native-device-owners-v13', 'w3c-media-accessibility-reqs-v13'],
     'status': 'active'},
    {'rule_id': 'ui.media.entitlement-failure-distinct-from-network-failure',
     'domain': 'media',
     'class': 'behavioral',
     'severity': 'major',
     'enforcement': 'block',
     'title': 'Playback authorization failures must be distinct from transport or buffering failures',
     'statement': 'If media cannot play because the account lacks entitlement, a rental expired, a region policy blocks '
                  'access, or authorization failed, the player must not present the state as generic buffering or '
                  'network retry.',
     'intent': 'Give users a recovery path that matches the actual playback authority failure instead of wasting time on '
               'transport diagnostics.',
     'applies_when': ['Media playback depends on both network delivery and account, purchase, rental, subscription, or '
                      'policy authorization.'],
     'does_not_apply_when': [],
     'failure_modes': ['An authorization rejection falls into the same spinner, reconnect loop, or network-error message '
                       'used for transport failures.'],
     'user_impacts': ['Users repeatedly retry connectivity, lose trust in the player, or cannot discover the purchase, '
                      'sign-in, or policy action actually required.'],
     'observables': ['Force network, CDN, entitlement, expired-rental, and account-auth failures and compare error '
                     'classification, retry behavior, and offered actions.'],
     'falsifiers': ['Authorization failures remain distinct from network delivery failures and expose only recovery '
                    'actions supported by the authoritative response.'],
     'repairs': ['Classify playback failure from provider and entitlement responses before mapping to UI state, and keep '
                 'transport retries from masking authorization errors.'],
     'exceptions': [],
     'verification': ['Exercise each provider failure class with the same media item and verify the UI preserves the '
                      'correct cause and recovery action after retries.'],
     'owner_hints': ['designing-media-playback-experiences'],
     'verifier_hints': ['critiquing-functional-completeness'],
     'capabilities': interaction_caps(),
     'provenance_ids': ['nui-commerce-lifecycle-owners-v13', 'nui-internal-product-truth-v13'],
     'status': 'active'},
]

__all__ = ['MEDIA_PLAYBACK_ACCESS_RULES_V13']
