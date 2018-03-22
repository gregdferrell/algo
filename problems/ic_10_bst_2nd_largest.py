#
# Problem: Find the 2nd largest item in a binary search tree.
#

from problem_solve_util import BinaryTreeNode


def find_largest_item_bst(root_node: BinaryTreeNode):
	if not root_node:
		raise ValueError('root node cannot be null')

	node = root_node
	while node.right:
		node = node.right

	return node


def find_second_largest_item_bst(root_node: BinaryTreeNode):
	"""
	Solution:
	Complexity:
		Time: O(?)
		Space: O(?)
	"""
	if not root_node or (not root_node.left and not root_node.right):
		raise ValueError('at least two nodes must be present in the tree')

	largest_node = find_largest_item_bst(root_node)

	if largest_node.left:
		return find_largest_item_bst(largest_node.left)
	else:
		return largest_node.parent


def find_second_largest_item_not_using_parent(root_node: BinaryTreeNode):
	# TODO implement this without referencing the parent
	pass
