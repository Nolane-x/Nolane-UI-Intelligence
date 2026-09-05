"""V13 map and location rules for accuracy, freshness, permission, selection, and route authority."""
from __future__ import annotations

from ._capabilities import interaction_caps


MAP_LOCATION_RULES_V13 = [
    {'rule_id': 'ui.map.position-accuracy-bound-visible',
     'domain': 'map',
     'class': 'contextual',
     'severity': 'moderate',
     'enforcement': 'warn',
     'title': 'Location-dependent UI must expose meaningful position accuracy when precision matters',
     'statement': 'If an action or interpretation depends on how precise a reported position is, the UI must expose or '
                  'operationalize the available accuracy bound instead of rendering every geolocation sample as an exact '
                  'point.',
     'intent': 'Prevent low-confidence location data from being mistaken for precise user, device, delivery, or asset '
               'position.',
     'applies_when': ['The product uses device geolocation for decisions where tens or hundreds of meters of uncertainty '
                      "could change the user's interpretation or available action."],
     'does_not_apply_when': [],
     'failure_modes': ['A coarse or degraded position is displayed as an exact marker or accepted for a '
                       'precision-dependent task without any accuracy boundary or fallback.'],
     'user_impacts': ['Users can choose the wrong nearby place, confirm an incorrect location, or believe the system '
                      'knows a precision it does not have.'],
     'observables': ['Feed positions with materially different reported accuracy and compare the marker, confidence '
                     'treatment, and precision-dependent action availability.'],
     'falsifiers': ['Low-accuracy samples are represented or constrained according to their actual uncertainty and '
                    'precise actions wait for sufficient evidence or user confirmation.'],
     'repairs': ['Carry the platform accuracy value into location state and use it to qualify precision-dependent '
                 'rendering, snapping, or confirmation decisions.'],
     'exceptions': [],
     'verification': ['Test high, medium, and poor accuracy samples plus missing accuracy and verify the interface never '
                      'upgrades uncertainty into false precision.'],
     'owner_hints': ['designing-geospatial-interfaces'],
     'verifier_hints': ['critiquing-user-experience'],
     'capabilities': interaction_caps(**{'visual-render': 'REQUIRED', 'browser-runtime': 'REQUIRED'}),
     'provenance_ids': ['w3c-geolocation-2026-v13'],
     'status': 'active'},
    {'rule_id': 'ui.map.position-freshness-visible',
     'domain': 'map',
     'class': 'behavioral',
     'severity': 'major',
     'enforcement': 'block',
     'title': 'Map position must not appear current after its location sample becomes stale',
     'statement': 'When a device or tracked asset stops producing fresh positions, the map must distinguish the last '
                  'known sample from a current live location rather than continuing to animate or label the marker as '
                  'present-tense truth.',
     'intent': 'Separate location freshness from marker persistence so stale coordinates remain useful without '
               'masquerading as a live fix.',
     'applies_when': ['A map retains a last known location while updates can pause because of connectivity, background '
                      'policy, permission, sensor availability, or tracking gaps.'],
     'does_not_apply_when': [],
     'failure_modes': ['The same live indicator persists indefinitely after updates stop, with no age, stale state, or '
                       'loss-of-signal transition.'],
     'user_impacts': ['Users can act on outdated position information while believing the device or person is still at '
                      'that location.'],
     'observables': ['Stop position updates at known timestamps and observe marker state, freshness labels, route '
                     'behavior, and actions as the configured staleness boundary passes.'],
     'falsifiers': ['The last sample remains explicitly last-known or stale and live-only actions do not imply newer '
                    'evidence than the product has.'],
     'repairs': ['Track sample timestamp separately from render time and transition location state when freshness no '
                 "longer satisfies the product's declared live threshold."],
     'exceptions': [],
     'verification': ['Simulate background suspension, network loss, permission revocation, and delayed samples and '
                      'verify freshness never resets merely because the map rerenders.'],
     'owner_hints': ['designing-geospatial-interfaces'],
     'verifier_hints': ['critiquing-functional-completeness'],
     'capabilities': interaction_caps(),
     'provenance_ids': ['w3c-geolocation-2026-v13', 'nui-internal-product-truth-v13'],
     'status': 'active'},
    {'rule_id': 'ui.map.map-list-selection-synchronized',
     'domain': 'map',
     'class': 'behavioral',
     'severity': 'major',
     'enforcement': 'block',
     'title': 'Map and list views must represent the same selected place identity',
     'statement': 'When a place can be selected from either a map marker or a coordinated result list, both views must '
                  'resolve selection through the same stable place identity rather than independent indexes or '
                  'nearest-visible heuristics.',
     'intent': 'Keep spatial and textual representations synchronized so users never inspect details for a different '
               'place than the marker they selected.',
     'applies_when': ['A product pairs a map with a list, carousel, results panel, or detail pane that can select the '
                      'same location entities.'],
     'does_not_apply_when': [],
     'failure_modes': ['Selecting a marker highlights or opens a list item belonging to another record after sorting, '
                       'clustering, filtering, pagination, or asynchronous refresh.'],
     'user_impacts': ['Users can navigate, call, book, or edit the wrong place because the two representations disagree '
                      'about selection.'],
     'observables': ['Select entities alternately from map and list while sorting, filtering, refreshing, and '
                     'clustering, then compare stable entity IDs in both views and the detail target.'],
     'falsifiers': ['Marker, list item, detail panel, and URL state all point to the same stable entity until an '
                    'explicit selection change occurs.'],
     'repairs': ['Use canonical place identifiers for cross-view selection and reconcile missing or filtered '
                 'counterparts explicitly rather than substituting by position.'],
     'exceptions': [],
     'verification': ['Exercise selection during result reordering, map pan, cluster expansion, and partial refresh and '
                      'verify identity stays aligned across every surface.'],
     'owner_hints': ['designing-map-list-coordination'],
     'verifier_hints': ['critiquing-functional-completeness'],
     'capabilities': interaction_caps(),
     'provenance_ids': ['nui-map-geospatial-owners-v13'],
     'status': 'active'},
    {'rule_id': 'ui.map.cluster-expansion-preserves-selected-place',
     'domain': 'map',
     'class': 'behavioral',
     'severity': 'moderate',
     'enforcement': 'warn',
     'title': 'Expanding or collapsing marker clusters must preserve an existing selected place',
     'statement': 'If a selected marker becomes part of a cluster or emerges from one as zoom changes, the product must '
                  'preserve that place identity or explicitly clear selection instead of silently transferring selection '
                  'to another cluster member.',
     'intent': 'Keep zoom-driven aggregation from mutating user intent when the selected geographic entity remains '
               'present in the dataset.',
     'applies_when': ['Map marker clustering changes as zoom, viewport, filtering, or density changes while a specific '
                      'place is selected.'],
     'does_not_apply_when': [],
     'failure_modes': ['Cluster recomputation assigns selected styling or detail state to a different marker because '
                       'selection was stored by rendered marker index or cluster representative.'],
     'user_impacts': ['Users can think they are still following one place while the map and details have switched to '
                      'another without an explicit action.'],
     'observables': ['Select a marker, cross multiple cluster thresholds, pan, and return while comparing the selected '
                     'entity ID with the detail surface and cluster membership.'],
     'falsifiers': ['The original entity remains selected when it still exists, or selection is explicitly cleared when '
                    'the entity leaves the result set; no substitute member inherits it implicitly.'],
     'repairs': ['Store selection independently of cluster render nodes and recompute only the visual representation of '
                 'that stable selected entity.'],
     'exceptions': [],
     'verification': ['Test cluster merge, split, filter removal, re-addition, and viewport return and verify selection '
                      'identity follows the entity rather than the cluster node.'],
     'owner_hints': ['designing-map-marker-clustering'],
     'verifier_hints': ['critiquing-user-experience'],
     'capabilities': interaction_caps(),
     'provenance_ids': ['nui-map-geospatial-owners-v13'],
     'status': 'active'},
    {'rule_id': 'ui.map.denied-location-has-manual-location-path',
     'domain': 'map',
     'class': 'behavioral',
     'severity': 'major',
     'enforcement': 'block',
     'title': 'Denied geolocation must preserve a manual path for location-dependent tasks when feasible',
     'statement': 'If a core task can be completed with a user-entered place, address, region, or map selection, denying '
                  'device geolocation must not trap the user behind repeated permission prompts or a dead location '
                  'screen.',
     'intent': 'Treat sensor permission as one acquisition path rather than automatic authority to block a task that can '
               'accept explicit user-provided location.',
     'applies_when': ['A location-dependent workflow has a meaningful manual location alternative and browser or '
                      'platform geolocation permission can be denied.'],
     'does_not_apply_when': [],
     'failure_modes': ['After denial, the interface keeps requesting location or disables the workflow even though '
                       'manual address, search, or map selection could satisfy the task.'],
     'user_impacts': ['Users who protect their location privacy can be excluded from otherwise available functionality '
                      'without a product necessity.'],
     'observables': ['Deny geolocation before and during the workflow and verify manual search, entry, or selection can '
                     'still reach the same location-dependent task boundary.'],
     'falsifiers': ['Denial produces a truthful permission state plus a usable manual alternative whenever the product '
                    'actually supports one.'],
     'repairs': ['Route denied permission into a manual location acquisition mode and reserve new permission requests '
                 'for explicit user intent or capability that truly requires the sensor.'],
     'exceptions': [],
     'verification': ['Test first-run denial, permanent denial, revocation after prior grant, and unavailable sensors '
                      'and verify the manual path remains functional.'],
     'owner_hints': ['designing-location-permission-recovery'],
     'verifier_hints': ['critiquing-user-experience'],
     'capabilities': interaction_caps(),
     'provenance_ids': ['w3c-geolocation-2026-v13', 'w3c-permissions-2025-v13'],
     'status': 'active'},
    {'rule_id': 'ui.map.background-location-active-state-visible',
     'domain': 'map',
     'class': 'behavioral',
     'severity': 'major',
     'enforcement': 'block',
     'title': 'Background location collection must have a truthful active state and stop boundary',
     'statement': 'When the product intentionally continues location collection outside the foreground task, its UI must '
                  'expose that ongoing state and provide the product-defined stop or permission-management boundary '
                  'instead of implying collection ended with the screen.',
     'intent': 'Make background location a visible continuing capability rather than a hidden consequence of a one-time '
               'foreground interaction.',
     'applies_when': ['The application can keep observing location in the background or after the initiating map screen '
                      'is no longer active.'],
     'does_not_apply_when': [],
     'failure_modes': ['The foreground control looks stopped or completed while background collection remains active, or '
                       'the UI exposes no way to understand how to end the declared collection behavior.'],
     'user_impacts': ['Users can continue sharing sensitive location without realizing the product still has an active '
                      'background purpose.'],
     'observables': ['Start background tracking, leave the initiating surface, inspect app and platform indicators, then '
                     'stop through each supported path and verify collection state actually ends.'],
     'falsifiers': ['The visible state matches whether background collection is currently active and the documented stop '
                    'path terminates or relinquishes that capability.'],
     'repairs': ['Persist an explicit background-tracking session state tied to the underlying location subscription and '
                 'reconcile it with platform permission and lifecycle changes.'],
     'exceptions': [],
     'verification': ['Test foreground exit, app backgrounding, device restart where supported, permission revocation, '
                      'and explicit stop and verify state stays truthful.'],
     'owner_hints': ['designing-background-location-awareness'],
     'verifier_hints': ['critiquing-security-and-privacy'],
     'capabilities': interaction_caps(),
     'provenance_ids': ['w3c-geolocation-2026-v13', 'w3c-permissions-2025-v13'],
     'status': 'active'},
    {'rule_id': 'ui.map.route-recalculation-does-not-change-destination',
     'domain': 'map',
     'class': 'behavioral',
     'severity': 'major',
     'enforcement': 'block',
     'title': 'Route recalculation must not silently substitute a different destination',
     'statement': 'Automatic rerouting may change the path around congestion or missed turns, but it must preserve the '
                  'user-selected destination identity unless the product explicitly asks to replace or refine that '
                  'destination.',
     'intent': 'Separate route optimization from destination authority so a recalculation cannot quietly navigate to a '
               'nearby but different entity.',
     'applies_when': ['A navigation or route-planning surface automatically recalculates paths as position, traffic, '
                      'road state, or travel mode changes.'],
     'does_not_apply_when': [],
     'failure_modes': ['Recalculation resolves the destination again from mutable search text or map proximity and '
                       'substitutes a different place record without explicit user intent.'],
     'user_impacts': ['Users can be guided to the wrong entrance, branch, address, or business while believing only the '
                      'route changed.'],
     'observables': ['Start routes to ambiguous and nearby destinations, trigger multiple recalculations, and compare '
                     'destination stable ID and coordinates before and after each route update.'],
     'falsifiers': ['The route path can change while destination identity remains fixed; any destination replacement '
                    'requires an explicit selection or confirmation boundary.'],
     'repairs': ['Freeze the selected destination entity into route state and recompute paths against that entity rather '
                 'than re-running destination discovery during reroute.'],
     'exceptions': [],
     'verification': ['Test missed turns, traffic reroute, travel-mode switch, map refresh, and search-result changes '
                      'and verify destination identity never changes implicitly.'],
     'owner_hints': ['designing-route-comparison'],
     'verifier_hints': ['critiquing-functional-completeness'],
     'capabilities': interaction_caps(),
     'provenance_ids': ['nui-map-geospatial-owners-v13'],
     'status': 'active'},
    {'rule_id': 'ui.map.location-unavailable-distinct-from-no-results',
     'domain': 'map',
     'class': 'behavioral',
     'severity': 'major',
     'enforcement': 'block',
     'title': 'Unavailable location evidence must not be rendered as an empty nearby-results state',
     'statement': 'A nearby-search or location-aware surface must distinguish failure to obtain a usable position from a '
                  'valid search that returned zero nearby results, because those states have different recovery actions '
                  'and meanings.',
     'intent': 'Keep sensor or permission failure from being misrepresented as a legitimate data result.',
     'applies_when': ['The product queries nearby entities only after acquiring device location or another current '
                      'position input.'],
     'does_not_apply_when': [],
     'failure_modes': ['Permission denial, timeout, sensor error, or unusable accuracy produces the same empty-state '
                       'copy and zero-count UI as a successful nearby query with no matches.'],
     'user_impacts': ['Users can conclude that nothing is nearby when the product actually never established the '
                      'location required to run the query.'],
     'observables': ['Force each acquisition failure and a true zero-result query, then compare status, copy, retry '
                     'paths, analytics state, and whether a search request was actually issued.'],
     'falsifiers': ['Location acquisition failures identify the missing prerequisite and recovery path, while a '
                    'zero-result state appears only after a valid query completes.'],
     'repairs': ['Model location acquisition and result retrieval as separate state machines and render empty results '
                 'only from the completed-query branch.'],
     'exceptions': [],
     'verification': ['Test denied, timeout, stale, low-accuracy, offline, and true-zero-result cases and verify each '
                      'reaches the correct distinct state.'],
     'owner_hints': ['designing-geospatial-interfaces'],
     'verifier_hints': ['critiquing-functional-completeness'],
     'capabilities': interaction_caps(),
     'provenance_ids': ['w3c-geolocation-2026-v13', 'nui-internal-product-truth-v13'],
     'status': 'active'},
]

__all__ = ['MAP_LOCATION_RULES_V13']
