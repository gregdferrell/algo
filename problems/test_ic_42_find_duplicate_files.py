import os

from .ic_42_find_duplicate_files import find_duplicate_files


def test_find_duplicate_files():
	base_dir = os.path.abspath('../data')
	duplicates = find_duplicate_files(base_dir)
	for dup in duplicates:
		print(f'\nDuplicate: {dup[0]}\nOriginal: {dup[1]}')
