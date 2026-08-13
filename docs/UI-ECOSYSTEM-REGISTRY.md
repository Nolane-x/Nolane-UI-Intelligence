# UI Ecosystem Registry Contract

`knowledge/ui-ecosystem-registry.json` is NUI's typed retrieval cache for external UI implementation sources. It is not an endorsement list or a popularity ranking.

Every source declares a canonical URL, source role, categories, capabilities, stack/platform compatibility, allowed adoption intents, license posture/evidence, accessibility posture, drift level, provenance, and use/non-use conditions. High/very-high drift sources must require live verification.

The registry contains no embedded third-party implementation code. Use `schemas/ui-reference-ledger.schema.json`, `schemas/ui-source-selection.schema.json`, and `schemas/rich-interaction-contract.schema.json` for task-local artifacts.

When local candidates are absent or stale, route live research and extend the **task reference ledger** first. Registry changes belong to `maintaining-ui-resource-registry` and require primary provenance.
