import pytest

from ic_15_fib import Fib
from timeit import default_timer


def assert_values(f):
    with pytest.raises(ValueError) as e:
        f(-1)
    assert f(0) == 0
    assert f(1) == 1
    assert f(2) == 1
    assert f(3) == 2
    assert f(4) == 3
    assert f(5) == 5
    assert f(6) == 8
    assert f(7) == 13
    assert f(8) == 21
    assert f(9) == 34
    assert f(10) == 55


def test_fib_recursive():
    f = Fib()
    assert_values(f.fib_1_recursive)


def test_fib_recursive_memoize():
    f = Fib()
    assert_values(f.fib_2_recursive_memoize)


def test_fib_iterative():
    f = Fib()
    assert_values(f.fib_3_iterative)


def test_fib_binets_formula():
    f = Fib()
    assert_values(f.fib_4_binets_formula)


def test_speed_of_algorithms():
    f = Fib()

    start = default_timer()
    f.fib_1_recursive(25)
    end = default_timer()
    length_recursive = end - start

    start = default_timer()
    f.fib_2_recursive_memoize(25)
    end = default_timer()
    length_recursive_memoize = end - start

    start = default_timer()
    f.fib_3_iterative(25)
    end = default_timer()
    length_iterative_short = end - start

    start = default_timer()
    f.fib_3_iterative(500)
    end = default_timer()
    length_iterative = end - start

    start = default_timer()
    f.fib_4_binets_formula(500)
    end = default_timer()
    length_binets = end - start

    assert length_recursive > length_recursive_memoize
    assert length_recursive_memoize > length_iterative_short
    assert length_iterative > length_binets
