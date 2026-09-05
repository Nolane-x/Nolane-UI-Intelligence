"""V13 seventh-wave independently authored rules for tree navigation."""
from __future__ import annotations

from ._capabilities import interaction_caps


TREE_NAVIGATION_RULES_V13 = [{'rule_id': 'ui.tree.expansion-state-distinct-from-selection',
  'domain': 'tree',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Tree expansion must remain distinct from item selection',
  'statement': 'Expanding or collapsing a tree node must not silently change the selected resource unless '
               'the product explicitly combines those actions and communicates the consequence.',
  'intent': 'Preserve the user’s current target while they inspect hierarchy around it.',
  'applies_when': ['A tree view supports independent hierarchy disclosure and item selection or activation.'],
  'does_not_apply_when': [],
  'failure_modes': ['Clicking an expander selects the node and replaces the detail pane, or selecting a node '
                    'unexpectedly toggles its children because hit targets share state.'],
  'user_impacts': ['Users can lose context, trigger unintended actions on a parent, or struggle to explore '
                   'hierarchy without changing their active resource.'],
  'observables': ['Use pointer and keyboard separately on disclosure and selection controls and inspect '
                  'selected identity after each expansion transition.'],
  'falsifiers': ['Expansion can change without altering selection, and selection changes only through the '
                 'documented activation interaction.'],
  'repairs': ['Separate disclosure and selection state and give their controls non-overlapping event '
              'ownership and accessible semantics.'],
  'exceptions': [],
  'verification': ['Exercise nested nodes with mouse, touch, and keyboard, verifying expansion and selected '
                   'resource remain independently controllable.'],
  'owner_hints': ['designing-tree-views'],
  'verifier_hints': ['critiquing-functional-completeness'],
  'capabilities': interaction_caps(),
  'provenance_ids': ['nui-tree-navigation-owners-v13'],
  'status': 'active'},
 {'rule_id': 'ui.tree.keyboard-hierarchy-navigation-complete',
  'domain': 'tree',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Tree keyboard navigation must cover parent, child, sibling, and activation movement without '
           'traps',
  'statement': 'A keyboard-operable hierarchy must provide a coherent path through visible nodes and allow '
               'users to enter and leave expanded branches without requiring pointer input.',
  'intent': 'Make tree navigation complete for keyboard and assistive-technology users rather than merely '
            'focusable.',
  'applies_when': ['A hierarchical tree or folder navigator exposes expandable nodes and interactive '
                   'leaves.'],
  'does_not_apply_when': [],
  'failure_modes': ['Focus can enter children but cannot return to the parent, skips visible siblings, or '
                    'requires Tab through every hidden or collapsed descendant.'],
  'user_impacts': ['Keyboard users can become trapped, miss nodes, or need excessive navigation compared '
                   'with the hierarchy’s visual structure.'],
  'observables': ['Navigate a deep mixed expanded/collapsed tree using only documented keyboard commands '
                  'while logging focused node identity.'],
  'falsifiers': ['Every visible hierarchy transition is reachable and reversible according to the tree '
                 'interaction model, with collapsed descendants excluded from active navigation.'],
  'repairs': ['Implement a roving or active-descendant focus model consistent with hierarchy semantics and '
              'update it on expansion changes.'],
  'exceptions': [],
  'verification': ['Test nested branches, disabled nodes, dynamic insertion, and collapse while focused, '
                   'verifying focus always lands on a valid logical node.'],
  'owner_hints': ['designing-roving-focus-composites'],
  'verifier_hints': ['critiquing-accessibility'],
  'capabilities': interaction_caps(),
  'provenance_ids': ['nui-tree-navigation-owners-v13'],
  'status': 'active'},
 {'rule_id': 'ui.tree.lazy-child-loading-state-visible',
  'domain': 'tree',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Lazy tree branches must expose child loading, failure, and true empty states distinctly',
  'statement': 'Expanding a node whose children are loaded asynchronously must distinguish loading from no '
               'children and provide recovery when the child request fails.',
  'intent': 'Prevent transient network state from being misread as an empty hierarchy.',
  'applies_when': ['Tree children are fetched only when a parent is expanded or scrolled into view.'],
  'does_not_apply_when': [],
  'failure_modes': ['The branch opens blank while loading or after failure, making the parent appear '
                    'leaf-like and offering no retry path.'],
  'user_impacts': ['Users can conclude content is missing or abandon navigation when the hierarchy is merely '
                   'delayed or unavailable.'],
  'observables': ['Throttle and fail child requests for nodes with and without real children, then inspect '
                  'disclosure, status, and retry behavior.'],
  'falsifiers': ['Loading, loaded-empty, loaded-with-children, and failed states are distinguishable and '
                 'expansion semantics match the final child result.'],
  'repairs': ['Model branch loading as explicit state and keep the disclosure affordance stable until '
              'authoritative child availability is known.'],
  'exceptions': [],
  'verification': ['Exercise repeated expand/collapse during load, network retry, and true empty nodes, '
                   'verifying no state is falsely represented as another.'],
  'owner_hints': ['designing-folder-tree-navigation'],
  'verifier_hints': ['critiquing-functional-completeness'],
  'capabilities': interaction_caps(),
  'provenance_ids': ['nui-tree-navigation-owners-v13'],
  'status': 'active'},
 {'rule_id': 'ui.tree.moved-node-preserves-focus-identity',
  'domain': 'tree',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Moving a tree node must preserve logical focus identity instead of leaving focus on its old '
           'position',
  'statement': 'When a focused or selected node is moved within the hierarchy, focus should follow that '
               'resource or transition predictably according to the product model, not attach to whatever '
               'row reuses the old index.',
  'intent': 'Avoid acting on the wrong resource after hierarchy reordering.',
  'applies_when': ['Users or collaborators can move nodes while the tree remains open and interactive.'],
  'does_not_apply_when': [],
  'failure_modes': ['A moved node disappears from its old slot and focus remains on the row index, which now '
                    'belongs to a different sibling.'],
  'user_impacts': ['A keyboard command issued immediately after the move can rename, delete, or open the '
                   'wrong item.'],
  'observables': ['Focus a node, move it from another client or command, then issue navigation and action '
                  'commands without first clicking.'],
  'falsifiers': ['Focus remains associated with the same stable resource where possible or moves to a '
                 'documented safe fallback, never an unrelated row by index coincidence.'],
  'repairs': ['Track active tree state by stable node identity and resolve that identity after structural '
              'updates before applying follow-up actions.'],
  'exceptions': [],
  'verification': ['Move selected and focused nodes across parents, including remote moves, and verify '
                   'subsequent actions target the intended identity.'],
  'owner_hints': ['designing-tree-views'],
  'verifier_hints': ['critiquing-functional-completeness'],
  'capabilities': interaction_caps(),
  'provenance_ids': ['nui-tree-navigation-owners-v13'],
  'status': 'active'},
 {'rule_id': 'ui.tree.invalid-parent-cycle-prevented',
  'domain': 'tree',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Hierarchy editing must prevent cycles or invalid parent relationships before commit',
  'statement': 'A move, drag, or reparent action must reject targets that would violate the hierarchy model, '
               'such as making a node its own descendant or crossing a forbidden root boundary.',
  'intent': 'Protect structural integrity while making invalid destinations understandable before users '
            'commit destructive reorganizations.',
  'applies_when': ['The tree supports moving or reparenting nodes and the data model imposes parent-child '
                   'constraints.'],
  'does_not_apply_when': [],
  'failure_modes': ['The UI allows a node to be dropped into its descendant or forbidden container and only '
                    'fails later, or worse persists an invalid cycle.'],
  'user_impacts': ['Users can lose navigability, trigger backend errors, or create structures other clients '
                   'cannot render safely.'],
  'observables': ['Attempt self-parenting, descendant moves, protected-root moves, and cross-scope '
                  'reparenting through every supported interaction path.'],
  'falsifiers': ['Invalid targets are disabled or rejected with a reason, and no authoritative tree cycle or '
                 'forbidden relationship is created.'],
  'repairs': ['Evaluate structural constraints against stable node identities before commit and use the same '
              'validator for drag, menu, and API-backed move paths.'],
  'exceptions': [],
  'verification': ['Fuzz reparenting around deep nested structures and concurrent moves, verifying both UI '
                   'and stored graph remain acyclic under the declared model.'],
  'owner_hints': ['designing-tree-views'],
  'verifier_hints': ['critiquing-functional-completeness'],
  'capabilities': interaction_caps(),
  'provenance_ids': ['nui-tree-navigation-owners-v13'],
  'status': 'active'},
 {'rule_id': 'ui.tree.breadcrumb-and-tree-path-consistent',
  'domain': 'tree',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Breadcrumb and tree selection must represent the same authoritative hierarchy path',
  'statement': 'When both breadcrumb and tree navigation describe location, they must derive from the same '
               'current resource lineage and reconcile after moves or deep links.',
  'intent': 'Prevent users from seeing contradictory parentage in two simultaneous navigation models.',
  'applies_when': ['A product shows a folder or resource tree together with breadcrumbs or path text.'],
  'does_not_apply_when': [],
  'failure_modes': ['The tree highlights one parent chain while the breadcrumb shows another because one '
                    'surface uses stale cached hierarchy or path aliases differently.'],
  'user_impacts': ['Users can navigate to the wrong parent, misunderstand where changes will be saved, or '
                   'duplicate resources in an unintended location.'],
  'observables': ['Move a selected node, deep-link into nested paths, and compare breadcrumb segments with '
                  'the expanded selected chain after refresh.'],
  'falsifiers': ['Both navigation surfaces resolve to the same stable resource lineage or explicitly '
                 'indicate alternate aliases rather than presenting two silent truths.'],
  'repairs': ['Centralize lineage resolution and update both tree and breadcrumb from the same current '
              'hierarchy version.'],
  'exceptions': [],
  'verification': ['Exercise rename, move, alias, and deleted-parent cases, verifying navigation surfaces '
                   'remain mutually consistent.'],
  'owner_hints': ['designing-folder-tree-navigation'],
  'verifier_hints': ['critiquing-functional-completeness'],
  'capabilities': interaction_caps(),
  'provenance_ids': ['nui-tree-navigation-owners-v13'],
  'status': 'active'},
 {'rule_id': 'ui.tree.virtualized-node-position-semantic',
  'domain': 'tree',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Virtualized trees must expose meaningful hierarchy position independent of rendered row count',
  'statement': 'When only part of a large tree is rendered, accessibility semantics and navigation must '
               'still reflect a node’s logical level, parent relationship, and position where the model can '
               'provide it.',
  'intent': 'Prevent virtualization from flattening or falsifying hierarchy for nonvisual navigation.',
  'applies_when': ['A large hierarchical tree virtualizes nodes and uses accessibility tree semantics for '
                   'keyboard or screen-reader users.'],
  'does_not_apply_when': [],
  'failure_modes': ['Rendered rows all appear as top-level siblings or report positions based only on the '
                    'current DOM window rather than the logical hierarchy.'],
  'user_impacts': ['Assistive-technology users cannot understand nesting or may hear misleading counts and '
                   'positions as the window recycles.'],
  'observables': ['Inspect the accessibility tree while navigating across virtualized boundaries and compare '
                  'reported level and relationships with the logical data structure.'],
  'falsifiers': ['Node semantics remain tied to logical hierarchy and recycled DOM nodes update all relevant '
                 'level, ownership, and position metadata.'],
  'repairs': ['Derive accessibility metadata from stable tree structure rather than DOM index, and update it '
              'atomically when virtualized rows are reused.'],
  'exceptions': [],
  'verification': ['Traverse beyond several virtualization windows with a screen reader or accessibility '
                   'snapshot, verifying hierarchy semantics remain accurate.'],
  'owner_hints': ['designing-tree-views'],
  'verifier_hints': ['critiquing-accessibility'],
  'capabilities': interaction_caps(),
  'provenance_ids': ['nui-tree-navigation-owners-v13'],
  'status': 'active'},
 {'rule_id': 'ui.tree.parent-child-selection-scope-explicit',
  'domain': 'tree',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Tree selection must make parent and descendant inclusion semantics explicit for bulk actions',
  'statement': 'Selecting a parent in a hierarchical multiselect must reveal whether descendants are '
               'included, partially selected, inherited, or independent before a bulk operation runs.',
  'intent': 'Avoid destructive bulk actions whose true scope is hidden behind a single parent checkbox '
            'state.',
  'applies_when': ['A tree supports selecting nodes for export, move, delete, permission, or other '
                   'multi-item operations.'],
  'does_not_apply_when': [],
  'failure_modes': ['A checked parent visually implies all descendants are selected while hidden or unloaded '
                    'descendants are excluded, or the reverse without indication.'],
  'user_impacts': ['Users can unintentionally act on far more or fewer resources than the visible selection '
                   'suggests.'],
  'observables': ['Select parents with collapsed and lazy-loaded descendants, then inspect selected count '
                  'and a consequential bulk-action preview.'],
  'falsifiers': ['Selection state distinguishes explicit, inherited, partial, and excluded descendants and '
                 'the bulk scope matches the previewed stable identities.'],
  'repairs': ['Represent selection as a hierarchy-aware set with explicit descendant policy and show partial '
              'or inherited states on parent nodes.'],
  'exceptions': [],
  'verification': ['Exercise collapsed, filtered, and dynamically loaded descendants, verifying preview and '
                   'committed bulk scope remain identical.'],
  'owner_hints': ['designing-tree-grids'],
  'verifier_hints': ['critiquing-functional-completeness'],
  'capabilities': interaction_caps(),
  'provenance_ids': ['nui-tree-navigation-owners-v13'],
  'status': 'active'}]

__all__ = ["TREE_NAVIGATION_RULES_V13"]
