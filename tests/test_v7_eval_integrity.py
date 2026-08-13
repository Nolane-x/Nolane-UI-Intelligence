import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REQUIRED_PLANES = {
    "evals/v7/authority-conflicts/cases.json",
    "evals/v7/concrete-knowledge/cases.json",
    "evals/v7/rendered-perception/cases.json",
    "evals/v7/fast-path/cases.json",
}
REQUIRED_IDS = {
    "v7-visual-gallery-semantic-authority-smear",
    "v7-apple-platform-genericization",
    "v7-public-service-without-local-research",
    "v7-react-aria-vs-visual-library",
    "v7-shopify-generalized-to-commerce",
    "v7-mcp-authority-inflation",
    "v7-screenshot-theater",
    "v7-pixel-noise-false-regression",
    "v7-fast-path-drops-hard-obligation",
    "v7-style-database-default-convergence",
    "v7-motion-effects-without-temporal-semantics",
    "v7-ai-surface-constant-animation",
}


class V7EvalIntegrityTests(unittest.TestCase):
    def test_manifest_registers_four_planes_and_32_cases(self):
        manifest = json.loads((ROOT / "evals/v7/manifest.json").read_text(encoding="utf-8"))
        self.assertEqual(manifest["version"], 7)
        self.assertEqual(set(manifest["assets"]), REQUIRED_PLANES)
        total = 0; ids = set()
        for rel in manifest["assets"]:
            doc = json.loads((ROOT / rel).read_text(encoding="utf-8"))
            self.assertEqual(doc["version"], 7)
            self.assertEqual(len(doc["cases"]), 8, rel)
            total += len(doc["cases"])
            for case in doc["cases"]:
                self.assertNotIn(case["id"], ids)
                ids.add(case["id"])
        self.assertEqual(total, 32)
        self.assertEqual(manifest["case_count"], 32)
        self.assertTrue(REQUIRED_IDS.issubset(ids), REQUIRED_IDS - ids)

    def test_cases_are_falsifiable_and_owner_mapped(self):
        graph = json.loads((ROOT / "skills/skill-graph.json").read_text(encoding="utf-8"))["skills"]
        manifest = json.loads((ROOT / "evals/v7/manifest.json").read_text(encoding="utf-8"))
        for rel in manifest["assets"]:
            for case in json.loads((ROOT / rel).read_text(encoding="utf-8"))["cases"]:
                self.assertIn(case["evaluator_owner"], graph, case["id"])
                self.assertTrue(case["setup"], case["id"])
                self.assertTrue(case["pressure"], case["id"])
                self.assertIn(case["expected_decision"], {"PASS", "BLOCKED", "RESEARCH_MORE", "RE_DIVERGE"}, case["id"])
                self.assertGreaterEqual(len(case["must_find"]), 2, case["id"])
                self.assertTrue(case["falsifier"], case["id"])
                self.assertTrue(case["recovery"], case["id"])

    def test_closure_doc_covers_all_critique_systems_and_core_gap(self):
        text = (ROOT / "docs/V7-CONCRETE-KNOWLEDGE-CLOSURE.md").read_text(encoding="utf-8").lower()
        for phrase in (
            "adobe spectrum 2", "apple hig", "gov.uk", "uswds", "react aria", "radix",
            "sap fiori", "ant design", "carbon", "atlassian", "shopify polaris", "primer",
            "ui/ux pro max", "shadcn", "mantine", "react bits", "aceternity", "magic ui", "motion",
            "accumulated concrete design knowledge", "biết mình phải suy nghĩ ở đâu", "đã sống trong bài toán đó hàng triệu giờ"
        ):
            self.assertIn(phrase, text, phrase)

    def test_research_doc_declares_no_copy_and_authority_not_access(self):
        text = (ROOT / "docs/research/UI-AUTHORITY-INTELLIGENCE-V7.md").read_text(encoding="utf-8").lower()
        self.assertIn("access protocol is not authority", text)
        self.assertIn("mechanism, not trade dress", text)
        self.assertIn("live verification", text)
        self.assertIn("rendered perception", text)


if __name__ == "__main__":
    unittest.main()
