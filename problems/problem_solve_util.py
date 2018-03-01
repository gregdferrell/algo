#
# Utility functions.
#
from math import floor


def binary_search(target, nums):
    """
    Checks to see if a given number appears in a sorted list of numbers.
    :param target: The number to look for
    :param nums: A sorted (ascending) list of numbers
    :return: Boolean indicating if the target was found
    """
    first_index = 0
    last_index = len(nums) - 1

    # If the target value isn't between the values at the beginning and end
    # of our list, return False immediately
    if not (nums[0] <= target <= nums[-1]):
        return False

    while True:
        # Calculate our target index -the middle point between the first
        # and last indexes that we're tracking
        target_index = (floor((last_index - first_index) / 2)) + first_index
        if target == nums[target_index]:
            return True
        elif first_index == last_index:
            return False
        elif target < nums[target_index]:
            last_index = target_index
        elif target > nums[target_index]:
            first_index = target_index + 1

    return False


class LinkedListNode:
    """
    Linked List Node
    """
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return self.value
