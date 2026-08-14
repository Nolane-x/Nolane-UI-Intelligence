import json, unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
OBLIGATIONS={
'adapting-external-ui-patterns':['source-version pin','foreign-style stripping','semantic parity ledger','local-token convergence','upstream-change isolation'],
'auditing-ui-library-integration':['dependency-surface inventory','bundled-global-style audit','runtime-semantic regression','upstream-update rehearsal','removal feasibility'],
'auditing-ui-research-depth':['evidence-chain reconstruction','unread-risk surface','negative-evidence coverage','stop-rule audit','epistemic-status verdict'],
'benchmarking-ui-skill-effect':['controlled-baseline family','skill-ablation delta','mutation sensitivity','transfer-regime test','harm-signal threshold'],
'binding-ui-evidence':['claim-evidence edge','evidence freshness clock','contradiction preservation','artifact identity pin','unsupported-obligation state'],
'challenging-ui-designs':['adversarial scenario lattice','assumption attack surface','counterexample generation','weakest-link challenge','challenge saturation stop'],
'compiling-ui-implementation-specifications':['component-behavior matrix','token-resolution table','breakpoint-state matrix','implementation ambiguity budget','executable acceptance hook'],
'compiling-ui-obligations':['obligation provenance chain','force-level encoding','conflict precedence map','waiver prohibition','closure evidence class'],
'covering-product-scenarios':['scenario cross-product pruning','lifecycle edge inventory','rare-high-impact scenario','role-permission variance','coverage frontier'],
'critiquing-functional-completeness':['reachable-but-useless defect','lifecycle gap verdict','orphan action detector','missing recovery surface','data-state completeness'],
'critiquing-research-validity':['claim-to-source trace','sampling-bias audit','recency mismatch','causal-overreach check','unresolved contradiction hold'],
'documenting-design-decisions':['decision rationale capsule','rejected-alternative ledger','assumption expiry','decision reversal trigger','maintenance audience'],
'engineering-rich-interactive-components':['interaction statechart','event ownership boundary','focus-transition graph','async race envelope','performance-interaction coupling'],
'gating-ui-completion':['non-waivable gate set','evidence lineage hash','cross-gate contradiction','conditional pass prohibition','release-claim bound'],
'governing-design-systems':['governance authority map','contribution acceptance rule','deprecation governance','exception debt register','adoption health signal'],
'inventorying-product-capabilities':['capability-action distinction','source-of-truth owner','permission-dependent capability','capability gap class','inventory freshness checkpoint'],
'iterating-rendered-visual-design':['rendered-delta hypothesis','visual-regression triage','local-vs-directional change','iteration stopping evidence','render-context pin'],
'maintaining-project-design-memory':['memory provenance tag','decision supersession graph','stale-memory eviction','context-specific recall','memory contamination check'],
'maintaining-ui-domain-atlas':['coverage-cell provenance','ontology drift trigger','uncovered intersection queue','owner-verifier separation','atlas saturation caveat'],
'maintaining-ui-resource-registry':['source identity normalization','role-capability indexing','license drift watch','archived-source demotion','registry-evidence boundary'],
'measuring-research-saturation':['marginal-information gain','source-class coverage','contradiction discovery rate','saturation false-positive','reopen signal'],
'modeling-cognitive-load-and-attention':['attentional bottleneck map','interruption switching cost','recognition-recall decision','vigilance decay','cognitive offloading strategy'],
'modeling-users-and-tasks':['role-vs-persona distinction','expertise trajectory','task-criticality map','edge-user inclusion','behavior-evidence trace'],
'nolane-ui':['lifecycle invariant map','root delegation contract','global stop condition','artifact coherence check','versioned-system boundary'],
'performing-ui-repository-archaeology':['artifact-depth ladder','source-tree path proof','commit-snapshot identity','implementation-claim trace','unread-material ledger'],
'planning-usability-research':['research-question decision','participant-task fit','protocol-bias risk','success-error metric','stopping sample rationale'],
'proving-interface-reachability':['action-to-surface graph','state reachability proof','dead-route detection','permission-reachability variant','keyboard-route verification'],
'recovering-ui-work':['recovery checkpoint graph','failure-scope containment','valid-artifact preservation','reroute minimality','recovery completion evidence'],
'registering-ui-actions':['canonical action identity','action side-effect class','action precondition contract','idempotency declaration','action deprecation path'],
'researching-ui-frontiers':['frontier uncertainty map','evidence-gap priority','emerging-source watch','speculative-vs-actionable','frontier exit criterion'],
'researching-ui-implementation-ecosystems':['capability-atom query','source-role mismatch','live-verification trigger','candidate-mechanism diversity','registry-staleness guard'],
'routing-ui-work':['route trigger proof','mandatory-route closure','optional-route suppression','risk escalation rule','routing cycle guard'],
'selecting-ui-building-blocks':['adopt-adapt-inspire-build matrix','integration-lockin cost','semantic fit score','replacement strategy','source-combination ceiling'],
'synthesizing-cross-source-ui-language':['layer-authority matrix','cross-source conflict graph','local-language normalization','source-removal test','synthesis-coherence verdict'],
'translating-standards-into-obligations':['normative-clause atomization','applicability condition','conformance-level trace','exception scope','standard-version pin'],
'ui-contracting':['raw-request preservation','obligation negotiation boundary','unresolved-ambiguity register','contract mutation check','downstream contract checksum'],
'verifying-runtime-ui-behavior':['event-sequence capture','browser-console evidence','focus-runtime trace','async failure injection','runtime-state reconciliation'],
}
class V6FullDepthSaturationTests(unittest.TestCase):
 def test_final_wave_semantic_anchors(self):
  bad=[]
  for s,v in OBLIGATIONS.items():
   t=(ROOT/'skills'/s/'SKILL.md').read_text().lower(); m=[x for x in v if x not in t]
   if m: bad.append((s,m))
  self.assertFalse(bad,bad)
 def test_final_wave_falsification_recovery(self):
  bad=[]
  for s in OBLIGATIONS:
   t=(ROOT/'skills'/s/'SKILL.md').read_text().lower()
   if 'falsif' not in t or 'recovery' not in t: bad.append(s)
  self.assertFalse(bad,bad)
 def test_depth_lock_exactly_covers_skill_graph_and_has_unique_anchors(self):
  d=json.loads((ROOT/'knowledge/v6-depth-focus-obligations.json').read_text())['skills']
  graph=json.loads((ROOT/'skills/skill-graph.json').read_text())['skills']
  self.assertEqual(len(d),166); self.assertTrue(set(d).issubset(graph))
  self.assertFalse([s for s,v in OBLIGATIONS.items() if d.get(s)!=v])
  flat=[term for terms in d.values() for term in terms]
  self.assertEqual(len(flat),len(set(flat)))
  self.assertTrue(all(len(v)==5 for v in d.values()))
if __name__=='__main__': unittest.main()
