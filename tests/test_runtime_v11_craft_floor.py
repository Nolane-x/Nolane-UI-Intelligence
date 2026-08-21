import json
import unittest
from pathlib import Path

from nolane_ui.runtime_v11 import scan_text

ROOT = Path(__file__).resolve().parents[1]
REGISTRY_PATH = ROOT / "knowledge" / "runtime-detector-rules-v11.json"
GRAPH_PATH = ROOT / "skills" / "skill-graph.json"
CRAFT_IDS = {
    "runtime.genericness.decorative-pill-saturation",
    "runtime.genericness.all-caps-micro-label-accumulation",
    "runtime.genericness.uniform-boundary-accumulation",
}


class RuntimeV11CraftFloorTests(unittest.TestCase):
    def setUp(self):
        self.registry = json.loads(REGISTRY_PATH.read_text(encoding="utf-8"))
        self.graph = json.loads(GRAPH_PATH.read_text(encoding="utf-8"))

    def craft_ids(self, findings):
        return {item["runtime"]["rule_id"] for item in findings if item["runtime"]["rule_id"] in CRAFT_IDS}

    def test_craft_floor_rules_are_admitted_as_non_edit_blocking_observations(self):
        rules = {rule["rule_id"]: rule for rule in self.registry["rules"]}
        self.assertTrue(CRAFT_IDS.issubset(rules))
        for rule_id in CRAFT_IDS:
            self.assertIn(rules[rule_id]["class"], {"genericness", "advisory", "contextual"})
            self.assertNotEqual(rules[rule_id]["tier"], "edit")

    def test_decorative_pill_accumulation_is_observed_but_semantic_status_is_not(self):
        decorative = "<main>" + "".join(f'<span class="pill">Feature {i}</span>' for i in range(6)) + "</main>"
        findings = scan_text(decorative, "page.html", self.registry, tier="session")
        self.assertIn("runtime.genericness.decorative-pill-saturation", self.craft_ids(findings))

        semantic = "<main>" + "".join(f'<span class="pill" data-semantic="status">Status {i}</span>' for i in range(6)) + "</main>"
        findings = scan_text(semantic, "status.html", self.registry, tier="session")
        self.assertNotIn("runtime.genericness.decorative-pill-saturation", self.craft_ids(findings))

    def test_all_caps_micro_label_accumulation_is_observed_but_metadata_contract_is_not(self):
        decorative = "<section>" + "".join(f'<span class="micro-label">SIGNAL {i}</span>' for i in range(6)) + "</section>"
        findings = scan_text(decorative, "labels.html", self.registry, tier="session")
        self.assertIn("runtime.genericness.all-caps-micro-label-accumulation", self.craft_ids(findings))

        metadata = "<section>" + "".join(f'<span class="micro-label" data-semantic="metadata">ID {i}</span>' for i in range(6)) + "</section>"
        findings = scan_text(metadata, "metadata.html", self.registry, tier="session")
        self.assertNotIn("runtime.genericness.all-caps-micro-label-accumulation", self.craft_ids(findings))

    def test_uniform_boundary_accumulation_observes_default_shells_but_not_declared_objects(self):
        generic = "<main>" + "".join(f'<article class="card">Object {i}</article>' for i in range(7)) + "</main>"
        findings = scan_text(generic, "cards.html", self.registry, tier="session")
        self.assertIn("runtime.genericness.uniform-boundary-accumulation", self.craft_ids(findings))

        objects = "<main>" + "".join(f'<article class="card" data-nui-boundary="independent-object">Object {i}</article>' for i in range(7)) + "</main>"
        findings = scan_text(objects, "objects.html", self.registry, tier="session")
        self.assertNotIn("runtime.genericness.uniform-boundary-accumulation", self.craft_ids(findings))

    def test_new_craft_rule_owner_hints_resolve_only_to_existing_874_graph(self):
        rules = {rule["rule_id"]: rule for rule in self.registry["rules"]}
        skills = self.graph["skills"]
        for rule_id in CRAFT_IDS:
            self.assertTrue(rules[rule_id].get("owner_hints"), rule_id)
            unresolved = [owner for owner in rules[rule_id]["owner_hints"] if owner not in skills]
            self.assertEqual(unresolved, [], f"{rule_id} has unresolved owner hints: {unresolved}")

    def test_existing_visual_owner_hint_drift_is_repaired_on_874_graph(self):
        rules = {rule["rule_id"]: rule for rule in self.registry["rules"]}
        self.assertIn("directing-visual-hierarchy", rules["runtime.genericness.repeated-nested-card-shell"]["owner_hints"])
        self.assertIn("crafting-color", rules["runtime.genericness.decorative-gradient-text"]["owner_hints"])
        self.assertIn("adapting-responsive-layouts", rules["runtime.browser.document-horizontal-overflow"]["owner_hints"])


if __name__ == "__main__":
    unittest.main()
