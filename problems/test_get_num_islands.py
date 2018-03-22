from get_num_islands import find_number_of_islands


def test_find_number_of_islands_zero():
	data = [[0, 0, 0],
			[0, 0, 0],
			[0, 0, 0]]

	assert find_number_of_islands(data) == 0


def test_find_number_of_islands_x():
	data = [[-1, 0, -1],
			[0, -1, 0],
			[-1, 0, -1]]

	assert find_number_of_islands(data) == 5


def test_find_number_of_islands_plus():
	data = [[0, -1, 0],
			[-1, -1, -1],
			[0, -1, 0]]

	assert find_number_of_islands(data) == 1


def test_find_number_of_islands_single():
	data = [[-1]]

	assert find_number_of_islands(data) == 1


def test_find_number_of_islands_random():
	data = [[-1, 0, 0, -1],
			[0, -1, -1, 0],
			[-1, 0, 0, 0],
			[0, 0, 0, -1]]
	assert find_number_of_islands(data) == 5


def test_find_number_of_islands_not_square():
	data = [[-1, -1, -1],
			[0, 0, 0, 0, 0, 0, -1],
			[-1, -1, -1, -1, -1, 0, -1],
			[0, 0, 0, 0],
			[0, 0, 0, -1],
			[-1],
			[-1, 0, -1, 0, -1],
			[-1, 0, -1, 0, -1],
			[-1, 0, 0, 0, -1],
			[-1, -1, -1, -1, -1, -1, -1]]

	assert find_number_of_islands(data) == 6


def test_find_number_of_islands_long_one():
	data = [[-1, -1, -1, -1, -1, -1, -1],
			[0, 0, 0, 0, 0, 0, -1],
			[-1, -1, -1, -1, -1, 0, -1],
			[-1, 0, 0, 0, -1, 0, -1],
			[-1, 0, -1, 0, -1, 0, -1],
			[-1, 0, -1, -1, -1, 0, -1],
			[-1, 0, 0, 0, 0, 0, -1],
			[-1, -1, -1, -1, -1, -1, -1]]

	assert find_number_of_islands(data) == 1
