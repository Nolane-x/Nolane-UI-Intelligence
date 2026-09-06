"""UX Intelligence: mechanisms, cognitive skills, rules, and v2 journey verification."""

from .canonical_bridge import (
    UX_CANONICAL_SKILL_BRIDGE,
    get_ux_canonical_skill_bridge,
    query_ux_canonical_skill_bridge,
    validate_ux_canonical_skill_bridge,
)
from .catalog import (
    get_ux_mechanism,
    get_ux_rule,
    get_ux_skill,
    query_ux_mechanisms,
    query_ux_rules,
    query_ux_skills,
    ux_intelligence_status,
)
from .evaluators import (
    UX_JOURNEY_EVALUATORS,
    evaluate_ux_journey_rule,
    get_ux_journey_evaluators,
    validate_ux_journey_evaluators,
)
from .journeys import normalize_ux_journey_spec, validate_ux_journey_spec
from .mechanisms import UX_MECHANISMS
from .provenance import (
    UX_PROVENANCE,
    get_ux_provenance,
    query_ux_provenance,
    validate_ux_provenance,
)
from .rules import UX_RULES
from .runtime_adapter import adapt_v11_browser_observation
from .skills import UX_SKILLS
from .v2_catalog import ux_v2_status
from .verifier import verify_ux_journey
from .product_model import build_ux_product_model, normalize_ux_product_model, validate_ux_product_model
from .goal_graph import build_ux_goal_graph, normalize_ux_goal_graph, validate_ux_goal_graph
from .discovery import discover_ux_journeys, query_ux_journey_candidates
from .promotion import promote_ux_journey_candidate
from .discovery_planner import plan_ux_discovery
from .temporal_evidence import create_ux_evidence_snapshot, ux_semantic_fingerprint, validate_ux_evidence_snapshot
from .regression import compare_ux_snapshots
from .impact import rank_ux_impacts
from .v3_catalog import ux_v3_status


__all__ = [
    "UX_CANONICAL_SKILL_BRIDGE",
    "UX_JOURNEY_EVALUATORS",
    "UX_MECHANISMS",
    "UX_PROVENANCE",
    "UX_RULES",
    "UX_SKILLS",
    "adapt_v11_browser_observation",
    "evaluate_ux_journey_rule",
    "get_ux_canonical_skill_bridge",
    "get_ux_journey_evaluators",
    "get_ux_mechanism",
    "get_ux_provenance",
    "get_ux_rule",
    "get_ux_skill",
    "normalize_ux_journey_spec",
    "query_ux_canonical_skill_bridge",
    "query_ux_mechanisms",
    "query_ux_provenance",
    "query_ux_rules",
    "query_ux_skills",
    "ux_intelligence_status",
    "ux_v2_status",
    "validate_ux_canonical_skill_bridge",
    "validate_ux_journey_evaluators",
    "validate_ux_journey_spec",
    "validate_ux_provenance",
    "verify_ux_journey",
    "build_ux_product_model",
    "normalize_ux_product_model",
    "validate_ux_product_model",
    "build_ux_goal_graph",
    "normalize_ux_goal_graph",
    "validate_ux_goal_graph",
    "discover_ux_journeys",
    "query_ux_journey_candidates",
    "promote_ux_journey_candidate",
    "plan_ux_discovery",
    "create_ux_evidence_snapshot",
    "ux_semantic_fingerprint",
    "validate_ux_evidence_snapshot",
    "compare_ux_snapshots",
    "rank_ux_impacts",
    "ux_v3_status",
]
