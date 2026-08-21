"""NUI V11 runtime design intelligence primitives."""

from .adjudication import adjudicate_findings, adjudicate_match
from .aesthetic_governor import commit_direction, evaluate_direction_candidates
from .aesthetic_intent import compile_aesthetic_intent, validate_aesthetic_intent
from .browser import (
    browser_observation_findings,
    normalize_browser_observation,
    validate_browser_observation,
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
from .quality_residue import assess_quality_residue_closure, plan_quality_residue_pass
from .registry import load_rule_registry, validate_rule_registry
from .reobserve import compare_runtime_observations
from .routing import route_runtime_finding, route_runtime_findings
from .taste_court import aggregate_taste_court, prepare_blinded_candidates, validate_taste_judgment

__all__ = [
    "REQUIRED_RUNTIME_ARTIFACTS",
    "adjudicate_findings",
    "adjudicate_match",
    "aggregate_taste_court",
    "append_live_event",
    "assess_design_memory_staleness",
    "assess_evidence_staleness",
    "assess_genericity",
    "assess_quality_residue_closure",
    "browser_observation_findings",
    "build_design_memory",
    "build_evidence_binding",
    "build_hook_capability",
    "commit_direction",
    "compare_runtime_observations",
    "compile_aesthetic_intent",
    "create_live_session",
    "diagnose_runtime_state",
    "evaluate_direction_candidates",
    "load_rule_registry",
    "normalize_browser_observation",
    "plan_quality_residue_pass",
    "prepare_blinded_candidates",
    "product_substitution_assessment",
    "route_runtime_finding",
    "route_runtime_findings",
    "scan_path",
    "scan_text",
    "sha256_file",
    "sha256_text",
    "transactional_replace",
    "validate_aesthetic_intent",
    "validate_browser_observation",
    "validate_design_memory",
    "validate_evidence_binding",
    "validate_live_session",
    "validate_rule_registry",
    "validate_taste_judgment",
    "validate_trend_registry",
]
