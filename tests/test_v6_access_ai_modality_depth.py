import json, unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
OBLIGATIONS={
'annotating-accessibility-intent':['access-barrier hypothesis','semantic-intent annotation','modality-loss consequence','assistive-path obligation','accessibility unknown marker'],
'critiquing-accessibility':['task-level accessibility verdict','barrier severity topology','assistive-technology disagreement','automated-check ceiling','accessibility regression block'],
'designing-aac-communication-interfaces':['communication-rate budget','vocabulary access topology','partner-assisted path','motor-planning consistency','message-ownership privacy'],
'designing-accessibility-settings-and-profiles':['preference precedence lattice','profile portability contract','reset-safe defaults','setting effect preview','assistive-setting conflict'],
'designing-agent-autonomy-and-control':['autonomy-level ladder','approval checkpoint graph','blast-radius bound','reversible delegation','stop-control latency'],
'designing-ai-feedback-and-correction':['correction affordance loop','feedback target specificity','model-state repair','learning-consent boundary','correction persistence'],
'designing-alternative-input':['switch-scan topology','dwell input fallback','voice-free action path','remapping persistence','fatigue-aware timing'],
'designing-ambient-context-aware-interfaces':['context-signal confidence','ambient privacy perimeter','context-change hysteresis','background-action ceiling','foreground override path'],
'designing-avatar-embodied-representation':['representation identity boundary','avatar expression uncertainty','nonverbal cue transparency','embodiment fallback','identity impersonation risk'],
'designing-cli-tui-interfaces':['terminal capability detection','keyboard-only command parity','resize reflow contract','colorless state distinction','shell safety boundary'],
'designing-cognitive-accessibility':['memory externalization map','plain-language decision','distraction suppression','time-pressure relief','cognitive recovery cue'],
'designing-collaboration-and-presence':['presence freshness','concurrent edit ownership','remote-cursor noise budget','conflict visibility','collaboration privacy'],
'designing-cross-device-action-equivalence':['action identity continuity','device-capability delta','handoff token','partial-action transfer','duplicate-execution guard'],
'designing-editor-canvas-workspaces':['infinite-canvas coordinate truth','zoom-level semantic scaling','selection transform invariants','history-command integration','canvas accessibility alternate'],
'designing-embedded-kiosk-interfaces':['session reset boundary','shoulder-surfing exposure','unattended timeout','physical escape path','peripheral-device recovery'],
'designing-flight-deck-interfaces':['phase-of-flight priority','mode-awareness invariant','alert acknowledgement semantics','sensor disagreement display','crew cross-check support'],
'designing-human-ai-interaction':['agency handoff contract','suggestion-action distinction','model capability boundary','user override prominence','automation surprise test'],
'designing-in-product-assistance':['help-trigger context','task-resume anchor','progressive help depth','stale-help detection','assistance dependency test'],
'designing-keyboard-power-user-ux':['shortcut namespace','chord conflict audit','discoverability surface','focus-command coherence','remapping support'],
'designing-medical-safety-critical-ui':['patient-identity lock','clinical data freshness','dose-unit integrity','alarm fatigue control','clinical override provenance'],
'designing-privacy-sensitive-interfaces':['data-exposure map','privacy expectation boundary','sensitive-screen shielding','retention-disclosure link','consent-context integrity'],
'designing-reduced-motion-and-photosensitivity':['motion-trigger inventory','vestibular-risk classification','photosensitive flash budget','reduced-motion substitution','autoplay escape'],
'designing-spatial-xr-interfaces':['spatial comfort envelope','locomotion choice','occlusion-depth truth','world-anchor persistence','boundary-safety cue'],
'designing-streaming-ai-responses':['token-stream commitment boundary','partial-answer stability','tool-call transition','citation-late-binding','stream-cancel semantics'],
'designing-voice-conversational-ui':['turn-taking state','recognition confidence boundary','repair dialogue path','private-context fallback','barge-in policy'],
'critiquing-ai-trust-and-agency':['automation-bias probe','authority inflation test','provenance-action gap','override friction','trust calibration verdict'],
'critiquing-cognitive-load':['working-memory load map','split-attention fault','choice-overload threshold','interruption recovery burden','learning-transfer penalty'],
'critiquing-human-factors-and-safety':['hazard-control trace','workload exceedance','alarm salience mismatch','error-forcing function','safety margin erosion'],
'critiquing-input-modality':['modality-exclusive action','parity-cost exception','gesture discoverability failure','input-switch continuity','inaccessible precision demand'],
'critiquing-localization':['untranslated semantic residue','layout expansion break','bidirectional logic fault','locale parsing hazard','cultural metaphor mismatch'],
'critiquing-performance-and-resilience':['interaction latency budget','long-task resilience','memory pressure failure','rendering-jank evidence','graceful degradation gap'],
'critiquing-security-and-privacy':['privilege-escalation surface','sensitive-state leakage','spoofing affordance','auth-context confusion','privacy-default regression'],
}
class V6AccessAiModalityDepthTests(unittest.TestCase):
 def test_domain_semantic_anchors(self):
  bad=[]
  for s,v in OBLIGATIONS.items():
   t=(ROOT/'skills'/s/'SKILL.md').read_text().lower(); m=[x for x in v if x not in t]
   if m: bad.append((s,m))
  self.assertFalse(bad,bad)
 def test_falsification_recovery(self):
  bad=[]
  for s in OBLIGATIONS:
   t=(ROOT/'skills'/s/'SKILL.md').read_text().lower()
   if 'falsif' not in t or 'recovery' not in t: bad.append(s)
  self.assertFalse(bad,bad)
 def test_production_lock(self):
  d=json.loads((ROOT/'knowledge/v6-depth-focus-obligations.json').read_text())['skills']
  self.assertFalse([s for s,v in OBLIGATIONS.items() if d.get(s)!=v])
  flat=sum(OBLIGATIONS.values(),[]); self.assertEqual(len(flat),len(set(flat)))
if __name__=='__main__': unittest.main()
