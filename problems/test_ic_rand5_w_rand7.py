from .ic_rand5_w_rand7 import rand5


def test_rand5():
	li = range(1, 6)
	vals = set()
	for i in range(100):
		r = rand5()
		assert r in li
		vals.add(r)
	assert len(vals) == 5
