from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
GRAPH = ROOT / "skills" / "skill-graph.json"

# Deterministic bookkeeping only. This literal map does not generate or rewrite SKILL.md prose.
NODES = {
    "designing-field-validation-and-error-recovery": {"family": "form-specialist", "parent": "designing-forms", "output": "field-validation-recovery-contract"},
    "designing-dependent-form-fields": {"family": "form-specialist", "parent": "designing-forms", "output": "dependent-field-state-contract"},
    "designing-multi-step-forms": {"family": "form-specialist", "parent": "designing-forms", "output": "multi-step-form-contract"},
    "designing-form-autosave-and-drafts": {"family": "form-specialist", "parent": "designing-forms", "output": "form-draft-persistence-contract"},
    "designing-address-entry": {"family": "form-specialist", "parent": "designing-forms", "output": "address-entry-contract"},
    "designing-phone-number-entry": {"family": "form-specialist", "parent": "designing-forms", "output": "phone-entry-contract"},
    "designing-one-time-code-entry": {"family": "trust-specialist", "parent": "designing-authentication-and-passkeys", "output": "one-time-code-entry-contract"},
    "designing-password-creation-and-strength": {"family": "trust-specialist", "parent": "designing-authentication-and-passkeys", "output": "password-creation-contract"},
    "designing-monetary-input": {"family": "form-specialist", "parent": "designing-forms", "output": "monetary-input-contract"},
    "designing-measurement-and-unit-input": {"family": "form-specialist", "parent": "designing-forms", "output": "measurement-input-contract"},

    "designing-global-navigation-shells": {"family": "navigation-specialist", "parent": "designing-navigation", "output": "global-navigation-shell-contract"},
    "designing-sidebar-navigation": {"family": "navigation-specialist", "parent": "designing-navigation", "output": "sidebar-navigation-contract"},
    "designing-breadcrumb-navigation": {"family": "navigation-specialist", "parent": "designing-navigation", "output": "breadcrumb-navigation-contract"},
    "designing-mega-navigation": {"family": "navigation-specialist", "parent": "designing-navigation", "output": "mega-navigation-contract"},
    "designing-pagination": {"family": "navigation-specialist", "parent": "designing-navigation", "output": "pagination-contract"},
    "designing-infinite-scroll-browsing": {"family": "navigation-specialist", "parent": "designing-navigation", "output": "infinite-scroll-browsing-contract"},
    "designing-search-result-interfaces": {"family": "search-specialist", "parent": "designing-search", "output": "search-result-interface-contract"},
    "designing-faceted-search": {"family": "search-specialist", "parent": "designing-search", "output": "faceted-search-contract"},
    "designing-saved-searches-and-views": {"family": "search-specialist", "parent": "designing-search", "output": "saved-search-view-contract"},
    "designing-recent-items-navigation": {"family": "navigation-specialist", "parent": "designing-navigation", "output": "recent-items-navigation-contract"},

    "designing-toast-feedback": {"family": "feedback-specialist", "parent": "designing-notifications-and-interruptions", "output": "toast-feedback-contract"},
    "designing-inline-status-feedback": {"family": "feedback-specialist", "parent": "designing-notifications-and-interruptions", "output": "inline-status-feedback-contract"},
    "designing-persistent-banner-alerts": {"family": "feedback-specialist", "parent": "designing-notifications-and-interruptions", "output": "persistent-banner-alert-contract"},
    "designing-notification-centers": {"family": "feedback-specialist", "parent": "designing-notifications-and-interruptions", "output": "notification-center-contract"},
    "designing-background-task-progress": {"family": "feedback-specialist", "parent": "designing-latency-and-progressive-feedback", "output": "background-task-progress-contract"},
    "designing-indeterminate-progress": {"family": "feedback-specialist", "parent": "designing-latency-and-progressive-feedback", "output": "indeterminate-progress-contract"},
    "designing-skeleton-loading": {"family": "feedback-specialist", "parent": "designing-empty-loading-error-states", "output": "skeleton-loading-contract"},
    "designing-partial-failure-states": {"family": "feedback-specialist", "parent": "designing-empty-loading-error-states", "output": "partial-failure-state-contract"},
    "designing-retry-and-recovery-actions": {"family": "feedback-specialist", "parent": "designing-empty-loading-error-states", "output": "retry-recovery-action-contract"},
    "designing-connectivity-recovery": {"family": "feedback-specialist", "parent": "designing-offline-degraded-experiences", "output": "connectivity-recovery-contract"},

    "designing-chat-interfaces": {"family": "messaging-specialist", "parent": "designing-collaboration-and-presence", "output": "chat-interface-contract"},
    "designing-threaded-conversations": {"family": "messaging-specialist", "parent": "designing-chat-interfaces", "output": "threaded-conversation-contract"},
    "designing-message-composers": {"family": "messaging-specialist", "parent": "designing-chat-interfaces", "output": "message-composer-contract"},
    "designing-message-delivery-state": {"family": "messaging-specialist", "parent": "designing-chat-interfaces", "output": "message-delivery-state-contract"},
    "designing-read-receipts": {"family": "messaging-specialist", "parent": "designing-chat-interfaces", "output": "read-receipt-contract"},
    "designing-typing-indicators": {"family": "messaging-specialist", "parent": "designing-chat-interfaces", "output": "typing-indicator-contract"},
    "designing-message-reactions": {"family": "messaging-specialist", "parent": "designing-chat-interfaces", "output": "message-reaction-contract"},
    "designing-message-attachments": {"family": "messaging-specialist", "parent": "designing-message-composers", "output": "message-attachment-contract"},
    "designing-mentions-and-references": {"family": "messaging-specialist", "parent": "designing-collaboration-and-presence", "output": "mention-reference-contract"},
    "designing-conversation-search": {"family": "messaging-specialist", "parent": "designing-chat-interfaces", "output": "conversation-search-contract"},

    "designing-comment-systems": {"family": "collaboration-specialist", "parent": "designing-collaboration-and-presence", "output": "comment-system-contract"},
    "designing-annotation-workflows": {"family": "collaboration-specialist", "parent": "designing-comment-systems", "output": "annotation-workflow-contract"},
    "designing-collaborative-cursors": {"family": "collaboration-specialist", "parent": "designing-collaboration-and-presence", "output": "collaborative-cursor-contract"},
    "designing-live-presence-indicators": {"family": "collaboration-specialist", "parent": "designing-collaboration-and-presence", "output": "live-presence-contract"},
    "designing-sharing-dialogs": {"family": "collaboration-specialist", "parent": "designing-collaboration-and-presence", "output": "sharing-dialog-contract"},
    "designing-invitation-flows": {"family": "collaboration-specialist", "parent": "designing-collaboration-and-presence", "output": "invitation-flow-contract"},
    "designing-link-sharing": {"family": "collaboration-specialist", "parent": "designing-collaboration-and-presence", "output": "link-sharing-contract"},
    "designing-collaboration-permissions": {"family": "collaboration-specialist", "parent": "designing-permissions-and-consent", "output": "collaboration-permission-contract"},
    "designing-review-feedback-workflows": {"family": "collaboration-specialist", "parent": "designing-task-flows", "output": "review-feedback-workflow-contract"},
    "designing-collaboration-awareness": {"family": "collaboration-specialist", "parent": "designing-collaboration-and-presence", "output": "collaboration-awareness-contract"},

    "designing-first-run-onboarding": {"family": "onboarding-specialist", "parent": "designing-onboarding", "output": "first-run-onboarding-contract"},
    "designing-product-tours": {"family": "onboarding-specialist", "parent": "designing-onboarding", "output": "product-tour-contract"},
    "designing-coach-marks": {"family": "onboarding-specialist", "parent": "designing-onboarding", "output": "coach-mark-contract"},
    "designing-onboarding-checklists": {"family": "onboarding-specialist", "parent": "designing-onboarding", "output": "onboarding-checklist-contract"},
    "designing-contextual-help": {"family": "onboarding-specialist", "parent": "designing-onboarding", "output": "contextual-help-contract"},
    "designing-help-center-navigation": {"family": "onboarding-specialist", "parent": "designing-onboarding", "output": "help-center-navigation-contract"},
    "designing-progressive-feature-discovery": {"family": "onboarding-specialist", "parent": "designing-onboarding", "output": "progressive-feature-discovery-contract"},
    "designing-sample-data-experiences": {"family": "onboarding-specialist", "parent": "designing-onboarding", "output": "sample-data-experience-contract"},
    "designing-permission-onboarding": {"family": "onboarding-specialist", "parent": "designing-permissions-and-consent", "output": "permission-onboarding-contract"},
    "designing-migration-onboarding": {"family": "onboarding-specialist", "parent": "designing-onboarding", "output": "migration-onboarding-contract"},

    "designing-product-catalog-browsing": {"family": "commerce-specialist", "parent": "designing-commerce-checkout", "output": "product-catalog-browsing-contract"},
    "designing-product-detail-purchase-decisions": {"family": "commerce-specialist", "parent": "designing-commerce-checkout", "output": "product-purchase-decision-contract"},
    "designing-product-variant-selection": {"family": "commerce-specialist", "parent": "designing-commerce-checkout", "output": "product-variant-selection-contract"},
    "designing-shopping-carts": {"family": "commerce-specialist", "parent": "designing-commerce-checkout", "output": "shopping-cart-contract"},
    "designing-checkout-step-orchestration": {"family": "commerce-specialist", "parent": "designing-commerce-checkout", "output": "checkout-step-orchestration-contract"},
    "designing-shipping-method-selection": {"family": "commerce-specialist", "parent": "designing-commerce-checkout", "output": "shipping-method-selection-contract"},
    "designing-promotion-code-entry": {"family": "commerce-specialist", "parent": "designing-commerce-checkout", "output": "promotion-code-entry-contract"},
    "designing-order-tracking": {"family": "commerce-specialist", "parent": "designing-commerce-checkout", "output": "order-tracking-contract"},
    "designing-return-and-refund-flows": {"family": "commerce-specialist", "parent": "designing-financial-transaction-ui", "output": "return-refund-flow-contract"},
    "designing-wishlists-and-saved-items": {"family": "commerce-specialist", "parent": "designing-commerce-checkout", "output": "saved-commerce-intent-contract"},

    "designing-rich-text-editors": {"family": "content-specialist", "parent": "designing-editor-canvas-workspaces", "output": "rich-text-editor-contract"},
    "designing-markdown-editors": {"family": "content-specialist", "parent": "designing-editor-canvas-workspaces", "output": "markdown-editor-contract"},
    "designing-content-composer-workflows": {"family": "content-specialist", "parent": "designing-editor-canvas-workspaces", "output": "content-composer-workflow-contract"},
    "designing-content-preview": {"family": "content-specialist", "parent": "designing-editor-canvas-workspaces", "output": "content-preview-contract"},
    "designing-publishing-controls": {"family": "content-specialist", "parent": "designing-task-flows", "output": "publishing-control-contract"},
    "designing-content-scheduling": {"family": "content-specialist", "parent": "designing-task-flows", "output": "content-scheduling-contract"},
    "designing-editorial-status-workflows": {"family": "content-specialist", "parent": "designing-task-flows", "output": "editorial-status-workflow-contract"},
    "designing-content-taxonomy-management": {"family": "content-specialist", "parent": "architecting-information", "output": "content-taxonomy-contract"},
    "designing-media-library-interfaces": {"family": "content-specialist", "parent": "designing-editor-canvas-workspaces", "output": "media-library-interface-contract"},
    "designing-content-localization-workflows": {"family": "content-specialist", "parent": "designing-localized-interfaces", "output": "content-localization-workflow-contract"},

    "designing-api-explorers": {"family": "developer-ops-specialist", "parent": "designing-data-dense-interfaces", "output": "api-explorer-contract"},
    "designing-schema-explorers": {"family": "developer-ops-specialist", "parent": "designing-data-dense-interfaces", "output": "schema-explorer-contract"},
    "designing-query-builders": {"family": "developer-ops-specialist", "parent": "designing-data-dense-interfaces", "output": "query-builder-contract"},
    "designing-log-viewers": {"family": "developer-ops-specialist", "parent": "designing-data-dense-interfaces", "output": "log-viewer-contract"},
    "designing-trace-exploration": {"family": "developer-ops-specialist", "parent": "designing-data-dense-interfaces", "output": "trace-exploration-contract"},
    "designing-metrics-exploration": {"family": "developer-ops-specialist", "parent": "designing-data-visualization", "output": "metrics-exploration-contract"},
    "designing-feature-flag-management": {"family": "developer-ops-specialist", "parent": "designing-high-stakes-decisions", "output": "feature-flag-management-contract"},
    "designing-webhook-management": {"family": "developer-ops-specialist", "parent": "designing-data-dense-interfaces", "output": "webhook-management-contract"},
    "designing-secret-credential-management": {"family": "developer-ops-specialist", "parent": "designing-privacy-sensitive-interfaces", "output": "secret-credential-management-contract"},
    "designing-environment-management": {"family": "developer-ops-specialist", "parent": "designing-organization-administration", "output": "environment-management-contract"},

    "designing-consent-preference-centers": {"family": "trust-specialist", "parent": "designing-permissions-and-consent", "output": "consent-preference-center-contract"},
    "designing-cookie-consent-controls": {"family": "trust-specialist", "parent": "designing-permissions-and-consent", "output": "cookie-consent-control-contract"},
    "designing-privacy-control-centers": {"family": "trust-specialist", "parent": "designing-privacy-sensitive-interfaces", "output": "privacy-control-center-contract"},
    "designing-security-centers": {"family": "trust-specialist", "parent": "designing-privacy-sensitive-interfaces", "output": "security-center-contract"},
    "designing-device-session-management": {"family": "trust-specialist", "parent": "designing-authentication-and-passkeys", "output": "device-session-management-contract"},
    "designing-two-factor-enrollment": {"family": "trust-specialist", "parent": "designing-authentication-and-passkeys", "output": "two-factor-enrollment-contract"},
    "designing-recovery-code-management": {"family": "trust-specialist", "parent": "designing-authentication-and-passkeys", "output": "recovery-code-management-contract"},
    "designing-data-export-portability": {"family": "trust-specialist", "parent": "designing-privacy-sensitive-interfaces", "output": "data-export-portability-contract"},
    "designing-account-deletion": {"family": "trust-specialist", "parent": "designing-authentication-and-passkeys", "output": "account-deletion-contract"},
    "designing-account-recovery-flows": {"family": "trust-specialist", "parent": "designing-authentication-and-passkeys", "output": "account-recovery-flow-contract"},
}


