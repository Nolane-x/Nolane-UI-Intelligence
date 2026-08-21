"""NUI V11 runtime design intelligence primitives."""

from .adjudication import adjudicate_findings, adjudicate_match
from .browser import (
    browser_observation_findings,
    normalize_browser_observation,
    validate_browser_observation,
)
from .detector import scan_path, scan_text
from .doctor import REQUIRED_RUNTIME_ARTIFACTS, diagnose_runtime_state
from .evidence import (
    assess_evidence_staleness,
    build_evidence_binding,
    sha256_file,
    sha256_text,
    validate_evidence_binding,
)
from .hooks import build_hook_capability
from .live import (
    append_live_event,
    create_live_session,
    transactional_replace,
    validate_live_session,
)
from .registry import load_rule_registry, validate_rule_registry
from .reobserve import compare_runtime_observations
from .routing import route_runtime_finding, route_runtime_findings

__all__ = [
    "REQUIRED_RUNTIME_ARTIFACTS",
    "adjudicate_findings",
    "adjudicate_match",
    "append_live_event",
    "assess_evidence_staleness",
    "browser_observation_findings",
    "build_evidence_binding",
    "build_hook_capability",
    "compare_runtime_observations",
    "create_live_session",
    "diagnose_runtime_state",
    "load_rule_registry",
    "normalize_browser_observation",
    "route_runtime_finding",
    "route_runtime_findings",
    "scan_path",
    "scan_text",
    "sha256_file",
    "sha256_text",
    "transactional_replace",
    "validate_browser_observation",
    "validate_evidence_binding",
    "validate_live_session",
    "validate_rule_registry",
]
