"""V13 eighth-wave independently authored rules for marketplace inventory."""
from __future__ import annotations

from ._capabilities import interaction_caps


MARKETPLACE_INVENTORY_RULES_V13 = [{'rule_id': 'ui.inventory.available-onhand-reserved-distinguished',
  'domain': 'inventory',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Inventory must distinguish on-hand, reserved, and available quantities',
  'statement': 'Physical stock, committed reservations, and sellable availability are different '
               'quantities and must not collapse into one number.',
  'intent': 'Prevent operators from releasing or selling stock based on an ambiguous aggregate.',
  'applies_when': ['Marketplace inventory tracks reservations against physical stock.'],
  'does_not_apply_when': [],
  'failure_modes': ['A dashboard shows “10 in stock” while 8 units are reserved, but the displayed '
                    'number could mean on-hand or available.'],
  'user_impacts': ['Operators can oversell or incorrectly cancel reservations.'],
  'observables': ['Create on-hand stock with mixed reservation states and compare list, detail, '
                  'API, and export quantities.'],
  'falsifiers': ['On-hand, reserved, and available quantities are labeled and reconcile through '
                 'the product’s inventory equation.'],
  'repairs': ['Expose each quantity separately and define available from authoritative reservation '
              'policy rather than presentation arithmetic.'],
  'exceptions': [],
  'verification': ['Change reservations and receipts and verify all three quantities reconcile '
                   'after every transition.'],
  'owner_hints': ['designing-marketplace-inventory-availability'],
  'verifier_hints': ['critiquing-functional-completeness'],
  'capabilities': interaction_caps(),
  'provenance_ids': ['nui-inventory-owners-v13'],
  'status': 'active'},
 {'rule_id': 'ui.inventory.variant-identity-stable',
  'domain': 'inventory',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Inventory operations must bind quantities to stable variant identity',
  'statement': 'SKU labels and option text can change; stock must remain tied to immutable '
               'product/variant identifiers.',
  'intent': 'Prevent stock movements from drifting between similarly named variants.',
  'applies_when': ['Products have multiple variants or mutable SKU/display labels.'],
  'does_not_apply_when': [],
  'failure_modes': ['Renaming “Blue / M” causes a pending adjustment to apply to the newly '
                    'matching label rather than the original variant.'],
  'user_impacts': ['Inventory can be moved or sold against the wrong variant.'],
  'observables': ['Rename SKUs/options while adjustments, reservations, and transfers are pending; '
                  'inspect resulting identities.'],
  'falsifiers': ['Every stock event resolves to the same immutable variant regardless of later '
                 'label changes.'],
  'repairs': ['Use stable variant identifiers for inventory events and show mutable labels only as '
              'descriptive metadata.'],
  'exceptions': [],
  'verification': ['Rename and reorder variants around concurrent inventory changes and verify '
                   'event ownership never changes.'],
  'owner_hints': ['designing-marketplace-inventory-availability'],
  'verifier_hints': ['critiquing-functional-completeness'],
  'capabilities': interaction_caps(),
  'provenance_ids': ['nui-inventory-owners-v13'],
  'status': 'active'},
 {'rule_id': 'ui.inventory.multi-location-source-visible',
  'domain': 'inventory',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Multi-location inventory must expose which location contributes each quantity',
  'statement': 'A global total can hide where units physically or logically exist and which '
               'location can fulfill a specific order.',
  'intent': 'Keep operators from treating network stock as locally fulfillable stock.',
  'applies_when': ['Inventory is distributed across warehouses, stores, or fulfillment nodes.'],
  'does_not_apply_when': [],
  'failure_modes': ['A product shows 20 available units but the selected shipping node has zero '
                    'and the other 20 are non-transferable.'],
  'user_impacts': ['Orders can be promised from inventory that cannot fulfill them.'],
  'observables': ['Create stock at multiple locations with transfer restrictions and inspect '
                  'totals, allocation, and fulfillment choices.'],
  'falsifiers': ['Global totals decompose by location and allocation decisions identify the actual '
                 'source location.'],
  'repairs': ['Carry location identity through stock quantities, reservations, and fulfillment '
              'allocation.'],
  'exceptions': [],
  'verification': ['Change location availability and restrictions and verify order allocation '
                   'never relies on an undisclosed remote quantity.'],
  'owner_hints': ['designing-marketplace-inventory-availability'],
  'verifier_hints': ['critiquing-functional-completeness'],
  'capabilities': interaction_caps(),
  'provenance_ids': ['nui-inventory-owners-v13'],
  'status': 'active'},
 {'rule_id': 'ui.inventory.oversell-conflict-reconciled',
  'domain': 'inventory',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Oversell conflicts must reconcile when concurrent reservations exceed effective stock',
  'statement': 'Concurrent channels can reserve against the same stock; the system must surface '
               'which reservation lost instead of leaving impossible negative availability as '
               'silent truth.',
  'intent': 'Make oversell resolution explicit and recoverable.',
  'applies_when': ['Multiple channels or workers can reserve the same finite inventory '
                   'concurrently.'],
  'does_not_apply_when': [],
  'failure_modes': ['Two channels reserve the last unit and both appear accepted until a later '
                    'background job creates negative availability.'],
  'user_impacts': ['Customers and operators receive contradictory promises that require manual '
                   'cleanup.'],
  'observables': ['Race reservations from multiple channels against one remaining unit and inspect '
                  'acceptance, rejection, and later stock state.'],
  'falsifiers': ['Authoritative reservation limits are enforced or any oversell is surfaced as an '
                 'explicit conflict with affected reservations.'],
  'repairs': ['Serialize or atomically validate reservations and create a dedicated '
              'oversell-resolution state when external systems violate the bound.'],
  'exceptions': [],
  'verification': ['Run concurrent reservations repeatedly and verify no silent negative '
                   'availability persists without a conflict record.'],
  'owner_hints': ['designing-marketplace-inventory-availability'],
  'verifier_hints': ['critiquing-functional-completeness'],
  'capabilities': interaction_caps(),
  'provenance_ids': ['nui-inventory-owners-v13'],
  'status': 'active'},
 {'rule_id': 'ui.inventory.backorder-distinct-from-preorder',
  'domain': 'inventory',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Backorder and preorder inventory states must remain distinct',
  'statement': 'Backorder means demand exceeds currently fulfillable stock, while preorder '
               'represents planned future availability; combining them hides different promises '
               'and dates.',
  'intent': 'Prevent operators and customers from receiving the wrong fulfillment expectation.',
  'applies_when': ['Products can be sold before current on-hand stock is available.'],
  'does_not_apply_when': [],
  'failure_modes': ['A product with delayed replenishment is labeled “preorder” even though '
                    'existing orders are already overdue backorders.'],
  'user_impacts': ['Promised dates and customer communication can be wrong.'],
  'observables': ['Create preorder, backorder, in-stock, and discontinued combinations and inspect '
                  'operational and customer-facing status.'],
  'falsifiers': ['Backorder and preorder are independently represented with their own source and '
                 'expected-availability semantics.'],
  'repairs': ['Model future-sale policy and shortage state separately and compute customer '
              'messaging from both.'],
  'exceptions': [],
  'verification': ['Transition products between planned launch and shortage conditions and verify '
                   'statuses and promises remain semantically correct.'],
  'owner_hints': ['designing-marketplace-inventory-availability'],
  'verifier_hints': ['critiquing-functional-completeness'],
  'capabilities': interaction_caps(),
  'provenance_ids': ['nui-inventory-owners-v13'],
  'status': 'active'},
 {'rule_id': 'ui.inventory.bundle-component-dependency-visible',
  'domain': 'inventory',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Bundle availability must expose limiting component dependencies',
  'statement': 'A bundle is fulfillable only when all required components are available in the '
               'needed quantities; a bundle-level number must not hide the constrained component.',
  'intent': 'Prevent bundles from appearing sellable when one component blocks fulfillment.',
  'applies_when': ['Inventory contains kits or bundles composed of multiple child variants.'],
  'does_not_apply_when': [],
  'failure_modes': ['A bundle shows 12 available because the parent stock is 12, but one required '
                    'component has only 2 units.'],
  'user_impacts': ['Orders can be accepted that cannot be assembled.'],
  'observables': ['Vary individual component quantities and reservations while inspecting bundle '
                  'availability and allocation.'],
  'falsifiers': ['Bundle availability derives from all required components and the limiting '
                 'dependency can be inspected.'],
  'repairs': ['Compute bundle capacity from component requirements and preserve component '
              'reservation provenance.'],
  'exceptions': [],
  'verification': ['Change each component independently and verify bundle availability follows the '
                   'mathematically limiting component.'],
  'owner_hints': ['designing-marketplace-inventory-availability'],
  'verifier_hints': ['critiquing-functional-completeness'],
  'capabilities': interaction_caps(),
  'provenance_ids': ['nui-inventory-owners-v13'],
  'status': 'active'},
 {'rule_id': 'ui.inventory.freshness-visible',
  'domain': 'inventory',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Inventory surfaces must disclose freshness when quantities are synchronized '
           'asynchronously',
  'statement': 'Cached or externally synchronized stock should not appear authoritative without a '
               'freshness marker when lag can affect fulfillment decisions.',
  'intent': 'Prevent operators from treating stale inventory as current availability.',
  'applies_when': ['Inventory data arrive through asynchronous warehouse, ERP, or channel '
                   'synchronization.'],
  'does_not_apply_when': [],
  'failure_modes': ['A warehouse feed is two hours old but the console displays its quantity '
                    'without any stale indicator.'],
  'user_impacts': ['Operators may promise inventory that has already moved elsewhere.'],
  'observables': ['Delay location feeds and compare displayed quantity, timestamp, direct-source '
                  'lookup, and reservation behavior.'],
  'falsifiers': ['The UI exposes a source watermark or stale state and critical actions revalidate '
                 'when freshness is insufficient.'],
  'repairs': ['Carry source freshness with quantity snapshots and require current validation '
              'before irreversible allocation when needed.'],
  'exceptions': [],
  'verification': ['Simulate delayed feeds and verify stale stock is labeled and cannot silently '
                   'authorize a conflicting commitment.'],
  'owner_hints': ['designing-marketplace-inventory-availability'],
  'verifier_hints': ['critiquing-functional-completeness'],
  'capabilities': interaction_caps(),
  'provenance_ids': ['nui-inventory-owners-v13'],
  'status': 'active'},
 {'rule_id': 'ui.inventory.reservation-expiration-visible',
  'domain': 'inventory',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Inventory reservations with expiry must expose the expiration boundary',
  'statement': 'Temporary reservations reduce availability only until their expiry; hiding that '
               'boundary makes release timing and capacity planning opaque.',
  'intent': 'Keep operators from assuming expiring stock is permanently committed.',
  'applies_when': ['Carts, holds, or pending orders create time-bounded inventory reservations.'],
  'does_not_apply_when': [],
  'failure_modes': ['Ten units appear reserved with no indication that seven holds expire in '
                    'ninety seconds.'],
  'user_impacts': ['Operators may trigger unnecessary replenishment or manually release stock that '
                   'would free itself.'],
  'observables': ['Create holds with different expiries and inspect aggregate reservation, '
                  'drilldown, and availability over time.'],
  'falsifiers': ['Expiring reservations expose their deadlines and aggregate availability updates '
                 'when each authoritative expiry occurs.'],
  'repairs': ['Store reservation expiry explicitly and include it in source-level inventory '
              'drilldowns.'],
  'exceptions': [],
  'verification': ['Advance across multiple expiries and verify reserved/available totals and '
                   'reservation records transition exactly once.'],
  'owner_hints': ['designing-marketplace-inventory-availability'],
  'verifier_hints': ['critiquing-functional-completeness'],
  'capabilities': interaction_caps(),
  'provenance_ids': ['nui-inventory-owners-v13'],
  'status': 'active'}]

__all__ = ["MARKETPLACE_INVENTORY_RULES_V13"]
