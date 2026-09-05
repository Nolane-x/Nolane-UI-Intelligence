import copy
import unittest

from nolane_ui.rules_v13.similarity import audit_catalog_similarity, compare_rule_similarity
try:
    from test_rules_v13_contracts import sample_rule
except ModuleNotFoundError:
    from tests.test_rules_v13_contracts import sample_rule


def variant(rule_id, title, failure, repair, verify):
    rule = sample_rule()
    rule["rule_id"] = rule_id
    rule["domain"] = rule_id.split(".")[1]
    rule["title"] = title
    rule["statement"] = title + ". The product must preserve a distinct and testable interaction contract rather than relying on a visually plausible shell."
    rule["intent"] = "Protect a concrete user outcome and keep the rule independently falsifiable through the specified observation and repair boundary."
    rule["failure_modes"] = [failure]
    rule["user_impacts"] = ["The affected user can lose task clarity, operability, or confidence because the interface no longer represents the intended interaction truth."]
    rule["observables"] = [failure]
    rule["falsifiers"] = ["A scoped observation demonstrates that the intended operation remains available and the described failure cannot be reproduced."]
    rule["repairs"] = [repair]
    rule["verification"] = [verify]
    return rule


class RuleV13SimilarityTests(unittest.TestCase):
    def test_exact_operational_duplicate_is_blocked_even_with_new_id(self):
        left = sample_rule()
        right = copy.deepcopy(left)
        right["rule_id"] = "ui.accessibility.keyboard-reachability-copy"
        result = compare_rule_similarity(left, right)
        self.assertTrue(result["duplicate"], result)

    def test_component_noun_substitution_is_detected(self):
        left = variant(
            "ui.components.button-wrapper-template",
            "Repeated button wrapper must not substitute for component semantics",
            "Every button is wrapped in the same decorative shell even when its semantic role differs.",
            "Remove the generic button wrapper and encode treatment from each control role and state.",
            "Inspect representative button roles and confirm their rendering follows role and state rather than one wrapper template.",
        )
        right = copy.deepcopy(left)
        right["rule_id"] = "ui.components.card-wrapper-template"
        for field in ("title", "statement", "intent"):
            right[field] = right[field].replace("button", "card").replace("Button", "Card")
        for field in ("failure_modes", "user_impacts", "observables", "falsifiers", "repairs", "verification"):
            right[field] = [item.replace("button", "card").replace("Button", "Card") for item in right[field]]
        result = compare_rule_similarity(left, right)
        self.assertTrue(result["noun_substitution_suspect"], result)
        self.assertTrue(result["duplicate"], result)

    def test_same_failure_repair_verification_signature_is_blocked(self):
        failure = "A delayed older request overwrites a newer user intent and makes the visible state move backward."
        repair = "Bind state commits to request or version identity so superseded work cannot replace a newer authoritative state."
        verify = "Artificially reorder overlapping responses and confirm only the newest applicable result becomes current."
        left = variant("ui.performance.stale-search-response", "Search responses must not overwrite newer query intent", failure, repair, verify)
        right = variant("ui.state.old-filter-result", "Filter responses must preserve newest intent", failure, repair, verify)
        result = compare_rule_similarity(left, right)
        self.assertTrue(result["signature_duplicate"], result)
        self.assertTrue(result["duplicate"], result)

    def test_legitimate_near_neighbors_remain_distinct(self):
        left = variant(
            "ui.accessibility.keyboard-operation",
            "Interactive functionality requires a supported keyboard operation path",
            "Keyboard users cannot invoke an action that pointer users can invoke.",
            "Expose the same operation through a semantic focusable control or equivalent keyboard command.",
            "Complete the workflow using keyboard input only and confirm the material operation remains available.",
        )
        right = variant(
            "ui.accessibility.focus-visibility",
            "Keyboard focus requires a perceivable current-location indicator",
            "The focused control is operable but the user cannot visually determine which control will receive the next keyboard action.",
            "Render a focus indicator with sufficient perceptual separation across every supported component state.",
            "Tab through every supported component state and compare focused and unfocused rendering at representative contrast modes.",
        )
        result = compare_rule_similarity(left, right)
        self.assertFalse(result["duplicate"], result)

    def test_catalog_reports_boilerplate_concentration(self):
        rules = []
        for noun in ("button", "card", "dialog", "panel"):
            rules.append(variant(
                f"ui.components.{noun}-same-template",
                f"{noun.title()} treatment must preserve product-specific semantics",
                f"The {noun} uses the same generic treatment regardless of task meaning and state.",
                "Replace the generic treatment with a mechanism selected from the actual semantic role and state.",
                "Inspect representative states and confirm the treatment follows semantic role instead of the shared generic template.",
            ))
        result = audit_catalog_similarity(rules)
        self.assertFalse(result["valid"], result)
        self.assertGreater(result["duplicate_pair_count"], 0, result)


if __name__ == "__main__":
    unittest.main()
