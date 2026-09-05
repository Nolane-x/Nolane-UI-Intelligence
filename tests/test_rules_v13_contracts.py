import copy
import unittest

from nolane_ui.rules_v13.contracts import validate_catalog_v13, validate_rule_v13
from nolane_ui.rules_v13.provenance import validate_provenance_ledger_v13


def sample_rule():
    return {
        "rule_id": "ui.accessibility.keyboard-reachability-v13",
        "domain": "accessibility",
        "class": "mechanical",
        "severity": "major",
        "enforcement": "block",
        "title": "Pointer-exposed actions require an operable non-pointer path",
        "statement": "Functionality exposed through ordinary pointer activation must remain operable through the supported non-pointer interaction path unless the operation intrinsically depends on continuous spatial input.",
        "intent": "Preserve operation for users who cannot or do not use a pointing device without pretending that free-form spatial input has an identical keyboard gesture.",
        "applies_when": ["A user can invoke, change, dismiss, select, or submit an ordinary product action using a pointer or touch target."],
        "does_not_apply_when": ["The operation's meaning intrinsically depends on a continuous free-form spatial path and an equivalent discrete operation would change the task."],
        "failure_modes": ["A supported non-pointer user can reach the surface but cannot invoke functionality that pointer users can invoke."],
        "user_impacts": ["The task becomes partially or completely inoperable for keyboard, switch, voice-control, or other supported alternative-input users."],
        "observables": ["The pointer target has no semantic focusable control, command, menu action, or equivalent supported operation path."],
        "falsifiers": ["A supported non-pointer path completes the same user-visible operation and preserves the same consequential result."],
        "repairs": ["Expose the operation through an appropriate semantic control, command, or equivalent supported input path while preserving the operation's consequence."],
        "exceptions": ["Free-form drawing or continuous spatial manipulation may legitimately require a path-based input while still exposing every separable non-spatial operation independently."],
        "verification": ["Complete the affected workflow without pointer input and confirm the same material operation and recovery path remain available."],
        "owner_hints": ["designing-accessible-interfaces"],
        "verifier_hints": ["critiquing-accessibility"],
        "capabilities": {
            "static": "PARTIAL",
            "dom": "PARTIAL",
            "computed-style": "UNSUPPORTED",
            "browser-runtime": "PARTIAL",
            "interaction": "REQUIRED",
            "accessibility-tree": "REQUIRED",
            "visual-render": "PARTIAL",
            "semantic-product": "REQUIRED",
            "cross-generation": "UNSUPPORTED",
            "human-review": "PARTIAL",
        },
        "provenance_ids": ["nui-internal-accessibility-001"],
        "status": "active",
    }


class RuleV13ContractTests(unittest.TestCase):
    def test_valid_rule_passes(self):
        result = validate_rule_v13(sample_rule())
        self.assertTrue(result["valid"], result["errors"])

    def test_every_operational_plane_is_required(self):
        fields = (
            "intent",
            "applies_when",
            "does_not_apply_when",
            "failure_modes",
            "user_impacts",
            "observables",
            "falsifiers",
            "repairs",
            "exceptions",
            "verification",
            "owner_hints",
            "verifier_hints",
            "capabilities",
            "provenance_ids",
            "status",
        )
        for field in fields:
            with self.subTest(field=field):
                rule = sample_rule()
                rule.pop(field)
                result = validate_rule_v13(rule)
                self.assertFalse(result["valid"])
                self.assertTrue(any(field in error for error in result["errors"]), result["errors"])

    def test_placeholder_strength_prose_is_rejected(self):
        replacements = {
            "title": "Looks bad",
            "statement": "Make it good",
            "intent": "Be better",
            "applies_when": ["When needed"],
            "failure_modes": ["It looks wrong"],
            "user_impacts": ["Bad UX"],
            "observables": ["Seems wrong"],
            "falsifiers": ["Looks fine"],
            "repairs": ["Fix it"],
            "verification": ["Check it"],
        }
        for field, value in replacements.items():
            with self.subTest(field=field):
                rule = sample_rule()
                rule[field] = value
                result = validate_rule_v13(rule)
                self.assertFalse(result["valid"], (field, result))

    def test_non_blocking_classes_cannot_block(self):
        for rule_class in ("advisory", "aesthetic", "convergence"):
            with self.subTest(rule_class=rule_class):
                rule = sample_rule()
                rule["class"] = rule_class
                rule["enforcement"] = "block"
                result = validate_rule_v13(rule)
                self.assertFalse(result["valid"])
                self.assertTrue(any("cannot block" in error for error in result["errors"]), result["errors"])

    def test_minor_or_observation_severity_cannot_block(self):
        for severity in ("minor", "observation"):
            with self.subTest(severity=severity):
                rule = sample_rule()
                rule["severity"] = severity
                result = validate_rule_v13(rule)
                self.assertFalse(result["valid"])

    def test_capabilities_use_closed_vocabulary(self):
        rule = sample_rule()
        rule["capabilities"]["interaction"] = "MAGIC"
        result = validate_rule_v13(rule)
        self.assertFalse(result["valid"])
        self.assertTrue(any("capabilit" in error.lower() for error in result["errors"]))

    def test_catalog_requires_unique_ids_and_no_rule_count_quota(self):
        rule = sample_rule()
        duplicate = copy.deepcopy(rule)
        record = {"version": 13, "rules": [rule, duplicate]}
        result = validate_catalog_v13(record)
        self.assertFalse(result["valid"])
        self.assertTrue(any("duplicate" in error.lower() for error in result["errors"]))

        quota_record = {"version": 13, "minimum_rule_count": 1000, "rules": [sample_rule()]}
        quota_result = validate_catalog_v13(quota_record)
        self.assertFalse(quota_result["valid"])
        self.assertTrue(any("quota" in error.lower() or "minimum_rule_count" in error for error in quota_result["errors"]))


class ProvenanceV13ContractTests(unittest.TestCase):
    def test_valid_provenance_ledger_passes(self):
        ledger = {
            "version": 13,
            "records": [
                {
                    "provenance_id": "nui-internal-accessibility-001",
                    "evidence_class": "internal-derived",
                    "source_id": "nui-v12-reality",
                    "source_role": "canonical-predecessor",
                    "reporter": "NUI independently authored rule system",
                    "reviewed_at": "2026-09-05",
                    "support_role": "Existing NUI operational rule and tests establish the predecessor failure contract.",
                    "contraindications": ["Do not infer that every continuous spatial operation has an identical keyboard gesture."],
                    "transfer_boundary": "Preserve the independently authored NUI failure semantics; do not import third-party rule wording or thresholds.",
                }
            ],
        }
        result = validate_provenance_ledger_v13(ledger)
        self.assertTrue(result["valid"], result["errors"])

    def test_emerging_provenance_cannot_claim_normative_role(self):
        ledger = {
            "version": 13,
            "records": [
                {
                    "provenance_id": "field-001",
                    "evidence_class": "emerging",
                    "source_id": "community-report",
                    "source_role": "normative-standard",
                    "reporter": "community discussion",
                    "reviewed_at": "2026-09-05",
                    "support_role": "Early field report of a possible convergence pattern requiring corroboration before promotion.",
                    "contraindications": ["The pattern may be legitimate for some product contexts."],
                    "transfer_boundary": "Hypothesis only; cannot become a hard gate without independent operational justification.",
                }
            ],
        }
        result = validate_provenance_ledger_v13(ledger)
        self.assertFalse(result["valid"])
        self.assertTrue(any("normative" in error.lower() for error in result["errors"]))


if __name__ == "__main__":
    unittest.main()
