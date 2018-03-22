#
# Problem: Unbounded knapsack. Write a function that takes 1) a list of tuples
# (weight, value) that represent items that have a weight and value
# and 2) a max weight capacity that represents the size of a knapsack. The
# function returns the maximum value of items the knapsack can hold.

# Assumptions:
# There are an unlimited number of each item type.
# No items will have a weight or value of 0.
#
# For example:
# Each tuple contains (weight, value):
# tuples = [(3, 30), (1, 7), (2, 10)]
# max_capacity = 5
# should return: 44 (one weighing 3, and two weighing 1)
#


def max_value_1_highest_weight_value_ratio(weight_value_tuples, max_capacity):
	"""
	Solution: Compute the max value by finding the item with the highest
	weight to value ratio and use it as many times as possible until we need
	to find a smaller one that fits into the knapsack but still has the
	greatest weight to value ratio.
	This algorithm won't always find the right solution (see tests), but is
	much faster than the optimal solution and uses O(1) space.
	Complexity:
		Time: O(n * lg{n}) (where n=number of items) (sorting the input first)
		Space: O(1)
	"""
	# Sort tuples by the highest weight to value ratio descending
	weight_value_tuples.sort(key=lambda tup: tup[1] / tup[0], reverse=True)

	# Repeatedly add the highest weight-to-value tuple that still fits into
	# the knapsack until nothing else will fit
	total_value = 0
	for weight, value in weight_value_tuples:
		while max_capacity >= weight:
			total_value += value
			max_capacity -= weight

	return total_value


def max_value_2_compute_all_until_max_capacity(weight_value_tuples,
											   max_capacity):
	"""
	Solution: Compute the max value for each capacity from 1 to max_capacity.
	This algorithm will always find the optimal max value, but is much
	slower than the less optimal solution and uses more space.
	Complexity:
		Time: O(n * k) (where n=number of items, k=max capacity)
		Space: O(k)
	"""
	# List to contain the max value for each capacity up to max_capacity
	# Ex: Index 1 will contain the max value of weight 1
	max_value_capacity = [0] * (max_capacity + 1)

	# For each weight from 1 to max_capacity, calculate the max value and
	# store it in our list
	for weight_to_compute_max_value_for in range(1, max_capacity + 1):
		for item_weight, item_value in weight_value_tuples:
			if item_weight <= weight_to_compute_max_value_for:
				diff = weight_to_compute_max_value_for - item_weight
				new_max_value = max_value_capacity[diff] + item_value
				max_value_capacity[weight_to_compute_max_value_for] = max(
					new_max_value,
					max_value_capacity[weight_to_compute_max_value_for])

	return max_value_capacity[max_capacity]
