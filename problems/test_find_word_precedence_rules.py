from .find_word_precedence_rules import find_word


def test_solution():
	assert find_word(["U>N", "G>A", "R>Y", "H>U", "N>G", "A>R"]) == 'HUNGARY'


def test_solution2():
	assert find_word(["I>F", "W>I", "S>W", "F>T"]) == 'SWIFT'


def test_solution3():
	assert find_word(["R>T", "A>L", "P>O", "O>R", "G>A", "T>U", "U>G"]) == 'PORTUGAL'


def test_solution4():
	assert find_word(["W>I", "R>L", "T>Z", "Z>E", "S>W", "E>R", "L>A", "A>N", "N>D", "I>T"]) == 'SWITZERLAND'
