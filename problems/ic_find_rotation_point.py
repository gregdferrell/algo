#
# Problem: Write a function that finds the index of a rotation point in a "mostly" ordered list.
#
from typing import List


def find_rotation_point(items: List) -> int:
	"""
	Solution:
	Complexity:
		Time: O(lg(n)) - Binary search-like algorithm
		Space: O(1) - Constant space, just tracking a few ints
	"""
	if not items:
		raise ValueError('items must contain at least one value')

	index_start = 0
	index_end = len(items) - 1

	# Covers scenarios where one item is in the list
	# or where the first item is the rotation point
	if items[index_start] <= items[index_end]:
		return 0

	while index_start != index_end:
		# If we've zeroed in on adjacent items, then we know the second is the rotation point
		if index_start + 1 == index_end:
			return index_end

		index_search = int((index_start + index_end) / 2)
		if items[index_search] < items[0]:
			index_end = index_search
		else:
			index_start = index_search

	return index_start
