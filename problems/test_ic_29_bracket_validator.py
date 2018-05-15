from .ic_29_bracket_validator import bracket_validator


def test_bracket_validator_paren():
	text = "alert('hi');"
	assert bracket_validator(text)


def test_bracket_validator_curly():
	text = "alert{'hi'};"
	assert bracket_validator(text)


def test_bracket_validator_box():
	text = "alert['hi'];"
	assert bracket_validator(text)


def test_bracket_validator_paren_no_open():
	text = "alert'hi');"
	assert not bracket_validator(text)


def test_bracket_validator_curly_no_open():
	text = "alert'hi'};"
	assert not bracket_validator(text)


def test_bracket_validator_box_no_open():
	text = "alert'hi'];"
	assert not bracket_validator(text)


def test_bracket_validator_paren_no_close():
	text = "alert('hi';"
	assert not bracket_validator(text)


def test_bracket_validator_curly_no_close():
	text = "alert{'hi';"
	assert not bracket_validator(text)


def test_bracket_validator_box_no_close():
	text = "alert['hi';"
	assert not bracket_validator(text)


def test_bracket_validator_paren_wrong_close():
	text = "alert('hi'];"
	assert not bracket_validator(text)

	text = "alert('hi'};"
	assert not bracket_validator(text)


def test_bracket_validator_curly_wrong_close():
	text = "alert{'hi'];"
	assert not bracket_validator(text)

	text = "alert{'hi');"
	assert not bracket_validator(text)


def test_bracket_validator_box_wrong_close():
	text = "alert['hi');"
	assert not bracket_validator(text)

	text = "alert['hi'};"
	assert not bracket_validator(text)


def test_bracket_validator_multiple():
	text = "alert('hi');(){}[]abc(abc)abc{abc}abc[abc]abc"
	assert bracket_validator(text)


def test_bracket_validator_nested():
	text = "([abcde(fg{h[]i[]j}klmnopqrst)uvwx]{y}z)"
	assert bracket_validator(text)


def test_bracket_validator_nested_bad_1():
	text = "([abcde(fg{h[]i[]j}klmnopqrst)uvwx]{y}z"
	assert not bracket_validator(text)


def test_bracket_validator_nested_bad_2():
	text = "([abcde(fg{h[]i]j}klmnopqrst)uvwx]{y}z)"
	assert not bracket_validator(text)


def test_bracket_validator_nested_bad_3():
	text = "([abcde(fg{h[]i[]j}klmnopqrstuvwx]{y}z)"
	assert not bracket_validator(text)


def test_bracket_validator_nested_bad_4():
	text = "(abcde(fg{h[]i[]j}klmnopqrst)uvwx]{y}z)"
	assert not bracket_validator(text)


def test_bracket_validator_nested_bad_5():
	text = "([abcde(fgh[]i[]j}klmnopqrst)uvwx]{y}z)"
	assert not bracket_validator(text)
