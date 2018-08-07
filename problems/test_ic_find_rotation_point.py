from .ic_find_rotation_point import find_rotation_point


def test_find_rotation_point_one_item():
	items = [
		'asymptote',  # <-- rotates here!
	]
	assert find_rotation_point(items) == 0


def test_find_rotation_point_first_item():
	items = [
		'asymptote',  # <-- rotates here!
		'babka',
		'banoffee',
		'engender',
		'karpatka',
		'othellolagkage',
	]
	assert find_rotation_point(items) == 0


def test_find_rotation_point_last_item():
	items = [
		'ptolemaic',
		'retrograde',
		'supplant',
		'undulate',
		'xenoepist',
		'asymptote',  # <-- rotates here!
	]
	assert find_rotation_point(items) == 5


def test_find_rotation_point_middle_item():
	items = [
		'ptolemaic',
		'retrograde',
		'supplant',
		'undulate',
		'xenoepist',
		'asymptote',  # <-- rotates here!
		'babka',
		'banoffee',
		'engender',
		'karpatka',
		'othellolagkage',
	]
	assert find_rotation_point(items) == 5


def test_find_rotation_point_middle_left_item():
	items = [
		'retrograde',
		'supplant',
		'undulate',
		'xenoepist',
		'asymptote',  # <-- rotates here!
		'babka',
		'banoffee',
		'engender',
		'karpatka',
		'othellolagkage',
		'ptolemaic',
	]
	assert find_rotation_point(items) == 4


def test_find_rotation_point_middle_right_item():
	items = [
		'othellolagkage',
		'ptolemaic',
		'retrograde',
		'supplant',
		'undulate',
		'xenoepist',
		'asymptote',  # <-- rotates here!
		'babka',
		'banoffee',
		'engender',
		'karpatka',
	]
	assert find_rotation_point(items) == 6


def test_find_rotation_point_left_half():
	items = [
		'ptolemaic',
		'asymptote',  # <-- rotates here!
		'babka',
		'banoffee',
		'engender',
		'karpatka',
		'othellolagkage',
	]
	assert find_rotation_point(items) == 1


def test_find_rotation_point_right_half():
	items = [
		'ptolemaic',
		'retrograde',
		'supplant',
		'undulate',
		'xenoepist',
		'asymptote',  # <-- rotates here!
		'othellolagkage',
	]
	assert find_rotation_point(items) == 5
