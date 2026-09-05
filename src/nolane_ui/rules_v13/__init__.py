"""NUI V13 Rule Intelligence public package surface."""
from .catalog import (
    explain_rule_capabilities_v13,
    get_rule_provenance_v13,
    get_rule_v13,
    load_rule_catalog_v13,
    query_rules_v13,
    rule_catalog_status_v13,
)
from .contracts import validate_catalog_v13, validate_rule_v13
from .provenance import validate_provenance_ledger_v13
from .similarity import audit_catalog_similarity, compare_rule_similarity

__all__ = [
    "audit_catalog_similarity",
    "compare_rule_similarity",
    "explain_rule_capabilities_v13",
    "get_rule_provenance_v13",
    "get_rule_v13",
    "load_rule_catalog_v13",
    "query_rules_v13",
    "rule_catalog_status_v13",
    "validate_catalog_v13",
    "validate_provenance_ledger_v13",
    "validate_rule_v13",
]
