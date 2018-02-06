from problem_solve_util import binary_search


def test_binary_search_out_of_bounds_smaller():
    target = 0
    nums = [1, 2, 3]
    assert not binary_search(target, nums)


def test_binary_search_out_of_bounds_greater():
    target = 4
    nums = [1, 2, 3]
    assert not binary_search(target, nums)


def test_binary_search_one_num_true():
    target = 1
    nums = [1]
    assert binary_search(target, nums)


def test_binary_search_one_num_false():
    target = 2
    nums = [1]
    assert not binary_search(target, nums)


def test_binary_search_two_num_true():
    target = 3
    nums = [1, 3]
    assert binary_search(target, nums)


def test_binary_search_two_num_false():
    target = 2
    nums = [1, 3]
    assert not binary_search(target, nums)


def test_binary_search_three_num_true():
    target = 1
    nums = [1, 3, 5]
    assert binary_search(target, nums)


def test_binary_search_three_num_false():
    target = 4
    nums = [1, 3, 5]
    assert not binary_search(target, nums)


def test_binary_search_many_true():
    nums = [1, 3, 5, 7, 9, 11, 13]
    for num in nums:
        assert binary_search(num, nums)


def test_binary_search_many_false():
    nums = [1, 3, 5, 7, 9, 11, 13]
    for num in nums:
        assert not binary_search(num + 1, nums)
