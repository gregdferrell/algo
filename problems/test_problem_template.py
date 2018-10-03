import pytest

from .problem_template import solution


def test_solution_exception():
	items = []
	with pytest.raises(ValueError) as e:
		solution(items)


def test_solution():
	items = [1, 2, 3]
	assert solution(items) == 0
