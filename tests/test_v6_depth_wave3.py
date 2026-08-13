import json
import unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
OBLIGATIONS={
'researching-visual-references':['interaction-state sampling','cross-screen reference walk','source-context reconstruction','blind-reference removal','reference contradiction log'],
'exploring-aesthetic-directions':['mechanism-level divergence','composition silhouette test','material-language divergence','typography-personality contrast','direction-convergence alarm'],
'evolving-component-apis':['compatibility matrix','consumer impact graph','semantic-version decision','codemod feasibility','deprecation exit test'],
'designing-generative-ui':['generation authority envelope','schema-to-surface contract','invalid-generation quarantine','ephemeral-state continuity','regeneration identity test'],
'designing-gaze-hand-spatial-input':['dwell-intent disambiguation','gaze-hand arbitration','spatial target envelope','vergence-depth comfort','fatigue calibration loop'],
'designing-sign-language-presentation':['signing-language identity','signer-frame integrity','sign-caption coordination','linguistic-content boundary','playback continuity contract'],
'engineering-human-factors':['task-demand model','workload budget','signal-detection threshold','error-cost asymmetry','fatigue-exposure envelope'],
'modeling-perception-and-motor-control':['visual-angle budget','target-acquisition model','contrast-sensitivity reserve','peripheral-vision demand','motor-variability margin'],
'evaluating-usability-evidence':['evidence-validity ladder','task-success confidence interval','observer-effect check','severity-calibration matrix','contradictory-finding resolution'],
'managing-theming-and-personalization':['semantic-theme invariants','personalization reversibility','accessibility-precedence rule','density-personalization boundary','theme-migration probe'],
'designing-accessible-interfaces':['accessibility-requirement trace','keyboard-path proof','programmatic-relationship map','sensory-equivalence test','conformance-usability gap'],
'designing-affective-adaptive-interfaces':['inferred-affect uncertainty','adaptation-consent boundary','adaptation transparency cue','mood-manipulation risk','state-reversion guarantee'],
'calibrating-ui-authority':['authority conflict matrix','normative-versus-informative','source-currentness horizon','claim-strength ceiling','supersession trace'],
'conducting-task-analysis':['job-trigger inventory','goal-action decomposition','frequency-consequence matrix','workaround evidence','task-variance sampling'],
}
class V6DepthWave3Tests(unittest.TestCase):
 def test_unique_obligations_present(self):
  failures=[]
  for skill,terms in OBLIGATIONS.items():
   t=(ROOT/'skills'/skill/'SKILL.md').read_text(encoding='utf-8').lower()
   m=[x for x in terms if x not in t]
   if m: failures.append((skill,m))
  self.assertFalse(failures,failures)
 def test_falsification_recovery_present(self):
  failures=[]
  for skill in OBLIGATIONS:
   t=(ROOT/'skills'/skill/'SKILL.md').read_text(encoding='utf-8').lower()
   if 'falsif' not in t or 'recovery' not in t: failures.append(skill)
  self.assertFalse(failures,failures)
 def test_production_focus_gate_tracks_wave3(self):
  data=json.loads((ROOT/'knowledge/v6-depth-focus-obligations.json').read_text(encoding='utf-8'))['skills']
  self.assertFalse([s for s in OBLIGATIONS if data.get(s)!=OBLIGATIONS[s]])
  flat=[x for v in OBLIGATIONS.values() for x in v]
  self.assertEqual(len(flat),len(set(flat)))
if __name__=='__main__': unittest.main()
