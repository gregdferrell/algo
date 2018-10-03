from .rect import solution


def test_solution_with_overlap():
	rect1 = {
		# Coordinates of bottom-left corner
		'left_x': 1,
		'bottom_y': 1,

		# Width and height
		'width': 6,
		'height': 3,
	}

	rect2 = {
		# Coordinates of bottom-left corner
		'left_x': 5,
		'bottom_y': 2,

		# Width and height
		'width': 3,
		'height': 8,
	}

	expected = {
		# Coordinates of bottom-left corner
		'left_x': 5,
		'bottom_y': 2,

		# Width and height
		'width': 2,
		'height': 2,
	}

	actual = solution(rect1, rect2)

	assert actual == expected


def test_solution_no_overlap():
	rect1 = {
		# Coordinates of bottom-left corner
		'left_x': 0,
		'bottom_y': 0,

		# Width and height
		'width': 2,
		'height': 2,
	}

	rect2 = {
		# Coordinates of bottom-left corner
		'left_x': 3,
		'bottom_y': 3,

		# Width and height
		'width': 2,
		'height': 2,
	}

	actual = solution(rect1, rect2)

	assert not actual
