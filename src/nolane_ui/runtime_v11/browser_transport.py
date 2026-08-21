"""Provider-neutral browser transport capability contracts for NUI V11 Phase 5."""
from __future__ import annotations

from typing import Any

CAPABILITY_KEYS = (
    "navigation",
    "geometry",
    "computed_style",
    "runtime_errors",
    "capture",
    "document_metrics",
    "occlusion",
    "rendered_metadata",
    "preview_injection",
    "hot_reload",
    "reload",
)
_CAPABILITY_SET = frozenset(CAPABILITY_KEYS)
_ALLOWED_TOP_LEVEL = frozenset({"version", "provider", "capabilities", "claim_boundary"})


def _text(value: Any) -> bool:
    return isinstance(value, str) and bool(value.strip())


def validate_browser_transport_capability(record: dict[str, Any]) -> dict[str, Any]:
    errors: list[str] = []
    if not isinstance(record, dict):
        return {
            "valid": False,
            "errors": ["browser transport capability must be an object"],
            "capability_count": 0,
        }

    extra_top = sorted(set(record) - _ALLOWED_TOP_LEVEL)
    if extra_top:
        errors.append("browser transport capability has unsupported fields: " + ", ".join(extra_top))
    if record.get("version") != 11:
        errors.append("browser transport capability must declare version 11")
    if not _text(record.get("provider")):
        errors.append("browser transport capability requires provider")
    if record.get("claim_boundary") != "browser-transport-only":
        errors.append("browser transport claim_boundary must be browser-transport-only")

    capabilities = record.get("capabilities")
    if not isinstance(capabilities, dict):
        errors.append("browser transport capability requires capabilities object")
        capabilities = {}
    else:
        missing = sorted(_CAPABILITY_SET - set(capabilities))
        extra = sorted(set(capabilities) - _CAPABILITY_SET)
        if missing:
            errors.append("browser transport capabilities missing: " + ", ".join(missing))
        if extra:
            errors.append("browser transport capabilities unsupported: " + ", ".join(extra))
        for key in sorted(_CAPABILITY_SET & set(capabilities)):
            if not isinstance(capabilities[key], bool):
                errors.append(f"browser transport capability {key} must be boolean")

    return {
        "valid": not errors,
        "errors": errors,
        "capability_count": len(capabilities) if isinstance(capabilities, dict) else 0,
    }


def build_browser_transport_capability(provider: str, capabilities: dict[str, Any]) -> dict[str, Any]:
    if not _text(provider):
        raise ValueError("browser transport provider must be a non-empty string")
    if not isinstance(capabilities, dict):
        raise TypeError("browser transport capabilities must be an object")

    unknown = sorted(set(capabilities) - _CAPABILITY_SET)
    missing = sorted(_CAPABILITY_SET - set(capabilities))
    if unknown:
        raise ValueError("unsupported browser transport capabilities: " + ", ".join(unknown))
    if missing:
        raise ValueError("browser transport capabilities missing: " + ", ".join(missing))

    normalized: dict[str, bool] = {}
    for key in CAPABILITY_KEYS:
        value = capabilities[key]
        if not isinstance(value, bool):
            raise ValueError(f"browser transport capability {key} must be boolean")
        normalized[key] = value

    record = {
        "version": 11,
        "provider": provider.strip(),
        "capabilities": normalized,
        "claim_boundary": "browser-transport-only",
    }
    validation = validate_browser_transport_capability(record)
    if not validation["valid"]:
        raise AssertionError("internal browser transport record invalid: " + "; ".join(validation["errors"]))
    return record


def require_transport_capabilities(record: dict[str, Any], required: list[str]) -> dict[str, Any]:
    validation = validate_browser_transport_capability(record)
    if not validation["valid"]:
        raise ValueError("invalid browser transport capability: " + "; ".join(validation["errors"]))
    if not isinstance(required, list):
        raise TypeError("required browser transport capabilities must be a list")
    if any(not _text(item) for item in required):
        raise ValueError("required browser transport capabilities must be non-empty strings")

    unknown = sorted({str(item) for item in required} - _CAPABILITY_SET)
    if unknown:
        raise ValueError("unknown required browser transport capabilities: " + ", ".join(unknown))

    required_unique = sorted(set(str(item) for item in required))
    missing = [key for key in required_unique if record["capabilities"][key] is False]
    return {
        "status": "READY" if not missing else "UNKNOWN",
        "provider": record["provider"],
        "required": required_unique,
        "missing": missing,
        "claim_boundary": "browser-transport-only",
    }


__all__ = [
    "CAPABILITY_KEYS",
    "build_browser_transport_capability",
    "require_transport_capabilities",
    "validate_browser_transport_capability",
]
