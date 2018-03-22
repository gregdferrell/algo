from collections import Counter

from ic_35_in_place_shuffle import shuffle_1


def test_shuffle_1():
	li = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
	li_shuffled = shuffle_1(li)

	# Assert each list is same length
	assert (len(li) == len(li_shuffled))

	# Assert each list has same values; can use "Counter" because integers are hashable
	assert (Counter(li) == Counter(li_shuffled))

	# Cannot guarantee the list is changed because items could be shuffled back into the same spot,
	# but can verify that each item from the original exists in the shuffled
	for item in li:
		assert item in li_shuffled


def test_shuffle_2():
	li = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
	# Need to copy li and pass in copy because the original list is destroyed in this impl
	li_copy = li.copy()
	li_shuffled = shuffle_1(li_copy)

	# Assert each list is same length
	assert (len(li) == len(li_shuffled))

	# Assert each list has same values; can use "Counter" because integers are hashable
	assert (Counter(li) == Counter(li_shuffled))

	# Cannot guarantee the list is changed because items could be shuffled back into the same spot,
	# but can verify that each item from the original exists in the shuffled
	for item in li:
		assert item in li_shuffled


def test_shuffle_3():
	li = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
	# Need to copy li and pass in copy because the original list is altered, so need a copy of orig
	# for comparison
	li_copy = li.copy()
	shuffle_1(li_copy)

	# Assert each list is same length
	assert (len(li) == len(li_copy))

	# Assert each list has same values; can use "Counter" because integers are hashable
	assert (Counter(li) == Counter(li_copy))

	# Cannot guarantee the list is changed because items could be shuffled back into the same spot,
	# but can verify that each item from the original exists in the shuffled
	for item in li:
		assert item in li_copy
