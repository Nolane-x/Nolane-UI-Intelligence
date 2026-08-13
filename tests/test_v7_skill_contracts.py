import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

NEW = {
    "routing-to-ui-authorities": ("routing-ui-work", "ui-authority-route-plan"),
    "compiling-concrete-design-packets": ("routing-to-ui-authorities", "concrete-design-packet"),
    "adapting-institutional-design-knowledge": ("synthesizing-cross-source-ui-language", "institutional-knowledge-synthesis"),
    "orchestrating-implementation-authorities": ("selecting-ui-building-blocks", "implementation-authority-plan"),
    "validating-rendered-perception": ("iterating-rendered-visual-design", "rendered-perception-evidence"),
    "designing-domain-native-signatures": ("deepening-signature-mechanisms", "domain-signature-brief"),
    "building-agent-readable-ui-context": ("performing-ui-repository-archaeology", "agent-readable-ui-context"),
    "compressing-ui-decisions-for-execution": ("compiling-ui-implementation-specifications", "ui-execution-brief"),
}

ANCHORS = {
    "routing-to-ui-authorities": ["decision-dimensional authority", "authority smear", "primary/corroborating split"],
    "compiling-concrete-design-packets": ["bounded decision packet", "contraindication carry-through", "unresolved-authority blocker"],
    "adapting-institutional-design-knowledge": ["institutional evidence debt", "local-context revalidation", "transfer-boundary ledger"],
    "orchestrating-implementation-authorities": ["semantic implementation authority", "visual implementation authority", "implementation lineage"],
    "validating-rendered-perception": ["screenshot theater", "capture matrix", "calibrated pixel evidence"],
    "designing-domain-native-signatures": ["subject-world inventory", "signature removal test", "trade-dress firewall"],
    "building-agent-readable-ui-context": ["access-mode neutrality", "live-source hydration", "agent context budget"],
    "compressing-ui-decisions-for-execution": ["lossless obligation compression", "decision budget", "re-expansion trigger"],
}

CONSUMERS = {
    "routing-ui-work": "V7 Authority-Aware Routing",
    "researching-visual-references": "V7 Reference Authority Split",
    "researching-ui-implementation-ecosystems": "V7 Concrete-Knowledge Escalation",
    "designing-motion": "V7 Temporal Craft Lineage",
    "crafting-typography": "V7 Rendered Type Proof",
    "critiquing-visual-design": "V7 Render-First Critique",
    "critiquing-aesthetic-adequacy": "V7 Concrete Adequacy Test",
    "iterating-rendered-visual-design": "V7 Perceptual Delta Loop",
    "gating-ui-completion": "V7 Concrete Craft Gate",
    "selecting-ui-building-blocks": "V7 Implementation Authority Split",
    "adapting-platform-conventions": "V7 Platform Authority Deference",
    "designing-human-ai-interaction": "V7 AI Surface Authority",
}


class V7SkillContractsTests(unittest.TestCase):
    def test_manifest_declares_exact_eight_new_owners(self):
        manifest = json.loads((ROOT / "knowledge/v7-skill-manifest.json").read_text(encoding="utf-8"))
        self.assertEqual(manifest["version"], 7)
        self.assertEqual({x["name"] for x in manifest["skills"]}, set(NEW))

    def test_graph_has_166_skills_and_unique_v7_outputs(self):
        graph = json.loads((ROOT / "skills/skill-graph.json").read_text(encoding="utf-8"))["skills"]
        self.assertEqual(len(graph), 166)
        outputs = []
        for name, (parent, output) in NEW.items():
            self.assertIn(name, graph)
            self.assertEqual(graph[name]["parent"], parent)
            self.assertEqual(graph[name]["output"], output)
            self.assertTrue(graph[name].get("ownership"))
            outputs.append(output)
        self.assertEqual(len(outputs), len(set(outputs)))

    def test_each_new_skill_has_unique_behavioral_depth(self):
        for name, anchors in ANCHORS.items():
            text = (ROOT / "skills" / name / "SKILL.md").read_text(encoding="utf-8").lower()
            for anchor in anchors:
                self.assertIn(anchor, text, (name, anchor))
            self.assertIn("hard gate", text, name)
            self.assertIn("falsif", text, name)
            self.assertIn("recovery", text, name)

    def test_selected_existing_consumers_are_wired_not_duplicated(self):
        blocks = []
        for name, heading in CONSUMERS.items():
            text = (ROOT / "skills" / name / "SKILL.md").read_text(encoding="utf-8")
            self.assertIn(heading, text, name)
            block = text.split(heading, 1)[1].strip()
            self.assertGreater(len(block), 180, name)
            blocks.append(block[:180])
        self.assertEqual(len(blocks), len(set(blocks)))

    def test_v6_depth_lock_remains_graph_complete_after_v7(self):
        depth = json.loads((ROOT / "knowledge/v6-depth-focus-obligations.json").read_text(encoding="utf-8"))["skills"]
        graph = json.loads((ROOT / "skills/skill-graph.json").read_text(encoding="utf-8"))["skills"]
        self.assertEqual(set(depth), set(graph))
        flat = [term for terms in depth.values() for term in terms]
        self.assertEqual(len(flat), len(set(flat)))
        self.assertTrue(all(len(v) == 5 for v in depth.values()))


if __name__ == "__main__":
    unittest.main()
