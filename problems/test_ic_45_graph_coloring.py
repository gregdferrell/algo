from ic_45_graph_coloring import color_graph
from problem_solve_util import GraphNode

colors = ['red', 'blue', 'green', 'yellow', 'purple', 'pink', 'orange']


def get_colors_for_graph(graph):
	max_neighbors = 0
	for graph_node in graph:
		max_neighbors = max(max_neighbors, len(graph_node.neighbors))
	if max_neighbors + 1 > len(colors):
		raise ValueError('not enough colors to support graph nodes')
	return colors[0:max_neighbors + 1]


def validate_graph_colors(graph):
	for graph_node in graph:
		if graph_node.color in (o.color for o in graph_node.neighbors):
			return False
	return True


def test_color_graph_1():
	a = GraphNode('a')
	b = GraphNode('b')
	c = GraphNode('c')

	a.neighbors.add(b)
	b.neighbors.add(a)
	b.neighbors.add(c)
	c.neighbors.add(b)

	graph = [a, b, c]

	colors = get_colors_for_graph(graph)

	# TODO impl algorithm instead of hard coding this example
	color_graph(graph, colors)
	a.color = 'red'
	b.color = 'blue'
	c.color = 'red'

	# Validate graph colors
	assert validate_graph_colors(graph)
