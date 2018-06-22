from .ic_permutation_palindrome import has_palindrome_permutation


def test_has_palindrome_permutation():
	s = "civic"
	assert has_palindrome_permutation(s)
	s = "ivicc"
	assert has_palindrome_permutation(s)
	s = "civil"
	assert not has_palindrome_permutation(s)
	s = "livci"
	assert not has_palindrome_permutation(s)
	s = "aabbccaabbcc"
	assert has_palindrome_permutation(s)
	s = "aabbccdaabbcc"
	assert has_palindrome_permutation(s)
	s = "abcdefghijihgjedcba"
	assert has_palindrome_permutation(s)
