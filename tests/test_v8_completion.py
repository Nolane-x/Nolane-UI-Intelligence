import unittest
from nolane_ui.validators import validate_v8_completion_evidence


class V8CompletionTests(unittest.TestCase):
    def test_plain_task_inherits_prior_gate(self):
        r=validate_v8_completion_evidence({})
        self.assertIn(r['decision'],{'PASS','BLOCKED'})

    def test_agent_export_needs_interop_evidence(self):
        r=validate_v8_completion_evidence({'agent_harness':True})
        self.assertEqual(r['decision'],'BLOCKED')

    def test_external_media_needs_asset_record(self):
        r=validate_v8_completion_evidence({'external_media_used':True})
        self.assertEqual(r['decision'],'BLOCKED')

    def test_subject_media_needs_opportunity_evidence(self):
        r=validate_v8_completion_evidence({'subject_native_media':True})
        self.assertEqual(r['decision'],'BLOCKED')

    def test_custom_media_needs_toolchain_and_brief(self):
        r=validate_v8_completion_evidence({'custom_visual_asset':True})
        self.assertEqual(r['decision'],'BLOCKED')

    def test_material_media_needs_rendered_integration(self):
        r=validate_v8_completion_evidence({'material_media_used':True})
        self.assertEqual(r['decision'],'BLOCKED')

    def test_external_skill_needs_review_record(self):
        r=validate_v8_completion_evidence({'external_agent_skill':True})
        self.assertEqual(r['decision'],'BLOCKED')

    def test_exceptional_visual_claim_needs_flagship_synthesis_evidence(self):
        r=validate_v8_completion_evidence({'visual_ambition':'exceptional'})
        self.assertEqual(r['decision'],'BLOCKED')
        self.assertTrue(any('flagship visual synthesis' in e.lower() for e in r['errors']))


if __name__=='__main__': unittest.main()
