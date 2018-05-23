#
# Problem: Avoid the spikes.
#
# 1) You’re given a flat runway with a bunch of spikes in it. The runway is represented by a boolean array which
# indicates if a particular (discrete) spot is clear of spikes. It is True for clear and False for not clear.
#
# 2) You’re given a starting speed S. S is a non-negative integer at any given point and it indicates how much you
# will move forward with the next jump.
#
# 3) Every time you land on a spot, you can adjust your speed by up to 1 unit before the next jump.
#
# 4) You want to safely stop anywhere along the runway (does not need to be at the end of the array). You stop when
# your speed becomes 0. However, if you land on a spike at any point, your crazy bouncing ball bursts and it’s a
# game over.
#
# The output of your function should be a boolean indicating whether we can safely stop anywhere along the runway.
#
# Attribution: http://blog.refdash.com/dynamic-programming-tutorial-example/
#
# Dynamic Programming Steps
#
# 1. How to recognize a DP problem
# 2. Identify problem variables
# 3. Clearly express the recurrence relation
# 4. Identify the base cases
# 5. Decide if you want to implement it iteratively or recursively
# 6. Add memoization
# 7. Determine time complexity
#

from functools import lru_cache


def can_stop_first_pass(runway, speed, pos=0):
	if not (0 <= pos < len(runway)) or not runway[pos]:
		return False

	if speed == 0 and (0 <= pos < len(runway)) and runway[pos]:
		return True

	return any((can_stop_first_pass(runway, speed - 1, pos + speed - 1),
				can_stop_first_pass(runway, speed, pos + speed),
				can_stop_first_pass(runway, speed + 1, pos + speed + 1)))


@lru_cache(32)
def can_stop_recursive_cache(runway, speed, pos=0):
	"""
	Solution: xxx
	Complexity:
		Time: O(?)
		Space: O(?)
	"""
	# If I'm on the runway, and I'm not on a spike, and (my speed is zero or I can can stop on a subsequent move)
	return 0 <= pos < len(runway) and runway[pos] and (
			speed == 0 or any(can_stop_recursive_cache(runway, s, s + pos) for s in (speed - 1, speed, speed + 1)))
