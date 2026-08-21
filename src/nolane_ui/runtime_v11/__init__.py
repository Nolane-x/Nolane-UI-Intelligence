"""NUI V11 runtime design intelligence.

The runtime layer observes source/rendered UI and emits evidence. It does not
become a design owner and a clean detector result is never release authority.
"""

from .adjudication import adjudicate_findings, adjudicate_match
from .browser import (
    browser_observation_findings,
    normalize_browser_observation,
    validate_browser_observation,
)
from .detector import scan_path, scan_text
from .doctor import diagnose_runtime_state
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
from .registry import REGISTRY_RELATIVE_PATH, load_rule_registry, validate_rule_registry

__all__ = [
    "REGISTRY_RELATIVE_PATH",
    "adjudicate_findings",
    "adjudicate_match",
    "append_live_event",
    "assess_evidence_staleness",
    "browser_observation_findings",
    "build_evidence_binding",
    "build_hook_capability",
    "create_live_session",
    "diagnose_runtime_state",
    "load_rule_registry",
    "normalize_browser_observation",
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
