from compare_text_read import get_ordered_matches_map


def test_get_ordered_matches_one_wrong():
    original = ["a", "b", "c", "d", "e"]
    altered = ["a", "b", "z", "d", "e"]

    result = get_ordered_matches_map(original, altered)

    assert len(result) == 4
    assert result[0] == 0
    assert result[1] == 1
    assert 2 not in result
    assert result[3] == 3
    assert result[4] == 4


def test_get_ordered_matches_one_missing():
    original = ["a", "b", "c", "d", "e"]
    altered = ["a", "b", "d", "e"]

    result = get_ordered_matches_map(original, altered)

    assert len(result) == 4
    assert result[0] == 0
    assert result[1] == 1
    assert 2 not in result
    assert result[3] == 2
    assert result[4] == 3


def test_get_ordered_matches_first_missing():
    original = ["a", "b", "c"]
    altered = ["b", "c"]

    result = get_ordered_matches_map(original, altered)

    assert len(result) == 2
    assert 0 not in result
    assert result[1] == 0
    assert result[2] == 1


def test_get_ordered_matches_come_back_around():
    original = ["a", "b", "c", "d", "e", "f", "a"]
    altered = ["b", "c", "d", "e", "f", "a"]

    result = get_ordered_matches_map(original, altered)

    assert len(result) == 6
    assert 0 not in result
    assert result[1] == 0
    assert result[2] == 1
    assert result[3] == 2
    assert result[4] == 3
    assert result[5] == 4
    assert result[6] == 5


def test_get_ordered_matches_skip_around():
    original = ["a", "b", "c", "d", "e", "f", "g", "h"]
    altered = ["b", "c", "a", "e", "f", "g", "h", "i"]

    result = get_ordered_matches_map(original, altered)

    assert len(result) == 6
    assert 0 not in result
    assert result[1] == 0
    assert result[2] == 1
    assert 3 not in result
    assert result[4] == 3
    assert result[5] == 4
    assert result[6] == 5
    assert result[7] == 6


def test_get_ordered_matches_trails_off():
    original = ["a", "b", "c", "d"]
    altered = ["a", "e", "f", "g"]

    result = get_ordered_matches_map(original, altered)

    assert len(result) == 1
    assert result[0] == 0
    assert 1 not in result
    assert 2 not in result
    assert 3 not in result


def test_get_ordered_matches_last():
    original = ["a", "b", "c", "d"]
    altered = ["e", "f", "g", "h", "i", "j", "k", "l", "m", "d"]

    result = get_ordered_matches_map(original, altered)

    assert len(result) == 1
    assert 0 not in result
    assert 1 not in result
    assert 2 not in result
    assert result[3] == 9


def test_get_ordered_matches_lowest_higher_index():
    original = ["the", "cat", "ran", "far"]
    altered = ["w1", "w2", "w3", "w4", "far", "cat", "ran"]

    result = get_ordered_matches_map(original, altered)

    assert len(result) == 1
    assert 0 not in result
    assert 1 not in result
    assert 2 not in result
    assert result[3] == 4

