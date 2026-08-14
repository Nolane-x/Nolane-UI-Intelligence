import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class V10SkillProtocolTests(unittest.TestCase):
    def _text(self, skill):
        return (ROOT / "skills" / skill / "SKILL.md").read_text(encoding="utf-8")

    def test_product_scope_owner_links_behavior_to_ablation_not_self_claim(self):
        text = self._text("modeling-product-intent")
        for phrase in ("V10 Empirical Scope Hypothesis", "H-SCOPE-BREADTH", "scope-compress", "holdout", "STRUCTURAL_ONLY"):
            self.assertIn(phrase, text)

    def test_visual_owners_distinguish_artifact_quality_from_efficacy(self):
        taste = self._text("exploring-aesthetic-directions")
        critic = self._text("critiquing-visual-design")
        fidelity = self._text("verifying-design-fidelity")
        for phrase, text in (
            ("H-TASTE-COMPARATIVE", taste),
            ("pairwise blinded evidence", taste),
            ("H-RENDER-CRITIQUE-CAUSAL", critic),
            ("repair effectiveness", critic),
            ("H-RENDER-FIDELITY", fidelity),
            ("artifact evidence is not efficacy evidence", fidelity),
        ):
            self.assertIn(phrase, text)

    def test_root_protocol_forbids_hidden_rubric_leakage_and_empirical_overclaim(self):
        using = self._text("using-nolane-ui")
        controller = self._text("nolane-ui")
        routing = self._text("routing-ui-work")
        self.assertIn("hidden evaluator rubric", using)
        self.assertIn("EMPIRICAL_TRANSFER", controller)
        self.assertIn("empirical-evaluation", routing)
        self.assertIn("ablation", routing.lower())

    def test_owner_extensions_are_not_one_copy_pasted_template(self):
        skills = [
            "modeling-product-intent", "inventorying-product-capabilities", "architecting-information",
            "designing-authentication-and-passkeys", "designing-editor-canvas-workspaces",
            "designing-desktop-windowed-workspaces", "modeling-users-and-tasks",
            "exploring-aesthetic-directions", "critiquing-visual-design", "verifying-design-fidelity",
            "designing-motion", "engineering-rich-interactive-components",
        ]
        tails = []
        for skill in skills:
            text = self._text(skill)
            marker = "## V10"
            self.assertIn(marker, text, skill)
            tails.append(text[text.index(marker):])
        self.assertGreaterEqual(len(set(tails)), len(skills) - 1)


if __name__ == "__main__":
    unittest.main()
