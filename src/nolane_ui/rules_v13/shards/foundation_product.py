"""Authored V13 product-state and design-system truth rules."""
from __future__ import annotations

from ._capabilities import convergence_caps

FOUNDATION_PRODUCT_RULES_V13 = [
    {
        "rule_id": "ui.product.workflow-state-coverage",
        "domain": "product",
        "class": "contextual",
        "severity": "major",
        "enforcement": "warn",
        "title": "Material workflows need state coverage beyond the ideal screenshot",
        "statement": "A product flow is incomplete when only its successful static state is designed while reachable loading, empty, disabled, permission, error, partial-success, stale, retry, or recovery states that materially affect task completion have no intentional behavior or presentation contract.",
        "intent": "Keep visual polish from substituting for product-state reasoning and make state completeness proportional to the actual workflow rather than a fixed checklist applied everywhere.",
        "applies_when": ["A workflow depends on asynchronous work, permissions, mutable data, validation, remote services, optional content, multi-step progress, or other conditions that create materially different reachable states."],
        "does_not_apply_when": ["A state cannot occur under the product's actual architecture or is owned entirely by a lower platform layer whose behavior is already verified and intentionally inherited."],
        "failure_modes": ["The happy path is visually specified but one or more reachable material states lack behavior, copy, action availability, preservation, or recovery rules."],
        "user_impacts": ["Real users encounter blank, misleading, dead-end, destructive, or inconsistent moments precisely when network, permission, validation, or data conditions differ from the ideal demo."],
        "observables": ["The state model or implementation exposes reachable branches for which no corresponding UI behavior, feedback, preservation policy, or recovery path can be identified."],
        "falsifiers": ["A state inventory tied to the actual implementation demonstrates that every reachable material state is either intentionally handled, delegated to a verified platform owner, or impossible by construction."],
        "repairs": ["Derive a workflow-specific state matrix from real transitions and add behavior, feedback, preservation, and recovery only for reachable states with material user impact."],
        "exceptions": ["Purely static content and tightly bounded local interactions may have very small state spaces and should not be forced to invent irrelevant loading or error states."],
        "verification": ["Exercise or simulate each material reachable state and confirm the user can understand current status, available actions, preserved work, and the next valid step."],
        "owner_hints": ["designing-empty-loading-error-states", "designing-component-state-evidence-matrices"],
        "verifier_hints": ["critiquing-user-experience"],
        "capabilities": convergence_caps(**{"interaction": "REQUIRED", "cross-generation": "UNSUPPORTED"}),
        "provenance_ids": ["nui-internal-product-truth-v13", "nui-anti-convergence-corpus-2026-09-01"],
        "status": "active",
    },
    {
        "rule_id": "ui.design-system.semantic-token-role-drift",
        "domain": "design-system",
        "class": "contextual",
        "severity": "major",
        "enforcement": "warn",
        "title": "Token values can match while semantic token roles still drift",
        "statement": "A generated interface violates design-system truth when it reuses approved color, spacing, radius, typography, or elevation values but assigns them to semantic roles that contradict the product's established hierarchy, state model, component ownership, or brand usage rules.",
        "intent": "Detect design-system drift that value-level linting misses and prevent agents from claiming compliance merely because familiar tokens appear in the source." ,
        "applies_when": ["The project has an established token or component system with semantic roles, usage guidance, state ownership, or examples that distinguish where otherwise valid values should be applied."],
        "does_not_apply_when": ["The project exposes only primitive tokens with no semantic usage contract, or the current task explicitly includes an approved redesign of the semantic token architecture."],
        "failure_modes": ["Approved primitive values are reused in the wrong semantic context, causing brand accents, danger colors, surfaces, typography roles, or spacing semantics to communicate the wrong hierarchy or state."],
        "user_impacts": ["Users see inconsistent state and hierarchy cues even though automated token checks may report apparent compliance, weakening predictability and product identity."],
        "observables": ["Rendered or source usage maps a valid token value to a component role or state that conflicts with the governing design-system documentation or component contract."],
        "falsifiers": ["The governing design system explicitly allows the questioned role, or an approved migration changes the semantic mapping and updates the relevant component and usage contracts together."],
        "repairs": ["Bind implementation to semantic token roles or component-owned aliases instead of selecting primitive values by visual resemblance; update the system contract first when a new role is genuinely needed."],
        "exceptions": ["Exploratory prototypes may temporarily use primitive values before systemization when they are clearly marked non-canonical and cannot be mistaken for verified design-system compliance."],
        "verification": ["Trace representative rendered roles back to semantic tokens or component-owned aliases and compare each mapping with the current design-system usage contract."],
        "owner_hints": ["governing-design-systems"],
        "verifier_hints": ["designing-design-system-consumer-regression-tests"],
        "capabilities": convergence_caps(**{"static": "REQUIRED", "semantic-product": "REQUIRED", "cross-generation": "UNSUPPORTED"}),
        "provenance_ids": ["nui-internal-product-truth-v13", "nui-anti-convergence-corpus-2026-09-01"],
        "status": "active",
    },
]

__all__ = ["FOUNDATION_PRODUCT_RULES_V13"]
