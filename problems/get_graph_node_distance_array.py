#
# Problem: Given an array of ints representing a graph, where:
# - the position of the array indicates the node value
# - the value of the array at that position indicates the node value that this node is attached to
# - the beginning of the graph will be the item whose value is equal to the index it is in
# Write a function that returns a list (size = n-1) of ints where each index is equal to the number of nodes at that
# distance away from the beginning of the graph.

# Example:
# Input: [9, 1, 4, 9, 0, 4, 8, 9, 0, 1]
# Beginning of graph is "1" (value 1 at index 1)
# - One item (node/index 9) is next to node 1
# - 3 items (0, 3, 7) is next to node 9
# - so on and so forth
# Solution: [1, 3, 2, 3, 0, 0, 0, 0, 0]


class GraphNode:
	def __init__(self, label):
		self.label = label
		self.neighbors = set()

	def __repr__(self):
		return f'{self.label}: {self.neighbors}'


def solution(T):
	nodes = [GraphNode(i) for i in range(len(T))]

	capital = -1
	# Create graph representation of our data
	for idx, item in enumerate(T):
		if idx == item:
			capital = idx
		else:
			nodes[idx].neighbors.add(item)
			nodes[item].neighbors.add(idx)

	# Track which nodes have been and need to be evaluated at each step
	nodes_evaluated = set()
	nodes_to_eval = [capital]

	# print(nodes)

	# Our resulting list
	result = []

	while len(nodes_to_eval) > 0:
		num_neighbors = 0
		next_nodes = set()
		for node_to_eval in nodes_to_eval:
			nodes_evaluated.add(node_to_eval)
			num_neighbors += len(nodes[node_to_eval].neighbors) - 1
			if node_to_eval == capital:
				num_neighbors += 1
			for node in nodes[node_to_eval].neighbors:
				if node not in nodes_evaluated:
					next_nodes.add(node)
		result.append(num_neighbors)

		nodes_to_eval.clear()
		nodes_to_eval.extend(next_nodes)

	# Extend our result array with 0s for each distance we did not get to
	zeroes = len(T) - 1 - len(result)
	result.extend([0 for i in range(zeroes)])
	return result
