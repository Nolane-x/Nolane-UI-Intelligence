"""Canonical semantic coordinates for UX failure reasoning.

Mechanisms describe *why* an experience can fail. They are not enforcement
rules and never imply a finding by themselves.
"""

from __future__ import annotations


UX_MECHANISMS = tuple(sorted((
    {
        "mechanism_id": "ambiguous-consequence",
        "title": "Ambiguous consequence",
        "definition": "The interface asks for commitment before the user can reliably understand what state, scope, cost, or other consequence the action will create.",
        "diagnostic_question": "Can a reasonable user predict the material consequence of the action before committing it?",
        "signals": ("Action labels describe mechanics but not material outcomes.", "Scope, permanence, price, audience, or destructive effect is revealed only after commit."),
        "non_examples": ("A reversible low-impact action whose immediate result is obvious from context.",),
    },
    {
        "mechanism_id": "context-loss",
        "title": "Task context loss",
        "definition": "A transition inside one continuing user goal discards information, position, selection, or intent that the user still needs to complete that goal.",
        "diagnostic_question": "After a transition, does the user retain the task context required to continue without reconstructing it?",
        "signals": ("Returning to a prior step clears still-relevant state.", "Navigation preserves the page destination but loses the working object or selection."),
        "non_examples": ("Intentional reset after the user explicitly starts a new independent task.",),
    },
    {
        "mechanism_id": "cross-step-inconsistency",
        "title": "Cross-step inconsistency",
        "definition": "Different stages of one workflow disagree about the same object, choice, constraint, or outcome without an explicit state transition explaining the difference.",
        "diagnostic_question": "Do all steps present a coherent view of shared state unless a visible event legitimately changed it?",
        "signals": ("A later step summarizes a different choice than the one confirmed earlier.", "Back-navigation reveals stale values that contradict the current commit state."),
        "non_examples": ("A value changes after a clearly surfaced server-side update and the workflow explains the refresh.",),
    },
    {
        "mechanism_id": "decision-overload",
        "title": "Decision overload",
        "definition": "The experience presents distinctions, options, or trade-offs in a form that exceeds what is necessary to make the current decision accurately.",
        "diagnostic_question": "Does the current decision expose only distinctions that materially change the user's next choice or outcome?",
        "signals": ("Equivalent options are presented without decision-relevant differentiation.", "Secondary configuration competes with the primary decision before it becomes relevant."),
        "non_examples": ("A professional tool exposes dense controls because expert users need simultaneous comparison to make the decision.",),
    },
    {
        "mechanism_id": "false-completion",
        "title": "False completion",
        "definition": "The interface communicates success or completion while required work remains pending, failed, conditional, or unconfirmed.",
        "diagnostic_question": "Does every completion signal correspond to a state that actually satisfies the promised outcome?",
        "signals": ("A success screen appears before the authoritative operation succeeds.", "A workflow closes while a required background step has failed silently."),
        "non_examples": ("The interface says an operation was submitted and clearly marks final completion as pending.",),
    },
    {
        "mechanism_id": "goal-displacement",
        "title": "Goal displacement",
        "definition": "The product architecture is organized around generic features, implementation entities, or fashionable UI patterns instead of the recurring goals users actually arrive to accomplish.",
        "diagnostic_question": "Can each major surface be justified by a concrete recurring user goal rather than by a generic product template?",
        "signals": ("A dashboard exists without a recurring question it helps answer.", "Navigation mirrors database entities while common user tasks span those entities awkwardly."),
        "non_examples": ("A conventional dashboard whose metrics directly drive the user's repeated operational decisions.",),
    },
    {
        "mechanism_id": "hidden-dependency",
        "title": "Hidden dependency",
        "definition": "A task outcome depends on another state, prerequisite, permission, resource, or actor that is not exposed before the user invests or commits relevant work.",
        "diagnostic_question": "Are material prerequisites visible at the point where they can still change the user's plan?",
        "signals": ("A final action fails because of a prerequisite that could have been known earlier.", "A choice appears available although a hidden permission makes it impossible."),
        "non_examples": ("An unpredictable external failure that could not reasonably be detected before execution.",),
    },
    {
        "mechanism_id": "mental-model-mismatch",
        "title": "Mental-model mismatch",
        "definition": "The interface names, groups, or behaves around concepts that conflict with how the intended user understands the domain or task.",
        "diagnostic_question": "Do interface concepts map to the user's domain concepts closely enough that consequences can be predicted without learning internal implementation terminology?",
        "signals": ("The UI exposes internal system jargon as the primary product vocabulary.", "Objects that users consider persistent appear to change identity across screens."),
        "non_examples": ("A specialized professional product intentionally uses established domain terminology unfamiliar to novices.",),
    },
    {
        "mechanism_id": "navigation-disorientation",
        "title": "Navigation disorientation",
        "definition": "A navigation transition weakens the user's understanding of where they are, which object they are acting on, how they arrived there, or how to resume the surrounding task.",
        "diagnostic_question": "After navigation, can the user identify location, working object, and meaningful return path without reconstructing history?",
        "signals": ("Detail views lose parent collection context.", "Two visually identical destinations operate on different objects without persistent identity cues."),
        "non_examples": ("A focused full-screen mode that deliberately removes navigation while clearly preserving the active object and exit path.",),
    },
    {
        "mechanism_id": "premature-commitment",
        "title": "Premature commitment",
        "definition": "The experience forces an irreversible, costly, or constraining decision before the information needed to make that decision is naturally available.",
        "diagnostic_question": "Is the user asked to commit only after the information that materially affects the commitment can be known?",
        "signals": ("A user must choose a long-term configuration before seeing its practical effect.", "Irreversible scope is chosen before dependent options are visible."),
        "non_examples": ("An early reversible preference that can be changed freely and helps tailor later choices.",),
    },
    {
        "mechanism_id": "state-without-explanation",
        "title": "State without explanation",
        "definition": "The product changes a task-relevant state, scope, availability, or result without exposing the event or reason needed to interpret the new state correctly.",
        "diagnostic_question": "When task-relevant state changes, is enough cause or freshness information visible to prevent a false inference?",
        "signals": ("A result set changes silently after background refresh.", "Previously available scope disappears without indicating the constraint that changed."),
        "non_examples": ("A live value changes continuously in a context where real-time updates are explicit and expected.",),
    },
    {
        "mechanism_id": "unnecessary-recall",
        "title": "Unnecessary recall",
        "definition": "The interface makes users remember or re-enter information that the product already possesses and can safely reuse or present for recognition.",
        "diagnostic_question": "Is the user reconstructing known state from memory when the system could preserve or surface it without creating ambiguity or risk?",
        "signals": ("A later step asks for the same identifier without semantic reason.", "A comparison flow hides prior values that are necessary to decide the next change."),
        "non_examples": ("Security-sensitive re-authentication that intentionally requires fresh proof rather than reuse.",),
    },
    {
        "mechanism_id": "unrecoverable-progress-loss",
        "title": "Unrecoverable progress loss",
        "definition": "User-authored or task-critical progress is destroyed without explicit intent, adequate warning, or a viable recovery path.",
        "diagnostic_question": "Can valuable in-progress work survive predictable navigation, interruption, expiry, retry, and recoverable failure modes?",
        "signals": ("Session expiry clears an unsaved form with no restoration path.", "A retry resets completed steps that remain semantically valid."),
        "non_examples": ("The user explicitly discards a draft after a consequence-confirming action.",),
    },
    {
        "mechanism_id": "workflow-fragmentation",
        "title": "Workflow fragmentation",
        "definition": "A coherent user goal is split across surfaces or states in a way that creates dead ends, missing handoffs, or unnecessary reconstruction between steps.",
        "diagnostic_question": "Can the user move through the complete goal with explicit handoffs and a viable next action at each recoverable state?",
        "signals": ("An error state offers no route back to a valid task state.", "A workflow hands off to another surface without carrying the identifiers needed to continue."),
        "non_examples": ("A deliberate cross-tool handoff that preserves context and clearly explains the next action.",),
    },
), key=lambda item: item["mechanism_id"]))


__all__ = ["UX_MECHANISMS"]
