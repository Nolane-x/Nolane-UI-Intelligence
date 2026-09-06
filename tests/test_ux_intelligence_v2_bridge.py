import unittest

from nolane_ui.ux_intelligence import UX_SKILLS


class UXCanonicalBridgeTests(unittest.TestCase):
    def test_bridge_is_selective_and_resolves_registry_entries(self):
        from nolane_ui.ux_intelligence import UX_CANONICAL_SKILL_BRIDGE

        ids = {item["skill_id"] for item in UX_CANONICAL_SKILL_BRIDGE}
        self.assertEqual(
            ids,
            {
                "identifying-user-goals",
                "mapping-critical-user-journeys",
                "conducting-cognitive-walkthroughs",
                "testing-mental-model-alignment",
                "assessing-recovery-completeness",
                "evaluating-task-success",
            },
        )
        self.assertLess(len(ids), len(UX_SKILLS))

    def test_supported_mechanisms_are_registry_subset(self):
        from nolane_ui.ux_intelligence import UX_CANONICAL_SKILL_BRIDGE

        skills = {item["skill_id"]: item for item in UX_SKILLS}
        for item in UX_CANONICAL_SKILL_BRIDGE:
            self.assertTrue(
                set(item["supported_mechanisms"])
                <= set(skills[item["skill_id"]]["related_mechanisms"])
            )

    def test_bridge_records_are_operational(self):
        from nolane_ui.ux_intelligence import UX_CANONICAL_SKILL_BRIDGE

        for item in UX_CANONICAL_SKILL_BRIDGE:
            self.assertTrue(item["canonical_slug"])
            self.assertEqual(
                item["canonical_path"], f"skills/{item['canonical_slug']}/SKILL.md"
            )
            self.assertTrue(item["reason_for_canonicalization"])
            self.assertTrue(item["required_outputs"])
            self.assertTrue(item["verification_dependencies"])


if __name__ == "__main__":
    unittest.main()
