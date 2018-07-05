#
# Problem: Write a recursive function to get all permutations of a string. Return them as a set.
#


def recursive_perm(s: str) -> set:
	# Base case
	if len(s) == 1:
		return set(s)

	# Recursive case
	perms = set()
	for i, char in enumerate(s):
		perms_inner = recursive_perm(s[0:i] + s[i + 1:])
		for perm in perms_inner:
			perms.add(char + perm)
	return perms