def main() -> None:
    data = json.loads(GRAPH.read_text(encoding="utf-8"))
    skills = data["skills"]
    if len(skills) != 274:
        raise SystemExit(f"expected 274-skill Batch 001 baseline, found {len(skills)}")
    if len(NODES) != 100:
        raise SystemExit(f"Batch 002 literal map must contain 100 nodes, found {len(NODES)}")
    overlap = sorted(set(skills) & set(NODES))
    if overlap:
        raise SystemExit(f"Batch 002 slugs already exist: {overlap}")
    missing_parents = sorted({node["parent"] for node in NODES.values()} - (set(skills) | set(NODES)))
    if missing_parents:
        raise SystemExit(f"unknown parents: {missing_parents}")
    existing_outputs = {node.get("output") for node in skills.values() if isinstance(node, dict)}
    new_outputs = [node["output"] for node in NODES.values()]
    if len(new_outputs) != len(set(new_outputs)):
        raise SystemExit("Batch 002 output collision inside literal map")
    collisions = sorted(set(new_outputs) & existing_outputs)
    if collisions:
        raise SystemExit(f"Batch 002 output collision with baseline: {collisions}")
    skills.update(NODES)
    if len(skills) != 374:
        raise SystemExit(f"expected final 374 skills, found {len(skills)}")
    GRAPH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print("Batch 002 graph integrated: 274 -> 374")


if __name__ == "__main__":
    main()
