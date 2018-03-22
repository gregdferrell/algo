#
# Problem: Given an array of integers, representing movie run times and a
# integer representing a flight time, pick 2 movies whose total runtimes equal
# the exact movie length.
#
# For example:
# movie_lengths: [90, 60, 110, 150, 75, 105]
# flight_length: 180 minutes
# return = True (75 + 105)
#
from problem_solve_util import binary_search


def flight_time_movies_1_brute_force(movie_lengths, flight_length):
	"""
	Solution: Brute force iterative solution compares each movie length with
	all subsequent movie lengths.
	Complexity:
		Time: O(n^2)
		Space: O(1)
	"""
	if len(movie_lengths) < 2:
		raise ValueError('movie length list must be at least 2 items long')

	# For each movie length
	for index, movie_length_first in enumerate(movie_lengths):
		movie_lengths_sub = movie_lengths[0:index] + movie_lengths[
													 index + 1:len(
														 movie_lengths)]
		# Check all other movie lengths (skipping over the first movie length)
		for movie_length_second in movie_lengths_sub:
			if movie_length_first + movie_length_second == flight_length:
				return True
	return False


def flight_time_movies_2_binary_search(movie_lengths, flight_length):
	"""
	Solution: Sort the list of movies, then iterate it, conducting a binary
	search on each item for different item, when added together, equals the
	flight length.
	Complexity:
		Time: O(n * lg{n})
		Space: O(1)
	"""
	if len(movie_lengths) < 2:
		raise ValueError('movie length list must be at least 2 items long')

	# Sort the movies first: Time: O(n * lg{n})
	movie_lengths.sort()

	# For each movie length
	for index, movie_length_first in enumerate(movie_lengths):
		# Conduct a binary search on movie_lengths: O(lg{n}) time
		target_length = flight_length - movie_length_first
		movie_lengths_sub = movie_lengths[0:index] + movie_lengths[
													 index + 1:len(
														 movie_lengths)]
		if binary_search(target=target_length, nums=movie_lengths_sub):
			return True

	return False


def flight_time_movies_3_utilize_set(movie_lengths, flight_length):
	"""
	Solution: As we iterate through our movie lengths, store the matching
	movie length needed in a set for a constant time lookup on all subsequent
	iterations.
	Complexity:
		Time: O(n)
		Space: O(n)
	"""
	if len(movie_lengths) < 2:
		raise ValueError('movie length list must be at least 2 items long')

	movie_lengths_needed = set()

	# For each movie length
	for movie_length_first in movie_lengths:
		if movie_length_first in movie_lengths_needed:
			return True
		movie_lengths_needed.add(flight_length - movie_length_first)
	return False
