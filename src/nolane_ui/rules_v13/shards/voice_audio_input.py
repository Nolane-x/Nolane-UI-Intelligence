"""V13 sixth-wave rules; all operational prose is independently authored."""
from __future__ import annotations

VOICE_AUDIO_INPUT_RULES_V13 = [{'rule_id': 'ui.voice.listening-state-visible',
  'domain': 'voice',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Voice interfaces must make active listening state continuously perceivable',
  'statement': 'When the application is actively capturing microphone input for a command, dictation, transcription, '
               'or assistant interaction, users must have a persistent indication that listening is active.',
  'intent': 'Give users control over a privacy-sensitive input channel whose active state may otherwise be invisible '
            'once a transient permission prompt disappears.',
  'applies_when': ['The product opens or keeps a microphone capture stream for voice input after an explicit user '
                   'interaction or wake condition.'],
  'does_not_apply_when': [],
  'failure_modes': ['Microphone capture continues while the interface looks idle or provides only a momentary '
                    'indicator that is easy to miss.'],
  'user_impacts': ['Users can speak private information believing the application is no longer listening or can be '
                   'unsure whether commands are being captured.'],
  'observables': ['Start microphone capture, navigate within the voice experience, background and foreground the '
                  'app, and inspect persistent visual and accessible listening state.'],
  'falsifiers': ['Active capture remains perceivable until the microphone stream closes or the product clearly '
                 'transitions to a non-listening state.'],
  'repairs': ['Bind listening indicators to authoritative capture lifecycle rather than button press state and '
              'expose a direct stop control.'],
  'exceptions': [],
  'verification': ['Exercise start, stop, permission loss, device loss, backgrounding, and error states and confirm '
                   'listening indicators track the real microphone stream.'],
  'owner_hints': ['designing-voice-conversational-ui'],
  'verifier_hints': ['critiquing-security-and-privacy'],
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
  'provenance_ids': ['nui-voice-audio-owners-v13'],
  'status': 'active'},
 {'rule_id': 'ui.voice.partial-transcript-distinct-from-final',
  'domain': 'voice',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Interim speech recognition text must remain distinct from finalized transcript content',
  'statement': 'Streaming recognition hypotheses that may still change must not be styled or persisted as final user '
               'text until the recognizer or user establishes a final transcript boundary.',
  'intent': 'Prevent provisional recognition from being mistaken for committed content in dictation, search, '
            'messaging, or command workflows.',
  'applies_when': ['The speech recognizer emits partial or interim transcript hypotheses before producing final '
                   'segments.'],
  'does_not_apply_when': [],
  'failure_modes': ['Interim words appear identical to finalized text and can be submitted, saved, or interpreted as '
                    'stable content before recognition settles.'],
  'user_impacts': ['Users can send incorrect text, trigger the wrong command, or lose confidence when words visibly '
                   'committed by the UI later mutate.'],
  'observables': ['Feed speech that causes recognizer hypotheses to revise and inspect visual styling, persistence, '
                  'submission eligibility, and final transcript events.'],
  'falsifiers': ['Partial text is visibly provisional and only finalized segments cross the product’s normal commit '
                 'boundary.'],
  'repairs': ['Maintain separate interim and final transcript state and gate downstream mutations on final '
              'recognition or explicit user acceptance.'],
  'exceptions': [],
  'verification': ['Test hypothesis revisions, pauses, correction, recognition failure, and manual submission and '
                   'confirm provisional text never masquerades as committed content.'],
  'owner_hints': ['designing-voice-conversational-ui'],
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
  'provenance_ids': ['nui-voice-audio-owners-v13'],
  'status': 'active'},
 {'rule_id': 'ui.voice.stop-recording-boundary-visible',
  'domain': 'voice',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Stopping voice capture must clearly distinguish capture end from processing completion',
  'statement': 'When users stop recording, the interface must indicate whether audio capture has ended while '
               'transcription, upload, encoding, or command interpretation is still processing.',
  'intent': 'Separate privacy-sensitive microphone closure from downstream processing so users know what stopped and '
            'what is still happening.',
  'applies_when': ['Voice input continues through asynchronous processing after the microphone stream itself can be '
                   'stopped.'],
  'does_not_apply_when': [],
  'failure_modes': ['The interface says “done” or becomes idle at stop even though microphone capture or downstream '
                    'processing remains active with no visible state.'],
  'user_impacts': ['Users can misjudge privacy exposure or navigate away before processing completes and lose the '
                   'result.'],
  'observables': ['Stop voice capture while delaying transcription or upload and compare microphone stream state '
                  'with processing indicators.'],
  'falsifiers': ['The UI marks capture stopped immediately when authoritative, then separately shows any remaining '
                 'processing until completion or failure.'],
  'repairs': ['Model capture, processing, and result commitment as distinct lifecycle states instead of mapping one '
              'Stop action to a generic complete state.'],
  'exceptions': [],
  'verification': ['Delay each post-capture stage and verify microphone state, progress, cancellation, and final '
                   'result remain independently truthful.'],
  'owner_hints': ['designing-voice-conversational-ui'],
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
  'provenance_ids': ['nui-voice-audio-owners-v13'],
  'status': 'active'},
 {'rule_id': 'ui.voice.input-device-switch-reconciles-recording',
  'domain': 'voice',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Changing microphone input devices must reconcile active recording without hidden gaps',
  'statement': 'If the active microphone changes during recording, the product must either transition capture '
               'deliberately or stop with an explicit interruption rather than silently dropping or mixing audio.',
  'intent': 'Keep recorded or transcribed input coherent when Bluetooth routing, headset connection, system '
            'settings, or user selection changes the input device.',
  'applies_when': ['The platform can change microphone device or route while a voice capture session remains '
                   'active.'],
  'does_not_apply_when': [],
  'failure_modes': ['The interface still shows continuous recording while the underlying input device disconnected '
                    'or changed and part of the user’s speech was lost.'],
  'user_impacts': ['Users can submit incomplete recordings or commands because the UI hides an input-route '
                   'discontinuity.'],
  'observables': ['Switch microphones and connect or disconnect headsets mid-capture while inspecting track events, '
                  'waveform continuity, transcript gaps, and device labels.'],
  'falsifiers': ['The application either performs an explicit seamless handoff with verified continuity or marks the '
                 'interruption and requires a recoverable resume.'],
  'repairs': ['Listen for device and track lifecycle changes, update capture routing atomically, and expose any '
              'unverified gap instead of pretending continuity.'],
  'exceptions': [],
  'verification': ['Exercise manual device selection, Bluetooth route changes, unplug events, and permission '
                   'revocation during capture and confirm recording state remains truthful.'],
  'owner_hints': ['designing-voice-conversational-ui'],
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
  'provenance_ids': ['nui-voice-audio-owners-v13'],
  'status': 'active'},
 {'rule_id': 'ui.voice.wake-word-active-scope-visible',
  'domain': 'voice',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Wake-word listening must communicate the scope in which activation is currently enabled',
  'statement': 'If a product listens for a wake phrase only in certain screens, foreground states, devices, or '
               'sessions, the interface must not imply broader always-on availability than the actual activation '
               'scope.',
  'intent': 'Align user expectations about hands-free activation with the real privacy and availability boundaries '
            'of wake-word detection.',
  'applies_when': ['Voice activation can be enabled or disabled depending on application state, hardware, user '
                   'preference, operating-system policy, or current surface.'],
  'does_not_apply_when': [],
  'failure_modes': ['The product advertises or displays wake-word readiness even while the detector is inactive, or '
                    'hides that detection remains active in a bounded context.'],
  'user_impacts': ['Users can either disclose speech under the wrong privacy assumption or rely on a wake command '
                   'that cannot actually be detected.'],
  'observables': ['Move through foreground, background, locked, device-switch, and disabled-preference states and '
                  'inspect wake detector activity versus visible readiness.'],
  'falsifiers': ['The visible readiness state matches the detector’s actual active scope and users can discover how '
                 'to disable or re-enable it.'],
  'repairs': ['Bind wake-word indicators to detector lifecycle and scope, not merely to a saved preference that may '
              'not be effective in the current context.'],
  'exceptions': [],
  'verification': ['Test every supported activation scope and ensure readiness labels, privacy indicators, and '
                   'actual wake behavior stay aligned.'],
  'owner_hints': ['designing-voice-control-targetability'],
  'verifier_hints': ['critiquing-security-and-privacy'],
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
  'provenance_ids': ['nui-voice-audio-owners-v13'],
  'status': 'active'},
 {'rule_id': 'ui.voice.echo-playback-not-treated-as-user-speech',
  'domain': 'voice',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Application audio playback must not be accepted as user speech without an explicit full-duplex model',
  'statement': 'A voice interface that plays its own speech or media while listening must prevent or visibly handle '
               'acoustic echo so generated playback is not mistaken for a new user utterance.',
  'intent': 'Avoid feedback loops where system output recursively triggers recognition, commands, or conversational '
            'turns.',
  'applies_when': ['Microphone capture can remain active while the same device outputs speech, prompts, media, or '
                   'assistant audio that can leak back into the microphone.'],
  'does_not_apply_when': [],
  'failure_modes': ['The recognizer transcribes or executes the application’s own playback as though the user spoke '
                    'it, creating phantom input or repeated commands.'],
  'user_impacts': ['The system can send unintended messages, trigger commands, or enter conversational loops without '
                   'new user intent.'],
  'observables': ['Play representative application audio during active listening and inspect raw capture, transcript '
                  'attribution, command events, and echo-cancellation state.'],
  'falsifiers': ['Playback leakage is suppressed, attributed, or otherwise prevented from crossing the user-intent '
                 'boundary under the supported audio model.'],
  'repairs': ['Use platform echo controls, turn-taking boundaries, source-aware attribution, or explicit full-duplex '
              'logic rather than assuming playback cannot re-enter recognition.'],
  'exceptions': [],
  'verification': ['Test speakerphone, headphones, Bluetooth, high volume, and multiple acoustic environments and '
                   'confirm application playback never becomes unintended user input.'],
  'owner_hints': ['designing-voice-conversational-ui'],
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
  'provenance_ids': ['nui-voice-audio-owners-v13'],
  'status': 'active'},
 {'rule_id': 'ui.voice.recognition-language-visible',
  'domain': 'voice',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Speech recognition language must be visible when it materially affects interpretation',
  'statement': 'When recognition behavior depends on an active language or locale that can differ from surrounding '
               'interface language, users must be able to see or change the recognition language before relying on '
               'the transcript.',
  'intent': 'Prevent unexplained recognition errors caused by a hidden language model selection that differs from '
            'the user’s speech.',
  'applies_when': ['The speech recognizer supports multiple languages or locale variants and the active recognition '
                   'language is configurable or inferred.'],
  'does_not_apply_when': [],
  'failure_modes': ['The recognizer uses a language the user cannot identify from the voice surface, causing '
                    'systematic misrecognition that looks like generic model failure.'],
  'user_impacts': ['Multilingual users can waste time correcting transcripts or unintentionally submit distorted '
                   'text because language selection is hidden.'],
  'observables': ['Switch interface and recognition languages independently, speak ambiguous multilingual samples, '
                  'and inspect visible recognition-language state.'],
  'falsifiers': ['The active recognition language is discoverable and any automatic language switching is '
                 'represented truthfully when confidence is sufficient.'],
  'repairs': ['Expose recognition locale as voice-session state and separate it from general UI locale when the two '
              'can differ.'],
  'exceptions': [],
  'verification': ['Test manual and automatic language changes, code-switching, and persisted preferences and '
                   'confirm users can always determine the active recognition context.'],
  'owner_hints': ['designing-voice-conversational-ui'],
  'verifier_hints': ['critiquing-localization'],
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
  'provenance_ids': ['nui-voice-audio-owners-v13'],
  'status': 'active'},
 {'rule_id': 'ui.voice.destructive-command-requires-explicit-confirmation',
  'domain': 'voice',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Destructive voice commands must require an explicit confirmation appropriate to recognition uncertainty',
  'statement': 'A spoken command that deletes, sends, purchases, publishes, revokes, or otherwise causes '
               'high-consequence side effects must not commit solely from a potentially misrecognized utterance.',
  'intent': 'Account for speech-recognition ambiguity at the moment where incorrect interpretation would create '
            'difficult or irreversible consequences.',
  'applies_when': ['Voice control can invoke consequential actions whose equivalent visual workflow includes '
                   'confirmation, undo, review, or another intentional safety boundary.'],
  'does_not_apply_when': [],
  'failure_modes': ['A single recognition hypothesis immediately commits a destructive action without giving the '
                    'user a chance to verify the interpreted target and action.'],
  'user_impacts': ['Background speech, accents, recognition errors, or ambiguous wording can trigger serious side '
                   'effects that the user did not intend.'],
  'observables': ['Exercise ambiguous spoken commands and recognition substitutions near destructive actions while '
                  'inspecting whether commit occurs before confirmation.'],
  'falsifiers': ['The product confirms the interpreted action and target or provides an equivalently strong '
                 'reversible boundary before the side effect becomes authoritative.'],
  'repairs': ['Route consequential voice commands through the canonical action-review lifecycle rather than directly '
              'executing the recognizer’s top hypothesis.'],
  'exceptions': [],
  'verification': ['Test low-confidence, homophone, noisy, and target-ambiguous utterances and confirm none can '
                   'commit the destructive action without an explicit review boundary.'],
  'owner_hints': ['designing-voice-control-targetability'],
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
  'provenance_ids': ['nui-voice-audio-owners-v13'],
  'status': 'active'}]

__all__ = ["VOICE_AUDIO_INPUT_RULES_V13"]
