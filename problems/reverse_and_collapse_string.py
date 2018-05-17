#
# Write a method which takes a string as an argument and returns its reverse, collapsing any adjacent
# duplicate characters.
#
# For example:
# "abbac" becomes "caba"
# "abbbaa" becomes "aba"
#
# Don't use any built-in helper functions like String.reverse.
#


def reverse_and_collapse(in_str: str) -> str:
	"""
	Solution: Iterate backwards and copy chars to a new string if they don't equal the last char of that new string.
		Time: O(n) -> Iterate every char
		Space: O(n) -> Construct another string with max size = length of input string
	"""
	if not in_str:
		raise ValueError('input string must not be empty')

	out_str = ''

	# Get indexes in reverse
	for i in range(len(in_str)-1, -1, -1):
		# If out_str last char doesn't match this one, add it to the end of out_str
		if not out_str or out_str[-1] != in_str[i]:
			out_str += in_str[i]

	return out_str


if __name__ == '__main__':
	in_str = 'yylllletinifEEED eeem Llllaac'
	out_str = reverse_and_collapse(in_str)
	print(out_str)
	assert reverse_and_collapse(in_str) == 'calL me DEfinitely'
