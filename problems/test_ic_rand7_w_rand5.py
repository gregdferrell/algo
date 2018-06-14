from .ic_rand7_w_rand5 import rand7

from collections import Counter


def test_rand7():
	li = range(1, 8)
	vals = set()
	for i in range(100):
		r = rand7()
		assert r in li
		vals.add(r)
	assert len(vals) == 7
