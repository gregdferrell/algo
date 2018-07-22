#
# Problem: Write a function that finds a duplicate in a list -optimizing for space.
#
from typing import List


def find_dup(numbers: List) -> int:
	"""
	Solution: Iterate through the list and store items in a set. When an item is found that already exists in the set
	return that item.
	Complexity:
		Time: O(n) - Iterate through our list once
		Space: O(n) - We could potentially store each item found
	"""
	numbers_seen = set()
	for num in numbers:
		if num in numbers_seen:
			return num
		numbers_seen.add(num)
	raise Exception("No duplicate found")


def find_dup_brute_force(numbers: List) -> int:
	"""
	Solution: Brute force double iteration.
	Complexity:
		Time: O(n^2) - Iterate through our list twice
		Space: O(1) - Storing a single boolean
	"""
	for num1 in numbers:
		num_found = False
		for num2 in numbers:
			if num1 == num2:
				if num_found:
					return num1
				else:
					num_found = True
	raise Exception("No duplicates found")


def find_dup_in_place_sort(numbers: List) -> int:
	"""
	Solution: 1) Sort the list in place (keeping O(1) space, 2) iterate the list, and
	3) and look for 2 adjacent numbers that are the same.
	Complexity:
		Time: O(n * log(n)) - Sorting cost and single iteration
		Space: O(1) - Sorting in place
	"""
	numbers.sort()
	for i in range(len(numbers)):
		if i > 0 and numbers[i - 1] == numbers[i]:
			return numbers[i]
