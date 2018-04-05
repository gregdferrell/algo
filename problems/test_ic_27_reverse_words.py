from ic_27_reverse_words import reverse_words


def test_reverse_words():
	message = ['c', 'a', 'k', 'e', ' ',
			   'p', 'o', 'u', 'n', 'd', ' ',
			   's', 't', 'e', 'a', 'l']

	reverse_words(message)
	print(''.join(message))
	assert message == 'steal pound cake'
