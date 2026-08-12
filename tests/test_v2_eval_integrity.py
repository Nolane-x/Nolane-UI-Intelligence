import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EVAL_ROOT = ROOT / "evals" / "v2"
MANIFEST_PATH = EVAL_ROOT / "manifest.json"
GRAPH = json.loads((ROOT / "skills" / "skill-graph.json").read_text(encoding="utf-8"))["skills"]


class V2EvalIntegrityTests(unittest.TestCase):
    def test_manifest_lists_every_v2_eval_json_exactly_once(self):
        self.assertTrue(MANIFEST_PATH.is_file(), "evals/v2/manifest.json is required")
        manifest = json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))
        assets = manifest.get("assets", [])
        paths = [asset.get("path") for asset in assets]
        self.assertEqual(len(paths), len(set(paths)), "v2 eval manifest contains duplicate paths")
        discovered = {
            str(path.relative_to(ROOT)).replace("\\", "/")
            for path in EVAL_ROOT.rglob("*.json")
            if path != MANIFEST_PATH
        }
        self.assertEqual(set(paths), discovered, ("manifest/discovered eval mismatch", sorted(set(paths) - discovered), sorted(discovered - set(paths))))

    def test_case_suites_are_falsifiable_and_reference_real_skills(self):
        manifest = json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))
        for asset in manifest["assets"]:
            relative = asset["path"]
            kind = asset["kind"]
            self.assertIn(kind, {"coverage", "cases", "rubric"}, f"unknown v2 eval kind for {relative}: {kind}")
            doc = json.loads((ROOT / relative).read_text(encoding="utf-8"))
            self.assertEqual(doc.get("version"), 2, f"{relative} must be version 2")
            if kind != "cases":
                continue
            cases = doc.get("cases")
            self.assertIsInstance(cases, list, f"{relative} must contain cases[]")
            self.assertTrue(cases, f"{relative} must contain at least one case")
            ids = []
            for case in cases:
                case_id = case.get("id")
                ids.append(case_id)
                self.assertIsInstance(case_id, str, f"{relative} case id must be string")
                self.assertTrue(case_id.strip(), f"{relative} case id must be non-empty")
                failure = case.get("failure")
                self.assertIsInstance(failure, str, f"{relative}/{case_id} needs failure")
                self.assertGreaterEqual(len(failure.split()), 6, f"{relative}/{case_id} failure is too vague")
                required = case.get("required_skills")
                self.assertIsInstance(required, list, f"{relative}/{case_id} needs required_skills")
                self.assertTrue(required, f"{relative}/{case_id} requires at least one skill")
                unknown = sorted(set(required) - set(GRAPH))
                self.assertEqual(unknown, [], f"{relative}/{case_id} references unknown skills {unknown}")
                must_find = case.get("must_find")
                self.assertIsInstance(must_find, list, f"{relative}/{case_id} needs must_find")
                self.assertGreaterEqual(len(must_find), 2, f"{relative}/{case_id} needs at least two falsifiable expectations")
            self.assertEqual(len(ids), len(set(ids)), f"{relative} contains duplicate case ids")


if __name__ == "__main__":
    unittest.main()
