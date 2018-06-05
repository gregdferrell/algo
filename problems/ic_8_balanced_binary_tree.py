#
# Problem: Write a function to see if the difference between the depths of any two leaf nodes is no greater than one.
#

from problems.problem_solve_util import BinaryTreeNode


def is_balanced_depth_search(root_node: BinaryTreeNode) -> bool:
	min_depth = -1
	max_depth = -1

	nodes = []
	nodes.append((root_node, 0))

	while len(nodes):
		nd, depth = nodes.pop()

		if nd.left:
			nodes.append((nd.left, depth + 1))
		if nd.right:
			nodes.append((nd.right, depth + 1))
		if not nd.left and not nd.right:
			# On leaf
			if min_depth == -1 or depth < min_depth:
				min_depth = depth
			if max_depth == -1 or depth > max_depth:
				max_depth = depth

		if max_depth - min_depth > 1:
			return False

	return True
