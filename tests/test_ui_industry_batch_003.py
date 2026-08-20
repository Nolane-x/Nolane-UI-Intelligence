import difflib
import json
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILLS_DIR = ROOT / "skills"
GRAPH_PATH = SKILLS_DIR / "skill-graph.json"

BATCH_003 = [
    ("designing-accessibility-navigation-landmarks", "accessibility-specialist", "designing-accessible-interfaces", "accessibility-landmark-contract"),
    ("designing-skip-navigation-mechanisms", "accessibility-specialist", "designing-accessible-interfaces", "skip-navigation-contract"),
    ("designing-live-region-announcement-strategy", "accessibility-specialist", "designing-screen-reader-experiences", "live-region-announcement-contract"),
    ("designing-accessible-names-and-descriptions", "accessibility-specialist", "designing-screen-reader-experiences", "accessible-name-description-contract"),
    ("designing-focus-order-and-restoration", "accessibility-specialist", "designing-accessible-interfaces", "focus-order-restoration-contract"),
    ("designing-roving-focus-composites", "accessibility-specialist", "designing-keyboard-power-user-ux", "roving-focus-contract"),
    ("designing-zoom-reflow-resilience", "accessibility-specialist", "designing-low-vision-and-high-contrast", "zoom-reflow-contract"),
    ("designing-text-spacing-resilience", "accessibility-specialist", "designing-low-vision-and-high-contrast", "text-spacing-resilience-contract"),
    ("designing-forced-colors-adaptation", "accessibility-specialist", "designing-low-vision-and-high-contrast", "forced-colors-contract"),
    ("designing-color-independent-status-encoding", "accessibility-specialist", "designing-accessible-interfaces", "color-independent-status-contract"),
    ("designing-target-size-and-spacing", "accessibility-specialist", "designing-pointer-touch-pen-input", "target-size-spacing-contract"),
    ("designing-voice-control-targetability", "accessibility-specialist", "designing-voice-conversational-ui", "voice-targetability-contract"),
    ("designing-time-limit-accessibility", "accessibility-specialist", "designing-accessible-interfaces", "time-limit-accessibility-contract"),
    ("designing-pointer-cancellation-accessibility", "accessibility-specialist", "designing-pointer-touch-pen-input", "pointer-cancellation-contract"),
    ("designing-caption-presentation", "accessibility-media-specialist", "designing-accessible-interfaces", "caption-presentation-contract"),
    ("designing-audio-description-access", "accessibility-media-specialist", "designing-accessible-interfaces", "audio-description-access-contract"),
    ("designing-transcript-navigation", "accessibility-media-specialist", "designing-accessible-interfaces", "transcript-navigation-contract"),
    ("designing-accessible-data-table-navigation", "accessibility-data-specialist", "designing-accessible-interfaces", "accessible-data-table-contract"),
    ("designing-nonvisual-chart-equivalents", "accessibility-data-specialist", "designing-data-visualization", "nonvisual-chart-equivalent-contract"),
    ("designing-accessible-verification-challenges", "accessibility-trust-specialist", "designing-authentication-and-passkeys", "accessible-verification-contract"),
    ("designing-locale-selection", "locale-specialist", "designing-localized-interfaces", "locale-selection-contract"),
    ("designing-language-negotiation-and-fallback", "locale-specialist", "designing-localized-interfaces", "language-negotiation-fallback-contract"),
    ("designing-bidirectional-layouts", "locale-specialist", "designing-localized-interfaces", "bidirectional-layout-contract"),
    ("designing-rtl-component-mirroring", "locale-specialist", "designing-localized-interfaces", "rtl-mirroring-contract"),
    ("designing-mixed-direction-text", "locale-specialist", "designing-localized-interfaces", "mixed-direction-text-contract"),
    ("designing-script-sensitive-typography", "locale-specialist", "designing-localized-interfaces", "script-sensitive-typography-contract"),
    ("designing-global-font-fallback", "locale-specialist", "designing-localized-interfaces", "global-font-fallback-contract"),
    ("designing-translation-expansion-resilience", "locale-specialist", "designing-localized-interfaces", "translation-expansion-contract"),
    ("designing-plural-sensitive-copy", "locale-specialist", "designing-localized-interfaces", "plural-sensitive-copy-contract"),
    ("designing-grammatical-gender-variants", "locale-specialist", "designing-localized-interfaces", "grammatical-gender-contract"),
    ("designing-locale-number-formatting", "locale-specialist", "designing-localized-interfaces", "locale-number-format-contract"),
    ("designing-locale-date-time-formatting", "locale-specialist", "designing-localized-interfaces", "locale-date-time-format-contract"),
    ("designing-time-zone-selection", "locale-specialist", "designing-localized-interfaces", "time-zone-selection-contract"),
    ("designing-non-gregorian-calendar-support", "locale-specialist", "designing-localized-interfaces", "calendar-system-contract"),
    ("designing-person-name-localization", "locale-specialist", "designing-localized-interfaces", "person-name-localization-contract"),
    ("designing-locale-aware-sorting", "locale-specialist", "designing-localized-interfaces", "locale-sorting-contract"),
    ("designing-locale-aware-search", "locale-specialist", "designing-search", "locale-search-contract"),
    ("designing-transliteration-workflows", "locale-specialist", "designing-localized-interfaces", "transliteration-contract"),
    ("designing-multilingual-content-language-labeling", "locale-specialist", "designing-localized-interfaces", "content-language-label-contract"),
    ("designing-pseudolocalization-stress-testing", "locale-specialist", "designing-localized-interfaces", "pseudolocalization-stress-contract"),
    ("designing-media-playback-experiences", "media", "routing-ui-work", "media-playback-contract"),
    ("designing-audio-player-controls", "media-specialist", "designing-media-playback-experiences", "audio-player-control-contract"),
    ("designing-video-player-controls", "media-specialist", "designing-media-playback-experiences", "video-player-control-contract"),
    ("designing-media-timeline-scrubbing", "media-specialist", "designing-media-playback-experiences", "media-scrubbing-contract"),
    ("designing-playback-speed-control", "media-specialist", "designing-media-playback-experiences", "playback-speed-contract"),
    ("designing-subtitle-track-selection", "media-specialist", "designing-media-playback-experiences", "subtitle-track-contract"),
    ("designing-audio-track-selection", "media-specialist", "designing-media-playback-experiences", "audio-track-contract"),
    ("designing-media-chapter-navigation", "media-specialist", "designing-media-playback-experiences", "media-chapter-contract"),
    ("designing-synchronized-transcript-playback", "media-specialist", "designing-media-playback-experiences", "synchronized-transcript-contract"),
    ("designing-picture-in-picture-playback", "media-specialist", "designing-media-playback-experiences", "picture-in-picture-contract"),
    ("designing-fullscreen-media-modes", "media-specialist", "designing-media-playback-experiences", "fullscreen-media-contract"),
    ("designing-live-stream-player-states", "media-specialist", "designing-media-playback-experiences", "live-stream-state-contract"),
    ("designing-live-stream-latency-control", "media-specialist", "designing-media-playback-experiences", "live-stream-latency-contract"),
    ("designing-media-buffering-recovery", "media-specialist", "designing-media-playback-experiences", "media-buffering-recovery-contract"),
    ("designing-adaptive-media-quality-control", "media-specialist", "designing-media-playback-experiences", "adaptive-media-quality-contract"),
    ("designing-casting-and-external-playback", "media-specialist", "designing-media-playback-experiences", "external-playback-contract"),
    ("designing-offline-media-downloads", "media-specialist", "designing-media-playback-experiences", "offline-media-contract"),
    ("designing-media-queue-and-up-next", "media-specialist", "designing-media-playback-experiences", "media-queue-contract"),
    ("designing-media-clip-selection", "media-specialist", "designing-media-playback-experiences", "media-clip-selection-contract"),
    ("designing-waveform-navigation", "media-specialist", "designing-media-playback-experiences", "waveform-navigation-contract"),
    ("designing-file-transfer-and-storage", "file", "routing-ui-work", "file-transfer-storage-contract"),
    ("designing-resumable-file-uploads", "file-specialist", "designing-file-transfer-and-storage", "resumable-upload-contract"),
    ("designing-multi-file-upload-queues", "file-specialist", "designing-file-transfer-and-storage", "multi-file-upload-queue-contract"),
    ("designing-upload-conflict-resolution", "file-specialist", "designing-file-transfer-and-storage", "upload-conflict-contract"),
    ("designing-download-progress-and-retry", "file-specialist", "designing-file-transfer-and-storage", "download-progress-retry-contract"),
    ("designing-file-browser-interfaces", "file-specialist", "designing-file-transfer-and-storage", "file-browser-contract"),
    ("designing-folder-tree-navigation", "file-specialist", "designing-file-transfer-and-storage", "folder-tree-contract"),
    ("designing-file-preview-surfaces", "file-specialist", "designing-file-transfer-and-storage", "file-preview-contract"),
    ("designing-file-conversion-workflows", "file-specialist", "designing-file-transfer-and-storage", "file-conversion-contract"),
    ("designing-structured-import-mapping", "file-specialist", "designing-file-transfer-and-storage", "structured-import-mapping-contract"),
    ("designing-export-configuration", "file-specialist", "designing-file-transfer-and-storage", "export-configuration-contract"),
    ("designing-cloud-sync-status", "file-specialist", "designing-file-transfer-and-storage", "cloud-sync-status-contract"),
    ("designing-storage-quota-management", "file-specialist", "designing-file-transfer-and-storage", "storage-quota-contract"),
    ("designing-trash-and-restore", "file-specialist", "designing-file-transfer-and-storage", "trash-restore-contract"),
    ("designing-file-locking-and-checkout", "file-specialist", "designing-file-transfer-and-storage", "file-lock-checkout-contract"),
    ("designing-document-signing-workflows", "file-specialist", "designing-file-transfer-and-storage", "document-signing-contract"),
    ("designing-file-rename-move-conflicts", "file-specialist", "designing-file-transfer-and-storage", "file-move-conflict-contract"),
    ("designing-file-sharing-expiration", "file-specialist", "designing-file-transfer-and-storage", "file-share-expiration-contract"),
    ("designing-sensitive-file-handling", "file-specialist", "designing-file-transfer-and-storage", "sensitive-file-handling-contract"),
    ("designing-large-file-transfer-estimation", "file-specialist", "designing-file-transfer-and-storage", "large-transfer-estimation-contract"),
    ("designing-device-integration-interfaces", "device", "adapting-platform-conventions", "device-integration-contract"),
    ("designing-camera-capture-flows", "device-specialist", "designing-device-integration-interfaces", "camera-capture-contract"),
    ("designing-document-scanning-capture", "device-specialist", "designing-device-integration-interfaces", "document-scanning-contract"),
    ("designing-barcode-scanning", "device-specialist", "designing-device-integration-interfaces", "barcode-scanning-contract"),
    ("designing-qr-code-scanning", "device-specialist", "designing-device-integration-interfaces", "qr-scanning-contract"),
    ("designing-bluetooth-device-pairing", "device-specialist", "designing-device-integration-interfaces", "bluetooth-pairing-contract"),
    ("designing-nearby-device-discovery", "device-specialist", "designing-device-integration-interfaces", "nearby-device-discovery-contract"),
    ("designing-nfc-interactions", "device-specialist", "designing-device-integration-interfaces", "nfc-interaction-contract"),
    ("designing-location-permission-recovery", "device-specialist", "designing-device-integration-interfaces", "location-permission-recovery-contract"),
    ("designing-background-location-awareness", "device-specialist", "designing-device-integration-interfaces", "background-location-contract"),
    ("designing-printer-selection-and-status", "device-specialist", "designing-device-integration-interfaces", "printer-selection-status-contract"),
    ("designing-print-preview", "device-specialist", "designing-device-integration-interfaces", "print-preview-contract"),
    ("designing-label-printing", "device-specialist", "designing-device-integration-interfaces", "label-printing-contract"),
    ("designing-scanner-device-selection", "device-specialist", "designing-device-integration-interfaces", "scanner-selection-contract"),
    ("designing-external-display-handoffs", "device-specialist", "designing-device-integration-interfaces", "external-display-handoff-contract"),
    ("designing-device-orientation-transitions", "device-specialist", "designing-device-integration-interfaces", "device-orientation-contract"),
    ("designing-shared-device-session-boundaries", "device-specialist", "designing-device-integration-interfaces", "shared-device-session-contract"),
    ("designing-device-battery-and-connectivity-state", "device-specialist", "designing-device-integration-interfaces", "device-health-state-contract"),
    ("designing-hardware-interruption-recovery", "device-specialist", "designing-device-integration-interfaces", "hardware-interruption-recovery-contract"),
    ("designing-sensor-permission-and-availability", "device-specialist", "designing-device-integration-interfaces", "sensor-availability-contract"),
]

