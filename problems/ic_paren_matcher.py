#
# Problem: Write a function that gives the index of a closing paren in a given string and index of the opening paren.
#


def paren_matcher(s: str, open_index: int) -> int:
	"""
	Solution: Iterate through the s from the open_paren index, keeping track of how many remaining open parens
	there are. When we get to 0, return the index.
	Complexity:
		Time: O(n) - Iterate through our string once
		Space: O(n) - We take a slice of the input s
	"""
	num_open = 1
	for idx, ch in enumerate(s[open_index + 1:]):
		if ch == '(':
			num_open += 1
		elif ch == ')':
			num_open -= 1
		if num_open == 0:
			return open_index + idx + 1
	return 0


def paren_matcher_less_space(s: str, open_index: int) -> int:
	"""
	Solution: Iterate through the s from the open_paren index, keeping track of how many remaining open parens
	there are. When we get to 0, return the index.
	Complexity:
		Time: O(n) - Iterate through our string once
		Space: O(1) - We take a slice of the input s
	"""
	num_open = 1
	for idx in range(open_index + 1, len(s)):
		ch = s[idx]
		if ch == '(':
			num_open += 1
		elif ch == ')':
			num_open -= 1
		if num_open == 0:
			return idx
	return 0
