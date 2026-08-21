"""Provider-neutral browser observation contracts and finding conversion for NUI V11."""
from __future__ import annotations

import hashlib
from typing import Any

from .contracts import NUI_FINDING_REQUIRED_FIELDS
from .registry import validate_rule_registry

_REQUIRED_CAPABILITY_KEYS = ("geometry", "computed_style", "runtime_errors", "capture")
_OPTIONAL_CAPABILITY_KEYS = ("document_metrics", "occlusion")
_ALL_CAPABILITY_KEYS = _REQUIRED_CAPABILITY_KEYS + _OPTIONAL_CAPABILITY_KEYS


def _text(value: Any) -> bool:
    return isinstance(value, str) and bool(value.strip())


def _positive_number(value: Any) -> bool:
    return isinstance(value, (int, float)) and not isinstance(value, bool) and value > 0


def _number(value: Any) -> bool:
    return isinstance(value, (int, float)) and not isinstance(value, bool)


def validate_browser_observation(record: dict[str, Any]) -> dict[str, Any]:
    errors: list[str] = []
    if not isinstance(record, dict):
        return {"valid": False, "errors": ["browser observation packet must be an object"], "observation_count": 0, "runtime_error_count": 0}
    if record.get("version") != 11:
        errors.append("browser observation packet must declare version 11")
    if not _text(record.get("collector")):
        errors.append("browser observation packet requires collector")
    if not _text(record.get("url")):
        errors.append("browser observation packet requires url")

    viewport = record.get("viewport")
    if not isinstance(viewport, dict):
        errors.append("browser observation packet requires viewport object")
    else:
        for key in ("width", "height"):
            value = viewport.get(key)
            if not isinstance(value, int) or isinstance(value, bool) or value <= 0:
                errors.append(f"browser viewport {key} must be a positive integer")
        if not _positive_number(viewport.get("dpr")):
            errors.append("browser viewport dpr must be a positive number")

    capabilities = record.get("capabilities")
    normalized_capabilities: dict[str, bool] = {}
    if not isinstance(capabilities, dict):
        errors.append("browser observation packet requires capabilities object")
        capabilities = {}
    for key in _REQUIRED_CAPABILITY_KEYS:
        value = capabilities.get(key)
        if not isinstance(value, bool):
            errors.append(f"browser capability {key} must be boolean")
            normalized_capabilities[key] = False
        else:
            normalized_capabilities[key] = value
    for key in _OPTIONAL_CAPABILITY_KEYS:
        value = capabilities.get(key, False)
        if not isinstance(value, bool):
            errors.append(f"browser capability {key} must be boolean when supplied")
            normalized_capabilities[key] = False
        else:
            normalized_capabilities[key] = value

    capture_ref = record.get("capture_ref")
    if normalized_capabilities.get("capture") is True and not _text(capture_ref):
        errors.append("browser capture capability requires capture_ref")
    if normalized_capabilities.get("capture") is False and capture_ref is not None:
        errors.append("browser capture_ref cannot be claimed when capture capability is false")

    document_metrics = record.get("document_metrics")
    if normalized_capabilities.get("document_metrics"):
        if not isinstance(document_metrics, dict):
            errors.append("browser document_metrics capability requires document_metrics object")
        else:
            for key in ("scroll_width", "client_width", "scroll_height", "client_height"):
                if not _positive_number(document_metrics.get(key)):
                    errors.append(f"browser document_metrics {key} must be positive")
    elif document_metrics is not None:
        errors.append("browser document_metrics cannot be claimed when document_metrics capability is false")

    observations_value = record.get("observations")
    observations: list[dict[str, Any]] = []
    if not isinstance(observations_value, list) or not observations_value:
        errors.append("browser observation packet requires non-empty observations[]")
    else:
        for index, item in enumerate(observations_value):
            if not isinstance(item, dict):
                errors.append(f"browser observation[{index}] must be an object")
                continue
            observations.append(item)
            locator = item.get("locator")
            if not _text(locator):
                errors.append(f"browser observation[{index}] requires locator")
            bbox = item.get("bounding_box")
            if normalized_capabilities.get("geometry"):
                if not isinstance(bbox, dict):
                    errors.append(f"browser observation[{index}] geometry capability requires bounding_box")
                else:
                    for key in ("x", "y"):
                        if not _number(bbox.get(key)):
                            errors.append(f"browser observation[{index}] bounding_box {key} must be numeric")
                    for key in ("width", "height"):
                        if not _positive_number(bbox.get(key)):
                            errors.append(f"browser observation[{index}] bounding_box {key} must be positive")
            elif bbox is not None:
                errors.append(f"browser observation[{index}] cannot claim bounding_box when geometry capability is false")

            computed_style = item.get("computed_style")
            if normalized_capabilities.get("computed_style"):
                if not isinstance(computed_style, dict):
                    errors.append(f"browser observation[{index}] computed_style capability requires computed_style object")
            elif computed_style is not None:
                errors.append(f"browser observation[{index}] cannot claim computed_style when capability is false")
            if "visible_text" in item and not isinstance(item["visible_text"], str):
                errors.append(f"browser observation[{index}] visible_text must be a string")
            if "attributes" in item and not isinstance(item["attributes"], dict):
                errors.append(f"browser observation[{index}] attributes must be an object")

            occluded_by = item.get("occluded_by")
            if normalized_capabilities.get("occlusion"):
                if occluded_by is not None and (
                    not isinstance(occluded_by, list)
                    or any(not _text(value) for value in occluded_by)
                ):
                    errors.append(f"browser observation[{index}] occluded_by must be a list of non-empty locators")
                if "essential_text" in item and not isinstance(item["essential_text"], bool):
                    errors.append(f"browser observation[{index}] essential_text must be boolean")
            elif occluded_by is not None:
                errors.append(f"browser observation[{index}] cannot claim occlusion when occlusion capability is false")

    runtime_errors_value = record.get("runtime_errors", [])
    runtime_errors: list[dict[str, Any]] = []
    if not isinstance(runtime_errors_value, list):
        errors.append("browser runtime_errors must be a list")
    else:
        for index, item in enumerate(runtime_errors_value):
            if not isinstance(item, dict):
                errors.append(f"browser runtime_error[{index}] must be an object")
                continue
            runtime_errors.append(item)
            if not _text(item.get("kind")):
                errors.append(f"browser runtime_error[{index}] requires kind")
            if not _text(item.get("message")):
                errors.append(f"browser runtime_error[{index}] requires message")
    if runtime_errors and normalized_capabilities.get("runtime_errors") is False:
        errors.append("browser runtime errors cannot be claimed when runtime_errors capability is false")

    return {
        "valid": not errors,
        "errors": errors,
        "observation_count": len(observations),
        "runtime_error_count": len(runtime_errors),
        "capabilities": normalized_capabilities,
    }


