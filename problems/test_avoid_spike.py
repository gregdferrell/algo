from .avoid_spike import can_stop_recursive_cache, can_stop_first_pass


def test_can_stop_1():
	runway = (1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 1, 1, 1)
	speed = 3
	pos = 0
	assert can_stop_recursive_cache(runway, speed, pos)
	assert can_stop_first_pass(runway, speed, pos)
