import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class V9KnowledgeTests(unittest.TestCase):
    def load(self, name):
        return json.loads((ROOT / "knowledge" / name).read_text(encoding="utf-8"))

    def test_benchmark_gallery_is_curated_mechanism_memory_not_copy_catalog(self):
        data = self.load("v9-design-benchmark-gallery.json")
        self.assertEqual(data["version"], 9)
        refs = data["references"]
        self.assertGreaterEqual(len(refs), 12)
        self.assertEqual(len({r["id"] for r in refs}), len(refs))
        categories = {r["category"] for r in refs}
        self.assertGreaterEqual(len(categories), 5)
        for ref in refs:
            self.assertTrue(ref["source"])
            self.assertGreaterEqual(len(ref["mechanisms"]), 2)
            self.assertTrue(ref["anti_copy"])
            self.assertTrue(ref["refresh_policy"])

    def test_domain_signatures_have_strategy_and_audience_axes(self):
        data = self.load("v9-domain-signatures.json")
        self.assertEqual(data["version"], 9)
        domains = data["domains"]
        self.assertGreaterEqual(len(domains), 8)
        required = {"fintech", "medtech", "developer-tools", "creative-tools", "ai-products", "education", "commerce"}
        self.assertTrue(required.issubset({d["id"] for d in domains}))
        for domain in domains:
            for key in ("trust_profile", "density_expectation", "emotional_profile", "interaction_tone", "risk_profile", "audience_variants", "anti_patterns"):
                self.assertIn(key, domain)
            self.assertGreaterEqual(len(domain["audience_variants"]), 2)

    def test_render_fidelity_knowledge_bridges_design_to_runtime(self):
        data = self.load("v9-render-fidelity.json")
        self.assertEqual(data["version"], 9)
        self.assertGreaterEqual(len(data["token_dimensions"]), 8)
        self.assertGreaterEqual(len(data["component_constraints"]), 8)
        self.assertGreaterEqual(len(data["default_chrome_audit"]), 10)
        self.assertGreaterEqual(len(data["motion_semantics"]), 5)
        self.assertGreaterEqual(len(data["visual_regression_obligations"]), 5)
        joined = json.dumps(data).lower()
        self.assertIn("scrollbar", joined)
        self.assertIn("reduced motion", joined)
        self.assertIn("runtime", joined)


if __name__ == "__main__":
    unittest.main()
