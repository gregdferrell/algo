#
# Problem: File all duplicate files (having different names) given a base directory.
#
# Return a list of tuples where:
# The first item is the duplicate file
# The second item is the original file
# Assume each file was only duplicated once
#

import os


def find_duplicate_files(base_dir):
	"""
	Solution: ???
	Complexity:
		Time: O(?)
		Space: O(?)
	"""
	for root, directories, filenames in os.walk(base_dir):
		for filename in filenames:
			file_path = os.path.join(root, filename)
			print(os.path.join(root, filename))
			print(os.path.getmtime(file_path))
