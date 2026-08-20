---
name: designing-flashcard-study-interfaces
description: Use when this specialist's decision ownership is materially in scope. Own flashcard study interactions across prompt/answer reveal, card variants, media, typed recall, self-grading, editing, bury/suspend, direction, and preservation of retrieval effort.
---
# Designing Flashcard Study Interfaces

## Parent Contract

**Required parent:** `designing-digital-learning-experiences`.

Inherit the broader routing and decision boundary from this canonical parent; this specialist remains accountable only for the narrower ownership, failure topology, falsification criteria, and output contract defined below.

## Decision ownership

Own the presentation and response mechanics of card-based retrieval practice. Decide front/back or cloze prompt, reveal action, typed recall, media, reverse variants, self-grade, card edit, bury/suspend, source note identity, and accessibility. Scheduling belongs to spaced repetition; this owner protects the retrieval interaction itself.

## Inputs and evidence

Require card/note model, prompt/answer fields, cloze syntax, media, direction variants, typed-answer comparison, scheduling callback, editing permission, keyboard/touch needs, and accessibility. Identify cards where answer formatting or alternate valid responses complicate automated comparison.

## Procedure

Present prompt without answer leakage, then require an intentional reveal after sufficient interaction. Typed recall should compare sensitively while allowing learners to inspect differences rather than treating formatting mismatch as knowledge failure. Reverse cards need distinct identity while remaining linked to source note. Editing during review must state whether the current scheduling event remains valid and synchronize all generated card variants. Media controls should not reveal answer content accidentally. Bury/suspend/flag actions remain distinguishable from recall grading.

## Failure topology

Failures include answer visible in image alt text or page title, accidental flip on scroll, typed comparison marking trivial whitespace as wrong, editing source note creating duplicate variants, suspend mistaken for "known", and grading controls shown before reveal. Another failure is rapid keyboard flow causing double grade/skip because state transitions lag.

## Falsification

Reject if answer information leaks before reveal; if reveal and grade can race into one action; if typed comparison hides meaningful difference context; if editing a note desynchronizes generated cards; if bury/suspend semantics are unclear; or if keyboard/screen-reader users cannot distinguish prompt, revealed answer, and grading state.

## Output contract

Return a `flashcard-study-interfaces-contract` with: card/note identity; prompt/reveal state; cloze/reverse variants; typed recall/diff; media behavior; self-grade handoff; edit synchronization; bury/suspend/flag; keyboard/touch; accessibility; and latency/double-action guard. Include one reverse-card edit case.

## Handoffs

Spaced repetition owns scheduling, content/media owners render assets, practice feedback may supply explanation, and progress should not equate card exposure with mastery automatically.