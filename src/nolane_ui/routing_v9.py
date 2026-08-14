"""Deterministic V9 routing predicates for product completeness and perceptual craft."""
from __future__ import annotations

from typing import Any


PRODUCT_AMBITIONS = {"production", "full-platform", "platform", "enterprise", "production-platform", "full-product"}
HIGH_VISUAL = {"flagship", "exceptional", "experiential"}


def mandatory_v9_routes(profile: dict[str, Any]) -> set[str]:
    if not isinstance(profile, dict):
        return set()
    required: set[str] = set()
    ambition = str(profile.get("product_ambition", profile.get("product_scope", ""))).strip().lower()
    if ambition in PRODUCT_AMBITIONS or profile.get("product_wide_completion"):
        required |= {
            "modeling-product-intent",
            "inventorying-product-capabilities",
            "covering-product-scenarios",
            "critiquing-functional-completeness",
        }
    if profile.get("settings_material") or profile.get("settings_system"):
        required |= {"architecting-information", "inventorying-product-capabilities"}
    if profile.get("account_workspace_material") or profile.get("multi_account_workspace"):
        required |= {"designing-authentication-and-passkeys", "inventorying-product-capabilities"}
    if profile.get("professional_editor") or profile.get("tool_rich_editor"):
        required |= {"designing-editor-canvas-workspaces", "designing-keyboard-power-user-ux"}
        surfaces = {str(x).strip().lower() for x in profile.get("platform_surfaces", []) if isinstance(x, str)}
        if "desktop" in surfaces or profile.get("desktop_workspace"):
            required.add("designing-desktop-windowed-workspaces")
    visual = str(profile.get("visual_ambition", "")).strip().lower()
    if visual in HIGH_VISUAL:
        required |= {
            "exploring-aesthetic-directions",
            "modeling-users-and-tasks",
            "critiquing-visual-design",
            "verifying-design-fidelity",
        }
    if profile.get("material_rendered_ui") or visual in HIGH_VISUAL:
        required |= {"verifying-design-fidelity", "adapting-platform-conventions"}
    if profile.get("motion_material") or profile.get("rich_interaction"):
        required.add("designing-motion")
    if profile.get("rich_interaction"):
        required.add("engineering-rich-interactive-components")
    return required


__all__ = ["mandatory_v9_routes"]
