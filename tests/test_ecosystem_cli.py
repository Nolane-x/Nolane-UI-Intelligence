import json
import subprocess
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class EcosystemCLITests(unittest.TestCase):
    def test_cli_returns_react_bits_with_canonical_citation_and_no_popularity_factor(self):
        run = subprocess.run(
            [sys.executable, str(ROOT / "scripts/nui-ecosystem-query"), "--capability", "animated-components", "--stack", "react", "--intent", "adapt"],
            cwd=ROOT,
            text=True,
            capture_output=True,
            check=True,
        )
        result = json.loads(run.stdout)
        match = next(item for item in result["matches"] if item["id"] == "react-bits")
        self.assertEqual(match["url"], "https://github.com/DavidHDev/react-bits")
        self.assertNotIn("stars", result["ranking_factors"])
        self.assertTrue(match["verify_live_before_use"])


if __name__ == "__main__":
    unittest.main()
