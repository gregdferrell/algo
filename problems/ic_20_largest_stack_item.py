#
# Problem: Implement class MaxStack that allows access to the largest element in the stack.
#
# Given the class Stack (from problem_solve_util.py) implement a class MaxStack that has a function get_max() which
# returns the largest element in the stack. Assume the stack contains only integers.
#

from problem_solve_util import Stack


class MaxStackIterate(Stack):
	"""
	Solution: Traverse the full stack, looking for the largest item.
	Complexity:
		Time: O(n)
		Space: O(1)
	"""

	def get_max(self):
		max = 0
		for item in self.items:
			if item > max:
				max = item
		return max


class MaxStackDouble(Stack):
	"""
	Solution: Keep track of the max_items in a separate stack. Override push/pop to maintain it as well.
	Complexity:
		Time: O(1)
		Space: O(n)
	"""

	def __init__(self):
		# Create a stack that will contain the max values as they're pushed onto the main stack
		super(MaxStackDouble, self).__init__()
		self.max_stack = Stack()

	def push(self, item):
		super(MaxStackDouble, self).push(item)
		if not self.max_stack.peek() or item > self.max_stack.peek():
			self.max_stack.push(item)

	def pop(self):
		item = super(MaxStackDouble, self).pop()
		if item == self.max_stack.peek():
			self.max_stack.pop()

	def get_max(self):
		return self.max_stack.peek()
