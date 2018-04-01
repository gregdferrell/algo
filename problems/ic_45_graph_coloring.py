#
# Problem: Given an undirected graph with maximum degree, find a graph coloring using at most D+1 colors.
#


def color_graph_first_available(graph, colors):
	"""
	Solution: For each graph node, assign to it the first color not in the list of neighbor colors.
	Complexity: (where n is # nodes, d is max degrees)
		Time: O(n * (d + d+1 + 1)) -> O(n * d)
		Space: O(g) -> size of graph
	"""
	# For every node
	for node in graph:
		if node in node.neighbors:
			raise ValueError('cannot color graph with node loops')

		# Look at each neighbor and create a set of their colors
		neighbor_colors = set([neighbor.color for neighbor in node.neighbors if neighbor.color])
		# Look at each color and create a set of available colors not in the neighbor colors set
		available_colors = [color for color in colors if color not in neighbor_colors]
		# Take the first available
		node.color = available_colors[0]


def color_graph_first_available_slightly_faster(graph, colors):
	"""
	Solution: For each graph node, assign to it the first available color not used by one of its neighbors.
	Complexity: (where n is # nodes, d is max degrees)
		Time: O(n * d)
		Space: O(g) -> size of graph
	"""
	for node in graph:
		if node in node.neighbors:
			raise ValueError('cannot color graph with node loops')

		# Look at each neighbor and create a set of their colors
		neighbor_colors = set([neighbor.color for neighbor in node.neighbors if neighbor.color])

		for color in colors:
			if color not in neighbor_colors:
				node.color = color
				break
