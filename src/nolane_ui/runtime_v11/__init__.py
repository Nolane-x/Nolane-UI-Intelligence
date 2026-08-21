"""NUI V11 runtime design intelligence.

The runtime layer observes source/rendered UI and emits evidence. It does not
become a design owner and a clean detector result is never release authority.
"""

from .registry import REGISTRY_RELATIVE_PATH, load_rule_registry, validate_rule_registry

__all__ = ["REGISTRY_RELATIVE_PATH", "load_rule_registry", "validate_rule_registry"]
