from ic_16_unbounded_knapsack import max_value_1_highest_weight_value_ratio, \
    max_value_2_compute_all_until_max_capacity


def test_max_1_1():
    t = [(3, 30), (1, 7), (2, 10)]
    c = 5
    assert max_value_1_highest_weight_value_ratio(t, c) == 44


def test_max_1_2():
    t = [(3, 40), (5, 70)]
    c = 8
    assert max_value_1_highest_weight_value_ratio(t, c) == 110


def test_max_1_3():
    t = [(3, 40), (5, 70)]
    c = 9
    assert max_value_1_highest_weight_value_ratio(t, c) == 110
    # Answer is really 120 -this algo not designed to solve this exact
    # type of input, but usually comes close


def test_max_2_1():
    t = [(3, 30), (1, 7), (2, 10)]
    c = 5
    assert max_value_2_compute_all_until_max_capacity(t, c) == 44


def test_max_2_2():
    t = [(3, 40), (5, 70)]
    c = 8
    assert max_value_2_compute_all_until_max_capacity(t, c) == 110


def test_max_2_3():
    t = [(3, 40), (5, 70)]
    c = 9
    assert max_value_2_compute_all_until_max_capacity(t, c) == 120


def test_max_2_4():
    t = [(1, 2), (2, 3), (3, 4), (4, 6)]
    c = 15
    assert max_value_2_compute_all_until_max_capacity(t, c) == 30


def test_max_2_5():
    t = [(1, 1), (2, 3), (3, 4), (4, 6)]
    c = 15
    assert max_value_2_compute_all_until_max_capacity(t, c) == 22
