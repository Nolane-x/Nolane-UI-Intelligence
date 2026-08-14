"""Deterministic invariants for Nolane UI Intelligence."""

from .validators import (
    mandatory_routes_for_profile,
    validate_bounded_saturation,
    validate_completion_packet,
    validate_industry_atlas,
    validate_mandatory_routes,
    validate_repository,
    validate_research_radar,
    validate_research_saturation,
    validate_skill_graph,
    validate_source_ledger,
    validate_state_matrix,
    validate_tokens,
    validate_v3_completion_evidence,
    validate_v4_completion_evidence,
    validate_v5_completion_evidence,
    validate_v6_completion_evidence,
    validate_v7_completion_evidence,
    validate_v8_completion_evidence,
    validate_v9_completion_evidence,
)
from .product_v9 import (
    validate_account_workspace_lifecycle,
    validate_capability_envelope,
    validate_domain_audience_fit,
    validate_interface_residue_audit,
    validate_render_critique,
    validate_render_fidelity,
    validate_settings_architecture,
    validate_taste_comparison,
    validate_v9_product_system,
)
from .scope_v9 import validate_scope_adequacy
from .behavior_v10 import validate_hypothesis_registry
from .benchmark_v10 import validate_task_corpus, materialize_task_for_generation, materialize_task_for_judge
from .mutation_v10 import validate_mutation_registry, expected_mutation_effects
from .experiment_v10 import validate_experiment_manifest, validate_run_record, pairing_key
from .judging_v10 import blind_run_for_judge, pair_orientation, detect_leakage, validate_judgment
from .stats_v10 import paired_delta, bootstrap_ci, summarize_paired, evaluate_ablation_recovery, aggregate_dimension
from .claims_v10 import promote_claim, validate_claim

__all__ = [
    "validate_completion_packet", "validate_repository", "validate_skill_graph",
    "validate_state_matrix", "validate_tokens", "validate_industry_atlas",
    "validate_source_ledger", "validate_research_saturation", "validate_bounded_saturation",
    "validate_research_radar", "validate_mandatory_routes", "mandatory_routes_for_profile",
    "validate_v3_completion_evidence", "validate_v4_completion_evidence", "validate_v5_completion_evidence", "validate_v6_completion_evidence", "validate_v7_completion_evidence", "validate_v8_completion_evidence", "validate_v9_completion_evidence",
    "validate_capability_envelope", "validate_scope_adequacy", "validate_settings_architecture",
    "validate_account_workspace_lifecycle", "validate_interface_residue_audit", "validate_taste_comparison",
    "validate_render_critique", "validate_domain_audience_fit", "validate_render_fidelity", "validate_v9_product_system",
    "validate_hypothesis_registry", "validate_task_corpus", "materialize_task_for_generation", "materialize_task_for_judge",
    "validate_mutation_registry", "expected_mutation_effects", "validate_experiment_manifest", "validate_run_record", "pairing_key",
    "blind_run_for_judge", "pair_orientation", "detect_leakage", "validate_judgment",
    "paired_delta", "bootstrap_ci", "summarize_paired", "evaluate_ablation_recovery", "aggregate_dimension",
    "promote_claim", "validate_claim",
    "query_ui_ecosystem", "validate_ui_ecosystem_registry", "validate_reference_ledger",
    "validate_source_selection", "validate_rich_interaction_contract", "validate_ui_integration_audit",
]

from .ecosystem import (
    query_ui_ecosystem, validate_reference_ledger, validate_rich_interaction_contract,
    validate_source_selection, validate_ui_ecosystem_registry, validate_ui_integration_audit,
)
