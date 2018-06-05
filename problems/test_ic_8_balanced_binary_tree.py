from .ic_8_balanced_binary_tree import is_balanced_depth_search
from .problem_solve_util import BinaryTreeNode


def test_is_balanced_depth_search_1():
	# Create the following tree, testing after each node insert
	#         10
	#      /      \
	#    5          20
	#      \      /    \
	#       6    15     25
	#                     \
	#                      30

	root_node = BinaryTreeNode(10, None)
	assert is_balanced_depth_search(root_node)
	new_node = root_node.insert_left(5)
	assert is_balanced_depth_search(root_node)
	new_node = new_node.insert_right(6)
	assert is_balanced_depth_search(root_node)
	new_node = root_node.insert_right(20)
	assert is_balanced_depth_search(root_node)
	new_node.insert_left(15)
	assert is_balanced_depth_search(root_node)
	new_node = new_node.insert_right(25)
	assert is_balanced_depth_search(root_node)
	new_node = new_node.insert_right(30)
	assert is_balanced_depth_search(root_node)
	new_node = new_node.insert_right(35)
	assert not is_balanced_depth_search(root_node)


def test_is_balanced_depth_search_right():
	# Create the following tree, testing after each node insert
	#         10
	#        /  \
	#       5    20
	#              \
	#               25
	#                 \
	#                  30

	root_node = BinaryTreeNode(10, None)
	assert is_balanced_depth_search(root_node)
	new_node = root_node.insert_right(20)
	assert is_balanced_depth_search(root_node)
	new_node = new_node.insert_right(25)
	assert is_balanced_depth_search(root_node)
	new_node = new_node.insert_right(30)
	assert is_balanced_depth_search(root_node)
	new_node = root_node.insert_left(5)
	assert not is_balanced_depth_search(root_node)


def test_is_balanced_depth_search_left():
	# Create the following tree, testing after each node insert
	#         10
	#        /  \
	#       5    20
	#      /
	#     4
	#    /
	#   3

	root_node = BinaryTreeNode(10, None)
	assert is_balanced_depth_search(root_node)
	new_node = root_node.insert_left(5)
	assert is_balanced_depth_search(root_node)
	new_node = new_node.insert_left(4)
	assert is_balanced_depth_search(root_node)
	new_node = new_node.insert_left(3)
	assert is_balanced_depth_search(root_node)
	new_node = root_node.insert_right(20)
	assert not is_balanced_depth_search(root_node)
