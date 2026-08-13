import json, unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
OBLIGATIONS={
'designing-wearable-glanceable-interfaces':['glance-duration budget','complication-information tier','wrist-motion tolerance','ambient-to-active transition','battery-attention tradeoff'],
'designing-tv-ten-foot-interfaces':['ten-foot angular scale','remote-navigation topology','focus-travel cost','overscan-safe composition','couch-distance legibility'],
'designing-supervisory-control-room-hmi':['alarm-priority topology','operator scan sector','control-room handoff state','nuisance-alarm load','degraded-sensor truth'],
'designing-robotic-teleoperation-interfaces':['command-feedback latency loop','camera-frame trust','deadman recovery','control-authority handoff','spatial reference integrity'],
'designing-real-time-updates':['update-coalescing policy','temporal-order guarantee','freshness timestamp contract','change-attention budget','live-freeze mode'],
'designing-pointer-touch-pen-input':['modality equivalence map','hover-only trap','pen barrel intent','palm-rejection boundary','coarse-pointer fallback'],
'designing-permissions-and-consent':['just-in-time permission ask','scope-to-benefit explanation','denial recovery path','consent revocation surface','permission-drift audit'],
'designing-offline-degraded-experiences':['offline capability envelope','queued-action provenance','conflict-merge policy','sync-recovery checkpoint','degraded-truth badge'],
'designing-notifications-and-interruptions':['interruption-value threshold','channel escalation ladder','notification deduplication','quiet-hours semantics','attention debt budget'],
'designing-multi-agent-surfaces':['agent-identity provenance','delegation boundary map','concurrent-action conflict','attribution timeline','agent handoff recovery'],
'designing-latency-and-progressive-feedback':['latency perceptual threshold','progress truth model','optimistic boundary','cancellation responsiveness','long-task backgrounding'],
'designing-high-stakes-decisions':['consequence model','dual-channel confirmation','decision evidence snapshot','forced-delay justification','post-commit recovery'],
'designing-haptics-and-multisensory-feedback':['haptic semantic vocabulary','actuator capability profile','cross-modal redundancy','haptic saturation','inaccessible-haptic fallback'],
'designing-gamepad-remote-focus':['spatial focus graph','wraparound policy','focus memory per region','analog-repeat envelope','remote key parity'],
'designing-game-hud-and-menus':['playfield occlusion budget','combat-attention priority','safe-zone adaptation','diegetic-vs-overlay decision','pause-state parity'],
'designing-foldable-large-screen-interfaces':['hinge occlusion map','posture transition state','pane continuity contract','span-versus-separate decision','half-open ergonomics'],
'designing-financial-transaction-ui':['amount-currency identity','fee-rate disclosure timing','beneficiary verification','irreversible settlement boundary','reconciliation receipt'],
'designing-desktop-windowed-workspaces':['window restoration contract','multiwindow object identity','shortcut-menu parity','drag-between-window semantics','monitor-density migration'],
'designing-commerce-checkout':['total-cost invariant','fulfillment-option truth','cart-state persistence','payment-failure continuity','guest-account boundary'],
'designing-brain-computer-interface-ux':['signal-confidence gating','false-activation ceiling','calibration burden','neural-data consent boundary','alternative-input escape'],
'designing-automotive-interfaces':['glance-time envelope','driving-state lockout','road-attention priority','vehicle-control distinction','passenger-driver context'],
'designing-authentication-and-passkeys':['ceremony-state model','account-device binding','recovery-channel integrity','phishing-resistant path','credential-discovery fallback'],
'designing-ai-uncertainty-and-provenance':['claim-source binding','uncertainty-type taxonomy','confidence-vs-evidence distinction','provenance freshness','unsupported-claim quarantine'],
'designing-accessible-media-alternatives':['media-alternative equivalence','audio-description timing','transcript navigation mapping','caption speaker identity','synchronized alternative track'],
'designing-accessible-drag-and-drop':['drag-intent action model','keyboard reorder path','pickup-drop announcement','target-list discoverability','cancellation restoration'],
}
class V6IndustryRiskDepthTests(unittest.TestCase):
 def test_domain_obligations(self):
  bad=[]
  for s,terms in OBLIGATIONS.items():
   t=(ROOT/'skills'/s/'SKILL.md').read_text().lower(); m=[x for x in terms if x not in t]
   if m: bad.append((s,m))
  self.assertFalse(bad,bad)
 def test_falsification_recovery(self):
  bad=[]
  for s in OBLIGATIONS:
   t=(ROOT/'skills'/s/'SKILL.md').read_text().lower()
   if 'falsif' not in t or 'recovery' not in t: bad.append(s)
  self.assertFalse(bad,bad)
 def test_production_lock(self):
  data=json.loads((ROOT/'knowledge/v6-depth-focus-obligations.json').read_text())['skills']
  self.assertFalse([s for s,v in OBLIGATIONS.items() if data.get(s)!=v])
  flat=sum(OBLIGATIONS.values(),[]); self.assertEqual(len(flat),len(set(flat)))
if __name__=='__main__': unittest.main()
