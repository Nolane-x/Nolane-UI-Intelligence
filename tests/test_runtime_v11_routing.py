import unittest

from nolane_ui.runtime_v11.routing import route_runtime_finding, route_runtime_findings


RULE = {
    "rule_id": "runtime.layout.example",
    "domain": "layout-integrity",
    "class": "contextual",
    "tier": "session",
    "severity": "major",
    "engines": ["text"],
    "description": "Example observable layout defect.",
    "falsifier": "A bounded re-observation proves the defect is absent.",
    "owner_hints": ["owner-layout", "owner-missing", "owner-layout", "owner-responsive"],
    "source_provenance": {
        "kind": "independent-nui-rule",
        "implementation": "independently-authored",
    },
}
REGISTRY = {"version": 11, "rules": [RULE]}
SKILL_GRAPH = {
    "version": 2,
    "root": "using-nolane-ui",
    "skills": {
        "using-nolane-ui": {"parent": None},
        "owner-layout": {"parent": "using-nolane-ui"},
        "owner-responsive": {"parent": "using-nolane-ui"},
    },
}
FINDING = {
    "finding_id": "runtime.layout.example:abc",
    "domain": "layout-integrity",
    "severity": "major",
    "evidence": ["src/app.tsx:10"],
    "violated_constraint": "Example observable layout defect.",
    "user_impact": "Layout can become unusable.",
    "falsifier": "A bounded re-observation proves the defect is absent.",
    "recommended_repair": "Route to the existing layout owner.",
    "status": "open",
    "runtime": {
        "rule_id": "runtime.layout.example",
        "path": "src/app.tsx",
        "line": 10,
        "engine": "text",
    },
}


class RuntimeV11RoutingTests(unittest.TestCase):
    def test_resolves_only_existing_owner_hints_without_synthesizing_ownership(self):
        route = route_runtime_finding(FINDING, REGISTRY, SKILL_GRAPH)
        self.assertEqual(route["status"], "ROUTED")
        self.assertEqual(route["owners"], ["owner-layout", "owner-responsive"])
        self.assertEqual(route["unresolved_owner_hints"], ["owner-missing"])
        self.assertTrue(route["evidence_only"])
        self.assertEqual(route["finding_id"], FINDING["finding_id"])
        self.assertEqual(route["rule_id"], RULE["rule_id"])

    def test_unknown_rule_is_explicit_and_never_invents_owner(self):
        finding = {**FINDING, "runtime": {**FINDING["runtime"], "rule_id": "runtime.unknown.rule"}}
        route = route_runtime_finding(finding, REGISTRY, SKILL_GRAPH)
        self.assertEqual(route["status"], "UNKNOWN_RULE")
        self.assertEqual(route["owners"], [])
        self.assertEqual(route["unresolved_owner_hints"], [])
        self.assertTrue(route["evidence_only"])
        self.assertIn("registry", route["reason"].lower())

    def test_known_rule_with_no_resolvable_owner_is_unresolved(self):
        registry = {"version": 11, "rules": [{**RULE, "owner_hints": ["missing-a", "missing-b"]}]}
        route = route_runtime_finding(FINDING, registry, SKILL_GRAPH)
        self.assertEqual(route["status"], "UNRESOLVED")
        self.assertEqual(route["owners"], [])
        self.assertEqual(route["unresolved_owner_hints"], ["missing-a", "missing-b"])
        self.assertTrue(route["evidence_only"])

    def test_batch_routes_are_stable_and_report_unresolved_count(self):
        finding_b = {**FINDING, "finding_id": "z-finding"}
        finding_a = {**FINDING, "finding_id": "a-finding"}
        batch = route_runtime_findings([finding_b, finding_a], REGISTRY, SKILL_GRAPH)
        self.assertEqual([item["finding_id"] for item in batch["routes"]], ["a-finding", "z-finding"])
        self.assertEqual(batch["route_count"], 2)
        self.assertEqual(batch["unresolved_route_count"], 0)
        self.assertEqual(batch["unresolved_hint_count"], 2)
        self.assertTrue(batch["evidence_only"])

    def test_duplicate_owner_hints_preserve_first_registry_order(self):
        route = route_runtime_finding(FINDING, REGISTRY, SKILL_GRAPH)
        self.assertEqual(route["owners"], ["owner-layout", "owner-responsive"])
        self.assertEqual(route["unresolved_owner_hints"], ["owner-missing"])


if __name__ == "__main__":
    unittest.main()
