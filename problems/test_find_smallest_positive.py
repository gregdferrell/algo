from .c_example_1 import find_smallest_positive, solution


def test_find_smallest_pos_1():
	items = [1, 2, 4, 3]
	assert find_smallest_positive(items) == 5
	items = [3]
	assert find_smallest_positive(items) == 1
	items = [1]
	assert find_smallest_positive(items) == 2
	items = [3, 2]
	assert find_smallest_positive(items) == 1
	items = [1, 3, 5, 7, 8, 2]
	assert find_smallest_positive(items) == 4


def test_1():
	A = [1, 2, 4, 3]
	B = [1, 3, 2, 3]
	assert solution(A, B) == 2


def test_2():
	A = [3, 2, 1, 6, 5]
	B = [4, 2, 1, 3, 3]
	assert solution(A, B) == 3


def test_3():
	A = [1, 2]
	B = [1, 2]
	assert solution(A, B) == 3
