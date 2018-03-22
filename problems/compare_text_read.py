#
# Problem: Compare original text vs what was altered and return a dict of
# indexes match_index_mapping the matching elements from the original text
# array to the altered text array.
#
# Algorithm should maximize the number of matches in sequential order.
#
# TODO: consider using dicts/tree instead of arrays
#


class MatchIndexMapping:
	def __init__(self, key, value):
		self.key = key
		self.value = value

	def __str__(self):
		return f"({self.key}, {self.value})"


def print_all_results(all_results):
	print("\nAll Results:")
	for index, result in enumerate(all_results):
		print(str(index) + ":")
		for match_index_mapping in result:
			print(match_index_mapping)


def get_all_possible_mappings(orig, alt):
	"""
	Creates a list of lists that contains the mappings of the items in orig
	to all possible indexes from alt.
	:param orig: a list of items
	:param alt: a list of items
	:return: a list of lists, each element represents a list of indexes in the
	altered list that the original list item matches.
	"""
	all_mappings = []
	for index_orig, item_orig in enumerate(orig):
		indexes = []
		for index_alt, item_alt in enumerate(alt):
			if item_orig == item_alt:
				indexes.append(index_alt)
		all_mappings.append(indexes)
	return all_mappings


def compare_text(orig, alt, debug=False):
	"""
	Gets the maximum length sequential intersection of data from org to alt.
	This is represented in a list of indexes from orig to alt.
	:param orig: the original data
	:param alt: the altered data
	:param debug: boolean indicating whether to print out debug info
	:return: a list of MatchIndexMapping that contains a key (the index of
	the value in the orig data) and a value (the index of the data mapped to)
	in the alt data
	"""

	# Convert lists of data to list of lists mapping indexes from orig to
	# indexes in alt.
	all_mappings = get_all_possible_mappings(orig, alt)
	if debug:
		print("\nAll Mappings:\n" + str(all_mappings))

	results = []
	for i, index_list in enumerate(all_mappings):
		# If our index list is empty, then the data point in orig that
		# this index represents doesn't map to any data point in alt, so
		# proceed to next match_index_mapping array
		if not index_list:
			continue

		# If there are no results yet, create one from the first item in
		# this index list
		if not results:
			results.append([MatchIndexMapping(i, index_list[0])])
			continue

		# For each index list, append the lowest possible index from the list
		# to each result.
		#
		# This will result in either:
		# 1. Simply appending the index to the end of a result or
		# 2. Inserting the index into the middle of a result. In this case
		# we'll fork the result creating a copy and insert it into the copy
		# which also blows away the indexes after it. This needs to be done
		# because there is no guarantee that simply appending an index on the
		# end of a result will achieve our goal of getting the longest
		# possible sequential intersection.
		forked_results = []
		for result in results:
			next_result = False
			for index in index_list:
				for mim_index, match_index_mapping in reversed(
						list(enumerate(result))):
					if index > match_index_mapping.value:
						if len(result) - 1 == mim_index:
							# Append this to the end of the result and go to the
							# next result
							result.append(MatchIndexMapping(i, index))
							next_result = True
							break
						else:
							# Fork the result and insert this in the middle,
							# blowing away the other results. Proceed to the
							# next index to see if we need to fork again
							forked_list = result[:mim_index + 1]
							forked_list.append(MatchIndexMapping(i, index))
							forked_results.append(forked_list)
							break

				if next_result:
					break

		if forked_results:
			results.extend(forked_results)

		# If nothing in this index was added to an existing result, then
		# create a new result if no results exist whose initial value is less
		# than the smallest value in the index list
		for result in results:
			initial_value = result[0].value
			first_value_from_index_list = index_list[0]
			if initial_value <= first_value_from_index_list:
				break
		else:
			results.append([MatchIndexMapping(i, index_list[0])])

	if debug:
		print_all_results(results)

	# Return the result of the longest length
	return max(results, key=len)


if __name__ == "__main__":
	l1 = [1, 2, 3, 4, 5]
	l2 = [1, 2, 4, 5, 3]

	print("\nList 1: " + str(l1))
	print("\nList 2: " + str(l2))
	test_result = compare_text(l1, l2, True)
	print("\nFinal Result:")
	for mim in test_result:
		print(mim)
