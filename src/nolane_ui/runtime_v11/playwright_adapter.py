"""Concrete Playwright reference adapter for the provider-neutral NUI V11 browser contract.

The module deliberately imports Playwright lazily so the NUI core remains usable
without the optional live-browser dependency installed.
"""
from __future__ import annotations

import importlib.util
from pathlib import Path
from typing import Any, Callable

from .browser import normalize_browser_observation, validate_browser_observation
from .browser_transport import build_browser_transport_capability


def _text(value: Any) -> bool:
    return isinstance(value, str) and bool(value.strip())


def playwright_available() -> bool:
    """Return whether the optional Playwright package can be imported."""
    try:
        return importlib.util.find_spec("playwright") is not None
    except (ImportError, ModuleNotFoundError, ValueError):
        return False


def playwright_capability() -> dict[str, Any]:
    """Describe only capabilities supplied by the Playwright adapter itself."""
    return build_browser_transport_capability(
        "playwright",
        {
            "navigation": True,
            "geometry": True,
            "computed_style": True,
            "runtime_errors": True,
            "capture": True,
            "document_metrics": True,
            "occlusion": False,
            "rendered_metadata": True,
            "preview_injection": True,
            # HMR requires a project/dev-server bridge supplied by the caller.
            "hot_reload": False,
            "reload": True,
        },
    )


def refresh_playwright_preview(
    page: Any,
    *,
    prefer_hmr: bool,
    hmr_bridge: Callable[[Any], Any] | None = None,
) -> dict[str, Any]:
    """Refresh a preview, preferring caller-supplied HMR and falling back to reload."""
    if not hasattr(page, "reload"):
        raise TypeError("Playwright preview refresh requires a page-like object with reload()")

    hmr_status = "NOT_REQUESTED"
    if prefer_hmr:
        if hmr_bridge is None:
            hmr_status = "HOT_RELOAD_UNAVAILABLE"
        else:
            try:
                hmr_status = "HMR_OK" if bool(hmr_bridge(page)) else "HOT_RELOAD_FAILED"
            except Exception:
                hmr_status = "HOT_RELOAD_FAILED"
            if hmr_status == "HMR_OK":
                return {
                    "status": "HMR_OK",
                    "hmr_status": "HMR_OK",
                    "reload_status": "NOT_RUN",
                    "claim_boundary": "preview-transport-only",
                }

    try:
        page.reload(wait_until="load")
    except Exception as exc:
        return {
            "status": "RELOAD_FAILED",
            "hmr_status": hmr_status,
            "reload_status": "RELOAD_FAILED",
            "error": str(exc),
            "claim_boundary": "preview-transport-only",
        }

    return {
        "status": "RELOAD_OK",
        "hmr_status": hmr_status,
        "reload_status": "RELOAD_OK",
        "claim_boundary": "preview-transport-only",
    }


def inject_playwright_preview(
    page: Any,
    *,
    selector: str,
    patch: dict[str, Any],
    candidate_id: str,
) -> dict[str, Any]:
    """Apply an ephemeral browser-only preview patch to the selected rendered node."""
    if not _text(selector):
        raise ValueError("Playwright preview injection requires selector")
    if not _text(candidate_id):
        raise ValueError("Playwright preview injection requires candidate_id")
    if not isinstance(patch, dict):
        raise TypeError("Playwright preview patch must be an object")
    if not hasattr(page, "evaluate"):
        raise TypeError("Playwright preview injection requires a page-like object with evaluate()")

    allowed = {"text", "styles", "attributes"}
    unknown = sorted(set(patch) - allowed)
    if unknown:
        raise ValueError("unsupported Playwright preview patch fields: " + ", ".join(unknown))
    if "text" in patch and not isinstance(patch["text"], str):
        raise ValueError("Playwright preview patch text must be a string")
    if "styles" in patch and not isinstance(patch["styles"], dict):
        raise ValueError("Playwright preview patch styles must be an object")
    if "attributes" in patch and not isinstance(patch["attributes"], dict):
        raise ValueError("Playwright preview patch attributes must be an object")

    payload = {
        "selector": selector.strip(),
        "patch": {
            "text": patch.get("text"),
            "styles": dict(patch.get("styles", {})),
            "attributes": dict(patch.get("attributes", {})),
        },
        "candidate_id": candidate_id.strip(),
    }
    expression = """
(payload) => {
  const element = document.querySelector(payload.selector);
  if (!element) return false;
  if (payload.patch.text !== null && payload.patch.text !== undefined) {
    element.textContent = payload.patch.text;
  }
  for (const [key, value] of Object.entries(payload.patch.styles || {})) {
    element.style[key] = String(value);
  }
  for (const [key, value] of Object.entries(payload.patch.attributes || {})) {
    if (value === null || value === false) element.removeAttribute(key);
    else element.setAttribute(key, String(value));
  }
  element.setAttribute('data-nui-preview-candidate', payload.candidate_id);
  return true;
}
"""
    applied = bool(page.evaluate(expression, payload))
    return {
        "status": "INJECTED" if applied else "TARGET_NOT_REFIND",
        "candidate_id": candidate_id.strip(),
        "selector": selector.strip(),
        "claim_boundary": "preview-transport-only",
    }


