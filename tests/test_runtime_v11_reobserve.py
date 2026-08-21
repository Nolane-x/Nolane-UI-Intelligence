import unittest

from nolane_ui.runtime_v11.reobserve import compare_runtime_observations


def finding(finding_id, rule_id="runtime.layout.example", path="src/app.tsx", line=10, locator=None):
    runtime = {"rule_id": rule_id, "path": path, "engine": "text"}
    if line is not None:
        runtime["line"] = line
    if locator is not None:
        runtime["locator"] = locator
    return {
        "finding_id": finding_id,
        "domain": "layout-integrity",
        "severity": "major",
        "evidence": [f"{path}:{line}"],
        "violated_constraint": "Observed runtime defect.",
        "user_impact": "The rendered interaction can fail.",
        "falsifier": "A bounded re-observation proves the same scoped defect is absent.",
        "recommended_repair": "Repair then re-observe the same scope.",
        "status": "open",
        "runtime": runtime,
    }


class RuntimeV11ReobserveTests(unittest.TestCase):
    def test_absent_prior_finding_resolves_only_when_capabilities_are_complete(self):
        result = compare_runtime_observations([finding("before-1")], [], capabilities_complete=True)
        self.assertEqual(result["closures"][0]["status"], "RESOLVED")
        self.assertEqual(result["counts"], {"resolved": 1, "persisted": 0, "unknown": 0, "regression": 0})
        self.assertEqual(result["decision"], "CLEAN")
        self.assertEqual(result["claim_boundary"], "runtime-closure-only")

    def test_same_scoped_finding_persists(self):
        result = compare_runtime_observations(
            [finding("before-1")],
            [finding("after-1")],
            capabilities_complete=True,
        )
        closure = result["closures"][0]
        self.assertEqual(closure["status"], "PERSISTED")
        self.assertEqual(closure["matched_finding_id"], "after-1")
        self.assertEqual(result["decision"], "OPEN")

    def test_missing_capability_keeps_absent_prior_finding_unknown(self):
        result = compare_runtime_observations([finding("before-1")], [], capabilities_complete=False)
        self.assertEqual(result["closures"][0]["status"], "UNKNOWN")
        self.assertEqual(result["decision"], "UNKNOWN")
        self.assertEqual(result["counts"]["unknown"], 1)

    def test_after_only_finding_is_regression(self):
        result = compare_runtime_observations(
            [finding("before-1", line=10)],
            [finding("after-new", rule_id="runtime.layout.other", line=40)],
            capabilities_complete=True,
        )
        self.assertEqual(result["closures"][0]["status"], "RESOLVED")
        self.assertEqual([item["finding_id"] for item in result["regressions"]], ["after-new"])
        self.assertEqual(result["counts"]["regression"], 1)
        self.assertEqual(result["decision"], "OPEN")

    def test_different_line_or_locator_does_not_false_match_prior_scope(self):
        before = finding("before-1", line=10, locator="#primary")
        after = finding("after-1", line=11, locator="#secondary")
        result = compare_runtime_observations([before], [after], capabilities_complete=True)
        self.assertEqual(result["closures"][0]["status"], "RESOLVED")
        self.assertEqual(result["regressions"][0]["finding_id"], "after-1")

    def test_duplicate_scope_uses_multiset_matching_not_set_collapse(self):
        before = [finding("before-a"), finding("before-b")]
        after = [finding("after-a")]
        result = compare_runtime_observations(before, after, capabilities_complete=True)
        statuses = [item["status"] for item in result["closures"]]
        self.assertEqual(statuses.count("PERSISTED"), 1)
        self.assertEqual(statuses.count("RESOLVED"), 1)
        self.assertEqual(result["counts"]["regression"], 0)

    def test_output_order_is_deterministic(self):
        before = [finding("z-before", line=30), finding("a-before", line=10)]
        after = [finding("z-after", line=30), finding("a-regression", rule_id="runtime.new", line=5)]
        result = compare_runtime_observations(before, after, capabilities_complete=True)
        self.assertEqual([item["finding_id"] for item in result["closures"]], ["a-before", "z-before"])
        self.assertEqual([item["finding_id"] for item in result["regressions"]], ["a-regression"])


if __name__ == "__main__":
    unittest.main()
