# problem-solve
I created this repo to be a place to solve interesting programming problems as I come across them. A focus is on writing clean, readable code that is efficient in terms of time and space utilization.

# Getting Started
### Dependencies
* Python 3.6.2
* pytest==3.3.1

### Running Tests
Execute: `py.test problems/<test_script_name.py>`

# Summary of Problems Solved
Each problem resides in its own python script and tests reside in a script matching the name prefixed with "test_."
* `compare_text_read.py`: Compare original text vs what was altered and return a dict of indexes mapping the matching elements from the original text array to the altered text array.
* `get_num_islands.py`: Find the number of islands in a 2 dimensional array.
* `get_permutations.py`: Get all permutations of a given list of items.
* `ic_1_stock_prices.py`: Get the max profit given 1 purchase and 1 sale of a stock in a given day.
* `ic_10_bst_2nd_largest.py`: Find the 2nd largest item in a binary search tree.
* `ic_14_inflight_entertainment.py`: Given a list of numbers (movie times) and a flight length, find if 2 movie times in the list equal the total flight time.
* `ic_15_fib.py`: Find the nth fibonacci number.
* `ic_16_unbounded_knapsack.py`: Unbounded knapsack problem. Find the max value that can fit into a knapsack of a given weight, given a list of items each having a weight and value.
* `ic_21_find_unique_int_in_list.py`: Given a list of IDs, which contains many duplicate integers and one unique integer, find the unique integer.
* `ic_24_reverse_linked_list.py`: Given a head node of a singly-linked list, reverse it in place and return the new head node.
* `ic_25_linked_list_nth_last_node.py`: Given a head node of a singly-linked list, find the nth to last node.
* `ic_27_reverse_words.py`: Create a function that takes a message as a list of characters and reverses the order of the words in-place.
* `ic_29_bracket_validator.py`: Write an efficient function that tells us whether or not an input string's openers and closers are properly nested.
* `ic_35_in_place_shuffle.py`: Write a function for doing an in-place shuffle of a list.
* `ic_36_single_riffle_shuffle.py`: Write a function that tells us if a full deck of cards is a single riffle of two other halves.
* `ic_42_find_duplicate_files.py`: File all duplicate files (having different names) given a base directory.
* `ic_43_merge_sorted_arrays.py`: Merge two sorted arrays into one sorted array.
* `ic_45_graph_coloring.py`: Given an undirected graph with maximum degree, find a graph coloring using at most D+1 colors.
