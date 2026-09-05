"""Deterministic anti-duplication court for NUI V13 rules.

The court is intentionally conservative: it blocks exact operational clones,
identical failure/repair/verification signatures, and high-confidence noun-
substitution copies. It does not treat topical similarity as duplication.
"""
from __future__ import annotations

import math
import re
import unicodedata
from collections import Counter, defaultdict
from hashlib import sha256
from itertools import combinations
from typing import Any, Iterable

_DISCRIMINATIVE_FIELDS = (
    "title", "failure_modes", "observables", "falsifiers", "repairs", "verification"
)
_OPERATIONAL_FIELDS = (
    "title", "statement", "intent", "applies_when", "does_not_apply_when",
    "failure_modes", "user_impacts", "observables", "falsifiers", "repairs",
    "exceptions", "verification",
)
_SIGNATURE_FIELDS = ("failure_modes", "repairs", "verification")
_UI_OBJECT_NOUNS = frozenset({
    "button", "buttons", "card", "cards", "dialog", "dialogs", "modal", "modals",
    "popover", "popovers", "panel", "panels", "drawer", "drawers", "sheet", "sheets",
    "menu", "menus", "tooltip", "tooltips", "input", "inputs", "field", "fields",
    "link", "links", "tab", "tabs", "badge", "badges", "chip", "chips", "tile", "tiles",
    "table", "tables", "row", "rows", "list", "lists", "grid", "grids", "section", "sections",
    "heading", "headings", "icon", "icons", "image", "images", "control", "controls",
    "component", "components", "widget", "widgets", "item", "items",
})
_TOKEN_RE = re.compile(r"[a-z0-9]+")


def _flatten_value(value: Any) -> str:
    if isinstance(value, str):
        return value
    if isinstance(value, list):
        return " ".join(item for item in value if isinstance(item, str))
    return ""


def _flatten(rule: dict[str, Any], fields: Iterable[str]) -> str:
    return " ".join(_flatten_value(rule.get(field)) for field in fields)


def _tokens(text: str, *, normalize_objects: bool = False) -> list[str]:
    folded = unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode("ascii").lower()
    tokens = _TOKEN_RE.findall(folded)
    if normalize_objects:
        return ["uiobject" if token in _UI_OBJECT_NOUNS else token for token in tokens]
    return tokens


def _word_shingles(tokens: list[str], size: int = 3) -> set[tuple[str, ...]]:
    if not tokens:
        return set()
    if len(tokens) < size:
        return {tuple(tokens)}
    return {tuple(tokens[index:index + size]) for index in range(len(tokens) - size + 1)}


def _char_shingles(tokens: list[str], size: int = 5) -> set[str]:
    text = " ".join(tokens)
    if not text:
        return set()
    if len(text) < size:
        return {text}
    return {text[index:index + size] for index in range(len(text) - size + 1)}


def _jaccard(left: set[Any], right: set[Any]) -> float:
    if not left and not right:
        return 1.0
    union = left | right
    return len(left & right) / len(union) if union else 1.0


def _normalized_text(rule: dict[str, Any], fields: Iterable[str], *, normalize_objects: bool = False) -> str:
    return " ".join(_tokens(_flatten(rule, fields), normalize_objects=normalize_objects))


def _signature(rule: dict[str, Any], *, normalize_objects: bool = False) -> str:
    text = _normalized_text(rule, _SIGNATURE_FIELDS, normalize_objects=normalize_objects)
    return sha256(text.encode("utf-8")).hexdigest() if text else ""


def _rule_repr(rule: dict[str, Any]) -> dict[str, Any]:
    raw_tokens = _tokens(_flatten(rule, _DISCRIMINATIVE_FIELDS))
    object_tokens = _tokens(_flatten(rule, _DISCRIMINATIVE_FIELDS), normalize_objects=True)
    operational = _normalized_text(rule, _OPERATIONAL_FIELDS)
    return {
        "rule_id": str(rule.get("rule_id", "")),
        "operational": operational,
        "raw_word": _word_shingles(raw_tokens, 3),
        "object_word": _word_shingles(object_tokens, 3),
        "object_char": _char_shingles(object_tokens, 5),
        "signature": _signature(rule),
        "object_signature": _signature(rule, normalize_objects=True),
        "index_shingles": _word_shingles(object_tokens, 4),
    }


