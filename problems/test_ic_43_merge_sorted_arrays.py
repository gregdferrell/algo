import pytest

from .ic_43_merge_sorted_arrays import merge_sorted_arrays


def test_merge_sorted_arrays_empty_lists():
	l1 = []
	l2 = []
	with pytest.raises(ValueError) as e:
		merge_sorted_arrays(l1, l2)


def test_merge_sorted_arrays_empty_half_1():
	l1 = []
	l2 = [6, 7, 8, 9, 10]
	merged_list = merge_sorted_arrays(l1, l2)
	assert merged_list == [6, 7, 8, 9, 10]


def test_merge_sorted_arrays_empty_half_2():
	l1 = [1, 2, 3, 4, 5]
	l2 = []
	merged_list = merge_sorted_arrays(l1, l2)
	assert merged_list == [1, 2, 3, 4, 5]


def test_merge_sorted_arrays_two_halves():
	l1 = [1, 2, 3, 4, 5]
	l2 = [6, 7, 8, 9, 10]
	merged_list = merge_sorted_arrays(l1, l2)
	assert merged_list == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def test_merge_sorted_arrays_unequal_lengths():
	l1 = [1, 3, 5]
	l2 = [2, 4, 6, 8, 10]
	merged_list = merge_sorted_arrays(l1, l2)
	assert merged_list == [1, 2, 3, 4, 5, 6, 8, 10]


def test_merge_sorted_arrays_smallest_half():
	l1 = [3]
	l2 = [1, 2, 4, 5]
	merged_list = merge_sorted_arrays(l1, l2)
	assert merged_list == [1, 2, 3, 4, 5]


def test_merge_sorted_arrays_perfect_split():
	l1 = [1, 3, 5, 7, 9]
	l2 = [2, 4, 6, 8, 10]
	merged_list = merge_sorted_arrays(l1, l2)
	assert merged_list == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def test_merge_sorted_arrays_duplicates():
	l1 = [1, 3, 5, 7, 9, 11]
	l2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
	merged_list = merge_sorted_arrays(l1, l2)
	assert merged_list == [1, 1, 2, 3, 3, 4, 5, 5, 6, 7, 7, 8, 9, 9, 10, 11]
