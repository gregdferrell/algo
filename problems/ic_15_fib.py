#
# Problem: Find the nth fibonacci number.
#

from math import pow, sqrt


def fib_1_recursive(n):
    """
    Solution: Brute force recursive solution.
    Complexity:
        Description: Number of computations can be represented as a binary
        tree has height of n.
        Time: O(2^n)
    """
    if n < 0:
        raise ValueError('input must be a positive whole number')

    if n in [0, 1]:
        return n

    return fib_1_recursive(n - 2) + fib_1_recursive(n - 1)


def fib_2_recursive_memoize(n, cache={}):
    """
    Solution: Recursive solution that memorizes previously computed
    values by storing them in memory.
    Complexity:
        Time: O(n)
        Space: O(n)
    """
    if n < 0:
        raise ValueError('input must be a positive whole number')

    if n in [0, 1]:
        return n

    if n in cache:
        return cache[n]

    val = fib_2_recursive_memoize(n - 2, cache) + fib_2_recursive_memoize(n - 1,
                                                                          cache)
    cache[n] = val
    return val


def fib_3_iterative(n):
    """
    Solution: Iterative solution.
    Complexity:
        Time: O(n)
        Space: O(1)
    """
    if n < 0:
        raise ValueError('input must be a positive whole number')

    if n in [0, 1]:
        return n

    p1 = 0
    p2 = 1
    return_val = 0

    for _ in range(n - 1):
        return_val = p1 + p2
        p1 = p2
        p2 = return_val

    return return_val


def fib_4_binets_formula(n):
    """
    Solution (cheat): Use Binet's formula.
    Sometimes math just wins.
    Complexity:
        Time: O(1)
        Space: O(1)
    """
    if n < 0:
        raise ValueError('input must be a positive whole number')

    v1 = 1 / sqrt(5)
    v2 = pow((1 + sqrt(5)) / 2, n)
    v3 = pow((1 - sqrt(5)) / 2, n)
    return int(v1 * (v2 - v3))
