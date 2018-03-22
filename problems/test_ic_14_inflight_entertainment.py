import pytest

from ic_14_inflight_entertainment import flight_time_movies_1_brute_force, \
	flight_time_movies_2_binary_search, flight_time_movies_3_utilize_set


def test_flight_time_movies_algorithms_not_enough_movies():
	movie_lengths = [90]
	flight_length = 180
	with pytest.raises(ValueError) as e:
		flight_time_movies_1_brute_force(movie_lengths, flight_length)
	with pytest.raises(ValueError) as e:
		flight_time_movies_2_binary_search(movie_lengths, flight_length)
	with pytest.raises(ValueError) as e:
		flight_time_movies_3_utilize_set(movie_lengths, flight_length)


def test_flight_time_movies_algorithms_none():
	movie_lengths = [80, 60, 110, 150, 75, 115]
	flight_length = 180
	assert not flight_time_movies_1_brute_force(movie_lengths, flight_length)
	assert not flight_time_movies_2_binary_search(movie_lengths, flight_length)
	assert not flight_time_movies_3_utilize_set(movie_lengths, flight_length)


def test_flight_time_movies_algorithms_found():
	movie_lengths = [80, 60, 110, 150, 75, 105]
	flight_length = 180
	assert flight_time_movies_1_brute_force(movie_lengths, flight_length)
	assert flight_time_movies_2_binary_search(movie_lengths, flight_length)
	assert flight_time_movies_3_utilize_set(movie_lengths, flight_length)


def test_flight_time_movies_algorithms_cant_use_same_movie_twice():
	movie_lengths = [90, 80, 70]
	flight_length = 180
	assert not flight_time_movies_1_brute_force(movie_lengths, flight_length)
	assert not flight_time_movies_2_binary_search(movie_lengths, flight_length)
	assert not flight_time_movies_3_utilize_set(movie_lengths, flight_length)
