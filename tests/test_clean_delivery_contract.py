from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]


class CleanDeliveryContractTests(unittest.TestCase):
    def test_registered_verifier_is_read_only_and_has_no_batch_mutation_step(self):
        workflow = (ROOT / ".github" / "workflows" / "verify.yml").read_text(encoding="utf-8")
        self.assertIn("permissions:\n  contents: read", workflow)
        self.assertNotIn("Finalize Batch 002", workflow)
        self.assertNotIn("batch002_docs_finalize.py", workflow)
        self.assertNotIn("git push origin HEAD:build/ui-industry-1000-batch-002", workflow)

    def test_one_time_batch_finalizers_are_absent_from_product_tree(self):
        forbidden = [
            ROOT / "scripts" / "batch002_docs_finalize.py",
            ROOT / ".github" / "workflows" / "batch002-graph-integrate.yml",
            ROOT / "scripts" / "batch002_graph_integrate.py",
        ]
        for path in forbidden:
            self.assertFalse(path.exists(), f"one-time integration tool leaked into product tree: {path.relative_to(ROOT)}")


if __name__ == "__main__":
    unittest.main()
