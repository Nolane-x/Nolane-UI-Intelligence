import unittest
from nolane_ui.media import validate_asset_provenance_ledger, validate_creative_toolchain_plan, validate_media_opportunity_map, validate_shape_substitution_audit, validate_visual_asset_integration

class V8MediaKernelTests(unittest.TestCase):
    def test_complete_media_map_passes(self):
        r={"opportunities":[{"slot":"hero","semantic_job":"show artifact","preferred_media":["photo"],"fallback":"illustration"}],"subject_native_media":True,"decision":"USE_MEDIA","shape_substitution_risk":"medium"}
        self.assertTrue(validate_media_opportunity_map(r)["valid"])
    def test_shape_accumulation_requests_new_direction(self):
        r={"subject_native_media_available":True,"material_slots":3,"abstract_shape_slots":2,"justified_abstract_slots":0,"examples":[],"replacement_actions":[]}
        self.assertEqual(validate_shape_substitution_audit(r)["decision"],"RE_DIVERGE")
    def test_owned_asset_record_passes(self):
        r={"assets":[{"id":"hero","origin":"project","source_url":"project://hero","license":"OWNED","asset_license_verified":True,"verified_at":"2026-08-14","modification_allowed":True,"commercial_use_allowed":True,"local_transformations":[]}]}
        self.assertTrue(validate_asset_provenance_ledger(r)["valid"])
    def test_asset_record_needs_item_verification(self):
        r={"assets":[{"origin":"source","source_url":"item","license":"CC0","verified_at":"2026-08-14","modification_allowed":True,"commercial_use_allowed":True,"local_transformations":[]}]}
        self.assertFalse(validate_asset_provenance_ledger(r)["valid"])
    def test_generation_plan_needs_render_stage(self):
        r={"goal":"hero","stages":[{"stage":"generate","tool":"visual-tool","authority":"asset creation","output":"asset","human_or_agent_check":"review"}],"fallback":"vector"}
        self.assertFalse(validate_creative_toolchain_plan(r)["valid"])
    def test_one_rendered_state_is_insufficient(self):
        r={"assets":["hero"],"rendered_states":["desktop"],"checks":{},"observed_failures":[],"decision":"PASS"}
        self.assertFalse(validate_visual_asset_integration(r)["valid"])
    def test_complete_integration_record_passes(self):
        checks={k:"PASS" for k in ("semantic_fit","composition_fit","crop_resilience","contrast_with_ui","responsive_recomposition","performance_budget","alt_or_equivalent","rights_provenance")}
        r={"assets":["hero"],"rendered_states":["desktop","mobile"],"checks":checks,"observed_failures":[],"decision":"PASS"}
        self.assertTrue(validate_visual_asset_integration(r)["valid"])

if __name__ == '__main__': unittest.main()
