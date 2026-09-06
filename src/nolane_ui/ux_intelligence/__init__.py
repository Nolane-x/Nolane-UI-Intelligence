"""UX Intelligence v1: mechanisms, cognitive skills, and operational rules."""

from .catalog import (
    get_ux_mechanism,
    get_ux_rule,
    get_ux_skill,
    query_ux_mechanisms,
    query_ux_rules,
    query_ux_skills,
    ux_intelligence_status,
)
from .mechanisms import UX_MECHANISMS
from .rules import UX_RULES
from .skills import UX_SKILLS


__all__ = [
    "UX_MECHANISMS",
    "UX_RULES",
    "UX_SKILLS",
    "get_ux_mechanism",
    "get_ux_rule",
    "get_ux_skill",
    "query_ux_mechanisms",
    "query_ux_rules",
    "query_ux_skills",
    "ux_intelligence_status",
]
