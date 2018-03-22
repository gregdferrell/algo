#
# Problem: Write an efficient function that tells us whether or not an input string's openers and
# closers are properly nested.
#


def bracket_validator(text: str):
	"""
	Solution: Iterate and push/pop brackets on stack.
	Complexity:
		Time: O(n)
		Space: O(n)
	"""
	if not text:
		raise ValueError('Input string needs a value')

	stack = []

	for i, c in enumerate(text):
		if c in ('{', '[', '('):
			stack.append(c)
		elif c in ('}', ']', ')'):
			if not stack:
				return False
			c_popped = stack.pop()
			if not (c_popped == '{' and c == '}' or c_popped == '[' and c == ']' or c_popped == '(' and c == ')'):
				return False

	return not stack
