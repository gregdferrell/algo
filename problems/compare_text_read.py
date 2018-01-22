#
# Problem: Compare original text vs what was altered and return a dict of
# indexes mapping the matching elements from the original text array to the
# altered text array.
#
# TODO: ported from Java -make this pythonic
#


def get_ordered_matches_map(text_original, text_altered):
    results = {}
    starting_match_index = MatchIndex(0, 0)

    # Search for matches until one of the lists has been fully searched through
    while starting_match_index.index_original < len(
            text_original) and starting_match_index.index_altered < len(
        text_altered):
        original_first_match_index = MatchIndex(-1, -1)
        altered_first_match_index = MatchIndex(-1, -1)

        # Starting at the last matched index, for each value in the original
        # list, scan the remaining values in the altered list for a match
        # and mark the index of the first match found.
        for original_index in range(starting_match_index.index_original,
                                    len(text_original)):
            for altered_index in range(starting_match_index.index_altered,
                                       len(text_altered)):
                if text_original[original_index] == text_altered[altered_index]:
                    original_first_match_index.index_original = original_index
                    original_first_match_index.index_altered = altered_index
                    break

            if original_first_match_index.is_set():
                break

        # Same for altered list
        for altered_index in range(starting_match_index.index_altered,
                                   len(text_altered)):
            for original_index in range(starting_match_index.index_original,
                                        len(text_original)):
                if text_altered[altered_index] == text_original[original_index]:
                    altered_first_match_index.index_original = original_index
                    altered_first_match_index.index_altered = altered_index
                    break

            if altered_first_match_index.is_set():
                break

        # No match found
        if not original_first_match_index.is_set() and \
                not altered_first_match_index.is_set():
            break

        # If a match is found in both loops, use the indexes for the match
        # with the highest lower index from either list
        match = get_match_with_highest_lower_index(original_first_match_index,
                                                   altered_first_match_index)

        results[match.index_original] = match.index_altered
        starting_match_index.index_original = match.index_original + 1
        starting_match_index.index_altered = match.index_altered + 1

    return results


def visualize_match_array(original: bool, li, results):
    i = -1
    match = 0
    str = ""
    if original:
        str += "Original: "
    else:
        str += "Altered: "

    for text in li:
        i += 1
        str += text
        if (original and results[i]) or (not original and i in results.values):
            match += 1
            str += "[" + match + "]"
        if len(li) != i + 1:
            str += ", "


class MatchIndex:
    def __init__(self, index_original, index_altered):
        self.index_original = index_original
        self.index_altered = index_altered

    def is_set(self):
        return self.index_original > -1 and self.index_altered > -1


def get_match_with_highest_lower_index(x: MatchIndex, y: MatchIndex):
    x_highest = x.index_original if x.index_original > x.index_altered else \
        x.index_altered
    y_highest = y.index_original if y.index_original > y.index_altered else \
        y.index_altered
    return x if (y_highest >= x_highest >= 0) else y
