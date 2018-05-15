#
# Problem: Given a head node of a singly-linked list, reverse it in place and
# return the new head node.
#
# Reverse a linked list (in-place)
# Your function will have one input: the head of the list.
# Your function should return the new head of the list.
#
from .problem_solve_util import LinkedListNode


def reverse_linked_list(head_node: LinkedListNode):
	"""
	Solution: Walk from head to tail, pointing the current to the previous.
	Complexity:
		Time: O(n)
		Space: O(1) -- constant number of a few variables in memory
	"""
	prev_node = None
	current_node = head_node
	next_node = None
	while current_node:
		next_node = current_node.next
		current_node.next = prev_node
		prev_node = current_node
		current_node = next_node
	return prev_node
