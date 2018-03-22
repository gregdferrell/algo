#
# Problem: Given a list of IDs, which contains many duplicate integers and one
# unique integer, find the unique integer.
#

from typing import List


def sbd_1_brute_force_double_iterative(ids: List):
	"""
	Solution: Brute force double iteration solution.
	Complexity:
		Time: O(n^2)
		Space: O(1)
	"""
	for index, item_first in enumerate(ids):
		for item_second in ids[:index] + ids[index + 1:]:
			if item_first == item_second:
				break
		else:
			return item_first


def sbd_2_memoize_set(ids: List):
	"""
	Solution: Iterate once through loop and save/remove values in another
	data structure -a set.
	Complexity:
		Time: O(n)
		Space: O(n/2) but usually less; yet technically O(n)
	"""
	values_saved = set()
	for item in ids:
		if item not in values_saved:
			values_saved.add(item)
		else:
			values_saved.remove(item)

	return values_saved.pop()


def sbd_3_bitwise(ids: List):
	"""
	Solution: Use bitwise XOR on a single variable for each element.
	Complexity:
		Time: O(n)
		Space: O(1)
	"""
	unique_id = 0
	for item in ids:
		unique_id ^= item

	return unique_id
