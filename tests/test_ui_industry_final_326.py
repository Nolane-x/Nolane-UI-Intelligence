import json
import re
import unittest
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILLS = ROOT / "skills"
GRAPH = SKILLS / "skill-graph.json"

COURTS = {
    "motion": [
        "designing-checkbox-mark-motion", "designing-radio-selection-motion", "designing-switch-thumb-motion", "designing-selection-highlight-motion", "designing-tooltip-appearance-motion", "designing-carousel-page-motion", "designing-navigation-stack-motion", "designing-route-depth-motion", "designing-drop-settlement-motion", "designing-resize-feedback-motion", "designing-pan-inertia-motion", "designing-zoom-continuity-motion", "designing-parallax-motion", "designing-progress-indicator-motion", "designing-skeleton-shimmer-motion", "designing-chart-enter-exit-motion", "designing-spring-motion", "designing-decay-motion", "designing-elastic-overscroll-motion", "designing-motion-reversal", "designing-motion-cancellation", "designing-attention-cue-motion", "designing-motion-choreography", "designing-loading-content-handoff-motion", "designing-spatial-reorientation-motion",
    ],
    "typography": [
        "designing-interface-type-scales", "designing-optical-heading-balance", "designing-line-length-and-measure", "designing-text-rag-quality", "designing-widow-orphan-control", "designing-numeric-typography", "designing-tabular-numeral-layout", "designing-decimal-number-alignment", "designing-truncation-and-ellipsis", "designing-multiline-control-labels", "designing-interface-hyphenation", "designing-code-monospace-typography", "designing-dense-table-typography", "designing-font-loading-transitions", "designing-variable-font-axes", "designing-optical-font-sizing", "designing-uppercase-label-tracking", "designing-link-text-legibility", "designing-caption-metadata-typography", "designing-reading-order-hierarchy", "designing-long-form-interface-reading", "designing-editorial-interface-type", "designing-responsive-type-scaling", "designing-numeric-unit-spacing", "designing-text-emphasis-ladders",
    ],
    "color-surface": [
        "designing-semantic-color-roles", "designing-neutral-color-scales", "designing-status-color-palettes", "designing-data-series-color-palettes", "designing-dark-theme-color-adaptation", "designing-tonal-elevation", "designing-border-hierarchy", "designing-translucent-surface-legibility", "designing-overlay-scrims", "designing-disabled-state-appearance", "designing-selection-color-systems", "designing-focus-indicator-color", "designing-warning-danger-color-semantics", "designing-brand-accent-allocation", "designing-color-interpolation", "designing-content-color-management", "designing-system-accent-integration", "designing-theme-transition-color", "designing-surface-material-contrast", "designing-shadow-color-and-tint",
    ],
    "imagery": [
        "designing-icon-semantic-vocabulary", "designing-icon-optical-sizing", "designing-icon-stroke-consistency", "designing-filled-outline-icon-states", "designing-icon-label-pairing", "designing-toolbar-iconography", "designing-status-iconography", "designing-app-and-product-icons", "designing-avatar-representation", "designing-thumbnail-hierarchies", "designing-image-cropping-behavior", "designing-image-placeholder-states", "designing-illustration-systems", "designing-data-glyphs", "designing-media-aspect-ratio-framing",
    ],
    "layout": [
        "designing-interface-grid-systems", "designing-optical-alignment", "designing-whitespace-allocation", "designing-density-modes", "designing-readable-content-width", "designing-container-query-layouts", "designing-breakpoint-strategy", "designing-content-reflow", "designing-sticky-regions", "designing-anchored-action-bars", "designing-full-bleed-regions", "designing-intrinsic-sizing-layouts", "designing-min-max-layout-constraints", "designing-nested-scroll-regions", "designing-viewport-height-layouts", "designing-safe-area-insets", "designing-fold-hinge-avoidance", "designing-virtual-keyboard-layout-avoidance", "designing-responsive-capability-preservation", "designing-orientation-adaptation", "designing-printable-interface-layouts", "designing-master-detail-layouts", "designing-multi-column-reading-layouts", "designing-empty-space-collapse", "designing-overlay-layout-anchoring",
    ],
    "controls": [
        "designing-checkbox-controls", "designing-radio-group-controls", "designing-switch-controls", "designing-segmented-controls", "designing-slider-controls", "designing-stepper-controls", "designing-listbox-controls", "designing-menubar-controls", "designing-toolbar-controls", "designing-disclosure-controls", "designing-badge-components", "designing-chip-components", "designing-meter-components", "designing-progress-bar-components", "designing-spinner-components", "designing-status-components", "designing-scrollbar-affordances", "designing-text-caret-affordances", "designing-text-selection-affordances", "designing-focus-ring-affordances", "designing-drag-ghost-affordances", "designing-number-spinner-controls", "designing-native-validation-bubbles", "designing-native-range-inputs", "designing-native-date-inputs",
    ],
    "forms": [
        "designing-email-address-entry", "designing-url-entry", "designing-search-field-entry", "designing-password-reveal-controls", "designing-masked-text-input", "designing-multiline-text-entry", "designing-signature-capture-input", "designing-browser-autofill-behavior", "designing-form-field-grouping", "designing-label-helper-error-hierarchy", "designing-required-optional-field-semantics", "designing-form-reset-and-clear", "designing-unsaved-form-abandonment", "designing-submit-concurrency", "designing-server-validation-races", "designing-inline-input-suggestions", "designing-ime-composition-input", "designing-paste-and-normalization-input", "designing-form-prefill-review", "designing-sensitive-field-reveal",
    ],
    "mobile": [
        "designing-mobile-bottom-navigation", "designing-mobile-top-app-bars", "designing-edge-swipe-navigation", "designing-thumb-reach-layouts", "designing-one-handed-mobile-flows", "designing-mobile-keyboard-transitions", "designing-pull-to-refresh", "designing-swipe-action-rows", "designing-long-press-actions", "designing-pinch-gesture-interfaces", "designing-mobile-drag-and-drop", "designing-mobile-haptic-confirmation", "designing-mobile-orientation-changes", "designing-mobile-split-screen-adaptation", "designing-mobile-dynamic-type-layout", "designing-mobile-system-back-behavior", "designing-mobile-share-sheets", "designing-mobile-deep-link-entry", "designing-mobile-home-indicator-avoidance", "designing-mobile-transient-bars",
    ],
    "desktop": [
        "designing-desktop-menu-bars", "designing-desktop-title-bars", "designing-desktop-window-chrome", "designing-multi-window-workflows", "designing-tabbed-document-interfaces", "designing-window-to-window-drag", "designing-desktop-status-bars", "designing-desktop-system-tray", "designing-desktop-notification-actions", "designing-open-save-dialog-workflows", "designing-desktop-print-workflows", "designing-clipboard-workflows", "designing-desktop-file-associations", "designing-pointer-cursor-semantics", "designing-hover-revealed-actions", "designing-right-click-discoverability", "designing-desktop-dense-toolbars", "designing-desktop-resize-behavior", "designing-desktop-multiple-display-workflows", "designing-desktop-keyboard-menu-navigation",
    ],
    "web-native": [
        "designing-browser-history-navigation", "designing-url-state", "designing-deep-link-state-restoration", "designing-scroll-restoration", "designing-anchor-link-navigation", "designing-page-reload-recovery", "designing-back-forward-cache-recovery", "designing-browser-download-experiences", "designing-browser-clipboard-permissions", "designing-browser-fullscreen-transitions", "designing-web-install-prompts", "designing-web-offline-cache-states", "designing-web-connection-quality-adaptation", "designing-web-overscroll-behavior", "designing-dynamic-viewport-units", "designing-web-virtual-keyboard-resize", "designing-cross-origin-embed-interfaces", "designing-iframe-focus-boundaries", "designing-web-popover-top-layer", "designing-web-page-visibility-recovery",
    ],
    "design-system": [
        "designing-token-layer-architecture", "designing-semantic-token-aliases", "designing-component-token-scopes", "designing-theme-inheritance", "designing-multi-brand-themes", "designing-density-token-systems", "designing-motion-token-systems", "designing-typography-token-systems", "designing-data-visualization-tokens", "designing-token-migration", "designing-token-deprecation", "designing-component-variant-architecture", "designing-component-slot-architecture", "designing-component-composition-rules", "designing-component-state-matrices", "designing-responsive-design-tokens", "designing-platform-specific-tokens", "designing-design-code-token-parity", "designing-design-system-contributions", "designing-design-system-release-migrations",
    ],
    "ai-agent": [
        "designing-ai-prompt-composers", "designing-ai-model-selection", "designing-ai-tool-call-visibility", "designing-ai-plan-surfaces", "designing-agent-activity-timelines", "designing-agent-approval-gates", "designing-agent-interruption-controls", "designing-agent-rollback", "designing-ai-citation-inspection", "designing-ai-memory-controls", "designing-ai-context-window-controls", "designing-ai-file-context-selection", "designing-agent-permission-scopes", "designing-agent-delegation", "designing-agent-background-task-status", "designing-ai-cost-and-usage-feedback", "designing-ai-latency-expectations", "designing-generated-ui-guardrails", "designing-ai-output-editing", "designing-ai-output-comparison", "designing-ai-diff-review", "designing-ai-error-recovery", "designing-ai-source-conflict-resolution", "designing-agent-goal-revision", "designing-agent-checkpoint-surfaces",
    ],
    "trust": [
        "designing-destructive-action-confirmation", "designing-irreversible-action-preview", "designing-permission-scope-explanations", "designing-consent-receipts", "designing-privacy-disclosure-timing", "designing-sensitive-data-redaction", "designing-secret-reveal-controls", "designing-session-timeout-experiences", "designing-suspicious-activity-alerts", "designing-money-transfer-confirmation", "designing-patient-identity-verification", "designing-age-assurance-flows", "designing-legal-attestation", "designing-electronic-signature-review", "designing-identity-verification-flows", "designing-sensitive-data-retention-controls", "designing-export-control-warnings", "designing-high-risk-action-second-person-review", "designing-secure-recovery-contact-flows", "designing-trust-center-evidence",
    ],
    "verification": [
        "verifying-pixel-level-fidelity", "verifying-optical-alignment", "verifying-text-overflow-and-wrapping", "verifying-localization-expansion", "verifying-rtl-layout-regressions", "verifying-keyboard-reachability", "verifying-focus-order", "verifying-screen-reader-semantics", "verifying-touch-target-geometry", "verifying-motion-interruption", "verifying-animation-jank", "verifying-layout-shift", "verifying-long-list-performance", "verifying-design-token-drift", "verifying-browser-native-residue", "verifying-cross-browser-behavior", "verifying-cross-platform-behavior", "verifying-data-display-integrity", "verifying-error-recovery-paths", "verifying-component-state-completeness", "verifying-responsive-capability-preservation", "verifying-forced-colors-rendering", "verifying-accessibility-tree-output", "verifying-network-degradation-behavior", "verifying-evidence-screenshot-quality",
    ],
    "domain": [
        "designing-clinical-timelines", "designing-medication-administration", "designing-critical-lab-result-review", "designing-care-team-handoffs", "designing-clinical-order-entry", "designing-legal-case-dockets", "designing-contract-redlining-workflows", "designing-ediscovery-review", "designing-fleet-monitoring", "designing-dispatch-boards", "designing-shipment-exception-management", "designing-warehouse-picking", "designing-manufacturing-work-orders", "designing-quality-inspection-workflows", "designing-hospitality-reservation-operations", "designing-housekeeping-operations", "designing-social-feed-composition", "designing-content-moderation-queues", "designing-creator-analytics", "designing-game-inventory-interfaces", "designing-game-loadout-management",
    ],
}

