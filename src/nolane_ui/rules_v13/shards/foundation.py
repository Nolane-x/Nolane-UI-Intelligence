"""Composition surface for independently authored V13 foundation rules."""
from .foundation_convergence import FOUNDATION_CONVERGENCE_RULES_V13
from .foundation_product import FOUNDATION_PRODUCT_RULES_V13

FOUNDATION_RULES_V13 = FOUNDATION_CONVERGENCE_RULES_V13 + FOUNDATION_PRODUCT_RULES_V13

__all__ = ["FOUNDATION_RULES_V13"]
