import pytest

from ic_10_bst_2nd_largest import find_second_largest_item_bst
from problem_solve_util import BinaryTreeNode


def test_find_second_largest_item_bst_not_enough_items():
	root_node = BinaryTreeNode(10, None)

	with pytest.raises(ValueError) as e:
		find_second_largest_item_bst(root_node)


def test_find_second_largest_item_bst_traverse_right_no_left():
	root_node = BinaryTreeNode(10, None)
	new_node = root_node.insert_right(11)
	new_node = new_node.insert_right(12)

	node_found = find_second_largest_item_bst(root_node)
	assert 11 == node_found.value


def test_find_second_largest_item_bst_traverse_right_left_subtree():
	root_node = BinaryTreeNode(10, None)
	new_node = root_node.insert_right(11)
	new_node = new_node.insert_right(12)
	new_node = new_node.insert_right(20)
	new_node = new_node.insert_left(15)
	new_node.insert_left(14)
	new_node = new_node.insert_right(16)
	new_node = new_node.insert_right(17)
	new_node = new_node.insert_right(18)
	new_node = new_node.insert_right(19)

	node_found = find_second_largest_item_bst(root_node)
	assert 19 == node_found.value