def _compare_repr(left: dict[str, Any], right: dict[str, Any]) -> dict[str, Any]:
    exact_operational = bool(left["operational"]) and left["operational"] == right["operational"]
    signature_duplicate = bool(left["signature"]) and left["signature"] == right["signature"]
    object_signature_duplicate = (
        bool(left["object_signature"])
        and left["object_signature"] == right["object_signature"]
        and left["signature"] != right["signature"]
    )
    raw_similarity = _jaccard(left["raw_word"], right["raw_word"])
    normalized_similarity = _jaccard(left["object_word"], right["object_word"])
    character_similarity = _jaccard(left["object_char"], right["object_char"])
    noun_substitution_suspect = (
        object_signature_duplicate
        or (
            normalized_similarity >= 0.94
            and character_similarity >= 0.94
            and raw_similarity + 0.015 < normalized_similarity
        )
    )
    near_clone = normalized_similarity >= 0.975 and character_similarity >= 0.965
    duplicate = exact_operational or signature_duplicate or noun_substitution_suspect or near_clone
    reasons: list[str] = []
    if exact_operational:
        reasons.append("exact-operational-copy")
    if signature_duplicate:
        reasons.append("identical-failure-repair-verification-signature")
    if noun_substitution_suspect:
        reasons.append("component-noun-substitution-copy")
    if near_clone and not noun_substitution_suspect:
        reasons.append("high-confidence-operational-near-clone")
    return {
        "left_rule_id": left["rule_id"],
        "right_rule_id": right["rule_id"],
        "duplicate": duplicate,
        "exact_operational": exact_operational,
        "signature_duplicate": signature_duplicate,
        "noun_substitution_suspect": noun_substitution_suspect,
        "raw_similarity": round(raw_similarity, 6),
        "normalized_similarity": round(normalized_similarity, 6),
        "character_similarity": round(character_similarity, 6),
        "reasons": reasons,
    }


def compare_rule_similarity(left: dict[str, Any], right: dict[str, Any]) -> dict[str, Any]:
    if not isinstance(left, dict) or not isinstance(right, dict):
        raise ValueError("V13 rule similarity requires two rule objects")
    return _compare_repr(_rule_repr(left), _rule_repr(right))


def _candidate_pairs(representations: list[dict[str, Any]]) -> set[tuple[int, int]]:
    count = len(representations)
    if count <= 80:
        return set(combinations(range(count), 2))

    candidates: set[tuple[int, int]] = set()
    signature_buckets: dict[str, list[int]] = defaultdict(list)
    object_signature_buckets: dict[str, list[int]] = defaultdict(list)
    for index, item in enumerate(representations):
        if item["signature"]:
            signature_buckets[item["signature"]].append(index)
        if item["object_signature"]:
            object_signature_buckets[item["object_signature"]].append(index)
    for bucket in list(signature_buckets.values()) + list(object_signature_buckets.values()):
        candidates.update(combinations(bucket, 2))

    postings: dict[tuple[str, ...], list[int]] = defaultdict(list)
    for index, item in enumerate(representations):
        for shingle in item["index_shingles"]:
            postings[shingle].append(index)
    max_posting = max(24, math.ceil(count * 0.08))
    shared_counts: Counter[tuple[int, int]] = Counter()
    for bucket in postings.values():
        if 1 < len(bucket) <= max_posting:
            for pair in combinations(bucket, 2):
                shared_counts[pair] += 1
    for pair, shared in shared_counts.items():
        if shared >= 3:
            candidates.add(pair)
    return candidates


def _boilerplate_clusters(representations: list[dict[str, Any]]) -> list[dict[str, Any]]:
    count = len(representations)
    if count < 4:
        return []
    threshold = max(4, math.ceil(count * 0.60))
    postings: dict[tuple[str, ...], set[int]] = defaultdict(set)
    for index, item in enumerate(representations):
        for shingle in item["index_shingles"]:
            postings[shingle].add(index)
    clusters = [
        {"phrase": " ".join(shingle), "rule_count": len(indices)}
        for shingle, indices in postings.items()
        if len(indices) >= threshold and len(set(shingle)) >= 3
    ]
    clusters.sort(key=lambda item: (-item["rule_count"], item["phrase"]))
    return clusters[:25]


def audit_catalog_similarity(rules: list[dict[str, Any]]) -> dict[str, Any]:
    if not isinstance(rules, list):
        raise ValueError("V13 similarity audit requires a rule list")
    representations = [_rule_repr(rule) for rule in rules]
    candidates = _candidate_pairs(representations)
    duplicate_pairs: list[dict[str, Any]] = []
    for left_index, right_index in sorted(candidates):
        result = _compare_repr(representations[left_index], representations[right_index])
        if result["duplicate"]:
            duplicate_pairs.append(result)
    clusters = _boilerplate_clusters(representations)
    return {
        "valid": not duplicate_pairs and not clusters,
        "rule_count": len(rules),
        "candidate_pair_count": len(candidates),
        "duplicate_pair_count": len(duplicate_pairs),
        "duplicate_pairs": duplicate_pairs,
        "boilerplate_cluster_count": len(clusters),
        "boilerplate_clusters": clusters,
        "claim_boundary": "anti-duplication-only",
    }


__all__ = ["audit_catalog_similarity", "compare_rule_similarity"]
