from __future__ import annotations

from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def replace_once(path: str, old: str, new: str) -> None:
    target = ROOT / path
    text = target.read_text(encoding="utf-8")
    count = text.count(old)
    if count != 1:
        raise SystemExit(f"{path}: expected exactly one match, found {count}: {old!r}")
    target.write_text(text.replace(old, new, 1), encoding="utf-8")


replace_once(
    "src/nolane_ui/v8_repository.py",
    '        if len(graph) != 174: errors.append(f"v8 graph requires 174 skills, found {len(graph)}")',
    '        if len(graph) < 174: errors.append(f"v8 graph must retain at least the 174-skill historical baseline, found {len(graph)}")',
)
replace_once(
    "src/nolane_ui/v8_repository.py",
    '        if set(union) != set(graph): errors.append("v8 combined depth focus must cover canonical skill graph")',
    '        if len(union) != 174: errors.append(f"v8 combined depth baseline must retain 174 historical skills, found {len(union)}")\n        missing_baseline = sorted(set(union) - set(graph))\n        if missing_baseline: errors.append(f"v8 combined depth baseline missing from canonical graph: {missing_baseline}")',
)
replace_once(
    "src/nolane_ui/v9_repository.py",
    '        if len(graph) != 174:\n            errors.append(f"v9 preserves 174 canonical skills; found {len(graph)}")',
    '        if len(graph) < 174:\n            errors.append(f"v9 must retain the 174-skill historical baseline; found {len(graph)}")',
)
replace_once(
    "src/nolane_ui/v10_repository.py",
    '        if len(graph) != 174:\n            errors.append(f"v10 preserves 174 canonical skills; found {len(graph)}")',
    '        if len(graph) < 174:\n            errors.append(f"v10 must retain the 174-skill historical baseline; found {len(graph)}")',
)
replace_once(
    "tests/test_v8_repository.py",
    '    def test_graph_is_174(self):\n        g=json.loads((ROOT/\'skills/skill-graph.json\').read_text())[\'skills\']; self.assertEqual(len(g),174)',
    '    def test_graph_retains_historical_v8_baseline(self):\n        g=json.loads((ROOT/\'skills/skill-graph.json\').read_text())[\'skills\']; self.assertGreaterEqual(len(g),174)',
)
replace_once(
    "tests/test_v9_skill_protocols.py",
    '    def test_v9_does_not_inflate_canonical_skill_count_with_duplicate_owners(self):\n        graph = json.loads((ROOT / "skills" / "skill-graph.json").read_text(encoding="utf-8"))\n        self.assertEqual(len(graph["skills"]), 174)',
    '    def test_v9_historical_owners_survive_canonical_graph_expansion(self):\n        graph = json.loads((ROOT / "skills" / "skill-graph.json").read_text(encoding="utf-8"))\n        baseline_v6 = json.loads((ROOT / "knowledge" / "v6-depth-focus-obligations.json").read_text(encoding="utf-8"))["skills"]\n        baseline_v8 = json.loads((ROOT / "knowledge" / "v8-depth-obligations.json").read_text(encoding="utf-8"))["skills"]\n        historical = set(baseline_v6) | set(baseline_v8)\n        self.assertEqual(len(historical), 174)\n        self.assertTrue(historical.issubset(graph["skills"]))',
)
replace_once(
    "tests/test_v10_repository.py",
    'import unittest\nfrom pathlib import Path',
    'import json\nimport unittest\nfrom pathlib import Path',
)
replace_once(
    "tests/test_v10_repository.py",
    '    def test_v10_keeps_174_skill_graph(self):\n        result = validate_repository(ROOT)\n        self.assertEqual(result["metrics"]["skill_count"], 174)',
    '    def test_v10_reports_current_graph_without_erasing_historical_baseline(self):\n        result = validate_repository(ROOT)\n        graph = json.loads((ROOT / "skills" / "skill-graph.json").read_text(encoding="utf-8"))["skills"]\n        self.assertGreaterEqual(len(graph), 174)\n        self.assertEqual(result["metrics"]["skill_count"], len(graph))',
)
replace_once(
    "tests/test_ui_industry_batch_001.py",
    '    def test_batch_has_exactly_one_hundred_unique_slugs(self):\n        self.assertEqual(100, len(BATCH_001))\n        self.assertEqual(100, len(set(BATCH_001)))',
    '    def test_batch_has_exactly_one_hundred_unique_slugs(self):\n        self.assertEqual(100, len(BATCH_001))\n        self.assertEqual(100, len(set(BATCH_001)))\n        self.assertGreaterEqual(len(self.graph_skills), 274)',
)