EXPECTED = {slug: {"family": family, "parent": parent, "output": output} for slug, family, parent, output in BATCH_003}
SLUGS = [slug for slug, _, _, _ in BATCH_003]


def _normalized_body(text: str) -> str:
    text = re.sub(r"^---.*?---\s*", "", text, flags=re.DOTALL)
    text = re.sub(r"^#.*$", "", text, flags=re.MULTILINE)
    text = re.sub(r"designing-[a-z0-9-]+", "<skill>", text.lower())
    text = re.sub(r"[^a-z0-9]+", " ", text)
    return " ".join(text.split())


class UIIndustryBatch003Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.graph = json.loads(GRAPH_PATH.read_text(encoding="utf-8"))
        cls.graph_skills = cls.graph["skills"]

    def test_batch_has_exactly_one_hundred_unique_slugs_and_outputs(self):
        self.assertEqual(100, len(BATCH_003))
        self.assertEqual(100, len(set(SLUGS)))
        self.assertEqual(100, len({node["output"] for node in EXPECTED.values()}))

    def test_each_skill_exists_and_frontmatter_name_matches_slug(self):
        for slug in SLUGS:
            path = SKILLS_DIR / slug / "SKILL.md"
            self.assertTrue(path.is_file(), slug)
            text = path.read_text(encoding="utf-8")
            match = re.match(r"^---\nname:\s*([^\n]+)\n", text)
            self.assertIsNotNone(match, slug)
            self.assertEqual(slug, match.group(1).strip())

    def test_each_skill_has_behavioral_depth_signals(self):
        signals = ("Parent Contract", "Decision Boundary", "Failure Topology", "Falsification and Recovery", "Output Contract")
        for slug in SLUGS:
            text = (SKILLS_DIR / slug / "SKILL.md").read_text(encoding="utf-8")
            self.assertGreaterEqual(len(text), 1800, slug)
            for signal in signals:
                self.assertIn(signal, text, f"{slug}: missing {signal}")

    def test_each_skill_is_registered_with_exact_metadata(self):
        for slug, expected in EXPECTED.items():
            self.assertIn(slug, self.graph_skills)
            node = self.graph_skills[slug]
            self.assertEqual(expected["family"], node.get("family"), slug)
            self.assertEqual(expected["parent"], node.get("parent"), slug)
            self.assertEqual(expected["output"], node.get("output"), slug)
            self.assertIn(node["parent"], self.graph_skills, slug)

    def test_batch_outputs_do_not_collide_with_prior_graph(self):
        batch_outputs = {node["output"] for node in EXPECTED.values()}
        prior_outputs = {
            node.get("output")
            for slug, node in self.graph_skills.items()
            if slug not in SLUGS and isinstance(node, dict)
        }
        self.assertFalse(batch_outputs & prior_outputs)

    def test_parent_chain_reaches_nui_root_without_cycles(self):
        for slug in SLUGS:
            self.assertIn(slug, self.graph_skills)
            seen = set()
            current = slug
            while current is not None:
                self.assertNotIn(current, seen, f"cycle from {slug}")
                seen.add(current)
                current = self.graph_skills[current]["parent"]
            self.assertIn("using-nolane-ui", seen, slug)

    def test_graph_preserves_batch_003_baseline_at_or_above_474(self):
        self.assertGreaterEqual(len(self.graph_skills), 474)

    def test_no_exact_normalized_body_duplicates(self):
        seen = {}
        for slug in SLUGS:
            text = (SKILLS_DIR / slug / "SKILL.md").read_text(encoding="utf-8")
            norm = _normalized_body(text)
            self.assertNotIn(norm, seen, f"{slug} duplicates {seen.get(norm)}")
            seen[norm] = slug

    def test_no_pair_is_a_trivial_rename(self):
        bodies = {slug: _normalized_body((SKILLS_DIR / slug / "SKILL.md").read_text(encoding="utf-8")) for slug in SLUGS}
        suspicious = []
        for index, left in enumerate(SLUGS):
            for right in SLUGS[index + 1:]:
                ratio = difflib.SequenceMatcher(None, bodies[left], bodies[right]).ratio()
                if ratio >= 0.86:
                    suspicious.append((left, right, round(ratio, 3)))
        self.assertEqual([], suspicious)


if __name__ == "__main__":
    unittest.main()
