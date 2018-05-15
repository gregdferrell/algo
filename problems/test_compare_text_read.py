from .compare_text_read import compare_text, get_all_possible_mappings


def test_get_all_possible_mappings_1():
	orig = [1, 2, 3, 5]
	alt = [0, 1, 2, 3, 4, 5, 4, 3, 2]
	result = get_all_possible_mappings(orig, alt)

	assert len(result) == 4
	assert len(result[0]) == 1
	assert 1 in result[0]
	assert len(result[1]) == 2
	assert 2 in result[1]
	assert 8 in result[1]
	assert len(result[2]) == 2
	assert 3 in result[2]
	assert 7 in result[2]
	assert len(result[3]) == 1
	assert 5 in result[3]


def test_get_all_possible_mappings_2():
	orig = [1, 2, 3]
	alt = [1, 2, 1, 2]
	result = get_all_possible_mappings(orig, alt)

	assert len(result) == 3
	assert len(result[0]) == 2
	assert 0 in result[0]
	assert 2 in result[0]
	assert len(result[1]) == 2
	assert 1 in result[1]
	assert 3 in result[1]
	assert len(result[2]) == 0


def test_compare_text_one_wrong():
	orig = ["a", "b", "c", "d", "e"]
	alt = ["a", "b", "z", "d", "e"]
	result = compare_text(orig, alt)

	assert len(result) == 4
	assert result[0].key == 0
	assert result[0].value == 0
	assert result[1].key == 1
	assert result[1].value == 1
	assert result[2].key == 3
	assert result[2].value == 3
	assert result[3].key == 4
	assert result[3].value == 4


def test_compare_text_one_missing():
	orig = ["a", "b", "c", "d", "e"]
	alt = ["a", "b", "d", "e"]
	result = compare_text(orig, alt)

	assert len(result) == 4
	assert result[0].key == 0
	assert result[0].value == 0
	assert result[1].key == 1
	assert result[1].value == 1
	assert result[2].key == 3
	assert result[2].value == 2
	assert result[3].key == 4
	assert result[3].value == 3


def test_compare_text_first_missing():
	orig = ["a", "b", "c"]
	alt = ["b", "c"]
	result = compare_text(orig, alt)

	assert len(result) == 2
	assert result[0].key == 1
	assert result[0].value == 0
	assert result[1].key == 2
	assert result[1].value == 1


def test_compare_text_come_back_around():
	orig = ["a", "b", "c", "d", "e", "f", "a"]
	alt = ["b", "c", "d", "e", "f", "a"]
	result = compare_text(orig, alt)

	assert len(result) == 6
	assert result[0].key == 1
	assert result[0].value == 0
	assert result[1].key == 2
	assert result[1].value == 1
	assert result[2].key == 3
	assert result[2].value == 2
	assert result[3].key == 4
	assert result[3].value == 3
	assert result[4].key == 5
	assert result[4].value == 4
	assert result[5].key == 6
	assert result[5].value == 5


def test_compare_text_skip_around():
	orig = ["a", "b", "c", "d", "e", "f", "g", "h"]
	alt = ["b", "c", "a", "e", "f", "g", "h", "i"]
	result = compare_text(orig, alt)

	assert len(result) == 6
	assert result[0].key == 1
	assert result[0].value == 0
	assert result[1].key == 2
	assert result[1].value == 1
	assert result[2].key == 4
	assert result[2].value == 3
	assert result[3].key == 5
	assert result[3].value == 4
	assert result[4].key == 6
	assert result[4].value == 5
	assert result[5].key == 7
	assert result[5].value == 6


def test_compare_text_trails_off():
	orig = ["a", "b", "c", "d"]
	alt = ["a", "e", "f", "g"]
	result = compare_text(orig, alt)

	assert len(result) == 1
	assert result[0].key == 0
	assert result[0].value == 0


def test_compare_text_last():
	orig = ["a", "b", "c", "d"]
	alt = ["e", "f", "g", "h", "i", "j", "k", "l", "m", "d"]
	result = compare_text(orig, alt)

	assert len(result) == 1
	assert result[0].key == 3
	assert result[0].value == 9


def test_compare_text_lowest_higher_index():
	orig = ["the", "cat", "ran", "far"]
	alt = ["w1", "w2", "w3", "w4", "far", "cat", "ran"]
	result = compare_text(orig, alt)

	assert len(result) == 2
	assert result[0].key == 1
	assert result[0].value == 5
	assert result[1].key == 2
	assert result[1].value == 6


def test_compare_text_fork():
	orig = [1, 2, 3, 4, 5]
	alt = [1, 2, 4, 5, 3]
	result = compare_text(orig, alt)

	assert len(result) == 4
	assert result[0].key == 0
	assert result[0].value == 0
	assert result[1].key == 1
	assert result[1].value == 1
	assert result[2].key == 3
	assert result[2].value == 2
	assert result[3].key == 4
	assert result[3].value == 3
