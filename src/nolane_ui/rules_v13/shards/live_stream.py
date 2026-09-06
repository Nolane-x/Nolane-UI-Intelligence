"""V13 eighth-wave independently authored rules for live stream."""
from __future__ import annotations

from ._capabilities import interaction_caps


LIVE_STREAM_RULES_V13 = [{'rule_id': 'ui.livestream.live-edge-distinct-from-dvr-position',
  'domain': 'livestream',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Live playback must distinguish the current live edge from a viewer’s DVR position',
  'statement': 'A viewer can be watching a delayed position inside a live stream; “live” status '
               'should not imply they are at the live edge.',
  'intent': 'Prevent time-sensitive interactions from being interpreted against the wrong stream '
            'position.',
  'applies_when': ['A live player supports rewind or DVR playback.'],
  'does_not_apply_when': [],
  'failure_modes': ['The player badge says LIVE while the viewer is five minutes behind the actual '
                    'broadcast.'],
  'user_impacts': ['Chat, polls, sports events, or moderation timestamps can feel contradictory or '
                   'reveal future content.'],
  'observables': ['Seek behind live edge, pause, resume, and jump live while inspecting status and '
                  'interaction timestamps.'],
  'falsifiers': ['The UI distinguishes broadcast live state from viewer position and exposes how '
                 'far behind live edge the playhead is.'],
  'repairs': ['Track live-edge time separately from media playhead and derive status from their '
              'distance.'],
  'exceptions': [],
  'verification': ['Exercise pause/seek/reconnect paths and verify live-edge labeling updates with '
                   'actual viewer position.'],
  'owner_hints': ['designing-live-stream-player-states'],
  'verifier_hints': ['critiquing-functional-completeness'],
  'capabilities': interaction_caps(),
  'provenance_ids': ['nui-live-stream-owners-v13'],
  'status': 'active'},
 {'rule_id': 'ui.livestream.latency-mode-visible',
  'domain': 'livestream',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Live-stream latency mode must be visible when it changes delay and feature behavior',
  'statement': 'Ultra-low, low, and standard latency can trade stability, quality, DVR, or '
               'captions; users should know the effective mode.',
  'intent': 'Make interaction timing and feature availability explainable.',
  'applies_when': ['The player supports selectable or adaptive latency modes.'],
  'does_not_apply_when': [],
  'failure_modes': ['A viewer selects low latency but a reconnect silently falls back to standard '
                    'latency while the control still shows low.'],
  'user_impacts': ['Time-sensitive interactions can be delayed without an understandable cause.'],
  'observables': ['Switch modes, induce fallback, and inspect effective latency, feature '
                  'availability, and control state.'],
  'falsifiers': ['Displayed mode reflects actual playback pipeline state, including fallback or '
                 'unavailable mode.'],
  'repairs': ['Separate requested from effective latency mode and update the UI from authoritative '
              'player telemetry.'],
  'exceptions': [],
  'verification': ['Force unsupported/fallback conditions and verify the effective mode and '
                   'consequences are disclosed.'],
  'owner_hints': ['designing-live-stream-latency-control'],
  'verifier_hints': ['critiquing-functional-completeness'],
  'capabilities': interaction_caps(),
  'provenance_ids': ['nui-live-stream-owners-v13'],
  'status': 'active'},
 {'rule_id': 'ui.livestream.reconnect-state-visible',
  'domain': 'livestream',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Live-stream reconnecting must remain distinct from paused, ended, or buffering states',
  'statement': 'A lost connection to an ongoing live source needs a recoverable reconnect state '
               'rather than ambiguous spinner or ended UI.',
  'intent': 'Prevent viewers from abandoning or misinterpreting a recoverable live session.',
  'applies_when': ['Network interruptions can break playback while the live event continues.'],
  'does_not_apply_when': [],
  'failure_modes': ['A brief network loss sends the player to an “ended” screen even though '
                    'reconnect would resume the broadcast.'],
  'user_impacts': ['Viewers may miss ongoing content or repeatedly reload the page.'],
  'observables': ['Interrupt network before, during, and after source end and inspect retry, '
                  'playhead, and final state.'],
  'falsifiers': ['Reconnecting, buffering, paused, source-ended, and terminal failure remain '
                 'distinguishable and converge correctly.'],
  'repairs': ['Model transport connectivity separately from source lifecycle and preserve last '
              'known live context across retries.'],
  'exceptions': [],
  'verification': ['Simulate recoverable and terminal failures and verify state transitions and '
                   'recovery controls match the source reality.'],
  'owner_hints': ['designing-live-stream-player-states'],
  'verifier_hints': ['critiquing-functional-completeness'],
  'capabilities': interaction_caps(),
  'provenance_ids': ['nui-live-stream-owners-v13'],
  'status': 'active'},
 {'rule_id': 'ui.livestream.track-sync-state-visible',
  'domain': 'livestream',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Live audio, video, caption, and alternate tracks must expose synchronization failures',
  'statement': 'A stream can continue while one track drifts, stalls, or switches; overall '
               '“playing” status does not prove tracks remain aligned.',
  'intent': 'Prevent degraded multi-track playback from masquerading as healthy playback.',
  'applies_when': ['The live experience uses multiple timed media tracks or captions.'],
  'does_not_apply_when': [],
  'failure_modes': ['Video continues but captions are twenty seconds behind and the player reports '
                    'no degraded state.'],
  'user_impacts': ['Viewers can misunderstand dialogue or miss accessibility content.'],
  'observables': ['Delay or drop individual tracks and inspect player health, track status, and '
                  'recovery behavior.'],
  'falsifiers': ['Material track drift or loss is detectable and surfaced; recovered tracks return '
                 'to the correct media timeline.'],
  'repairs': ['Monitor per-track timestamps/health and reconcile or report synchronization failure '
              'rather than hiding it behind global playback state.'],
  'exceptions': [],
  'verification': ['Inject track-specific delay and recovery and verify the player detects and '
                   'corrects or exposes the mismatch.'],
  'owner_hints': ['designing-live-stream-player-states'],
  'verifier_hints': ['critiquing-functional-completeness'],
  'capabilities': interaction_caps(),
  'provenance_ids': ['nui-live-stream-owners-v13'],
  'status': 'active'},
 {'rule_id': 'ui.livestream.ended-distinct-from-network-failure',
  'domain': 'livestream',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'A live event ending must remain distinct from a viewer-side network failure',
  'statement': 'Both conditions can stop media delivery, but only one means the source has '
               'actually ended.',
  'intent': 'Prevent false end-of-event messaging during connectivity loss.',
  'applies_when': ['The player may lose packets or receive an authoritative end-of-stream signal.'],
  'does_not_apply_when': [],
  'failure_modes': ['A network outage produces the same “Thanks for watching” screen as the '
                    'broadcaster ending the event.'],
  'user_impacts': ['Viewers may stop trying to reconnect while the event continues.'],
  'observables': ['Compare authoritative source end, encoder failure, CDN loss, and local offline '
                  'conditions.'],
  'falsifiers': ['The ended state requires source lifecycle evidence; transport failures instead '
                 'expose retry or degraded state.'],
  'repairs': ['Use separate source-lifecycle and transport-health signals when deriving terminal '
              'playback state.'],
  'exceptions': [],
  'verification': ['Simulate each stop condition and verify only source termination produces the '
                   'final ended state.'],
  'owner_hints': ['designing-live-stream-player-states'],
  'verifier_hints': ['critiquing-functional-completeness'],
  'capabilities': interaction_caps(),
  'provenance_ids': ['nui-live-stream-owners-v13'],
  'status': 'active'},
 {'rule_id': 'ui.livestream.interaction-timestamps-align-with-stream-time',
  'domain': 'livestream',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Live interactions must align timestamps to the viewer’s stream position when DVR delay '
           'exists',
  'statement': 'Chat markers, polls, annotations, or reactions can reference broadcast time rather '
               'than wall clock; alignment matters when viewers are behind live.',
  'intent': 'Keep interactions temporally coherent with the media a viewer is actually seeing.',
  'applies_when': ['The live product overlays time-sensitive interactions on rewindable playback.'],
  'does_not_apply_when': [],
  'failure_modes': ['A viewer rewinds five minutes but receives a poll result tied to the current '
                    'live moment, revealing future context.'],
  'user_impacts': ['Interactions can become confusing, spoil content, or record responses against '
                   'the wrong event.'],
  'observables': ['Seek across live history and compare media time with interaction display and '
                  'submission timestamps.'],
  'falsifiers': ['Interaction presentation follows the documented stream-time policy and does not '
                 'silently mix live wall time with delayed playhead time.'],
  'repairs': ['Associate interactions with explicit broadcast/media timestamps and map them to '
              'each viewer’s playhead where appropriate.'],
  'exceptions': [],
  'verification': ['Exercise DVR lag and jump-live transitions and verify interactions appear and '
                   'submit against the intended timeline.'],
  'owner_hints': ['designing-live-stream-player-states'],
  'verifier_hints': ['critiquing-functional-completeness'],
  'capabilities': interaction_caps(),
  'provenance_ids': ['nui-live-stream-owners-v13'],
  'status': 'active'},
 {'rule_id': 'ui.livestream.quality-downgrade-source-visible',
  'domain': 'livestream',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Live quality downgrades must distinguish adaptive network response from source '
           'limitations',
  'statement': 'Lower resolution can result from bandwidth adaptation, device constraints, or the '
               'source itself; the reason affects recovery and user expectations.',
  'intent': 'Prevent viewers from repeatedly changing settings when the source cannot provide '
            'higher quality.',
  'applies_when': ['The player adapts or selects among multiple live renditions.'],
  'does_not_apply_when': [],
  'failure_modes': ['The player drops to 360p because the source stops publishing HD, but the UI '
                    'implies the user’s network is the problem.'],
  'user_impacts': ['Users may troubleshoot the wrong cause or believe a manual quality choice is '
                   'ignored.'],
  'observables': ['Remove source renditions and separately throttle network while inspecting '
                  'selected/effective quality and reason.'],
  'falsifiers': ['Effective quality and material downgrade cause are distinguishable when the '
                 'player has evidence for them.'],
  'repairs': ['Track rendition availability separately from adaptive selection and surface '
              'source-limited versus network-adapted states.'],
  'exceptions': [],
  'verification': ['Trigger both causes and verify recovery/settings behavior corresponds to the '
                   'actual limiting layer.'],
  'owner_hints': ['designing-live-stream-player-states'],
  'verifier_hints': ['critiquing-functional-completeness'],
  'capabilities': interaction_caps(),
  'provenance_ids': ['nui-live-stream-owners-v13'],
  'status': 'active'},
 {'rule_id': 'ui.livestream.live-caption-availability-visible',
  'domain': 'livestream',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Live caption availability must expose pending, unavailable, delayed, and active states',
  'statement': 'Live captions can start late, fail independently, or be unsupported; a caption '
               'toggle alone should not imply accessible text exists.',
  'intent': 'Keep viewers informed about the actual availability of live captions.',
  'applies_when': ['A live event offers human or automatic captions.'],
  'does_not_apply_when': [],
  'failure_modes': ['The CC control appears enabled but the caption service has not connected and '
                    'no text will arrive.'],
  'user_impacts': ['Deaf or hard-of-hearing viewers can wait for accessibility support that is not '
                   'actually active.'],
  'observables': ['Start streams before caption feed, interrupt captions mid-event, and inspect '
                  'control/status/recovery.'],
  'falsifiers': ['Caption state reflects active track availability and distinguishes '
                 'delayed/pending from unsupported or failed.'],
  'repairs': ['Model caption service/track lifecycle explicitly and update controls from '
              'authoritative availability.'],
  'exceptions': [],
  'verification': ['Exercise late start, outage, recovery, and language-switch paths and verify '
                   'status matches actual caption delivery.'],
  'owner_hints': ['designing-live-stream-player-states'],
  'verifier_hints': ['critiquing-functional-completeness'],
  'capabilities': interaction_caps(),
  'provenance_ids': ['nui-live-stream-owners-v13'],
  'status': 'active'}]

__all__ = ["LIVE_STREAM_RULES_V13"]
