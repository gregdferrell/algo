from .ic_27_reverse_words import reverse_characters, reverse_words


def test_reverse_characters():
	message = ['c', 'a', 'k', 'e', ' ',
			   'p', 'o', 'u', 'n', 'd', ' ',
			   's', 't', 'e', 'a', 'l']

	reverse_characters(message, 0, len(message) - 1)
	print(''.join(message))
	assert ''.join(message) == 'laets dnuop ekac'


def test_reverse_words():
	message = ['c', 'a', 'k', 'e', ' ',
			   'p', 'o', 'u', 'n', 'd', ' ',
			   's', 't', 'e', 'a', 'l']

	reverse_words(message)
	print(''.join(message))
	assert ''.join(message) == 'steal pound cake'
