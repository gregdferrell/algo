#
# Problem: Find the nth fibonacci number.
#

from math import pow, sqrt


class Fib:
    def __init__(self, logging: bool = False):
        self.logging = logging

    def fib_1_recursive(self, n):
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

        return self.fib_1_recursive(n - 2) + self.fib_1_recursive(n - 1)

    def fib_2_recursive_memoize(self, n, cache={}):
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

        func_name = self.fib_2_recursive_memoize.__name__
        if n in cache:
            if self.logging:
                print('{}: getting {} from cache'.format(func_name, n))
            return cache[n]

        if self.logging:
            print('{}: computing fib for {}'.format(func_name, n))
        val = self.fib_2_recursive_memoize(n - 2,
                                           cache) + self.fib_2_recursive_memoize(
            n - 1, cache)
        cache[n] = val
        return val

    def fib_3_iterative(self, n):
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

    def fib_4_binets_formula(self, n):
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
