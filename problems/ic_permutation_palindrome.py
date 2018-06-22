#
# Problem: Write a function that checks whether any permutation of an input string is a palindrome.
#


def has_palindrome_permutation(s: str) -> bool:
	"""
	Solution: Single iteration through the string, adding and removing chars from a set. We know it's a palindrome if
	we have 0 or 1 characters left in the set. If there are 0 left, we had an even number of each char. If there is one
	left, we could effectively place it in the middle of the string and it would still be a palindrome.
	Complexity:
		Time: O(n)
		Space: O(n) (or O(k) where k = the total number of possible characters which would be less than n
	"""
	chars_found = set()
	for ch in s:
		if ch in chars_found:
			chars_found.remove(ch)
		else:
			chars_found.add(ch)
	return len(chars_found) < 2
