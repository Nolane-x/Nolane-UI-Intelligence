import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from nolane_ui.runtime_v11.evidence import sha256_file, sha256_text
from nolane_ui.runtime_v11.live import (
    append_live_event,
    create_live_session,
    transactional_replace,
    validate_live_session,
)


class RuntimeV11LiveTests(unittest.TestCase):
    def make_preview_session(self):
        session = create_live_session(
            session_id="live-1",
            target="src/Hero.tsx",
            selected_source_digest=sha256_text("<Hero />"),
        )
        session = append_live_event(session, "bind_context", {"task_profile_ref": "task-1"})
        session = append_live_event(session, "variants_ready", {"variant_ids": ["a", "b", "c"]})
        return append_live_event(session, "preview_started", {"variant_ids": ["a", "b", "c"]})

    def test_legal_transition_chain_reaches_closed(self):
        session = self.make_preview_session()
        session = append_live_event(session, "accept", {"variant_id": "b"})
        session = append_live_event(session, "apply", {"new_source_digest": sha256_text("<Hero variant='b' />")})
        session = append_live_event(session, "reobserve", {"evidence_ref": "render:b"})
        session = append_live_event(session, "close", {})
        result = validate_live_session(session)
        self.assertTrue(result["valid"], result["errors"])
        self.assertEqual(session["state"], "CLOSED")
        self.assertEqual([event["seq"] for event in session["events"]], list(range(1, len(session["events"]) + 1)))

    def test_illegal_skip_is_rejected(self):
        session = create_live_session(
            session_id="live-2",
            target="src/Hero.tsx",
            selected_source_digest=sha256_text("x"),
        )
        with self.assertRaises(ValueError):
            append_live_event(session, "accept", {"variant_id": "a"})

    def test_interrupted_preview_can_enter_recovery_and_resume(self):
        session = self.make_preview_session()
        session = append_live_event(session, "interrupt", {"reason": "browser disconnected"})
        self.assertEqual(session["state"], "RECOVERY")
        session = append_live_event(session, "resume_preview", {"restored_variant_ids": ["a", "b", "c"]})
        self.assertEqual(session["state"], "PREVIEWING")
        self.assertTrue(validate_live_session(session)["valid"])

    def test_interrupt_after_source_apply_is_rejected(self):
        session = self.make_preview_session()
        session = append_live_event(session, "accept", {"variant_id": "b"})
        session = append_live_event(session, "apply", {"new_source_digest": sha256_text("applied")})
        with self.assertRaises(ValueError):
            append_live_event(session, "interrupt", {"reason": "browser disconnected after apply"})

    def test_transactional_replace_refuses_concurrent_source_change(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "Hero.tsx"
            path.write_text("hello world", encoding="utf-8")
            stale_digest = sha256_text("older source")
            result = transactional_replace(path, stale_digest, 6, 11, "NUI")
            self.assertFalse(result["applied"])
            self.assertEqual(result["status"], "CONFLICT")
            self.assertEqual(path.read_text(encoding="utf-8"), "hello world")

    def test_transactional_replace_rechecks_digest_immediately_before_commit(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "Hero.tsx"
            path.write_text("hello world", encoding="utf-8")
            expected = sha256_file(path)

            def concurrent_edit(_fd):
                path.write_text("concurrent change", encoding="utf-8")

            with patch("nolane_ui.runtime_v11.live.os.fsync", side_effect=concurrent_edit):
                result = transactional_replace(path, expected, 6, 11, "NUI")

            self.assertFalse(result["applied"])
            self.assertEqual(result["status"], "CONFLICT")
            self.assertEqual(result["phase"], "pre-commit")
            self.assertEqual(path.read_text(encoding="utf-8"), "concurrent change")

    def test_transactional_replace_does_not_resurrect_concurrently_deleted_source(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "Hero.tsx"
            path.write_text("hello world", encoding="utf-8")
            expected = sha256_file(path)

            def concurrent_delete(_fd):
                path.unlink()

            with patch("nolane_ui.runtime_v11.live.os.fsync", side_effect=concurrent_delete):
                result = transactional_replace(path, expected, 6, 11, "NUI")

            self.assertFalse(result["applied"])
            self.assertEqual(result["status"], "CONFLICT")
            self.assertEqual(result["phase"], "pre-commit")
            self.assertFalse(path.exists())

    def test_transactional_replace_is_atomic_and_returns_new_digest(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "Hero.tsx"
            path.write_text("hello world", encoding="utf-8")
            expected = sha256_file(path)
            result = transactional_replace(path, expected, 6, 11, "NUI")
            self.assertTrue(result["applied"])
            self.assertEqual(result["status"], "APPLIED")
            self.assertEqual(path.read_text(encoding="utf-8"), "hello NUI")
            self.assertEqual(result["old_digest"], expected)
            self.assertEqual(result["new_digest"], sha256_file(path))
            self.assertNotEqual(result["old_digest"], result["new_digest"])


if __name__ == "__main__":
    unittest.main()
