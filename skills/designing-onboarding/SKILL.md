---
name: designing-onboarding
description: Use when new or returning users need to understand value, configure prerequisites, learn interaction, import/create initial data, or reach a meaningful first success.
---

# Designing Onboarding

## Overview
Onboarding should get users to a meaningful product outcome with the least unnecessary ceremony. It is not a carousel of feature claims.

## Parent Contract
**Required parent:** `routing-ui-work`.

Use product intent, first-use user/task model, prerequisites, permissions, and first valuable action.

## Define activation
Name the earliest outcome that demonstrates real value. Examples: first teammate invited and working, first data source connected and showing valid data, first project deployed, first document published. Avoid vanity activation such as “completed tutorial” unless the tutorial itself creates value.

## Prerequisite map
Separate:
- must happen before value
- can happen just-in-time
- optional personalization
- admin-only setup
- irreversible/high-consequence choices

Ask for configuration only when the downstream product actually needs it.

## Learning model
Prefer learning in context:
- empty state that starts the real task
- inline explanation at the first unfamiliar control
- progressive checklist linked to useful actions
- sample data only when users can distinguish it from real data and it teaches the product
- interactive tutorial when the interaction itself cannot be understood safely through normal use

Avoid forced multi-screen tours that users cannot connect to actual controls later.

## Choice and escape
Allow skip/dismiss when onboarding is not required for product correctness. Preserve a way to resume. Do not hold the core product hostage to optional profile questions or marketing preferences.

## Role-aware onboarding
Different actors may have different activation paths: admin configures workspace; member joins existing context. Do not show creation/setup to users without permission.

## Returning users
Detect stale/partial onboarding and changed product state. Do not replay completed steps because a UI flag reset. Re-entry should say what remains and why.

## Progress
Use progress only when there is a meaningful bounded sequence. A checklist can be non-linear; a stepper implies order/dependency. Do not fabricate linearity for aesthetic neatness.

## Trust
Explain permissions, data import, billing, or external connections before requesting consequential access. Do not hide scope inside a tooltip after authorization.

## Output: `onboarding-contract`
Return `activation_event`, `prerequisites`, `deferred_setup`, `learning_moments`, `role_paths`, `skip_resume_policy`, `sample_data_policy`, `progress_model`, `trust_explanations`, and `success_transition`.
