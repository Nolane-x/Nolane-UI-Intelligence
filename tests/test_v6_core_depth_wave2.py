import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

OBLIGATIONS = {
    'using-nolane-ui': ['task-profile checksum','route-justification ledger','capability-evidence boundary','omission declaration','bootstrap recovery path'],
    'modeling-product-intent': ['outcome-to-capability map','invariant-versus-preference','anti-goal register','success-observability plan','intent drift test'],
    'architecting-information': ['object-action taxonomy','polyhierarchy decision','retrieval-path budget','information-scent probe','scale-growth simulation'],
    'designing-task-flows': ['commit-point map','interruption re-entry contract','partial-success semantics','reversible-edge audit','flow dead-end probe'],
    'designing-interactions': ['input-to-state transition table','acquisition-cost check','interruption-and-cancel path','optimistic-action rollback','mode-visibility probe'],
    'modeling-component-semantics': ['role-action-state invariant','native-first semantic decision','semantic surface area','accessible-name computation','composition ownership test'],
    'modeling-component-states': ['state orthogonality matrix','impossible-state elimination','derived-versus-stored decision','cross-component synchronization','transition completeness probe'],
    'designing-forms': ['field-dependency graph','validation-timing policy','draft-persistence contract','error-summary focus path','autofill-and-input-mode audit'],
    'designing-navigation': ['place-versus-mode test','wayfinding cue stack','deep-link history contract','navigation-state persistence','hierarchy-growth stress'],
    'designing-search': ['query-intent model','result-confidence contract','facet-state persistence','zero-result recovery strategy','ranking-feedback loop'],
    'writing-interface-copy': ['action-semantic alignment','referent precision audit','irreversible-consequence wording','localization expansion budget','error-repair copy'],
    'directing-visual-hierarchy': ['saliency budget','task-priority projection','hierarchy-channel redundancy','glance-path hypothesis','hierarchy collapse test'],
    'architecting-design-tokens': ['semantic alias graph','mode-invariance contract','literal-escape audit','token lifecycle policy','theme-drift probe'],
    'architecting-component-systems': ['primitive-to-composite boundary','extension-point budget','variant-authority map','escape-hatch debt','component evolution contract'],
    'adapting-responsive-layouts': ['relationship-preservation map','reflow-versus-transform','container-query decision','responsive state continuity','content-breakpoint probe'],
    'adapting-platform-conventions': ['native-convention delta','system-gesture collision','platform chrome contract','safe-area behavior','fallback-parity test'],
    'designing-localized-interfaces': ['bidirectional-isolation audit','script-specific line breaking','locale-format semantics','expansion stress envelope','cultural-assumption falsifier'],
    'designing-motion': ['temporal-information budget','continuity-anchor map','interruption graph','reduced-motion semantic equivalence','settling-envelope test'],
    'designing-data-dense-interfaces': ['information-compression ratio','comparison-anchor map','frozen-context contract','filter-sort provenance','density degradation probe'],
    'designing-data-visualization': ['analytic-question mapping','encoding-capacity budget','scale-and-baseline audit','interaction-to-insight trace','uncertainty legibility probe'],
    'designing-empty-loading-error-states': ['uncertainty-state taxonomy','skeleton-truth test','partial-data policy','retry-idempotency contract','stale-data disclosure'],
    'designing-onboarding': ['first-value path','activation horizon','progressive-commitment schedule','sample-data truth boundary','skip-and-reentry contract'],
    'verifying-design-fidelity': ['authoritative-target graph','semantic-versus-pixel invariant','dynamic-state parity','font-and-viewport lock','diff false-positive audit'],
    'critiquing-responsive-behavior': ['breakpoint discontinuity scan','relationship-loss test','capability-parity audit','zoom-reflow stress','orientation-transition probe'],
    'critiquing-platform-fit': ['platform-affordance mismatch','convention-cost ledger','system-integration gap','input-modality conflict','platform-native counterexample'],
    'designing-screen-reader-experiences': ['virtual-cursor versus focus','name-role-value trace','live-region cadence','dom-visual-order audit','focus-restoration contract'],
    'designing-low-vision-and-high-contrast': ['magnification viewport','forced-colors contract','non-text contrast map','color-dependence falsifier','target-separation audit'],
}

class V6CoreDepthWave2Tests(unittest.TestCase):
    def test_each_core_owner_contains_its_bespoke_behavioral_obligations(self):
        failures = []
        for skill, terms in OBLIGATIONS.items():
            text = (ROOT / 'skills' / skill / 'SKILL.md').read_text(encoding='utf-8').lower()
            missing = [term for term in terms if term not in text]
            if missing:
                failures.append((skill, missing))
        self.assertFalse(failures, failures)

    def test_each_core_owner_contains_explicit_falsification_and_recovery(self):
        failures = []
        for skill in OBLIGATIONS:
            text = (ROOT / 'skills' / skill / 'SKILL.md').read_text(encoding='utf-8').lower()
            if 'falsif' not in text or 'recovery' not in text:
                failures.append(skill)
        self.assertFalse(failures, failures)

    def test_wave2_vocabulary_is_unique_and_production_gate_tracks_it(self):
        flattened = [term for terms in OBLIGATIONS.values() for term in terms]
        self.assertEqual(len(flattened), len(set(flattened)))
        record = json.loads((ROOT / 'knowledge' / 'v6-depth-focus-obligations.json').read_text(encoding='utf-8'))
        tracked = record['skills']
        missing = [skill for skill in OBLIGATIONS if skill not in tracked]
        self.assertFalse(missing, missing)
        mismatched = [skill for skill, terms in OBLIGATIONS.items() if tracked.get(skill) != terms]
        self.assertFalse(mismatched, mismatched)

if __name__ == '__main__':
    unittest.main()
