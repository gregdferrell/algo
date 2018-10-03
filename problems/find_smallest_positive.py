#
# Problem: Create a new array from two int arrays where each value is the largest value at the same index of the two
# input arrays, then find the smallest positive integer not in that array.
#


def find_smallest_positive(items) -> int:
	"""
	Returns the smallest positive integer that does not exist in the given int array.
	:param items: array of ints
	:return: the smallest positive int not in the array
	"""
	# Create boolean array to hold if an integer is found
	# Maps index of array to the integer in items
	items_b = [False] * len(items)
	for item in items:
		if len(items_b) >= item > 0:
			items_b[item - 1] = True

	# Return the index(+1) of the first False value
	for idx, item_b in enumerate(items_b):
		if not item_b:
			return idx + 1

	# If all ints in items are sequential from 1, return the next positive integer
	return len(items) + 1


def solution(A, B):
	# Iterate both arrays at same time and copy larger value between the two to
	# array A, then we'll find the smallest positive integer not in that array.
	for idx, a in enumerate(A):
		b = B[idx]
		if b > a:
			A[idx] = b
	return find_smallest_positive(A)
