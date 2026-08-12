import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ROUTER = ROOT / "skills/routing-ui-work/SKILL.md"


class RouterV2ContractTests(unittest.TestCase):
    def test_router_declares_v2_profile_dimensions(self):
        text = ROUTER.read_text(encoding="utf-8")
        for dimension in (
            "platform_surfaces",
            "input_modalities",
            "ai_role",
            "risk_class",
            "temporal_behaviors",
            "social_context",
            "regulatory_or_standard_sensitivity",
            "research_freshness_requirement",
        ):
            self.assertIn(dimension, text, f"router missing v2 profile dimension {dimension}")

    def test_router_declares_hard_routes_for_high_risk_and_new_surfaces(self):
        text = ROUTER.read_text(encoding="utf-8")
        required_skill_names = (
            "designing-automotive-interfaces",
            "designing-spatial-xr-interfaces",
            "designing-tv-ten-foot-interfaces",
            "designing-wearable-glanceable-interfaces",
            "designing-human-ai-interaction",
            "designing-agent-autonomy-and-control",
            "designing-medical-safety-critical-ui",
            "critiquing-human-factors-and-safety",
            "critiquing-ai-trust-and-agency",
        )
        for skill in required_skill_names:
            self.assertIn(skill, text, f"router does not expose mandatory route {skill}")
        self.assertIn("Hard routing", text)


if __name__ == "__main__":
    unittest.main()
