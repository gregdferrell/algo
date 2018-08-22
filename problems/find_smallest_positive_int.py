#
# Problem: Given an array of integers, find the smallest positive integer not in the array.
#
# Examples:
# [1, 7, 3, 2, 5, 4] = 6
# [-1, -3] = 1
# [1, 2, 3] = 4
# [-1, -2, 4, 3, 2, 1] = 5
#


def find_smallest_positive(items) -> int:
	"""
	Solution: Store if an integer is found in an array of bools and then go through that
	array and return the first integer not found.
	Complexity:
		Time: O(n) - Iterate through the input array and boolean array of same size
		Space: O(n) - Store a bool array equal to the size of the input
	"""
	# Create boolean array to hold if an integer is found
	# Maps index of array to the integer in items
	items_b = [False] * len(items)
	for item in items:
		if len(items_b) >= item > 0:
			items_b[item - 1] = True

	# Return the index(+1) of the first False value
	# This will return the positive integer 1
	for idx, item_b in enumerate(items_b):
		if not item_b:
			return idx + 1

	return len(items) + 1
