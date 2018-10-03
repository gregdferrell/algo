#
# Problem: Write a function returns the total number of carry operations performed on two numbers when adding them.
#


def number_of_carry_operations(n1, n2):
	str1 = str(n1)
	str2 = str(n2)

	num_carry = 0
	prev_carry = 0

	if len(str2) > len(str1):
		str1, str2 = str2, str1

	for idx, s in enumerate(str1[::-1]):
		str2_val = 0
		if idx < len(str2):
			str2_val = int(str2[::-1][idx])

		val = int(s) + str2_val + prev_carry
		if val > 9:
			num_carry += 1
			prev_carry = 1
		else:
			prev_carry = 0

	return num_carry
