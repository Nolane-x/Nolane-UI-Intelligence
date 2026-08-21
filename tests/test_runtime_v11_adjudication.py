import unittest

from nolane_ui.runtime_v11.adjudication import adjudicate_match, adjudicate_findings


CONTEXTUAL_RULE = {
    "rule_id": "runtime.accessibility.focus-visibility-suppressed",
    "domain": "accessibility-mechanics",
    "class": "contextual",
    "tier": "session",
    "severity": "major",
    "engines": ["css"],
    "description": "Focus visibility is suppressed.",
    "falsifier": "A visible replacement focus indicator exists.",
    "owner_hints": ["designing-accessible-interfaces"],
    "source_provenance": {"kind": "independent-nui-rule", "mechanism_sources": [], "implementation": "independently-authored"},
}

MECHANICAL_RULE = {
    **CONTEXTUAL_RULE,
    "rule_id": "runtime.integrity.broken-image-src",
    "domain": "runtime-integrity",
    "class": "mechanical",
    "description": "Image source is broken.",
    "falsifier": "The runtime supplies a valid asset before render.",
}

FINDING = {
    "finding_id": "runtime.accessibility.focus-visibility-suppressed:abc",
    "domain": "accessibility-mechanics",
    "severity": "major",
    "evidence": ["src/app.css:9: outline: none"],
    "violated_constraint": "Focus visibility is suppressed.",
    "user_impact": "Keyboard focus can disappear.",
    "falsifier": "A visible replacement focus indicator exists.",
    "recommended_repair": "Restore a visible focus treatment.",
    "status": "open",
    "runtime": {
        "rule_id": "runtime.accessibility.focus-visibility-suppressed",
        "rule_class": "contextual",
        "path": "src/app.css",
        "line": 9,
        "engine": "css",
        "snippet": "outline: none",
    },
}


class RuntimeV11AdjudicationTests(unittest.TestCase):
    def test_contextual_rule_without_authority_is_unknown(self):
        result = adjudicate_match(FINDING, CONTEXTUAL_RULE)
        self.assertEqual(result["disposition"], "unknown")
        self.assertIn("authority", result["reason"].lower())

    def test_explicit_file_scoped_exception_is_accepted(self):
        exception = {
            "rule_id": CONTEXTUAL_RULE["rule_id"],
            "file": "src/app.css",
            "authority": "DESIGN.md focus contract",
            "reason": "A stronger box-shadow focus ring is rendered by the component state.",
            "created_revision": "abc123",
        }
        result = adjudicate_match(FINDING, CONTEXTUAL_RULE, exceptions=[exception])
        self.assertEqual(result["disposition"], "accepted-exception")
        self.assertEqual(result["exception"]["created_revision"], "abc123")
        self.assertEqual(result["exception"]["file"], "src/app.css")

    def test_broad_exception_without_file_scope_is_not_applied(self):
        exception = {
            "rule_id": CONTEXTUAL_RULE["rule_id"],
            "authority": "team preference",
            "reason": "Ignore this everywhere",
            "created_revision": "abc123",
        }
        result = adjudicate_match(FINDING, CONTEXTUAL_RULE, exceptions=[exception])
        self.assertEqual(result["disposition"], "unknown")
        self.assertTrue(any("file" in error.lower() for error in result["exception_errors"]))

    def test_context_can_confirm_contextual_violation(self):
        context = {"confirmed_violations": [CONTEXTUAL_RULE["rule_id"]]}
        result = adjudicate_match(FINDING, CONTEXTUAL_RULE, context=context)
        self.assertEqual(result["disposition"], "finding")

    def test_mechanical_rule_remains_finding_without_explicit_exception(self):
        finding = {**FINDING, "runtime": {**FINDING["runtime"], "rule_id": MECHANICAL_RULE["rule_id"], "rule_class": "mechanical"}}
        result = adjudicate_match(finding, MECHANICAL_RULE)
        self.assertEqual(result["disposition"], "finding")

    def test_batch_preserves_three_disposition_buckets(self):
        mechanical_finding = {**FINDING, "finding_id": "broken:1", "runtime": {**FINDING["runtime"], "rule_id": MECHANICAL_RULE["rule_id"], "rule_class": "mechanical"}}
        batch = adjudicate_findings(
            [mechanical_finding, FINDING],
            {"version": 11, "rules": [MECHANICAL_RULE, CONTEXTUAL_RULE]},
        )
        self.assertEqual(len(batch["findings"]), 1)
        self.assertEqual(len(batch["unknowns"]), 1)
        self.assertEqual(len(batch["accepted_exceptions"]), 0)


if __name__ == "__main__":
    unittest.main()
