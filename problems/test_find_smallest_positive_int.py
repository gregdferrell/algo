from .find_smallest_positive_int import find_smallest_positive


def test_smallest_positive():
	items = [1, 7, 3, 2, 5, 4]
	assert find_smallest_positive(items) == 6


def test_small_positive_negatives():
	items = [-1, -3]
	assert find_smallest_positive(items) == 1


def test_small_positive_sequence():
	items = [1, 2, 3]
	assert find_smallest_positive(items) == 4


def test_small_positive_mixed():
	items = [-1, -2, 4, 3, 2, 1]
	assert find_smallest_positive(items) == 5
