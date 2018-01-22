from get_permutations import get_permutations_f1


def test_get_permutations_f1_sz1():
    perms = get_permutations_f1([1])
    assert len(perms) == 1


def test_get_permutations_f1_sz2():
    perms = get_permutations_f1([1, 2])
    assert len(perms) == 2
    assert [1, 2] in perms
    assert [2, 1] in perms


def test_get_permutations_f1_sz3():
    perms = get_permutations_f1([1, 2, 3])
    assert len(perms) == 6
    assert [1, 2, 3] in perms
    assert [1, 3, 2] in perms
    assert [2, 1, 3] in perms
    assert [2, 3, 1] in perms
    assert [3, 1, 2] in perms
    assert [3, 2, 1] in perms


def test_get_permutations_f1_str():
    perms = get_permutations_f1(['a', 'b'])
    assert len(perms) == 2
    assert ['a', 'b'] in perms
    assert ['b', 'a'] in perms
