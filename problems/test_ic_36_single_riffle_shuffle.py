from .ic_36_single_riffle_shuffle import single_riffle_shuffle_1


def test_single_riffle_shuffle_1_empty_deck():
	shuffled_deck = []
	half_1 = [1, 2, 3, 4, 5]
	half_2 = [6, 7, 8, 9, 10]

	assert not single_riffle_shuffle_1(shuffled_deck, half_1, half_2)


def test_single_riffle_shuffle_1_empty_half_1():
	shuffled_deck = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
	half_1 = []
	half_2 = [6, 7, 8, 9, 10]

	assert not single_riffle_shuffle_1(shuffled_deck, half_1, half_2)


def test_single_riffle_shuffle_1_empty_half_2():
	shuffled_deck = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
	half_1 = [1, 2, 3, 4, 5]
	half_2 = []

	assert not single_riffle_shuffle_1(shuffled_deck, half_1, half_2)


def test_single_riffle_shuffle_1_unequal_lengths():
	shuffled_deck = [1, 2, 3, 4, 5, 6, 7, 8, 9]
	half_1 = [1, 2, 3, 4, 5]
	half_2 = [6, 7, 8, 9, 10]

	assert not single_riffle_shuffle_1(shuffled_deck, half_1, half_2)


def test_single_riffle_shuffle_1_cut_the_deck():
	shuffled_deck = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
	half_1 = [1, 2, 3, 4, 5]
	half_2 = [6, 7, 8, 9, 10]

	assert single_riffle_shuffle_1(shuffled_deck, half_1, half_2)


def test_single_riffle_shuffle_1_smallest_half():
	shuffled_deck = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
	half_1 = [1]
	half_2 = [2, 3, 4, 5, 6, 7, 8, 9, 10]

	assert single_riffle_shuffle_1(shuffled_deck, half_1, half_2)


def test_single_riffle_shuffle_1_beauty_shuffle():
	shuffled_deck = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
	half_1 = [1, 3, 5, 7, 9]
	half_2 = [2, 4, 6, 8, 10]

	assert single_riffle_shuffle_1(shuffled_deck, half_1, half_2)


def test_single_riffle_shuffle_1_good_shuffle():
	shuffled_deck = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
	half_1 = [1, 2, 5, 6, 9, 10]
	half_2 = [3, 4, 7, 8]

	assert single_riffle_shuffle_1(shuffled_deck, half_1, half_2)


def test_single_riffle_shuffle_1_barely_off_1():
	shuffled_deck = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
	half_1 = [1, 2, 5, 6, 10, 9]
	half_2 = [3, 4, 7, 8]

	assert not single_riffle_shuffle_1(shuffled_deck, half_1, half_2)


def test_single_riffle_shuffle_1_different_card():
	shuffled_deck = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
	half_1 = [1, 2, 4, 11, 7, 8, 10]
	half_2 = [3, 6, 9]

	assert not single_riffle_shuffle_1(shuffled_deck, half_1, half_2)
