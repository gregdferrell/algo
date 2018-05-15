#
# Problem: Find the 2nd largest item in a binary search tree.
#

from .problem_solve_util import BinaryTreeNode


def find_largest_item_bst(root_node: BinaryTreeNode):
	if not root_node:
		raise ValueError('root node cannot be null')

	node = root_node
	while node.right:
		node = node.right

	return node


def find_second_largest_item_bst(root_node: BinaryTreeNode):
	"""
	Solution: Find the largest item, then we know the second largest is the largest in the left subtree
	if it exists, or its parent.
	Complexity:
		Time: O(h) where h=height of tree; O(lg n) if tree is balanced, O(n) otherwise
		Space: O(1)
	"""
	if not root_node or (not root_node.left and not root_node.right):
		raise ValueError('at least two nodes must be present in the tree')

	largest_node = find_largest_item_bst(root_node)

	if largest_node.left:
		return find_largest_item_bst(largest_node.left)
	else:
		return largest_node.parent


def find_second_largest_item_bst_no_parent(root_node: BinaryTreeNode):
	"""
	Solution: (Using a data structure whose nodes do not know their parent nodes) -- Traverse down the right
	of the tree as long as the right node has another sub-node. Otherwise return it or the largest subtree
	on the left.
	Complexity:
		Time: O(h) where h=height of tree; O(lg n) if tree is balanced, O(n) otherwise
		Space: O(1)
	"""
	if not root_node or (not root_node.left and not root_node.right):
		raise ValueError('at least two nodes must be present in the tree')

	node = root_node
	# While the node has a node on the right, and that node has a node on the left or right,
	# follow the tree to the right
	while node.right and (node.right.right or node.right.left):
		node = node.right

	if node.right:
		return node

	if node.left:
		return find_largest_item_bst(node.left)
