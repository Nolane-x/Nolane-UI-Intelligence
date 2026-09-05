import unittest
from pathlib import Path

from nolane_ui.rules_v13.catalog import load_rule_catalog_v13
from nolane_ui.rules_v13.similarity import audit_catalog_similarity
from nolane_ui.rules_v13.shards import FIRST_WAVE_RULE_IDS


EXPECTED_FIRST_WAVE = {
    # AI / agent execution truth.
    "ui.ai.approval-scope-matches-action",
    "ui.ai.tool-result-attribution",
    "ui.ai.stale-plan-revalidation",
    "ui.ai.interruption-preserves-authority",
    "ui.ai.irreversible-action-last-mile-confirmation",
    "ui.ai.tool-failure-not-success",
    "ui.ai.generated-content-origin-visible",
    "ui.ai.autonomy-boundary-visible",
    # Forms / authentication / account recovery.
    "ui.forms.async-validation-does-not-race",
    "ui.forms.password-manager-compatible",
    "ui.forms.otp-paste-completes-sequence",
    "ui.forms.session-expiry-preserves-draft",
    "ui.forms.server-normalization-visible",
    "ui.forms.conditional-fields-preserve-dependent-data",
    "ui.forms.submit-retry-does-not-double-commit",
    "ui.forms.identity-recovery-does-not-enumerate-secret-state",
    # Data / tables / analytical visualization.
    "ui.data.sort-preserves-row-identity",
    "ui.data.hidden-transformation-count-visible",
    "ui.data.aggregate-scope-explicit",
    "ui.data.chart-uncertainty-not-false-certainty",
    "ui.data.time-series-timezone-basis-visible",
    "ui.data.virtualized-selection-keeps-identity",
    "ui.data.color-legend-distinguishes-state-from-category",
    "ui.data.visualization-has-nonvisual-reading-path",
    # Editors / workspaces / direct manipulation.
    "ui.editor.undo-restores-logical-selection",
    "ui.editor.remote-change-conflict-visible",
    "ui.editor.zoom-preserves-manipulation-target",
    "ui.editor.command-context-matches-focus",
    "ui.editor.unsaved-document-close-recovery",
    "ui.editor.multi-selection-transform-is-atomic",
    "ui.editor.paste-preserves-semantic-structure",
    "ui.editor.background-save-does-not-steal-version",
    # Commerce / consequential transactions.
    "ui.commerce.total-price-components-visible",
    "ui.commerce.currency-before-commit",
    "ui.commerce.inventory-reservation-truth",
    "ui.commerce.payment-pending-not-success",
    "ui.commerce.quantity-scope-before-purchase",
    "ui.commerce.subscription-renewal-basis-visible",
    "ui.commerce.cancellation-scope-explicit",
    "ui.commerce.refund-state-not-instantly-final",
}


class RuleV13AuthorshipQualityTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.root = Path(__file__).resolve().parents[1]
        cls.catalog = load_rule_catalog_v13(cls.root)
        cls.by_id = {rule["rule_id"]: rule for rule in cls.catalog["rules"]}

    def test_first_wave_contract_is_explicit_not_count_driven(self):
        self.assertEqual(set(FIRST_WAVE_RULE_IDS), EXPECTED_FIRST_WAVE)
        self.assertTrue(EXPECTED_FIRST_WAVE <= set(self.by_id))
        self.assertNotIn("minimum_rule_count", self.catalog)
        self.assertNotIn("target_rule_count", self.catalog)
        self.assertFalse(self.catalog["composition"]["rule_count_is_quality_target"])

    def test_each_first_wave_rule_has_distinct_operational_signature(self):
        signatures = {}
        for rule_id in sorted(EXPECTED_FIRST_WAVE):
            rule = self.by_id[rule_id]
            signature = (
                tuple(rule["failure_modes"]),
                tuple(rule["repairs"]),
                tuple(rule["verification"]),
            )
            self.assertNotIn(signature, signatures, (rule_id, signatures.get(signature)))
            signatures[signature] = rule_id

    def test_first_wave_owner_hints_resolve_to_real_canonical_skills(self):
        for rule_id in sorted(EXPECTED_FIRST_WAVE):
            rule = self.by_id[rule_id]
            self.assertTrue(rule["owner_hints"], rule_id)
            for owner in rule["owner_hints"]:
                self.assertTrue((self.root / "skills" / owner / "SKILL.md").is_file(), (rule_id, owner))
            for verifier in rule["verifier_hints"]:
                self.assertTrue((self.root / "skills" / verifier / "SKILL.md").is_file(), (rule_id, verifier))

    def test_first_wave_provenance_is_resolved_and_not_emerging_only(self):
        records = {item["provenance_id"]: item for item in self.catalog["provenance"]["records"]}
        for rule_id in sorted(EXPECTED_FIRST_WAVE):
            rule = self.by_id[rule_id]
            self.assertTrue(rule["provenance_ids"], rule_id)
            evidence_classes = {records[pid]["evidence_class"] for pid in rule["provenance_ids"]}
            self.assertNotEqual(evidence_classes, {"emerging"}, rule_id)

    def test_full_catalog_has_no_duplicate_or_boilerplate_regression(self):
        similarity = audit_catalog_similarity(self.catalog["rules"])
        self.assertTrue(similarity["valid"], similarity)
        self.assertEqual(similarity["duplicate_pair_count"], 0, similarity)
        self.assertEqual(similarity["boilerplate_cluster_count"], 0, similarity)

    def test_rule_source_files_do_not_encode_count_quota_or_loop_generation(self):
        shard_root = self.root / "src" / "nolane_ui" / "rules_v13" / "shards"
        for path in shard_root.glob("*.py"):
            text = path.read_text(encoding="utf-8")
            self.assertNotIn("minimum_rule_count", text, path)
            self.assertNotIn("target_rule_count", text, path)
            self.assertNotIn("for _ in range(", text, path)
            self.assertNotIn("for i in range(", text, path)


if __name__ == "__main__":
    unittest.main()
