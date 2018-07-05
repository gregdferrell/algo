from .ic_recursive_perm import recursive_perm


def test_recursive_perm_1_char():
	s = "a"
	perms = recursive_perm(s)
	assert len(perms) == 1
	assert "a" in perms


def test_recursive_perm_2_chars():
	s = "ab"
	perms = recursive_perm(s)
	assert len(perms) == 2
	assert "ab" in perms
	assert "ba" in perms


def test_recursive_perm_3_chars():
	s = "abc"
	perms = recursive_perm(s)
	assert len(perms) == 6
	assert "abc" in perms
	assert "acb" in perms
	assert "bac" in perms
	assert "bca" in perms
	assert "cab" in perms
	assert "cba" in perms
