#
# Problem: Write a function that tells us if a full deck of cards is a single riffle of two other halves.
#
# Is the full deck of cards shuffled_deck is a single riffle of two other halves half1 and half2? The stack of
# cards as a list of integers in the range 1..52.
#

from typing import List


def single_riffle_shuffle_1(shuffled_deck: List, half_1: List, half_2: List):
    """
    Solution: Iterate the shuffled deck and pull cards off the top of each half, making sure the next card of one
    of the halves matches the top card of the shuffled deck.
    Complexity:
        Time: O(n)
        Space: O(1)
    """
    # The input lists must be populated with at least one value, and the lengths of both halves must
    # equal the length of the fully shuffled deck.
    if not (shuffled_deck, half_1, half_2) or len(shuffled_deck) != (len(half_1) + len(half_2)):
        return False

    half_1_start_index = 0
    half_2_start_index = 0
    for card in shuffled_deck:
        if half_1_start_index < len(half_1) and card == half_1[half_1_start_index]:
            half_1_start_index += 1
        elif half_2_start_index < len(half_2) and card == half_2[half_2_start_index]:
            half_2_start_index += 1
        else:
            return False
    if half_1_start_index == len(half_1) and half_2_start_index == len(half_2):
        return True

    return False
