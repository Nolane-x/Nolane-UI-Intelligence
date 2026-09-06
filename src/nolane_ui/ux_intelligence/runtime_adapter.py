"""Deterministic adapter from V11 browser packets to UX journey evidence.

The adapter never guesses which DOM observation represents a UX fact.  Callers
must provide an explicit binding map from journey fields to V11 packet sources.
That keeps browser collection provider-neutral and preserves evidence lineage.
"""
from __future__ import annotations

from copy import deepcopy
from typing import Any
from urllib.parse import urlsplit


_SUPPORTED_SOURCES = {"url", "url_path", "visible_text", "attribute", "runtime_error_count"}
_SUPPORTED_COERCIONS = {"identity", "string", "bool", "int", "float"}
_MISSING = object()


def _normalize_v11_packet(packet: dict[str, Any]) -> dict[str, Any]:
    # Lazy import avoids coupling UX package import to optional browser transports.
    from ..runtime_v11.browser import normalize_browser_observation

    return normalize_browser_observation(packet)


def _validate_binding(binding: Any, label: str) -> dict[str, Any]:
    if not isinstance(binding, dict):
        raise TypeError(f"{label} must be an object")
    source = binding.get("source")
    if source not in _SUPPORTED_SOURCES:
        raise ValueError(f"{label}: unsupported source {source!r}")
    coerce = binding.get("coerce", "identity")
    if coerce not in _SUPPORTED_COERCIONS:
        raise ValueError(f"{label}: unsupported coerce {coerce!r}")
    if source in {"visible_text", "attribute"}:
        locator = binding.get("locator")
        if not isinstance(locator, str) or not locator.strip():
            raise ValueError(f"{label}: {source} binding requires non-empty locator")
    if source == "attribute":
        name = binding.get("name")
        if not isinstance(name, str) or not name.strip():
            raise ValueError(f"{label}: attribute binding requires non-empty name")
    return binding


def _coerce(value: Any, mode: str, label: str) -> Any:
    if mode == "identity":
        return deepcopy(value)
    if mode == "string":
        if value is None:
            raise ValueError(f"{label}: cannot coerce null to string")
        return str(value)
    if mode == "bool":
        if isinstance(value, bool):
            return value
        if isinstance(value, str):
            normalized = value.strip().casefold()
            if normalized == "true":
                return True
            if normalized == "false":
                return False
        raise ValueError(f"{label}: bool coercion accepts only boolean or 'true'/'false'")
    if mode == "int":
        if isinstance(value, bool):
            raise ValueError(f"{label}: bool is not an integer evidence value")
        try:
            return int(value)
        except (TypeError, ValueError) as exc:
            raise ValueError(f"{label}: value cannot be coerced to int") from exc
    if mode == "float":
        if isinstance(value, bool):
            raise ValueError(f"{label}: bool is not a numeric evidence value")
        try:
            return float(value)
        except (TypeError, ValueError) as exc:
            raise ValueError(f"{label}: value cannot be coerced to float") from exc
    raise AssertionError(mode)


def _observation_index(packet: dict[str, Any]) -> dict[str, dict[str, Any]]:
    return {item["locator"]: item for item in packet["observations"]}


def _extract(
    packet: dict[str, Any],
    index: dict[str, dict[str, Any]],
    binding: dict[str, Any],
    label: str,
) -> tuple[Any, str] | object:
    source = binding["source"]
    coerce = binding.get("coerce", "identity")
    if source == "url":
        value = packet["url"]
        ref = f"runtime-v11:url:{packet['url']}"
    elif source == "url_path":
        value = urlsplit(packet["url"]).path or "/"
        ref = f"runtime-v11:url-path:{packet['url']}"
    elif source == "runtime_error_count":
        value = len(packet["runtime_errors"])
        ref = f"runtime-v11:runtime-errors:{packet['url']}"
    else:
        locator = binding["locator"]
        item = index.get(locator)
        if item is None:
            return _MISSING
        if source == "visible_text":
            if "visible_text" not in item:
                return _MISSING
            value = item["visible_text"]
            ref = f"runtime-v11:locator:{locator}:visible_text"
        elif source == "attribute":
            attributes = item.get("attributes")
            if not isinstance(attributes, dict) or binding["name"] not in attributes:
                return _MISSING
            value = attributes[binding["name"]]
            ref = f"runtime-v11:locator:{locator}:attribute:{binding['name']}"
        else:
            raise AssertionError(source)
    return _coerce(value, coerce, label), ref


def _adapt_field_group(
    packet: dict[str, Any],
    index: dict[str, dict[str, Any]],
    bindings: dict[str, Any],
    label: str,
) -> dict[str, Any]:
    if not isinstance(bindings, dict):
        raise TypeError(f"{label} must be an object")
    out: dict[str, Any] = {}
    refs: dict[str, str] = {}
    for field in sorted(bindings):
        if not isinstance(field, str) or not field.strip():
            raise ValueError(f"{label}: evidence field names must be non-empty strings")
        binding = _validate_binding(bindings[field], f"{label}.{field}")
        extracted = _extract(packet, index, binding, f"{label}.{field}")
        if extracted is _MISSING:
            continue
        value, ref = extracted
        out[field] = value
        refs[field] = ref
    if refs:
        out["_evidence_refs"] = refs
    return out


def adapt_v11_browser_observation(
    packet: dict[str, Any],
    bindings: dict[str, Any],
) -> dict[str, Any]:
    """Convert a validated V11 packet into verifier-ready, step-scoped evidence.

    Binding shape::

        {
          "steps": {
            "step-id": {
              "route": {"source": "url_path"},
              "object_id": {
                "source": "attribute",
                "locator": "#context",
                "name": "data-object-id"
              }
            }
          },
          "success": { ...field bindings... }
        }

    Missing locators/attributes are omitted so the verifier records an evidence
    gap. Invalid packet/binding contracts raise instead of silently degrading.
    """
    if not isinstance(packet, dict):
        raise TypeError("V11 browser packet must be an object")
    if not isinstance(bindings, dict):
        raise TypeError("UX V11 bindings must be an object")
    normalized = _normalize_v11_packet(packet)
    index = _observation_index(normalized)

    step_bindings = bindings.get("steps")
    if not isinstance(step_bindings, dict):
        raise TypeError("UX V11 bindings require steps object")
    steps: dict[str, dict[str, Any]] = {}
    for step_id in sorted(step_bindings):
        if not isinstance(step_id, str) or not step_id.strip():
            raise ValueError("UX V11 binding step ids must be non-empty strings")
        steps[step_id] = _adapt_field_group(
            normalized,
            index,
            step_bindings[step_id],
            f"bindings.steps.{step_id}",
        )

    success_bindings = bindings.get("success", {})
    success = _adapt_field_group(normalized, index, success_bindings, "bindings.success")

    runtime_evidence: dict[str, Any] = {
        "version": 11,
        "collector": normalized["collector"],
        "url": normalized["url"],
        "capabilities": deepcopy(normalized["capabilities"]),
        "runtime_error_count": len(normalized["runtime_errors"]),
    }
    if "capture_ref" in normalized:
        runtime_evidence["capture_ref"] = normalized["capture_ref"]

    return {
        "steps": steps,
        "success": success,
        "runtime_evidence": runtime_evidence,
    }


__all__ = ["adapt_v11_browser_observation"]
