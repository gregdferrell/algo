#
# Problem: Write a function that finds the word represented by the given precedence rules.
#
# The word doesn't contain duplicate characters (each char is unique).
# Examples:
# findWord(["P>E","E>R","R>U"]) // PERU
# findWord(["I>N","A>I","P>A","S>P"]) // SPAIN


def find_word(items):
	result = []
	all_letters = set()

	g = {}
	for item in items:
		letter = item[0]
		next_letter = item[2]
		g[letter] = next_letter
		all_letters.add(letter)
		all_letters.add(next_letter)

	first_letter = ''
	for letter in all_letters:
		if letter not in g.values():
			first_letter = letter
			break

	result.append(first_letter)
	for i in range(len(items)):
		result.append(g[result[-1]])

	return ''.join(result)


print(find_word(["I>F", "W>I", "S>W", "F>T"]))  # 'SWIFT'
