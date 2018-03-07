#
# Problem: Merge two sorted arrays into one sorted array.
#

from typing import List


def merge_sorted_arrays(l1: List, l2: List):
    """
    Solution: Iterate
    Complexity:
        Time: O(n)
        Space: O(n)
    """
    if not l1 and not l2:
        raise ValueError('At least one list needs a value')

    merged_list = []

    l1_start_index = 0
    l2_start_index = 0
    while l1_start_index < len(l1) or l2_start_index < len(l2):
        if l1_start_index < len(l1) and l2_start_index < len(l2):
            if l1[l1_start_index] <= l2[l2_start_index]:
                merged_list.append(l1[l1_start_index])
                l1_start_index += 1
            else:
                merged_list.append(l2[l2_start_index])
                l2_start_index += 1
        elif l1_start_index < len(l1):
            merged_list.append(l1[l1_start_index])
            l1_start_index += 1
        elif l2_start_index < len(l2):
            merged_list.append(l2[l2_start_index])
            l2_start_index += 1

    return merged_list
