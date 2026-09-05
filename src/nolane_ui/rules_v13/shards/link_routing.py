"""V13 seventh-wave independently authored rules for link routing."""
from __future__ import annotations

from ._capabilities import interaction_caps


LINK_ROUTING_RULES_V13 = [{'rule_id': 'ui.link.deep-link-target-scope-visible',
  'domain': 'link',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Deep links must resolve to the intended resource scope rather than whichever similar context is '
           'currently active',
  'statement': 'A deep link should carry enough stable resource and tenant context that opening it cannot '
               'silently reinterpret the target inside the viewer’s previously active workspace.',
  'intent': 'Prevent same-named resources from being opened or modified in the wrong scope.',
  'applies_when': ['The application has multiple workspaces or tenants and supports deep links to nested '
                   'resources.'],
  'does_not_apply_when': [],
  'failure_modes': ['A link contains only a local item ID and the app opens the same ID in the currently '
                    'selected workspace rather than the sender’s intended scope.'],
  'user_impacts': ['Users can inspect or act on a different resource than the one the link was meant to '
                   'identify.'],
  'observables': ['Open the same link from sessions with different active scopes and compare resolved stable '
                  'resource identity.'],
  'falsifiers': ['The link either resolves the intended scope explicitly or blocks with an understandable '
                 'access/context error instead of retargeting.'],
  'repairs': ['Encode stable scoped identity in deep links and revalidate authorization without substituting '
              'the current client context.'],
  'exceptions': [],
  'verification': ['Test copied links across accounts, workspaces, and revoked access, verifying the target '
                   'never changes because of local navigation state.'],
  'owner_hints': ['designing-mobile-deep-link-routing'],
  'verifier_hints': ['critiquing-functional-completeness'],
  'capabilities': interaction_caps(),
  'provenance_ids': ['nui-link-routing-owners-v13'],
  'status': 'active'},
 {'rule_id': 'ui.link.broken-link-has-context-preserving-fallback',
  'domain': 'link',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Broken internal links should preserve enough target context to offer a relevant fallback',
  'statement': 'When an internal resource was moved, deleted, or permission-restricted, the fallback should '
               'explain that outcome and retain safe context rather than dumping users at a generic home '
               'page.',
  'intent': 'Help users recover from stale references without pretending the target never existed.',
  'applies_when': ['Internal links can outlive resource moves, deletions, or access changes.'],
  'does_not_apply_when': [],
  'failure_modes': ['Opening a stale resource URL redirects silently to the dashboard, making it impossible '
                    'to distinguish deletion, permission loss, and malformed link.'],
  'user_impacts': ['Users search the wrong place, assume data loss, or cannot request restored access.'],
  'observables': ['Open links after move, deletion, archive, and permission revocation and inspect the '
                  'resulting route plus available context.'],
  'falsifiers': ['The fallback preserves safe resource or parent context and distinguishes known absence '
                 'from authorization and malformed targets.'],
  'repairs': ['Resolve links through a target lifecycle lookup before choosing contextual fallback; avoid '
              'silent generic redirects.'],
  'exceptions': [],
  'verification': ['Test old bookmarks and links from notifications after lifecycle changes, verifying each '
                   'failure class leads to the appropriate recovery.'],
  'owner_hints': ['designing-mobile-deep-link-routing'],
  'verifier_hints': ['critiquing-functional-completeness'],
  'capabilities': interaction_caps(),
  'provenance_ids': ['nui-link-routing-owners-v13'],
  'status': 'active'},
 {'rule_id': 'ui.link.external-destination-disclosed-before-context-loss',
  'domain': 'link',
  'class': 'behavioral',
  'severity': 'moderate',
  'enforcement': 'warn',
  'title': 'External navigation should disclose destination when leaving the product changes trust or task '
           'context',
  'statement': 'Links that leave the product for an unrelated external site or application should provide '
               'enough destination context when users might otherwise mistake the action for internal '
               'navigation.',
  'intent': 'Reduce accidental context loss and make cross-origin transitions understandable without warning '
            'on every ordinary link.',
  'applies_when': ['An action opens an external origin, native app, or third-party system from a context '
                   'where internal links are otherwise common.'],
  'does_not_apply_when': [],
  'failure_modes': ['A control labelled simply View or Continue opens an unrelated domain with no indication '
                    'that the user is leaving the product.'],
  'user_impacts': ['Users can lose unsaved context or place trust in a destination they did not realize was '
                   'external.'],
  'observables': ['Inspect ambiguous navigation controls and follow them with unsaved state and assistive '
                  'technology, comparing destination cues.'],
  'falsifiers': ['Cross-context navigation is identifiable from label or supporting cue where the '
                 'distinction is decision-relevant, and unsaved-work handling follows product policy.'],
  'repairs': ['Include destination identity in ambiguous external actions and coordinate navigation with '
              'dirty-state protection.'],
  'exceptions': [],
  'verification': ['Test same-tab, new-tab, and native-app destinations, confirming decision-relevant '
                   'external transitions are not visually disguised as internal routes.'],
  'owner_hints': ['designing-link-sharing'],
  'verifier_hints': ['critiquing-functional-completeness'],
  'capabilities': interaction_caps(),
  'provenance_ids': ['nui-link-routing-owners-v13'],
  'status': 'active'},
 {'rule_id': 'ui.link.single-use-link-consumption-visible',
  'domain': 'link',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Single-use links must reconcile clearly after consumption and never appear reusable',
  'statement': 'A one-time invitation, recovery, or action link must transition to consumed state '
               'authoritatively after success and provide a safe explanation on later opens.',
  'intent': 'Prevent repeated use expectations and confusing generic failures after a one-time capability is '
            'spent.',
  'applies_when': ['A link grants an action that policy allows only once.'],
  'does_not_apply_when': [],
  'failure_modes': ['After successful use, the original tab still presents the action as available or a '
                    'later open reports an unexplained server error.'],
  'user_impacts': ['Users may attempt duplicate operations or share a token they believe remains valid.'],
  'observables': ['Consume the link in one session, then revisit and open it concurrently from other '
                  'sessions.'],
  'falsifiers': ['Only one authoritative consumption succeeds and every other client reconciles to a '
                 'consumed/expired outcome with appropriate next steps.'],
  'repairs': ['Make link consumption atomic and map terminal token state into explicit UI instead of '
              'retaining stale actionable controls.'],
  'exceptions': [],
  'verification': ['Race concurrent opens and repeated back/forward navigation, verifying the one-time '
                   'capability never reappears as active.'],
  'owner_hints': ['designing-link-sharing'],
  'verifier_hints': ['critiquing-security-and-privacy'],
  'capabilities': interaction_caps(),
  'provenance_ids': ['nui-link-routing-owners-v13'],
  'status': 'active'},
 {'rule_id': 'ui.link.signed-link-expiry-state-visible',
  'domain': 'link',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Signed or presigned links must expose expired state without conflating it with missing resources',
  'statement': 'When a temporary signed URL expires, the product should distinguish token expiry from file '
               'deletion or permission denial and offer regeneration only through current authority.',
  'intent': 'Make temporary delivery links recoverable without weakening their expiry boundary.',
  'applies_when': ['The system uses expiring signed URLs for downloads, previews, invitations, or temporary '
                   'access.'],
  'does_not_apply_when': [],
  'failure_modes': ['An expired URL shows 404 Not Found or a generic broken-file state, leading users to '
                    'believe the underlying resource disappeared.'],
  'user_impacts': ['Users may duplicate uploads or escalate false data-loss reports instead of refreshing '
                   'authorization.'],
  'observables': ['Open the same resource with valid, expired, revoked, and deleted-link states and compare '
                  'recovery behavior.'],
  'falsifiers': ['Expiry is identifiable and regeneration requires fresh authorization against the resource '
                 'rather than extending the old token.'],
  'repairs': ['Separate resource existence from token validity in error mapping and route authorized users '
              'through new signed-link issuance.'],
  'exceptions': [],
  'verification': ['Test expired links after permission loss and resource deletion, verifying each terminal '
                   'state stays distinct.'],
  'owner_hints': ['designing-link-sharing'],
  'verifier_hints': ['critiquing-security-and-privacy'],
  'capabilities': interaction_caps(),
  'provenance_ids': ['nui-link-routing-owners-v13'],
  'status': 'active'},
 {'rule_id': 'ui.link.copy-uses-canonical-shareable-url',
  'domain': 'link',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Copy-link actions must produce a canonical shareable URL rather than transient application state '
           'URLs',
  'statement': 'A dedicated copy-link action should remove session-only fragments, temporary preview '
               'parameters, or local navigation state that makes the copied URL invalid or misleading for '
               'another recipient.',
  'intent': 'Ensure link sharing reproduces the intended resource view outside the sender’s current browser '
            'state.',
  'applies_when': ['The application has transient routes or query parameters alongside a deliberate Copy '
                   'link action.'],
  'does_not_apply_when': [],
  'failure_modes': ['The copied URL includes an expiring local preview token or sender-only pane state, so '
                    'recipients see an error or unrelated view.'],
  'user_impacts': ['Users believe they shared a stable resource reference when they actually copied a '
                   'browser-session artifact.'],
  'observables': ['Compare address-bar URLs with the dedicated copy action across preview, edit, filtered, '
                  'and temporary states using clean recipient sessions.'],
  'falsifiers': ['The copy action emits the product’s documented canonical resource link and includes '
                 'optional view state only when it is intentionally shareable.'],
  'repairs': ['Construct share links from stable resource routing metadata rather than blindly copying '
              'location.href.'],
  'exceptions': [],
  'verification': ['Test copied links after sender logout, browser restart, and recipient access changes, '
                   'verifying the URL remains a valid reference within policy.'],
  'owner_hints': ['designing-link-sharing'],
  'verifier_hints': ['critiquing-functional-completeness'],
  'capabilities': interaction_caps(),
  'provenance_ids': ['nui-link-routing-owners-v13'],
  'status': 'active'},
 {'rule_id': 'ui.link.mobile-app-web-fallback-preserves-task',
  'domain': 'link',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'App-to-web fallback must preserve the intended task when the native app cannot handle a deep '
           'link',
  'statement': 'If a mobile deep link fails because the app is absent, outdated, or lacks a route, the web '
               'fallback should retain safe task context rather than landing generically or looping between '
               'app and browser.',
  'intent': 'Keep cross-surface continuation usable without creating redirect traps.',
  'applies_when': ['A resource link may open native application routes with web fallback.'],
  'does_not_apply_when': [],
  'failure_modes': ['An unsupported app route bounces repeatedly through the store or home page and loses '
                    'the resource or action the user intended to reach.'],
  'user_impacts': ['Users abandon the task or cannot recover the original target after a failed native '
                   'handoff.'],
  'observables': ['Open deep links with app absent, installed-but-old, logged out, and route unsupported, '
                  'then follow each fallback.'],
  'falsifiers': ['Fallback preserves the safe target context and offers a clear route to web, update, or '
                 'authentication without redirect loops.'],
  'repairs': ['Carry canonical task identity through universal-link and fallback routing and detect '
              'unsupported native capability before repeated redirects.'],
  'exceptions': [],
  'verification': ['Exercise supported and unsupported native versions plus browser-only clients, verifying '
                   'target context survives every fallback path.'],
  'owner_hints': ['designing-mobile-deep-link-routing'],
  'verifier_hints': ['critiquing-functional-completeness'],
  'capabilities': interaction_caps(),
  'provenance_ids': ['nui-link-routing-owners-v13'],
  'status': 'active'},
 {'rule_id': 'ui.link.fragment-navigation-focuses-logical-target',
  'domain': 'link',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Fragment and in-page links must move logical focus when they are used as navigation for keyboard '
           'users',
  'statement': 'When an in-page link jumps to a section that begins meaningful task context, keyboard focus '
               'or a programmatic equivalent should follow the destination rather than leaving the active '
               'element behind off-screen.',
  'intent': 'Align visual location and interaction location for keyboard and assistive-technology '
            'navigation.',
  'applies_when': ['The application uses skip links, table-of-contents fragments, validation anchors, or '
                   'in-page navigation to move the viewport.'],
  'does_not_apply_when': [],
  'failure_modes': ['The viewport jumps to the target heading but keyboard focus remains on the original '
                    'link, so the next Tab continues from the old location.'],
  'user_impacts': ['Keyboard users see one part of the page while interaction and screen-reader context '
                   'remain elsewhere.'],
  'observables': ['Activate each fragment link by keyboard and inspect active element, screen-reader '
                  'announcement, and next-focus order at the destination.'],
  'falsifiers': ['Navigation moves to or establishes a logical focus target consistent with the visible '
                 'destination without creating duplicate tab stops unnecessarily.'],
  'repairs': ['Ensure destination headings or containers can receive programmatic focus and coordinate '
              'scroll plus focus during fragment navigation.'],
  'exceptions': [],
  'verification': ['Test skip navigation, error summaries, and deep-linked fragments, verifying visual and '
                   'logical navigation context stay synchronized.'],
  'owner_hints': ['designing-focus-order-and-restoration'],
  'verifier_hints': ['critiquing-accessibility'],
  'capabilities': interaction_caps(),
  'provenance_ids': ['nui-link-routing-owners-v13'],
  'status': 'active'}]

__all__ = ["LINK_ROUTING_RULES_V13"]
