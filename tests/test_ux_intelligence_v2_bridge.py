import json
from pathlib import Path
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

    def test_bridge_targets_exist_in_canonical_graph_and_checkout(self):
        from nolane_ui.ux_intelligence import UX_CANONICAL_SKILL_BRIDGE

        root = Path(__file__).resolve().parents[1]
        graph = json.loads((root / "skills" / "skill-graph.json").read_text(encoding="utf-8"))
        canonical_skills = graph["skills"]
        for item in UX_CANONICAL_SKILL_BRIDGE:
            self.assertIn(item["canonical_slug"], canonical_skills)
            path = root / item["canonical_path"]
            self.assertTrue(path.is_file(), item["canonical_path"])
            content = path.read_text(encoding="utf-8")
            self.assertIn(f"name: {item['canonical_slug']}", content)


if __name__ == "__main__":
    unittest.main()
