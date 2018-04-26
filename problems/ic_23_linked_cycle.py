#
# Problem: Find if a Linked List has a cycle.
#

from problem_solve_util import LinkedListNode


def contains_cycle_set_impl(head_node: LinkedListNode):
	"""
	Solution: Store all visited nodes in a set and check to see if each node has been visited.
	Complexity:
		Time: O(n)
		Space: O(n)
	"""
	node = head_node
	node_set = set()
	while node:
		if node in node_set:
			return True
		else:
			node_set.add(node)
		node = node.next
	return False


def contains_cycle(head_node: LinkedListNode):
	"""
	Solution: Traverse the linked list twice, at the same time with one traversal "moving faster" than the other.
	If they ever end up as the same node (except at the start of traversal), then we know the faster one looped back
	and caught up to the first.
	Complexity:
		Time: O(n)
		Space: O(1)
	"""
	node_first = head_node
	node_second = head_node
	first_time = True
	while node_second and node_second.next:
		if not first_time and node_first == node_second:
			return True
		node_first = node_first.next
		node_second = node_second.next.next
		first_time = False

	return False
