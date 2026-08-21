"""NUI V11 runtime design intelligence primitives."""

from .adjudication import adjudicate_findings, adjudicate_match
from .aesthetic_governor import commit_direction, evaluate_direction_candidates
from .aesthetic_intent import compile_aesthetic_intent, validate_aesthetic_intent
from .browser import (
    browser_observation_findings,
    normalize_browser_observation,
    validate_browser_observation,
)
from .browser_transport import (
    build_browser_transport_capability,
    require_transport_capabilities,
    validate_browser_transport_capability,
)
from .design_memory import assess_design_memory_staleness, build_design_memory, validate_design_memory
from .detector import scan_path, scan_text
from .doctor import REQUIRED_RUNTIME_ARTIFACTS, diagnose_runtime_state
from .evidence import (
    assess_evidence_staleness,
    build_evidence_binding,
    sha256_file,
    sha256_text,
    validate_evidence_binding,
)
from .genericity import assess_genericity, product_substitution_assessment, validate_trend_registry
from .hooks import build_hook_capability
from .live import (
    append_live_event,
    create_live_session,
    transactional_replace,
    validate_live_session,
)
from .live_visual import (
    accept_live_visual_preview,
    assess_visual_observation_capabilities,
    prepare_live_visual_preview,
    prepare_live_visual_selection,
)
from .overlay import build_overlay_packet, validate_overlay_packet
from .playwright_adapter import (
    collect_playwright_observation,
    inject_playwright_preview,
    playwright_available,
    playwright_capability,
    refresh_playwright_preview,
)
from .preview import (
    assess_preview_freshness,
    build_preview_candidate,
    prepare_preview_application,
    record_preview_observation,
    validate_preview_candidate,
)
from .quality_residue import assess_quality_residue_closure, plan_quality_residue_pass
from .registry import load_rule_registry, validate_rule_registry
from .reobserve import compare_runtime_observations
from .routing import route_runtime_finding, route_runtime_findings
from .source_attribution import resolve_source_attribution, select_source_candidate, validate_source_attribution
from .taste_court import aggregate_taste_court, prepare_blinded_candidates, validate_taste_judgment

__all__ = [
    "REQUIRED_RUNTIME_ARTIFACTS",
    "accept_live_visual_preview",
    "adjudicate_findings",
    "adjudicate_match",
    "aggregate_taste_court",
    "append_live_event",
    "assess_design_memory_staleness",
    "assess_evidence_staleness",
    "assess_genericity",
    "assess_preview_freshness",
    "assess_quality_residue_closure",
    "assess_visual_observation_capabilities",
    "browser_observation_findings",
    "build_browser_transport_capability",
    "build_design_memory",
    "build_evidence_binding",
    "build_hook_capability",
    "build_overlay_packet",
    "build_preview_candidate",
    "collect_playwright_observation",
    "commit_direction",
    "compare_runtime_observations",
    "compile_aesthetic_intent",
    "create_live_session",
    "diagnose_runtime_state",
    "evaluate_direction_candidates",
    "inject_playwright_preview",
    "load_rule_registry",
    "normalize_browser_observation",
    "plan_quality_residue_pass",
    "playwright_available",
    "playwright_capability",
    "prepare_blinded_candidates",
    "prepare_live_visual_preview",
    "prepare_live_visual_selection",
    "prepare_preview_application",
    "product_substitution_assessment",
    "record_preview_observation",
    "refresh_playwright_preview",
    "require_transport_capabilities",
    "resolve_source_attribution",
    "route_runtime_finding",
    "route_runtime_findings",
    "scan_path",
    "scan_text",
    "select_source_candidate",
    "sha256_file",
    "sha256_text",
    "transactional_replace",
    "validate_aesthetic_intent",
    "validate_browser_observation",
    "validate_browser_transport_capability",
    "validate_design_memory",
    "validate_evidence_binding",
    "validate_live_session",
    "validate_overlay_packet",
    "validate_preview_candidate",
    "validate_rule_registry",
    "validate_source_attribution",
    "validate_taste_judgment",
    "validate_trend_registry",
]
