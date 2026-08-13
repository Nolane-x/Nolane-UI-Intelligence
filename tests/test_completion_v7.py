import copy
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))
from nolane_ui.validators import mandatory_routes_for_profile, validate_v7_completion_evidence


def base():
    return {
        "visual_ambition": "polished",
        "functional_closure": {"status": "PASS"},
        "ui_specification": {"status": "IMPLEMENTABLE"},
    }


def good_authority_plan():
    return {
        "status": "PASS",
        "decisions": [
            {
                "dimension": "component-semantics",
                "source_id": "react-aria",
                "role": "semantic-authority",
                "reason": "tested interaction semantics for the selected web primitive",
            }
        ],
    }


def good_packet():
    return {
        "status": "READY",
        "task_thesis": "build a behaviorally correct dialog with local art direction",
        "authority_stack": [{"dimension": "component-semantics", "source_id": "react-aria"}],
        "decisions": [
            {
                "pattern_id": "semantic-primitive-before-styling",
                "dimension": "component-semantics",
                "decision": "bind visual treatment onto the selected semantic primitive",
                "rationale": "semantic behavior should survive visual substitution",
                "provenance": [{"source_id": "react-aria", "url": "https://react-spectrum.adobe.com/react-aria/"}],
                "contraindications": ["do not replace product state with primitive internal state"],
                "transfer_boundary": "semantics transfer; upstream visual language does not",
            }
        ],
        "implementation_shortcuts": ["reuse the selected semantic primitive"],
        "validation_obligations": ["keyboard and focus regression"],
        "unresolved_blockers": [],
    }


class CompletionV7Tests(unittest.TestCase):
    def test_authority_sensitive_completion_requires_valid_route(self):
        x = base(); x["authority_sensitive_decisions"] = True
        r = validate_v7_completion_evidence(x)
        self.assertEqual(r["decision"], "BLOCKED")
        self.assertTrue(any("authority route" in e.lower() for e in r["errors"]))
        x["authority_route_plan"] = good_authority_plan()
        r = validate_v7_completion_evidence(x)
        self.assertEqual(r["decision"], "PASS", r)

    def test_institutional_transfer_requires_context_and_debt_record(self):
        x = base(); x["institutional_knowledge_material"] = True
        x["institutional_knowledge_synthesis"] = {"status": "PASS"}
        r = validate_v7_completion_evidence(x)
        self.assertEqual(r["decision"], "BLOCKED")
        x["institutional_knowledge_synthesis"] = {
            "status": "PASS",
            "borrowed_mechanisms": ["eligibility before application"],
            "transfer_boundary_ledger": [{"mechanism": "eligibility", "action": "adapt"}],
            "institutional_evidence_debt": ["validate comprehension with local service users"],
            "local_revalidation": ["moderated usability study"],
        }
        r = validate_v7_completion_evidence(x)
        self.assertEqual(r["decision"], "PASS", r)

    def test_external_implementation_shortcut_requires_layer_authority_plan(self):
        x = base(); x["implementation_shortcut_used"] = True
        r = validate_v7_completion_evidence(x)
        self.assertEqual(r["decision"], "BLOCKED")
        x["implementation_authority_plan"] = {
            "status": "PASS",
            "layers": [
                {
                    "layer": "component-semantics",
                    "source_id": "react-aria",
                    "owned_responsibilities": ["focus", "keyboard"],
                    "forbidden_responsibilities": ["brand art direction"],
                    "version_snapshot": "current verified release",
                }
            ],
            "implementation_lineage": ["product dialog -> local wrapper -> React Aria primitive"],
        }
        r = validate_v7_completion_evidence(x)
        self.assertEqual(r["decision"], "PASS", r)

    def test_fast_path_requires_ready_concrete_packet_and_keeps_blockers(self):
        x = base(); x["fast_path"] = True
        r = validate_v7_completion_evidence(x)
        self.assertEqual(r["decision"], "BLOCKED")
        x["concrete_design_packet"] = good_packet()
        r = validate_v7_completion_evidence(x)
        self.assertEqual(r["decision"], "PASS", r)
        bad = copy.deepcopy(x); bad["concrete_design_packet"]["unresolved_blockers"] = ["unresolved platform authority"]
        r = validate_v7_completion_evidence(bad)
        self.assertEqual(r["decision"], "BLOCKED")

    def test_high_ambition_adds_rendered_perception_gate(self):
        x = base(); x["visual_ambition"] = "exceptional"
        r = validate_v7_completion_evidence(x)
        self.assertTrue(any("rendered perception" in e.lower() for e in r["errors"]), r)

    def test_agent_adapter_usage_cannot_escalate_authority(self):
        x = base(); x["agent_readable_adapter_used"] = True
        x["agent_readable_context"] = {"status": "PASS", "authority_escalation": True}
        r = validate_v7_completion_evidence(x)
        self.assertEqual(r["decision"], "BLOCKED")
        x["agent_readable_context"] = {"status": "PASS", "authority_escalation": False, "underlying_authority": "primer"}
        r = validate_v7_completion_evidence(x)
        self.assertEqual(r["decision"], "PASS", r)

    def test_v7_deterministic_routes_activate_new_owners(self):
        routes = mandatory_routes_for_profile({
            "external_authority_used": True,
            "institutional_knowledge_material": True,
            "implementation_shortcut_used": True,
            "agent_readable_adapter_used": True,
            "fast_path": True,
            "execution_brief_required": True,
            "visual_ambition": "exceptional",
        })
        for name in (
            "routing-to-ui-authorities", "adapting-institutional-design-knowledge",
            "orchestrating-implementation-authorities", "building-agent-readable-ui-context",
            "compiling-concrete-design-packets", "compressing-ui-decisions-for-execution",
            "validating-rendered-perception", "designing-domain-native-signatures",
        ):
            self.assertIn(name, routes)


if __name__ == "__main__":
    unittest.main()
