import tempfile
import unittest
from pathlib import Path

from nolane_ui.runtime_v11.evidence import (
    assess_evidence_staleness,
    build_evidence_binding,
    sha256_file,
    sha256_text,
    validate_evidence_binding,
)


class RuntimeV11EvidenceTests(unittest.TestCase):
    def test_overlapping_source_change_marks_binding_stale(self):
        binding = build_evidence_binding(
            evidence_id="render:settings-desktop",
            revision="rev-a",
            source_digests={"src/settings.tsx": sha256_text("before")},
            artifacts=["artifacts/settings.png"],
        )
        result = assess_evidence_staleness(
            binding,
            {"src/settings.tsx": sha256_text("after")},
        )
        self.assertEqual(result["status"], "STALE")
        self.assertEqual(result["changed_paths"], ["src/settings.tsx"])

    def test_unrelated_change_does_not_stale_scoped_evidence(self):
        digest = sha256_text("stable")
        binding = build_evidence_binding(
            evidence_id="render:settings-desktop",
            revision="rev-a",
            source_digests={"src/settings.tsx": digest},
            artifacts=["artifacts/settings.png"],
        )
        result = assess_evidence_staleness(
            binding,
            {"src/settings.tsx": digest, "src/unrelated.tsx": sha256_text("changed")},
        )
        self.assertEqual(result["status"], "CURRENT")
        self.assertEqual(result["changed_paths"], [])

    def test_missing_current_digest_is_unknown_not_pass(self):
        binding = build_evidence_binding(
            evidence_id="a11y:checkout",
            revision="rev-a",
            source_digests={"src/checkout.tsx": sha256_text("known")},
            artifacts=["evidence/checkout.json"],
        )
        result = assess_evidence_staleness(binding, {})
        self.assertEqual(result["status"], "UNKNOWN")
        self.assertEqual(result["missing_paths"], ["src/checkout.tsx"])

    def test_binding_requires_nonempty_scope_artifact_and_sha256(self):
        invalid = {
            "version": 11,
            "evidence_id": "render:x",
            "revision": "rev-a",
            "source_digests": {"src/x.tsx": "not-a-digest"},
            "artifacts": [],
        }
        result = validate_evidence_binding(invalid)
        self.assertFalse(result["valid"])
        joined = " ".join(result["errors"]).lower()
        self.assertIn("sha256", joined)
        self.assertIn("artifacts", joined)

    def test_sha256_file_matches_text_digest(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "source.txt"
            path.write_text("same", encoding="utf-8")
            self.assertEqual(sha256_file(path), sha256_text("same"))


if __name__ == "__main__":
    unittest.main()
