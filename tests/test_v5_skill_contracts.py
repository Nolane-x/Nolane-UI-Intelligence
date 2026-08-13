import json
import unittest
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
MANIFEST_PATH=ROOT/'knowledge/v5-skill-manifest.json'
GRAPH_PATH=ROOT/'skills/skill-graph.json'

EXPECTED={
 'preserving-experiential-intent':('kernel','ui-contracting','experiential-intent',('desired_feelings','forbidden_feelings','operationalization supplements')),
 'directing-visual-ambition':('kernel','routing-ui-work','visual-ambition-contract',('flagship','exceptional','hard route')),
 'modeling-aspirational-identity':('strategy','modeling-users-and-tasks','aspirational-identity-model',('aspirational_role','power_perception','rituals_of_use')),
 'composing-spatial-dramaturgy':('visual','composing-layouts','spatial-drama-contract',('compression','expansion','monumental')),
 'detecting-aesthetic-attractors':('critic','preventing-generic-ui','aesthetic-attractor-audit',('subject_specificity','removal_cost','accumulation')),
 'engineering-visual-legibility':('visual','crafting-typography','visual-legibility-evidence',('11px','10px','computed')),
 'directing-visual-energy':('visual','crafting-color','visual-energy-contract',('chroma','luminance','restraint')),
 'deepening-signature-mechanisms':('visual','exploring-aesthetic-directions','signature-depth-contract',('semantic_depth','information_gain','failure_if_removed')),
 'proving-visual-encoding-semantics':('verification','designing-data-visualization','encoding-provenance-table',('channel','decorative','meaning')),
 'critiquing-aesthetic-adequacy':('verification','critiquing-visual-design','aesthetic-adequacy-findings',('adequacy','original intent','reopen')),
 'escaping-aesthetic-basins':('visual','iterating-rendered-visual-design','aesthetic-basin-decision',('RE_DIVERGE','reference frontier','local refinement')),
 'evaluating-perceptual-diversity':('verification','gating-ui-completion','workspace-visual-matrix',('coherent diversity','template repetition','dominant_geometry')),
 'testing-skill-interactions':('verification','gating-ui-completion','skill-interaction-evidence',('semantic mutation','factorial','ablation')),
}

class V5SkillContractTests(unittest.TestCase):
 def test_v5_manifest_has_unique_non_overlapping_owners(self):
  self.assertTrue(MANIFEST_PATH.is_file())
  manifest=json.loads(MANIFEST_PATH.read_text())
  self.assertEqual(manifest['version'],5)
  items=manifest['skills']; self.assertEqual(set(x['name'] for x in items),set(EXPECTED))
  owners=[x['ownership'].strip().lower() for x in items]
  self.assertEqual(len(owners),len(set(owners)))

 def test_v5_depth_is_behavioral_not_word_count(self):
  manifest=json.loads(MANIFEST_PATH.read_text()); graph=json.loads(GRAPH_PATH.read_text())['skills']
  for item in manifest['skills']:
   name=item['name']; family,parent,output,anchors=EXPECTED[name]
   self.assertEqual((item['family'],item['parent'],item['output']),(family,parent,output))
   self.assertEqual(graph[name],{'family':family,'parent':parent,'output':output})
   text=(ROOT/'skills'/name/'SKILL.md').read_text()
   self.assertIn(f'**Required parent:** `{parent}`',text)
   self.assertIn(f'`{output}`',text)
   self.assertIn('## Decision Boundary',text)
   self.assertIn('## Evidence',text)
   self.assertIn('## Failure Traps',text)
   for anchor in anchors:
    self.assertIn(anchor.lower(),text.lower(),(name,anchor))
   self.assertNotIn('word count',text.lower())

if __name__=='__main__': unittest.main()
