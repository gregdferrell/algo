#
# Problem: Get all permutations of a given list of items.
#


def get_permutations_f1(li):
    if len(li) == 1:
        permutations = li
    elif len(li) == 2:
        permutations = [li, li[::-1]]
    else:
        permutations = []
        for index, item in enumerate(li):
            sub_list = [x for i, x in enumerate(li) if i != index]
            sub_permutations = get_permutations_f1(sub_list)
            permutations.extend([[item] + sub_permutation for sub_permutation in
                                 sub_permutations])

    return permutations
