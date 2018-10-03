from .get_number_of_carry_ops import number_of_carry_operations


def test_solution():
	assert number_of_carry_operations(123, 456) == 0
	assert number_of_carry_operations(555, 555) == 3
	assert number_of_carry_operations(0, 0) == 0
	assert number_of_carry_operations(101, 809) == 1
	assert number_of_carry_operations(189, 209) == 1
	assert number_of_carry_operations(900, 11) == 0
	assert number_of_carry_operations(145, 55) == 2
	assert number_of_carry_operations(999045, 1055) == 5
	assert number_of_carry_operations(99999, 1) == 5
	assert number_of_carry_operations(1, 99999) == 5
