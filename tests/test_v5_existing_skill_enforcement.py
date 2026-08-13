import unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
REQUIRED={
 'ui-contracting':('EXPERIENTIAL_INTENT','operationalization','supplement'),
 'routing-ui-work':('visual_ambition','flagship','hard route'),
 'modeling-users-and-tasks':('aspirational identity','role fantasy'),
 'exploring-aesthetic-directions':('at least three','rendered candidates','materially different'),
 'researching-visual-references':('reference frontier','high visual freedom','exceptional'),
 'composing-layouts':('spatial dramaturgy','magnitude'),
 'preventing-generic-ui':('accumulation','subject specificity','removal cost'),
 'crafting-depth-and-surfaces':('boundary density','material variety','quiet region'),
 'crafting-spacing-and-rhythm':('legibility floor','expert'),
 'crafting-typography':('11px','resolved font','computed'),
 'crafting-color':('visual energy','restraint','chroma mass'),
 'directing-visual-hierarchy':('PX','experiential identity'),
 'directing-iconography-and-imagery':('high visual ambition','procedural','media role'),
 'designing-data-visualization':('encoding provenance','visualization grammar','channel'),
 'designing-motion':('dynamic information','propagation','reduced motion'),
 'critiquing-visual-design':('execution critic','adequacy critic'),
 'challenging-ui-designs':('correlation_class','epistemic','same-model'),
 'iterating-rendered-visual-design':('RE_DIVERGE','reference frontier','basin'),
 'gating-ui-completion':('aesthetic adequacy','render health','high visual ambition'),
}
class ExistingSkillV5EnforcementTests(unittest.TestCase):
 def test_existing_owners_include_v5_enforcement_hooks(self):
  for name,anchors in REQUIRED.items():
   text=(ROOT/'skills'/name/'SKILL.md').read_text(encoding='utf-8').lower()
   for anchor in anchors:
    self.assertIn(anchor.lower(),text,(name,anchor))
if __name__=='__main__': unittest.main()
