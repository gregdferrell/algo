#
# Problem: Compare original text vs what was altered and return a dict of
# indexes match_index_mapping the matching elements from the original text
# array to the altered text array.
#
# Algorithm should maximize the number of matches in sequential order.
#
# TODO: creating more permutations than needed when forking; fix this
#       consider using tree data structure
#       clean up this awful code in other ways


def get_all_possible_mappings(orig, alt):
    """
    For each item in the original list, calculates a list of indexes in the
    altered list that match the item in the original list.
    :param orig: a list of items
    :param alt: a list of items
    :return: a list of lists, each element represents a list of indexes in the
    altered list that the original list item matches.
    """
    all_mappings = []
    for index_orig, item_orig in enumerate(orig):
        indexes = []
        for index_alt, item_alt in enumerate(alt):
            if item_orig == item_alt:
                indexes.append(index_alt)
        all_mappings.append(indexes)
    return all_mappings


def print_all_results(all_results):
    print("\nAll Results:")
    for index, result in enumerate(all_results):
        print(str(index) + ":")
        for match_index_mapping in result:
            print(match_index_mapping)


class MatchIndexMapping:
    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __str__(self):
        return f"({self.key}, {self.value})"


def sequential_compare(orig, alt, debug=False):
    all_mappings = get_all_possible_mappings(orig, alt)
    if debug:
        print("\nAll Mappings:\n" + str(all_mappings))
    results = []
    for i, index_list in enumerate(all_mappings):
        # If our index list is empty, proceed to next match_index_mapping array
        if not index_list:
            continue

        # If there are no root nodes, create one from this index list
        if not results:
            results.append([MatchIndexMapping(i, index_list[0])])
            continue

        # Append lowest possible index from index_list to each result.
        #
        # This will either result in either:
        # 1. Simply appending it to the end of a result or
        # 2. Inserting it into the middle in which case we'll fork the
        # result into a copy and insert it there, blowing away the remaining
        # elements.
        forked_results = []
        for result in results:
            next_result = False
            for index in index_list:
                for mim_index, match_index_mapping in enumerate(result):
                    if index > match_index_mapping.value:
                        if len(result) - 1 == mim_index:
                            # Append this to the end of the result and go to the
                            # next result
                            result.append(MatchIndexMapping(i, index))
                            next_result = True
                            break
                        else:
                            # Fork the result and insert this in the middle,
                            # blowing away the other results. Proceed to the
                            # next index to see if we need to fork again
                            forked_list = result[:mim_index + 1]
                            forked_list.append(MatchIndexMapping(i, index))
                            forked_results.append(forked_list)
                            # break
                if next_result:
                    break

        if forked_results:
            results.extend(forked_results)

        # If nothing in this index was added to an existing result, then
        # create a new root node if no nodes exist whose initial value is less
        # than the smallest value in the array
        for result in results:
            initial_value = result[0].value
            first_value_from_array = index_list[0]
            if initial_value <= first_value_from_array:
                break
        else:
            results.append([MatchIndexMapping(i, index_list[0])])

    if debug:
        print_all_results(results)

    # Return longest result
    index_longest = -1
    size_longest = -1
    for index_results, result in enumerate(results):
        if len(result) > size_longest:
            index_longest = index_results
            size_longest = len(result)

    return results[index_longest]


if __name__ == "__main__":
    l1 = [1, 2, 3, 4]
    l2 = [1, 4, 2, 3]

    l1 = ["a", "b", "c", "d", "e", "f", "a"]
    l2 = ["b", "c", "d", "e", "f", "a"]

    print("\nList 1: " + str(l1))
    print("\nList 2: " + str(l2))
    result = sequential_compare(l1, l2, True)
    print("\nFinal Result:")
    for match_index_mapping in result:
        print(match_index_mapping)
