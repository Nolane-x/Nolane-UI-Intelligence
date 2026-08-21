"""NUI V11 runtime design intelligence.

The runtime layer observes source/rendered UI and emits evidence. It does not
become a design owner and a clean detector result is never release authority.
"""

from .adjudication import adjudicate_findings, adjudicate_match
from .browser import normalize_browser_observation, validate_browser_observation
from .detector import scan_path, scan_text
from .hooks import build_hook_capability
from .registry import REGISTRY_RELATIVE_PATH, load_rule_registry, validate_rule_registry

__all__ = [
    "REGISTRY_RELATIVE_PATH",
    "adjudicate_findings",
    "adjudicate_match",
    "build_hook_capability",
    "load_rule_registry",
    "normalize_browser_observation",
    "scan_path",
    "scan_text",
    "validate_browser_observation",
    "validate_rule_registry",
]