def collect_playwright_observation(
    url: str,
    *,
    selector: str,
    viewport: dict[str, Any],
    capture_path: str | None = None,
) -> dict[str, Any]:
    """Open Chromium and collect a canonical V11 browser observation packet."""
    if not playwright_available():
        raise RuntimeError("Playwright optional dependency is not installed")
    if not _text(url) or not _text(selector):
        raise ValueError("Playwright collection requires non-empty url and selector")
    if not isinstance(viewport, dict):
        raise TypeError("Playwright collection viewport must be an object")
    width = viewport.get("width")
    height = viewport.get("height")
    dpr = viewport.get("dpr")
    if isinstance(width, bool) or not isinstance(width, int) or width <= 0:
        raise ValueError("Playwright viewport width must be a positive integer")
    if isinstance(height, bool) or not isinstance(height, int) or height <= 0:
        raise ValueError("Playwright viewport height must be a positive integer")
    if isinstance(dpr, bool) or not isinstance(dpr, (int, float)) or dpr <= 0:
        raise ValueError("Playwright viewport dpr must be a positive number")

    from playwright.sync_api import sync_playwright  # type: ignore[import-not-found]

    runtime_errors: list[dict[str, str]] = []
    capture_ref: str | None = None

    with sync_playwright() as runtime:
        browser = runtime.chromium.launch(headless=True)
        try:
            context = browser.new_context(
                viewport={"width": width, "height": height},
                device_scale_factor=float(dpr),
            )
            page = context.new_page()

            def _page_error(error: Any) -> None:
                runtime_errors.append({"kind": "pageerror", "message": str(error)})

            def _console(message: Any) -> None:
                try:
                    if str(message.type).lower() == "error":
                        runtime_errors.append({"kind": "console", "message": str(message.text)})
                except Exception:
                    return

            page.on("pageerror", _page_error)
            page.on("console", _console)
            page.goto(url.strip(), wait_until="load")

            target = page.locator(selector.strip()).first
            target.wait_for(state="attached")
            bounding_box = target.bounding_box()
            if not isinstance(bounding_box, dict):
                raise RuntimeError("Playwright target has no observable bounding box")

            visible_text = target.inner_text()
            attributes = target.evaluate(
                "el => Object.fromEntries(Array.from(el.attributes).map(a => [a.name, a.value]))"
            )
            computed_style = target.evaluate(
                """el => {
  const s = getComputedStyle(el);
  return {
    display: s.display,
    position: s.position,
    visibility: s.visibility,
    opacity: s.opacity,
    color: s.color,
    backgroundColor: s.backgroundColor,
    fontFamily: s.fontFamily,
    fontSize: s.fontSize,
    fontWeight: s.fontWeight,
    lineHeight: s.lineHeight,
    borderRadius: s.borderRadius,
    overflowX: s.overflowX,
    overflowY: s.overflowY,
    zIndex: s.zIndex
  };
}"""
            )
            document_metrics = page.evaluate(
                """() => ({
  scroll_width: Math.max(document.documentElement.scrollWidth, document.body ? document.body.scrollWidth : 0),
  client_width: document.documentElement.clientWidth,
  scroll_height: Math.max(document.documentElement.scrollHeight, document.body ? document.body.scrollHeight : 0),
  client_height: document.documentElement.clientHeight
})"""
            )

            if capture_path is not None:
                if not _text(capture_path):
                    raise ValueError("Playwright capture_path must be non-empty when supplied")
                capture = Path(capture_path).expanduser().resolve()
                capture.parent.mkdir(parents=True, exist_ok=True)
                page.screenshot(path=capture.as_posix(), full_page=True)
                capture_ref = capture.as_uri()

            packet: dict[str, Any] = {
                "version": 11,
                "collector": "playwright",
                "url": url.strip(),
                "viewport": {"width": width, "height": height, "dpr": dpr},
                "capabilities": {
                    "geometry": True,
                    "computed_style": True,
                    "runtime_errors": True,
                    "capture": capture_ref is not None,
                    "document_metrics": True,
                    "occlusion": False,
                },
                "observations": [
                    {
                        "locator": selector.strip(),
                        "visible_text": visible_text,
                        "attributes": attributes if isinstance(attributes, dict) else {},
                        "computed_style": computed_style if isinstance(computed_style, dict) else {},
                        "bounding_box": {
                            "x": bounding_box["x"],
                            "y": bounding_box["y"],
                            "width": bounding_box["width"],
                            "height": bounding_box["height"],
                        },
                    }
                ],
                "runtime_errors": runtime_errors,
                "document_metrics": document_metrics,
            }
            if capture_ref is not None:
                packet["capture_ref"] = capture_ref

            validation = validate_browser_observation(packet)
            if not validation["valid"]:
                raise RuntimeError(
                    "Playwright collector produced invalid canonical browser packet: "
                    + "; ".join(validation["errors"])
                )
            return normalize_browser_observation(packet)
        finally:
            browser.close()


__all__ = [
    "collect_playwright_observation",
    "inject_playwright_preview",
    "playwright_available",
    "playwright_capability",
    "refresh_playwright_preview",
]
