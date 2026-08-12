import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REQUIRED = json.loads((ROOT / "evals/v2/coverage/required-domains.json").read_text(encoding="utf-8"))


class IndustryAtlasContractTests(unittest.TestCase):
    def test_mandatory_surfaces_exist_in_atlas(self):
        path = ROOT / "knowledge/ui-domain-atlas.json"
        self.assertTrue(path.is_file(), "v2 requires knowledge/ui-domain-atlas.json")
        atlas = json.loads(path.read_text(encoding="utf-8"))
        surfaces = set(atlas.get("axes", {}).get("surfaces", []))
        self.assertEqual(set(REQUIRED["mandatory_surfaces"]), set(REQUIRED["mandatory_surfaces"]) & surfaces)

    def test_every_mandatory_surface_has_owner_and_verifier_skills(self):
        atlas_path = ROOT / "knowledge/ui-domain-atlas.json"
        graph_path = ROOT / "skills/skill-graph.json"
        self.assertTrue(atlas_path.is_file(), "industry atlas is missing")
        atlas = json.loads(atlas_path.read_text(encoding="utf-8"))
        graph = json.loads(graph_path.read_text(encoding="utf-8"))["skills"]
        cells = {cell["id"]: cell for cell in atlas.get("coverage_cells", [])}
        for surface in REQUIRED["mandatory_surfaces"]:
            cell = cells.get(f"surface:{surface}")
            self.assertIsNotNone(cell, f"missing coverage cell for surface {surface}")
            owners = cell.get("owner_skills", [])
            verifiers = cell.get("verifier_skills", [])
            self.assertTrue(owners, f"surface {surface} has no owner skill")
            self.assertTrue(verifiers, f"surface {surface} has no verifier skill")
            self.assertTrue(all(name in graph for name in owners), f"surface {surface} references undeclared owner")
            self.assertTrue(all(name in graph for name in verifiers), f"surface {surface} references undeclared verifier")


if __name__ == "__main__":
    unittest.main()
