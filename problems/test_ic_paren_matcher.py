from .ic_paren_matcher import paren_matcher, paren_matcher_less_space


def test_paren_matcher():
	s = "Sometimes (when I nest them (my parentheticals) too much (like this (and this))) they get confusing."
	assert paren_matcher(s, 10) == 79
	assert paren_matcher(s, 28) == 46
	assert paren_matcher(s, 57) == 78
	assert paren_matcher(s, 68) == 77


def test_paren_matcher_less_space():
	s = "Sometimes (when I nest them (my parentheticals) too much (like this (and this))) they get confusing."
	assert paren_matcher_less_space(s, 10) == 79
	assert paren_matcher_less_space(s, 28) == 46
	assert paren_matcher_less_space(s, 57) == 78
	assert paren_matcher_less_space(s, 68) == 77
