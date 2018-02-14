#
# Problem: Write a function for doing an in-place shuffle of a list.
#
# The shuffle must be "uniform," meaning each item in the original list must have the same probability of ending up
# in each spot in the final list. Assume that you have a function get_random(floor, ceiling) for getting a random
# integer that is >= floor and <= ceiling.
#

import random
from typing import List


def get_random(floor, ceiling):
    """
    Helper function to get a random number.
    """
    return random.randrange(floor, ceiling + 1)


def shuffle_1(list_input: List):
    """
    Solution: Allocate new list; for every item in the input list, get a random index and set its value. Only set the
    value if the index has not been chosen before.
    *** Problems: 1) Does not solve requirement to shuffle a list in place since it creates a new list; very slow
        and theoretically could never finish
    Complexity:
        Time: O(n * x) where x = the time it takes to get the random index properly. This is slow and a bad solution.
        Space: O(n)
    """
    list_shuffled = [None] * len(list_input)
    for item in list_input:
        while True:
            index = get_random(0, len(list_input) - 1)
            if list_shuffled[index] is None:
                list_shuffled[index] = item
                break
    return list_shuffled


def shuffle_2(list_input: List):
    """
    Solution: Allocate new list; add a value to the new list starting at the beginning by getting a random value from
    the input list, then removing it from the input list so it's not chosen again.
    *** Problems: 1) Does not solve requirement to shuffle a list in place since it creates a new list;
        2) destroys the original list
    Complexity:
        Time: O(n^2) --- Iterate and delete for each iteration
        Space: O(n)
    """
    list_shuffled = [None] * len(list_input)
    for i in range(0, len(list_input)):
        index = get_random(0, len(list_input) - 1)
        list_shuffled[i] = list_input[index]
        del list_input[index]
    return list_shuffled


def shuffle_3(list_input: List):
    """
    Solution: For each index in the list, swap its value with a random other value from the list.
    Complexity:
        Time: O(n)
        Space: O(n)
    """
    for i in range(0, len(list_input)):
        index = get_random(i, len(list_input) - 1)
        if i != index:
            list_input[i], list_input[index] = list_input[index], list_input[i]
    return list_input