def normalize_browser_observation(record: dict[str, Any]) -> dict[str, Any]:
    validation = validate_browser_observation(record)
    if not validation["valid"]:
        raise ValueError("invalid browser observation packet: " + "; ".join(validation["errors"]))
    capabilities = {
        key: bool(record["capabilities"].get(key, False)) for key in _ALL_CAPABILITY_KEYS
    }
    normalized: dict[str, Any] = {
        "version": 11,
        "collector": str(record["collector"]).strip(),
        "url": str(record["url"]).strip(),
        "viewport": {
            "width": int(record["viewport"]["width"]),
            "height": int(record["viewport"]["height"]),
            "dpr": record["viewport"]["dpr"],
        },
        "capabilities": capabilities,
        "observations": [],
        "runtime_errors": [
            {"kind": str(item["kind"]).strip(), "message": str(item["message"]).strip()}
            for item in record.get("runtime_errors", [])
        ],
    }
    if capabilities["capture"]:
        normalized["capture_ref"] = str(record["capture_ref"]).strip()
    if capabilities["document_metrics"]:
        normalized["document_metrics"] = {
            key: record["document_metrics"][key]
            for key in ("scroll_width", "client_width", "scroll_height", "client_height")
        }

    for item in sorted(record["observations"], key=lambda candidate: str(candidate.get("locator", ""))):
        out: dict[str, Any] = {"locator": str(item["locator"]).strip()}
        if "visible_text" in item:
            out["visible_text"] = item["visible_text"]
        if "attributes" in item:
            out["attributes"] = {str(key): value for key, value in sorted(item["attributes"].items(), key=lambda pair: str(pair[0]))}
        if capabilities["geometry"]:
            out["bounding_box"] = {
                key: item["bounding_box"][key] for key in ("x", "y", "width", "height")
            }
        if capabilities["computed_style"]:
            out["computed_style"] = {
                str(key): value for key, value in sorted(item["computed_style"].items(), key=lambda pair: str(pair[0]))
            }
        if capabilities["occlusion"]:
            if "occluded_by" in item:
                out["occluded_by"] = sorted(str(value) for value in item["occluded_by"])
            if "essential_text" in item:
                out["essential_text"] = item["essential_text"]
        normalized["observations"].append(out)
    return normalized


