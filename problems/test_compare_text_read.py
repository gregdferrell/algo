from compare_text_read import sequential_compare


def test_get_ordered_matches_one_wrong():
    original = ["a", "b", "c", "d", "e"]
    altered = ["a", "b", "z", "d", "e"]

    result = sequential_compare(original, altered)

    assert len(result) == 4


def test_get_ordered_matches_one_missing():
    original = ["a", "b", "c", "d", "e"]
    altered = ["a", "b", "d", "e"]

    result = sequential_compare(original, altered)

    assert len(result) == 4


def test_get_ordered_matches_first_missing():
    original = ["a", "b", "c"]
    altered = ["b", "c"]

    result = sequential_compare(original, altered)

    assert len(result) == 2


def test_get_ordered_matches_come_back_around():
    original = ["a", "b", "c", "d", "e", "f", "a"]
    altered = ["b", "c", "d", "e", "f", "a"]

    result = sequential_compare(original, altered)

    assert len(result) == 6


def test_get_ordered_matches_skip_around():
    original = ["a", "b", "c", "d", "e", "f", "g", "h"]
    altered = ["b", "c", "a", "e", "f", "g", "h", "i"]

    result = sequential_compare(original, altered)

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


def test_get_ordered_matches_trails_off():
    original = ["a", "b", "c", "d"]
    altered = ["a", "e", "f", "g"]

    result = sequential_compare(original, altered)

    assert len(result) == 1

    assert result[0].key == 0
    assert result[0].value == 0


def test_get_ordered_matches_last():
    original = ["a", "b", "c", "d"]
    altered = ["e", "f", "g", "h", "i", "j", "k", "l", "m", "d"]

    result = sequential_compare(original, altered)

    assert len(result) == 1

    assert result[0].key == 3
    assert result[0].value == 9


def test_get_ordered_matches_lowest_higher_index():
    original = ["the", "cat", "ran", "far"]
    altered = ["w1", "w2", "w3", "w4", "far", "cat", "ran"]

    result = sequential_compare(original, altered)

    assert len(result) == 2

    assert result[0].key == 1
    assert result[0].value == 5

    assert result[1].key == 2
    assert result[1].value == 6


def test_fork():
    original = [1, 2, 3, 4, 5]
    altered = [1, 2, 4, 5, 3]

    result = sequential_compare(original, altered)

    assert len(result) == 4

    assert result[0].key == 0
    assert result[0].value == 0

    assert result[1].key == 1
    assert result[1].value == 1

    assert result[2].key == 3
    assert result[2].value == 2

    assert result[3].key == 4
    assert result[3].value == 3
