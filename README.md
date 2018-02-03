# problem-solve
Problem Solve contains scripts and tests for random programming problems I have found and wanted to solve for learning and fun.

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
* `ic_15_fib.py`: Find the nth fibonacci number.
* `ic_16_unbounded_knapsack.py`: Unbounded knapsack problem. Find the max value that can fit into a knapsack of a given weight, given a list of items each with a unique weight and value.
* `ic_21_find_unique_int_in_list.py`: Given a list of IDs, which contains many duplicate integers and one unique integer, find the unique integer.
