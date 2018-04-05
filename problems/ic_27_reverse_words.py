#
# Problem: Create a function that takes a message as a list of characters and reverses the order of the words
# in-place.
#
# For example:
#   message = [ 'c', 'a', 'k', 'e', ' ',
#             'p', 'o', 'u', 'n', 'd', ' ',
#             's', 't', 'e', 'a', 'l' ]
#
#   reverse_words(message)
#
#   print ''.join(message) --- prints "steal pound cake"
#


def reverse_characters(chars, start_index, end_index):
	while start_index < end_index:
		chars[start_index], chars[end_index] = chars[end_index], chars[start_index]
		start_index += 1
		end_index -= 1


def reverse_words(chars):
	"""
	Solution: Reverse each character to get the words in the right order, then re-reverse each word.
	Complexity:
		Time: O(n) (twice)
		Space: O(1)
	"""
	reverse_characters(chars, 0, len(chars) - 1)
	start_index = 0
	for i, char in enumerate(chars):
		if char == ' ' or i == len(chars) - 1:
			# If we find a space, set end index to previous index, otherwise we're at the end of our list
			# and leave it at the last index
			end_index = i - 1 if char == ' ' else i
			reverse_characters(chars, start_index, end_index)
			start_index = i + 1
