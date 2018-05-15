#
# Problem: Given a head node of a singly-linked list, find the nth to last node.
#

from .problem_solve_util import LinkedListNode


def nth_to_last_node(n_back: int, head_node: LinkedListNode) -> LinkedListNode:
	"""
	Solution: Iterate the linked list, keeping track of which node is n back from the current
	Complexity:
		Time: O(n)
		Space: O(1)
	:param n_back: the number of nodes back from the tail (1 being the tail)
	:param head_node: the head of the linked list
	:return: the nth to last node of the linked list
	"""
	node_n_back = head_node
	node_current = head_node
	node_num = 0
	while node_current:
		node_num += 1
		if node_num > n_back:
			node_n_back = node_n_back.next

		node_current = node_current.next

	return node_n_back if node_num >= n_back else None
