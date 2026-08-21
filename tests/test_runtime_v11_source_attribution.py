from __future__ import annotations

import hashlib
import json
import tempfile
import unittest
from pathlib import Path

try:
    from nolane_ui.runtime_v11.source_attribution import (
        resolve_source_attribution,
        select_source_candidate,
        validate_source_attribution,
    )
except ModuleNotFoundError:
    def _missing(*args, **kwargs):
        raise AssertionError("Phase 5 source attribution API is missing")

    resolve_source_attribution = _missing
    select_source_candidate = _missing
    validate_source_attribution = _missing


class RuntimeV11SourceAttributionTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name).resolve()
        (self.root / "src").mkdir()
        self.app = self.root / "src" / "App.tsx"
        self.alt = self.root / "src" / "Alt.tsx"
        self.app.write_text("export const App = () => <main data-testid='app'>App</main>;", encoding="utf-8")
        self.alt.write_text("export const Alt = () => <main data-testid='app'>Alt</main>;", encoding="utf-8")

    def tearDown(self) -> None:
        self.temp.cleanup()

    @staticmethod
    def digest(path: Path) -> str:
        return "sha256:" + hashlib.sha256(path.read_bytes()).hexdigest()

    def identity(self) -> dict:
        return {
            "locator": "[data-testid='app']",
            "tag": "main",
            "visible_text_fingerprint": "App",
            "evidence_refs": ["browser:smoke#app"],
        }

    def candidate(self, path: str, *, digest: str | None = None, confidence: str = "HIGH") -> dict:
        target = self.root / path
        return {
            "candidate_id": path.replace("/", ":"),
            "source_path": path,
            "source_digest": digest or (self.digest(target) if target.exists() else "sha256:" + "0" * 64),
            "range": {"start": 0, "end": 6},
            "attribution_mechanisms": ["development-instrumentation"],
            "evidence_refs": ["browser:smoke#app"],
            "confidence": confidence,
            "provider_metadata": {"component": "App"},
        }

    def test_one_valid_current_high_confidence_candidate_can_be_exact(self) -> None:
        result = resolve_source_attribution(
            self.identity(),
            [self.candidate("src/App.tsx")],
            repository_root=self.root,
        )
        self.assertEqual(result["status"], "EXACT")
        self.assertTrue(result["mutation_authorized"])
        self.assertEqual(result["selected_candidate_id"], "src:App.tsx")
        self.assertEqual(result["claim_boundary"], "source-attribution-only")

    def test_equivalent_high_confidence_candidates_are_ambiguous_and_block_mutation(self) -> None:
        result = resolve_source_attribution(
            self.identity(),
            [self.candidate("src/App.tsx"), self.candidate("src/Alt.tsx")],
            repository_root=self.root,
        )
        self.assertEqual(result["status"], "AMBIGUOUS")
        self.assertFalse(result["mutation_authorized"])
        self.assertIsNone(result["selected_candidate_id"])

    def test_candidate_state_requires_explicit_selection_before_mutation(self) -> None:
        result = resolve_source_attribution(
            self.identity(),
            [self.candidate("src/App.tsx", confidence="MEDIUM")],
            repository_root=self.root,
        )
        self.assertEqual(result["status"], "CANDIDATE")
        self.assertFalse(result["mutation_authorized"])
        selected = select_source_candidate(result, "src:App.tsx")
        self.assertEqual(selected["status"], "EXACT")
        self.assertTrue(selected["mutation_authorized"])
        self.assertEqual(selected["selection_authority"], "explicit-candidate-selection")

    def test_unknown_attribution_cannot_be_selected(self) -> None:
        result = resolve_source_attribution(self.identity(), [], repository_root=self.root)
        self.assertEqual(result["status"], "UNKNOWN")
        self.assertFalse(result["mutation_authorized"])
        with self.assertRaises(ValueError):
            select_source_candidate(result, "missing")

    def test_parent_traversal_and_absolute_escape_are_rejected(self) -> None:
        outside = self.root.parent / "outside-phase5.txt"
        outside.write_text("secret", encoding="utf-8")
        try:
            for path in ("../outside-phase5.txt", outside.as_posix()):
                with self.subTest(path=path):
                    result = resolve_source_attribution(
                        self.identity(),
                        [self.candidate(path, digest=self.digest(outside))],
                        repository_root=self.root,
                    )
                    self.assertEqual(result["status"], "UNKNOWN")
                    self.assertIn("SOURCE_OUTSIDE_ROOT", result["failures"])
                    self.assertFalse(result["mutation_authorized"])
        finally:
            outside.unlink(missing_ok=True)

    def test_symlink_escape_is_rejected_when_supported(self) -> None:
        outside = self.root.parent / "outside-phase5-link.txt"
        outside.write_text("secret", encoding="utf-8")
        link = self.root / "src" / "escape.tsx"
        try:
            try:
                link.symlink_to(outside)
            except (OSError, NotImplementedError):
                self.skipTest("symlink creation unavailable")
            result = resolve_source_attribution(
                self.identity(),
                [self.candidate("src/escape.tsx", digest=self.digest(outside))],
                repository_root=self.root,
            )
            self.assertEqual(result["status"], "UNKNOWN")
            self.assertIn("SOURCE_OUTSIDE_ROOT", result["failures"])
        finally:
            link.unlink(missing_ok=True)
            outside.unlink(missing_ok=True)

    def test_stale_digest_cannot_be_exact(self) -> None:
        result = resolve_source_attribution(
            self.identity(),
            [self.candidate("src/App.tsx", digest="sha256:" + "0" * 64)],
            repository_root=self.root,
        )
        self.assertNotEqual(result["status"], "EXACT")
        self.assertFalse(result["mutation_authorized"])
        self.assertIn("SOURCE_STALE", result["failures"])

    def test_provider_metadata_alone_cannot_force_exactness(self) -> None:
        candidate = self.candidate("src/App.tsx", confidence="LOW")
        candidate["provider_metadata"] = {"sourceFile": "src/App.tsx", "line": 1, "provider_claim": "exact"}
        result = resolve_source_attribution(self.identity(), [candidate], repository_root=self.root)
        self.assertNotEqual(result["status"], "EXACT")
        self.assertFalse(result["mutation_authorized"])

    def test_validator_rejects_release_authority_and_invalid_status(self) -> None:
        record = {
            "version": 11,
            "status": "VERIFIED",
            "rendered_identity": self.identity(),
            "candidates": [],
            "failures": [],
            "mutation_authorized": False,
            "selected_candidate_id": None,
            "claim_boundary": "source-attribution-only",
        }
        validation = validate_source_attribution(record)
        self.assertFalse(validation["valid"])

    def test_schema_exists_and_declares_closed_status_enum(self) -> None:
        schema_path = Path(__file__).resolve().parents[1] / "schemas" / "runtime-source-attribution-v11.schema.json"
        self.assertTrue(schema_path.exists(), "Phase 5 source attribution schema is missing")
        schema = json.loads(schema_path.read_text(encoding="utf-8"))
        enum = schema["properties"]["status"]["enum"]
        self.assertEqual(enum, ["EXACT", "CANDIDATE", "AMBIGUOUS", "UNKNOWN"])


if __name__ == "__main__":
    unittest.main()