SLUGS = [slug for slugs in COURTS.values() for slug in slugs]


def output_for(slug):
    return slug.removeprefix("designing-").removeprefix("verifying-") + "-contract"


class Final326Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.graph = json.loads(GRAPH.read_text(encoding="utf-8"))["skills"]

    def test_exactly_326_unique_locked_slugs(self):
        self.assertEqual(326, len(SLUGS))
        self.assertEqual(326, len(set(SLUGS)))
        self.assertEqual(326, sum(Counter(SLUGS).values()))

    def test_skill_files_are_substantive_and_independently_falsifiable(self):
        required = ("## Decision ownership", "## Evidence and inputs", "## Decision procedure", "## Failure topology", "## Falsification", "## Output contract")
        for slug in SLUGS:
            path = SKILLS / slug / "SKILL.md"
            self.assertTrue(path.is_file(), slug)
            text = path.read_text(encoding="utf-8")
            self.assertGreaterEqual(len(text), 1600, slug)
            self.assertRegex(text, rf"\A---\nname:\s*{re.escape(slug)}\n")
            self.assertIn("description: Use when", text, slug)
            self.assertIn("## Parent Contract", text, slug)
            for heading in required:
                self.assertIn(heading, text, f"{slug}: {heading}")

    def test_every_final_skill_is_registered_and_outputs_are_unique(self):
        outputs = []
        for slug in SLUGS:
            self.assertIn(slug, self.graph, slug)
            node = self.graph[slug]
            self.assertIsNotNone(node.get("parent"), slug)
            self.assertIn(node["parent"], self.graph, slug)
            outputs.append(node.get("output"))
        self.assertEqual(326, len(set(outputs)))

    def test_final_graph_is_exactly_one_thousand(self):
        self.assertEqual(1000, len(self.graph))

    def test_parent_chains_reach_root_without_cycles(self):
        for slug in SLUGS:
            current = slug
            seen = set()
            while current is not None:
                self.assertNotIn(current, seen, slug)
                seen.add(current)
                self.assertIn(current, self.graph, slug)
                current = self.graph[current]["parent"]
            self.assertIn("using-nolane-ui", seen, slug)

    def test_no_placeholder_language(self):
        banned = re.compile(r"\b(TODO|TBD|fill this in|implement later)\b", re.I)
        for slug in SLUGS:
            text = (SKILLS / slug / "SKILL.md").read_text(encoding="utf-8")
            self.assertIsNone(banned.search(text), slug)


if __name__ == "__main__":
    unittest.main()
