#
# Problem: File all duplicate files (having different names) given a base directory.
#
# Return a list of tuples where:
# The first item is the duplicate file
# The second item is the original file
# Assume each file was only duplicated once
#

import hashlib
import os


def chunk_reader(file, chunk_size=1024):
	while True:
		chunk = file.read(chunk_size)
		if not chunk:
			return
		yield chunk


def get_hash(filename, first_chunk_only=False):
	# Use sha1 hashing algorithm
	hashed_object = hashlib.sha1()
	file_object = open(filename, 'rb')

	# Feed it bytes
	if first_chunk_only:
		hashed_object.update(file_object.read(1024))
	else:
		for chunk in chunk_reader(file_object):
			hashed_object.update(chunk)

	# Get the digest
	hashed = hashed_object.digest()

	file_object.close()
	return hashed


def find_duplicate_files(base_dir):
	"""
	Solution: ???
	Complexity:
		Time: O(n) - The time it takes to hash the whole file (or the first chunk)
		Space: O(n) - The hash (plus the list of duplicates)
	"""
	duplicates = []
	hashes = {}
	for root, directories, filenames in os.walk(base_dir):
		for filename in filenames:
			file_path = os.path.join(root, filename)

			# Get file hash
			hash = get_hash(file_path)

			# Compare with dict
			if not hashes.get(hash):
				hashes[hash] = file_path
			else:
				if os.path.getmtime(file_path) > os.path.getmtime(hashes.get(hash)):
					duplicates.append((file_path, hashes.get(hash)))
				else:
					duplicates.append((hashes.get(hash), file_path))
				del hashes[hash]
	return duplicates
