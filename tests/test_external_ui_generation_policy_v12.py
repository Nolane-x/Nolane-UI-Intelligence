import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class ExternalUIGenerationPolicyV12Tests(unittest.TestCase):
    def text(self, path):
        return (ROOT / path).read_text(encoding="utf-8")

    def test_agent_policy_makes_reference_execution_non_optional_for_material_ui(self):
        text = self.text("AGENTS.md")
        self.assertIn("V12.1 external UI generation enforcement", text)
        self.assertIn("material UI generation MUST", text)
        self.assertIn("ACTIVE", text)
        self.assertIn("EVALUATED_NO_MATCH", text)
        self.assertIn("permissive", text.lower())

    def test_bootstrap_emits_reference_execution_contract_not_only_reference_prose(self):
        text = self.text("skills/using-nolane-ui/SKILL.md")
        self.assertIn("V12.1 Generation-Time Hard Gate", text)
        self.assertIn("external_ui_execution.py", text)
        self.assertIn("reference_execution_ref", text)
        self.assertIn("task_fingerprint", text)
        self.assertIn("must_preserve_source_ids", text)

    def test_root_lifecycle_maps_reference_checkpoints_to_generation_and_release_phases(self):
        text = self.text("skills/nolane-ui/SKILL.md")
        self.assertIn("V12.1 Reference Execution Lifecycle Lock", text)
        self.assertIn("IMPLEMENTABLE", text)
        self.assertIn("implementation-selection", text)
        self.assertIn("license-gate", text)
        self.assertIn("CRITIQUED", text)
        self.assertIn("runtime-verification", text)
        self.assertIn("RELEASED", text)
        self.assertIn("provenance", text)
        self.assertIn("reference_execution_ref", text)

    def test_completion_court_blocks_reference_dropout_even_if_build_is_green(self):
        text = self.text("skills/gating-ui-completion/SKILL.md")
        self.assertIn("V12.1 External Reference Completion Gate", text)
        self.assertIn("reference_execution", text)
        self.assertIn("validate_reference_completion", text)
        self.assertIn("must_preserve_source_ids", text)
        self.assertIn("BLOCKED", text)
        self.assertIn("build", text.lower())

    def test_policy_explicitly_separates_research_fallback_from_adoption_consent(self):
        combined = self.text("skills/using-nolane-ui/SKILL.md") + self.text("skills/gating-ui-completion/SKILL.md")
        self.assertIn("research fallback", combined.lower())
        self.assertIn("adoption candidate", combined.lower())
        self.assertIn("does not trigger consent", combined.lower())


if __name__ == "__main__":
    unittest.main()