def _browser_finding(
    rule: dict[str, Any],
    record: dict[str, Any],
    *,
    evidence_text: str,
    locator: str | None = None,
) -> dict[str, Any]:
    capture_ref = record.get("capture_ref")
    viewport = record["viewport"]
    rule_id = str(rule["rule_id"])
    seed = f"{record['url']}\n{rule_id}\n{locator or ''}\n{evidence_text}\n{viewport}"
    digest = hashlib.sha256(seed.encode("utf-8")).hexdigest()
    evidence = [
        f"browser:{record['url']} viewport={viewport['width']}x{viewport['height']}@{viewport['dpr']}: {evidence_text}"
    ]
    if capture_ref:
        evidence.append(f"capture:{capture_ref}")
    domain = str(rule["domain"])
    impact = {
        "runtime-integrity": "The rendered surface can be functionally broken or silently omit behavior users depend on.",
        "layout-integrity": "Rendered content can become unreachable, obscured, or structurally broken at the inspected viewport/state.",
    }.get(domain, "The rendered observation conflicts with the active UI contract and needs evidence-bound review.")
    repair = {
        "runtime-integrity": "Repair the runtime failure, reproduce the same state on the same revision, and bind a clean re-observation.",
        "layout-integrity": "Route to the existing layout/responsive owner, repair the causal geometry/stacking issue, and re-observe the affected viewport/state.",
    }.get(domain, "Route to the existing NUI owner and re-observe after repair.")
    finding = {
        "finding_id": f"{rule_id}:{digest[:16]}",
        "domain": domain,
        "severity": str(rule["severity"]),
        "evidence": evidence,
        "violated_constraint": str(rule["description"]),
        "user_impact": impact,
        "falsifier": str(rule["falsifier"]),
        "recommended_repair": repair,
        "status": "open",
        "runtime": {
            "rule_id": rule_id,
            "rule_class": str(rule["class"]),
            "declared_tier": str(rule["tier"]),
            "engine": "browser",
            "url": str(record["url"]),
            "locator": locator,
            "viewport": dict(viewport),
            "capture_ref": capture_ref,
            "observation_digest": f"sha256:{digest}",
        },
    }
    missing = [field for field in NUI_FINDING_REQUIRED_FIELDS if field not in finding]
    if missing:
        raise AssertionError(f"browser finding construction omitted fields: {missing}")
    return finding


def browser_observation_findings(
    record: dict[str, Any],
    registry: dict[str, Any],
) -> list[dict[str, Any]]:
    """Convert explicit browser observations into NUI-compatible raw findings."""
    validation = validate_browser_observation(record)
    if not validation["valid"]:
        raise ValueError("invalid browser observation packet: " + "; ".join(validation["errors"]))
    registry_validation = validate_rule_registry(registry)
    if not registry_validation["valid"]:
        raise ValueError("invalid runtime rule registry: " + "; ".join(registry_validation["errors"]))
    normalized = normalize_browser_observation(record)
    rules = {str(rule["rule_id"]): rule for rule in registry["rules"]}
    findings: list[dict[str, Any]] = []

    script_rule = rules.get("runtime.browser.script-error")
    if script_rule is not None:
        for error in normalized["runtime_errors"]:
            findings.append(_browser_finding(
                script_rule,
                normalized,
                evidence_text=f"{error['kind']}: {error['message']}",
            ))

    overflow_rule = rules.get("runtime.browser.document-horizontal-overflow")
    metrics = normalized.get("document_metrics")
    if overflow_rule is not None and isinstance(metrics, dict):
        if metrics["scroll_width"] > metrics["client_width"] + 1:
            findings.append(_browser_finding(
                overflow_rule,
                normalized,
                evidence_text=(
                    f"document scroll_width={metrics['scroll_width']} exceeds "
                    f"client_width={metrics['client_width']}"
                ),
            ))

    occlusion_rule = rules.get("runtime.browser.text-occlusion")
    if occlusion_rule is not None and normalized["capabilities"].get("occlusion"):
        for item in normalized["observations"]:
            occluders = item.get("occluded_by", [])
            if occluders and item.get("essential_text") is True and _text(item.get("visible_text")):
                findings.append(_browser_finding(
                    occlusion_rule,
                    normalized,
                    locator=str(item["locator"]),
                    evidence_text=(
                        f"essential text {item['visible_text']!r} is occluded by "
                        f"{', '.join(occluders)}"
                    ),
                ))

    return sorted(
        findings,
        key=lambda item: (
            item["runtime"]["rule_id"],
            str(item["runtime"].get("locator") or ""),
            item["finding_id"],
        ),
    )


__all__ = [
    "browser_observation_findings",
    "normalize_browser_observation",
    "validate_browser_observation",
]
