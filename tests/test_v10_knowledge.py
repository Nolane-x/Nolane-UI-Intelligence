import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class V10KnowledgeTests(unittest.TestCase):
    def test_hypotheses_are_falsifiable_and_cross_linked(self):
        data = json.loads((ROOT / "knowledge/v10-behavioral-hypotheses.json").read_text(encoding="utf-8"))
        self.assertEqual(data["version"], 10)
        self.assertGreaterEqual(len(data["hypotheses"]), 12)
        for h in data["hypotheses"]:
            for field in ("owners", "positive_controls", "negative_controls", "evidence_channels", "falsifiers", "dimensions", "tasks", "mutations", "ablations", "prohibited_overclaims"):
                self.assertTrue(h[field], f"{h['hypothesis_id']} missing {field}")

    def test_corpus_has_48_original_tasks_12_families_and_holdout_per_family(self):
        public = json.loads((ROOT / "benchmarks/v10/tasks-public.json").read_text(encoding="utf-8"))
        hidden = json.loads((ROOT / "benchmarks/v10/tasks-hidden.json").read_text(encoding="utf-8"))
        self.assertEqual(len(public["tasks"]), 48)
        self.assertEqual({x["id"] for x in public["tasks"]}, {x["id"] for x in hidden["tasks"]})
        families = {x["family"] for x in public["tasks"]}
        self.assertEqual(len(families), 12)
        for family in families:
            items = [x for x in public["tasks"] if x["family"] == family]
            self.assertEqual(len(items), 4)
            self.assertEqual(sum(x["split"] == "holdout" for x in items), 1)
            self.assertEqual({x["complexity"] for x in items}, {"low", "medium", "high"})

    def test_source_ledger_is_primary_mechanism_level_and_non_authority_smearing(self):
        data = json.loads((ROOT / "knowledge/v10-empirical-evaluation-sources.json").read_text(encoding="utf-8"))
        self.assertEqual(data["version"], 10)
        self.assertGreaterEqual(len(data["sources"]), 5)
        for source in data["sources"]:
            for field in ("primary_url", "source_type", "authority_role", "inspected_mechanisms", "transfer_boundary", "contraindications", "drift_posture", "v10_uses"):
                self.assertTrue(source[field], f"{source['id']} missing {field}")
            self.assertNotEqual(source["authority_role"], "global-design-authority")

    def test_mutations_include_targeted_and_placebo_controls(self):
        data = json.loads((ROOT / "benchmarks/v10/mutations.json").read_text(encoding="utf-8"))
        kinds = {x["kind"] for x in data["mutations"]}
        self.assertIn("semantic", kinds)
        self.assertIn("placebo", kinds)
        self.assertGreaterEqual(len(data["mutations"]), 16)


if __name__ == "__main__":
    unittest.main()
