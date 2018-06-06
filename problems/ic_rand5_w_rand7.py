#
# Problem: Write a function that generates a random int from 1-5 using a function that generates a random int from 1-7.
#
import random

li7 = range(1, 8)


def rand7() -> int:
	return random.choice(li7)


def rand5() -> int:
	r = 6
	while r > 5:
		r = rand7()
	return r
