---
name: designing-help-center-navigation
description: Use when a documentation or support center needs users to move from a problem statement to the right article, section, product area, or support path through taxonomy, search, breadcrumbs, and recovery.
---

# Designing Help Center Navigation

## Parent Contract
**Required parent:** `designing-onboarding`.

This faculty owns information finding inside a help/support corpus. It does not write the documentation itself and does not replace in-product contextual help. Its success is measured by whether a user with a concrete question can identify and reach the right guidance or escalation route without first learning the documentation team's internal taxonomy.

## Decision Architecture
Organize the help center around user-recognizable products, tasks, and problem classes. Internal org structures such as “Platform Services” or “Growth Infrastructure” are weak top-level categories unless customers already use those concepts. Support browsing and search as complementary paths: browsing helps users who cannot name the problem, while search serves users with a term or error phrase.

Article destinations need orientation. Preserve category breadcrumbs, version/product scope, related next steps, and a route back to search results. If an article applies only to a plan, platform, role, or software version, declare that before users follow instructions that cannot work in their context.

Search no-results and article dead ends need recovery. Suggest broader categories, corrected terms, relevant troubleshooting, or escalation based on evidence rather than generic “contact support” everywhere. When content is translated, fallback to another language must be explicit; silently mixing languages in a navigation tree can make users think sections are missing.

## Failure Topology
- Categories mirror internal teams and users cannot predict where account recovery belongs.
- Search result opens an article but browser Back loses the original query and filters.
- Old-version article ranks first and instructs users to click a control that no longer exists.
- Category page has hundreds of articles with no task grouping or scan hierarchy.
- No-results offers only a blank page despite known related terms or error families.
- Localized help tree hides untranslated articles with no fallback indication.

## Falsification and Recovery
Falsify with vague user language, exact error codes, renamed features, multiple product versions, plan-restricted instructions, mobile navigation, screen-reader landmarks, browser Back, and a locale with partial translation coverage. The design fails if successful navigation requires knowledge of the documentation organization rather than the user's product task or problem.

Recover by task-oriented taxonomy, scoped search metadata, preserved query history, explicit version/plan applicability, useful no-result expansion, localized fallback policy, and escalation links connected to the unresolved problem context.

## Output Contract
Return `help-center-navigation-contract` with taxonomy, browse/search relationship, article scope metadata, breadcrumbs, query-return behavior, no-result recovery, related-content logic, version/plan/locale handling, escalation paths, accessibility navigation, and falsification cases.