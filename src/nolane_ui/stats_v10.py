"""Paired statistics and ablation-identification helpers for NUI V10."""
from __future__ import annotations

import random
from statistics import mean, median
from typing import Any


def paired_delta(full: dict[str, float], control: dict[str, float]) -> float:
    if set(full) != set(control) or not full:
        raise ValueError("paired samples must have identical non-empty keys")
    deltas = [float(full[k]) - float(control[k]) for k in sorted(full)]
    return mean(deltas)


def bootstrap_ci(paired_deltas: list[float], confidence: float = 0.95, resamples: int = 5000, seed: int = 0) -> tuple[float, float]:
    if not paired_deltas:
        raise ValueError("bootstrap requires paired deltas")
    if not 0 < confidence < 1:
        raise ValueError("confidence must be within 0..1")
    if resamples < 100:
        raise ValueError("resamples must be at least 100")
    values = [float(x) for x in paired_deltas]
    rng = random.Random(seed)
    draws: list[float] = []
    n = len(values)
    for _ in range(resamples):
        sample = [values[rng.randrange(n)] for _ in range(n)]
        draws.append(mean(sample))
    draws.sort()
    alpha = (1 - confidence) / 2
    lo_i = max(0, min(len(draws) - 1, int(alpha * (len(draws) - 1))))
    hi_i = max(0, min(len(draws) - 1, int((1 - alpha) * (len(draws) - 1))))
    observed = mean(values)
    return (min(draws[lo_i], observed), max(draws[hi_i], observed))


def summarize_paired(full: dict[str, float], control: dict[str, float], *, seed: int = 0) -> dict[str, Any]:
    if set(full) != set(control) or not full:
        raise ValueError("paired samples must have identical non-empty keys")
    keys = sorted(full)
    deltas = [float(full[k]) - float(control[k]) for k in keys]
    return {
        "n": len(keys),
        "full_mean": mean(float(full[k]) for k in keys),
        "control_mean": mean(float(control[k]) for k in keys),
        "paired_delta": mean(deltas),
        "median_delta": median(deltas),
        "ci": bootstrap_ci(deltas, seed=seed),
        "wins": sum(1 for x in deltas if x > 0),
        "ties": sum(1 for x in deltas if x == 0),
        "losses": sum(1 for x in deltas if x < 0),
    }


def evaluate_ablation_recovery(full: dict[str, list[float]], ablated: dict[str, list[float]], target_dimension: str, *, min_delta: float = 0.0) -> dict[str, Any]:
    errors: list[str] = []
    full_values = full.get(target_dimension, []) if isinstance(full, dict) else []
    ablated_values = ablated.get(target_dimension, []) if isinstance(ablated, dict) else []
    if not isinstance(full_values, list) or not isinstance(ablated_values, list) or not full_values or len(full_values) != len(ablated_values):
        return {"identified": False, "errors": ["ablation comparison requires matched non-empty samples"], "delta": None}
    deltas = [float(a) - float(b) for a, b in zip(full_values, ablated_values)]
    delta = mean(deltas)
    ci = bootstrap_ci(deltas, resamples=1000, seed=17)
    if delta <= min_delta:
        errors.append("targeted ablation did not degrade the owned dimension")
    if len(deltas) >= 3 and ci[0] <= 0:
        errors.append("targeted ablation degradation is not directionally stable under bootstrap")
    return {"identified": not errors, "errors": errors, "delta": delta, "ci": ci, "n": len(deltas)}


def aggregate_dimension(samples: list[dict[str, Any]], dimension: str) -> dict[str, Any]:
    observed = [x for x in samples if isinstance(x, dict) and x.get("dimension") == dimension]
    statuses = [str(x.get("status", "missing")) for x in observed]
    scores = [float(x["score"]) for x in observed if x.get("status") == "success" and isinstance(x.get("score"), (int, float))]
    return {
        "dimension": dimension,
        "n_total": len(observed),
        "n_scored": len(scores),
        "mean": mean(scores) if scores else None,
        "median": median(scores) if scores else None,
        "failed": sum(1 for s in statuses if s == "failed"),
        "timeout": sum(1 for s in statuses if s == "timeout"),
        "excluded": sum(1 for s in statuses if s == "excluded"),
        "missing_rate": 0 if not observed else 1 - (len(scores) / len(observed)),
    }


__all__ = ["paired_delta", "bootstrap_ci", "summarize_paired", "evaluate_ablation_recovery", "aggregate_dimension"]
