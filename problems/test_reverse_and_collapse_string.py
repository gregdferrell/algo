from reverse_and_collapse_string import reverse_and_collapse


def test_reverse_and_collapse_1():
	in_str = 'abbc'
	assert reverse_and_collapse(in_str) == 'cba'


def test_reverse_and_collapse_2():
	in_str = 'abbac'
	assert reverse_and_collapse(in_str) == 'caba'


def test_reverse_and_collapse_3():
	in_str = 'abbbaa'
	assert reverse_and_collapse(in_str) == 'aba'


def test_reverse_and_collapse_4():
	in_str = 'svsddvsvvssvvdsdssddvvvvds'
	assert reverse_and_collapse(in_str) == 'sdvdsdsdvsvsvdsvs'
