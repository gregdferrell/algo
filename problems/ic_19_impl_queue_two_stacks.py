#
# Problem: Implement a queue with two stacks.
#
# Implement a queue with 2 stacks.
# Your queue should have an enqueue and a dequeue method and it should be "first in first out" (FIFO).
#


class Queue:
	"""
	Solution:
	Complexity:
		Enqueue: O(1)
		Dequeue: O(m) where m = size of queue
	"""
	def __init__(self):
		self.stack_in = []
		self.stack_out = []

	def enqueue(self, item):
		self.stack_in.append(item)

	def dequeue(self):
		if not self.stack_out:
			for i in range(len(self.stack_in)):
				self.stack_out.append(self.stack_in.pop())
		if self.stack_out:
			return self.stack_out.pop()
		else:
			return None
