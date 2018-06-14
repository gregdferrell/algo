#
# Problem: Write a function that generates a random int from 1-7 using a function that generates a random int from 1-5.
#
import random

li5 = range(1, 6)


def rand5() -> int:
	return random.choice(li5)


def rand7() -> int:
	while True:
		r1 = rand5()
		r2 = rand5()

		# Solution: Uses 7 of the 25 possible outcomes (re-rolls on 18 of 25)
		# if r1 == r2:
		# 	return r1
		# elif r1 == 1 and r2 == 4:
		# 	return 6
		# elif r1 == 1 and r2 == 5:
		# 	return 7

		# Solution: Uses 21 of the 25 possible outcomes (re-rolls on only 4 of 25)
		outcome = (r1 - 1) * 5 + r2
		if outcome < 22:
			return outcome % 7 + 1
