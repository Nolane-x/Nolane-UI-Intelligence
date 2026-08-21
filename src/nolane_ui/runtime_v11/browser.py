"""Provider-neutral browser observation contracts for NUI V11."""
from __future__ import annotations

from typing import Any

_CAPABILITY_KEYS = ("geometry", "computed_style", "runtime_errors", "capture")


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
    else:
        for key in _CAPABILITY_KEYS:
            value = capabilities.get(key)
            if not isinstance(value, bool):
                errors.append(f"browser capability {key} must be boolean")
                normalized_capabilities[key] = False
            else:
                normalized_capabilities[key] = value

    capture_ref = record.get("capture_ref")
    if normalized_capabilities.get("capture") is True and not _text(capture_ref):
        errors.append("browser capture capability requires capture_ref")
    if normalized_capabilities.get("capture") is False and capture_ref is not None:
        errors.append("browser capture_ref cannot be claimed when capture capability is false")

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
    capabilities = {key: bool(record["capabilities"][key]) for key in _CAPABILITY_KEYS}
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
        normalized["observations"].append(out)
    return normalized


__all__ = ["normalize_browser_observation", "validate_browser_observation"]
