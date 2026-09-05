"""Independently reviewable V13 rule shards."""

from .ai_agent import AI_AGENT_RULES_V13
from .commerce import COMMERCE_RULES_V13
from .data_viz import DATA_VIZ_RULES_V13
from .editor_workspace import EDITOR_WORKSPACE_RULES_V13
from .forms_auth import FORMS_AUTH_RULES_V13
from .foundation import FOUNDATION_RULES_V13

FIRST_WAVE_RULES_V13 = (
    AI_AGENT_RULES_V13
    + FORMS_AUTH_RULES_V13
    + DATA_VIZ_RULES_V13
    + EDITOR_WORKSPACE_RULES_V13
    + COMMERCE_RULES_V13
)
FIRST_WAVE_RULE_IDS = tuple(rule["rule_id"] for rule in FIRST_WAVE_RULES_V13)

__all__ = [
    "AI_AGENT_RULES_V13",
    "COMMERCE_RULES_V13",
    "DATA_VIZ_RULES_V13",
    "EDITOR_WORKSPACE_RULES_V13",
    "FIRST_WAVE_RULE_IDS",
    "FIRST_WAVE_RULES_V13",
    "FORMS_AUTH_RULES_V13",
    "FOUNDATION_RULES_V13",
]
