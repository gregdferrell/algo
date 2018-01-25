from ic_21_find_unique_int_in_list import sbd_1_brute_force_double_iterative, \
    sbd_2_memoize_set, sbd_3_bitwise


def assert_values(f):
    assert f([1, 2, 3, 2, 1]) == 3
    assert f([1, 2, 3, 3, 2]) == 1
    assert f([1, 2, 3, 3, 2, 1, 4]) == 4
    assert f([1, 2, 3, 4, 5, 6, 7, 8, 1, 3, 4, 5, 6, 7, 8]) == 2


def test_sbd_brute_force_double_iterative():
    assert_values(sbd_1_brute_force_double_iterative)


def test_sbd_memoize_set():
    assert_values(sbd_2_memoize_set)


def test_sbd_3_bitwise():
    assert_values(sbd_3_bitwise)
