# UX Intelligence v3 RED Evidence

## Contract-first phase

Branch: `feat/ux-intelligence-v3`

The first production capability is intentionally absent while Task 1 contract tests are committed.

Expected RED command:

```bash
PYTHONPATH=src python -m unittest tests.test_ux_intelligence_v3_product_model -v
```

Expected failure boundary: import error for `nolane_ui.ux_intelligence.product_model` because `product_model.py` does not exist yet.

This file records intent only; hosted workflow evidence must confirm the actual RED state before Task 1 production code is added.
