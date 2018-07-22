import pytest

from .ic_find_dup import find_dup, find_dup_brute_force, find_dup_in_place_sort


def test_find_dup():
	numbers = [1, 2, 3, 4, 5, 2, 7, 8]
	assert find_dup(numbers) == 2


def test_find_dup_none():
	numbers = [1, 2, 3, 4, 5, 6, 7, 8]
	with pytest.raises(Exception) as e:
		find_dup(numbers)


def test_find_dup_brute():
	numbers = [1, 2, 3, 4, 5, 2, 7, 8]
	assert find_dup_brute_force(numbers) == 2


def test_find_dup_brute_none():
	numbers = [1, 2, 3, 4, 5, 6, 7, 8]
	with pytest.raises(Exception) as e:
		find_dup_brute_force(numbers)


def test_find_dup_in_place_sort():
	numbers = [1, 2, 3, 4, 5, 2, 7, 8]
	assert find_dup_in_place_sort(numbers) == 2


def test_find_dup_in_place_sort_none():
	numbers = [1, 2, 3, 4, 5, 6, 7, 8]
	with pytest.raises(Exception) as e:
		find_dup_in_place_sort(numbers)
