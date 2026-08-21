import io
import json
import tempfile
import unittest
from contextlib import redirect_stdout
from pathlib import Path

from nolane_ui.runtime_v11.cli import main


ROOT = Path(__file__).resolve().parents[1]
FIXTURES = ROOT / "tests" / "fixtures" / "runtime_v11"


class RuntimeV11CliTests(unittest.TestCase):
    def run_cli(self, argv):
        output = io.StringIO()
        with redirect_stdout(output):
            code = main(argv)
        payload = json.loads(output.getvalue())
        return code, payload

    def test_clean_file_exits_zero_with_json_batch(self):
        code, payload = self.run_cli([
            str(FIXTURES / "clean.html"),
            "--root", str(ROOT),
            "--tier", "session",
        ])
        self.assertEqual(code, 0)
        self.assertTrue(payload["valid"])
        self.assertEqual(payload["finding_count"], 0)
        self.assertEqual(payload["unknown_count"], 0)
        self.assertEqual(payload["accepted_exception_count"], 0)

    def test_defective_file_exits_two(self):
        code, payload = self.run_cli([
            str(FIXTURES / "defects.html"),
            "--root", str(ROOT),
            "--tier", "session",
        ])
        self.assertEqual(code, 2)
        self.assertGreater(payload["finding_count"], 0)
        self.assertGreater(payload["unknown_count"], 0)
        self.assertIn("findings", payload)
        self.assertIn("unknowns", payload)
        self.assertIn("accepted_exceptions", payload)

    def test_invalid_target_exits_one_with_error_json(self):
        code, payload = self.run_cli([
            str(ROOT / "does-not-exist.html"),
            "--root", str(ROOT),
        ])
        self.assertEqual(code, 1)
        self.assertFalse(payload["valid"])
        self.assertIn("does not exist", payload["error"].lower())

    def test_directory_scan_filters_non_ui_extensions(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "page.html").write_text('<a href="">Broken</a>', encoding="utf-8")
            (root / "notes.txt").write_text('<a href="">Should not scan</a>', encoding="utf-8")
            code, payload = self.run_cli([str(root), "--root", str(ROOT), "--tier", "edit"])
            self.assertEqual(code, 2)
            scanned = payload["scanned_files"]
            self.assertEqual(len(scanned), 1)
            self.assertTrue(scanned[0].endswith("page.html"))

    def test_context_and_exception_files_are_loaded(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            source = root / "app.css"
            source.write_text(".button:focus { outline: none; }", encoding="utf-8")
            context = root / "context.json"
            context.write_text(json.dumps({"confirmed_violations": []}), encoding="utf-8")
            exceptions = root / "exceptions.json"
            exceptions.write_text(json.dumps({"exceptions": [{
                "rule_id": "runtime.accessibility.focus-visibility-suppressed",
                "file": source.as_posix(),
                "authority": "rendered focus contract",
                "reason": "A visible replacement focus ring is verified by runtime evidence.",
                "created_revision": "test-revision"
            }]}), encoding="utf-8")
            code, payload = self.run_cli([
                str(source), "--root", str(ROOT), "--context", str(context), "--exceptions", str(exceptions)
            ])
            self.assertEqual(code, 0)
            self.assertEqual(payload["accepted_exception_count"], 1)
            self.assertEqual(payload["unknown_count"], 0)


if __name__ == "__main__":
    unittest.main()
