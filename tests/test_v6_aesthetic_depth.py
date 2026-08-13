import unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]

OBLIGATIONS={
'preserving-experiential-intent':['affective invariant ledger','semantic compression loss','source-language checkpoint','intent contradiction test','recovery trigger'],
'directing-visual-ambition':['ambition budget','evidence escalation ladder','ambition mismatch','de-escalation rule','quality floor'],
'modeling-aspirational-identity':['competence ritual','status projection trap','power without false capability','identity contradiction','symbolic object audit'],
'composing-spatial-dramaturgy':['spatial beat map','compression-to-release','viewport occupation curve','spatial climax','dramaturgy falsification'],
'detecting-aesthetic-attractors':['mechanism co-occurrence','attractor concentration','removal-cost test','aesthetic entropy','anti-timidity countercheck'],
'engineering-visual-legibility':['resolved-font delta','compound legibility risk','zoom-reflow probe','occlusion audit','reading-distance context'],
'directing-visual-energy':['energy topology','chroma mass map','quiet-field ratio','luminance excursion','energy contradiction'],
'deepening-signature-mechanisms':['signature causal chain','recognition-without-logo','copyability test','failure-if-removed','signature saturation'],
'proving-visual-encoding-semantics':['channel truth table','perceptual ordering','decorative quarantine','uncertainty encoding','legend dependency audit'],
'critiquing-aesthetic-adequacy':['thesis adequacy','blind comparison','reference-frontier delta','intent-to-render gap','execution-success trap'],
'escaping-aesthetic-basins':['local-optimum signature','plateau detector','direction mutation','re-divergence threshold','basin relapse'],
'evaluating-perceptual-diversity':['screen-family signature','recurrence justification','template fingerprint','coherence-versus-repetition','cross-surface entropy'],
'testing-skill-interactions':['factorial matrix','antagonistic interaction','synergistic interaction','semantic force mutation','critic lineage'],
'crafting-typography':['optical-size decision','x-height and width','script stress matrix','line-box geometry','font-loading failure'],
'crafting-color':['perceptual color space','gamut clipping','simultaneous contrast','semantic tone ladder','dark-mode inversion'],
'crafting-spacing-and-rhythm':['density ladder','baseline rhythm','optical spacing correction','touch-target exception','rhythm discontinuity'],
'crafting-depth-and-surfaces':['material hierarchy','light-model consistency','occlusion ownership','boundary-density budget','transparency failure'],
'directing-iconography-and-imagery':['symbol grammar','optical grid','metaphor collision','cultural interpretation','asset provenance'],
'composing-layouts':['intrinsic sizing','content-driven breakpoint','asymmetry budget','constraint graph','layout failure envelope'],
'preventing-generic-ui':['blind-product substitution','reference substitution test','mechanism necessity','genericity fingerprint','timidity failure'],
'critiquing-visual-design':['squint test','grayscale hierarchy','saliency path','rhythm fracture','material inconsistency'],
'critiquing-user-experience':['information scent','time-to-action','recovery cost','mode error','state visibility'],
'critiquing-design-system':['token semantic drift','component escape hatch','variant explosion','cross-surface consistency','governance debt']
}

class V6AestheticDepthTests(unittest.TestCase):
    def test_focus_skills_have_unique_behavioral_obligations(self):
        failures=[]
        for skill,terms in OBLIGATIONS.items():
            text=(ROOT/'skills'/skill/'SKILL.md').read_text(encoding='utf-8').lower()
            missing=[t for t in terms if t.lower() not in text]
            if missing: failures.append((skill,missing))
        self.assertFalse(failures, failures)

    def test_each_focus_skill_has_explicit_falsification_and_recovery_behavior(self):
        failures=[]
        for skill in OBLIGATIONS:
            text=(ROOT/'skills'/skill/'SKILL.md').read_text(encoding='utf-8').lower()
            if 'falsif' not in text or 'recovery' not in text:
                failures.append(skill)
        self.assertFalse(failures,failures)

    def test_focus_obligation_vocabulary_is_not_copy_pasted(self):
        all_terms=[t for terms in OBLIGATIONS.values() for t in terms]
        self.assertEqual(len(all_terms),len(set(all_terms)))

if __name__=='__main__': unittest.main()
