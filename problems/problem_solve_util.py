#
# Utility functions.
#
from math import floor


def binary_search(target, nums):
	"""
	Checks to see if a given number appears in a sorted list of numbers.
	:param target: The number to look for
	:param nums: A sorted (ascending) list of numbers
	:return: Boolean indicating if the target was found
	"""
	first_index = 0
	last_index = len(nums) - 1

	# If the target value isn't between the values at the beginning and end
	# of our list, return False immediately
	if not (nums[0] <= target <= nums[-1]):
		return False

	while True:
		# Calculate our target index -the middle point between the first
		# and last indexes that we're tracking
		target_index = (floor((last_index - first_index) / 2)) + first_index
		if target == nums[target_index]:
			return True
		elif first_index == last_index:
			return False
		elif target < nums[target_index]:
			last_index = target_index
		elif target > nums[target_index]:
			first_index = target_index + 1


class LinkedListNode:
	"""
	Linked List Node
	"""

	def __init__(self, value):
		self.value = value
		self.next = None

	def __repr__(self):
		return self.value


class BinaryTreeNode:
	"""
	Binary Tree Node
	"""

	def __init__(self, value, parent=None):
		self.value = value
		self.left = None
		self.right = None
		self.parent = parent

	def insert_left(self, value):
		self.left = BinaryTreeNode(value, self)
		return self.left

	def insert_right(self, value):
		self.right = BinaryTreeNode(value, self)
		return self.right


class GraphNode:
	"""
	Graph Node
	"""

	def __init__(self, label):
		self.label = label
		self.neighbors = set()
		self.color = None


class Stack(object):

	def __init__(self):
		"""Initialize an empty stack"""
		self.items = []

	def push(self, item):
		"""Push new item to stack"""
		self.items.append(item)

	def pop(self):
		"""Remove and return last item"""
		# If the stack is empty, return None
		# (it would also be reasonable to throw an exception)
		if not self.items:
			return None

		return self.items.pop()

	def peek(self):
		"""See what the last item is"""
		if not self.items:
			return None
		return self.items[-1]
