import io
import json
import unittest
from contextlib import redirect_stdout
from pathlib import Path

from nolane_ui.runtime_v11.doctor_cli import main


ROOT = Path(__file__).resolve().parents[1]


class RuntimeV11DoctorCliTests(unittest.TestCase):
    def test_healthy_runtime_report_exits_zero(self):
        output = io.StringIO()
        with redirect_stdout(output):
            code = main(["--root", str(ROOT)])
        payload = json.loads(output.getvalue())
        self.assertEqual(code, 0)
        self.assertTrue(payload["valid"])
        self.assertEqual(payload["blocking_count"], 0)

    def test_missing_required_capability_exits_two(self):
        output = io.StringIO()
        with redirect_stdout(output):
            code = main([
                "--root", str(ROOT),
                "--require-capability", "browser",
                "--require-capability", "screenshot",
                "--available-capability", "browser",
            ])
        payload = json.loads(output.getvalue())
        self.assertEqual(code, 2)
        self.assertFalse(payload["valid"])
        self.assertTrue(any(item["id"] == "runtime-capability.missing" for item in payload["findings"]))


if __name__ == "__main__":
    unittest.main()
