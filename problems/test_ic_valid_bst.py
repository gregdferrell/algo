from .ic_valid_bst import is_tree_valid_bst
from .problem_solve_util import BinaryTreeNode


def test_is_valid_bst_1():
	#
	#         50
	#       /    \
	#     30      80
	#    /  \    /   \
	#   20  40  70   90
	#

	root_node = BinaryTreeNode(50, None)
	assert is_tree_valid_bst(root_node)
	new_node = root_node.insert_left(30)
	assert is_tree_valid_bst(root_node)
	new_node.insert_left(20)
	assert is_tree_valid_bst(root_node)
	new_node.insert_right(40)
	assert is_tree_valid_bst(root_node)
	new_node = root_node.insert_right(80)
	assert is_tree_valid_bst(root_node)
	new_node.insert_left(70)
	assert is_tree_valid_bst(root_node)
	new_node.insert_right(90)
	assert is_tree_valid_bst(root_node)


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
	assert is_tree_valid_bst(root_node)
	new_node = root_node.insert_right(20)
	assert is_tree_valid_bst(root_node)
	new_node = new_node.insert_right(25)
	assert is_tree_valid_bst(root_node)
	new_node = new_node.insert_right(30)
	assert is_tree_valid_bst(root_node)
	new_node = root_node.insert_left(5)
	assert is_tree_valid_bst(root_node)


def test_is_balanced_depth_search_left():
	# Create the following tree, testing after each node insert
	#         10
	#        /  \
	#       5    20
	#      /    /
	#     4    21
	#    /
	#   3

	root_node = BinaryTreeNode(10, None)
	assert is_tree_valid_bst(root_node)
	new_node = root_node.insert_left(5)
	assert is_tree_valid_bst(root_node)
	new_node = new_node.insert_left(4)
	assert is_tree_valid_bst(root_node)
	new_node = new_node.insert_left(3)
	assert is_tree_valid_bst(root_node)
	new_node = root_node.insert_right(20)
	assert is_tree_valid_bst(root_node)
	new_node = new_node.insert_left(21)
	assert not is_tree_valid_bst(root_node)


def test_is_balanced_depth_search_simple_left():
	#        50
	#       /
	#     30
	#       \
	#        60

	root_node = BinaryTreeNode(50, None)
	new_node = root_node.insert_left(30)
	new_node = new_node.insert_right(60)
	assert not is_tree_valid_bst(root_node)


def test_is_balanced_depth_search_simple_right():
	#        50
	#          \
	#           60
	#          /
	#        40

	root_node = BinaryTreeNode(50, None)
	new_node = root_node.insert_right(60)
	new_node = new_node.insert_left(40)
	assert not is_tree_valid_bst(root_node)


def test_is_valid_bst_gotcha():
	#
	#         50
	#       /    \
	#     30      80
	#    /  \    /   \
	#   20  60  70   90
	#

	root_node = BinaryTreeNode(50, None)
	assert is_tree_valid_bst(root_node)
	new_node = root_node.insert_left(30)
	assert is_tree_valid_bst(root_node)
	new_node.insert_left(20)
	assert is_tree_valid_bst(root_node)
	new_node.insert_right(60)
	assert not is_tree_valid_bst(root_node)
	new_node = root_node.insert_right(80)
	assert not is_tree_valid_bst(root_node)
	new_node.insert_left(70)
	assert not is_tree_valid_bst(root_node)
	new_node.insert_right(90)
	assert not is_tree_valid_bst(root_node)
