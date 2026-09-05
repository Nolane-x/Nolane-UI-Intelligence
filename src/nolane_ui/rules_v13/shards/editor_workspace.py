"""Composition surface for independently authored V13 editor/workspace rules."""
from .editor_interaction import EDITOR_INTERACTION_RULES_V13
from .editor_persistence import EDITOR_PERSISTENCE_RULES_V13

EDITOR_WORKSPACE_RULES_V13 = EDITOR_INTERACTION_RULES_V13 + EDITOR_PERSISTENCE_RULES_V13

__all__ = ["EDITOR_WORKSPACE_RULES_V13"]
