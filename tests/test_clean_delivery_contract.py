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
        leaked = []
        for pattern in ("batch*_finalize*.py", "batch*_graph_integrate.py"):
            leaked.extend(ROOT.joinpath("scripts").glob(pattern))
        for pattern in ("batch*-finalize.yml", "batch*-graph-integrate.yml"):
            leaked.extend(ROOT.joinpath(".github", "workflows").glob(pattern))

        self.assertEqual(
            [],
            sorted(path.relative_to(ROOT).as_posix() for path in leaked),
            "one-time integration tooling leaked into the product tree",
        )

    def test_completed_batches_do_not_ship_pending_checkpoint_artifacts(self):
        checkpoints = sorted(
            path.relative_to(ROOT).as_posix()
            for path in ROOT.joinpath("artifacts").glob("UI-INDUSTRY-1000-BATCH-*-CHECKPOINT.md")
        )
        self.assertEqual([], checkpoints, "completed UI-industry batches must not ship stale pending checkpoints")

    def test_materialized_ui_industry_batches_keep_provenance_records(self):
        records = [
            ROOT / "docs" / "research" / "UI-INDUSTRY-1000-BATCH-001.md",
            ROOT / "docs" / "research" / "UI-INDUSTRY-1000-BATCH-002.md",
            ROOT / "docs" / "research" / "UI-INDUSTRY-1000-BATCH-003.md",
            ROOT / "docs" / "research" / "UI-INDUSTRY-1000-BATCH-004.md",
            ROOT / "docs" / "research" / "UI-INDUSTRY-1000-BATCH-005.md",
            ROOT / "docs" / "research" / "UI-INDUSTRY-1000-BATCH-006.md",
        ]
        for path in records:
            self.assertTrue(path.is_file(), f"missing batch provenance record: {path.relative_to(ROOT)}")

        batch003 = records[2].read_text(encoding="utf-8")
        self.assertIn("## Exact inventory and canonical ownership", batch003)
        self.assertIn("| 100 | `designing-sensor-permission-and-availability`", batch003)
        self.assertIn("no loop, macro, template expander", batch003.lower())

    def test_repository_policy_matches_the_874_node_batch_006_graph(self):
        agents = (ROOT / "AGENTS.md").read_text(encoding="utf-8")
        self.assertIn("**874 canonical skills**", agents)
        self.assertIn("700 independently owned UI-industry specialists", agents)
        self.assertNotIn("currently contains **274 canonical skills**", agents)
        self.assertNotIn("currently contains **374 canonical skills**", agents)


if __name__ == "__main__":
    unittest.main()
