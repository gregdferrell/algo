#
# Problem: Write a function to check that a binary tree is a valid binary search tree.
#

from problems.problem_solve_util import BinaryTreeNode


def is_tree_valid_bst(root_node: BinaryTreeNode) -> bool:
	# nodes is a list of tuples containing a node, the max value for child nodes on the right, and the min
	# min value for child nodes on the left
	nodes = []
	nodes.append((root_node, None, None))  # node, max, min

	while len(nodes):
		nd, max, min = nodes.pop()
		if nd.left:
			# If left node is greater than current node, or if it is less than the min value allowed, return False
			if nd.left.value > nd.value:
				return False
			if min and nd.left.value < min:
				return False
			nodes.append((nd.left, nd.value, min))
		if nd.right:
			# If right node is less than current node, or if it is greater than the max value allowed, return False
			if nd.right.value < nd.value:
				return False
			if max and nd.right.value > max:
				return False
			nodes.append((nd.right, max, nd.value))
	return True
