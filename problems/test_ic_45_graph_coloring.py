import pytest

from ic_45_graph_coloring import color_graph_first_available_slightly_faster
from problem_solve_util import GraphNode

colors = ['red', 'blue', 'green', 'yellow', 'purple', 'pink', 'orange']


def get_colors_for_graph(graph):
	"""
	Given a graph, returns a list of colors whose length is D + 1 where D = the max degree of the graph
	:param graph: the graph to return a list of colors for
	:return: the list of colors
	"""
	max_neighbors = 0
	for graph_node in graph:
		max_neighbors = max(max_neighbors, len(graph_node.neighbors))
	if max_neighbors + 1 > len(colors):
		raise ValueError('not enough colors to support graph nodes')
	return colors[0:max_neighbors + 1]


def validate_graph_colors(graph):
	"""
	Validates that each graph node has a color distinct from the colors of its neighbors.
	:param graph: the graph to examine
	:return: boolean indicating whether the graph nodes have valid colors
	"""
	for graph_node in graph:
		print(graph_node.color + ': ' + ', '.join(str(o.color) for o in graph_node.neighbors))
		if graph_node.color in (o.color for o in graph_node.neighbors):
			return False
	return True


def test_color_graph_1_node():
	a = GraphNode('a')

	graph = [a]

	graph_colors = get_colors_for_graph(graph)

	color_graph_first_available_slightly_faster(graph, graph_colors)

	assert validate_graph_colors(graph)


def test_color_graph_3_nodes():
	a = GraphNode('a')
	b = GraphNode('b')
	c = GraphNode('c')

	a.neighbors.add(b)
	b.neighbors.add(a)
	b.neighbors.add(c)
	c.neighbors.add(b)

	graph = [a, b, c]

	graph_colors = get_colors_for_graph(graph)

	color_graph_first_available_slightly_faster(graph, graph_colors)

	assert validate_graph_colors(graph)


def test_color_graph_many_nodes():
	a = GraphNode('a')
	b = GraphNode('b')
	c = GraphNode('c')
	d = GraphNode('d')
	e = GraphNode('e')

	a.neighbors.add(b)
	a.neighbors.add(c)
	a.neighbors.add(d)
	a.neighbors.add(e)
	b.neighbors.add(a)
	b.neighbors.add(c)
	b.neighbors.add(d)
	b.neighbors.add(e)
	c.neighbors.add(a)
	c.neighbors.add(b)
	d.neighbors.add(a)
	d.neighbors.add(b)
	d.neighbors.add(e)
	e.neighbors.add(a)
	e.neighbors.add(b)
	e.neighbors.add(d)

	graph = [a, b, c, d, e]

	graph_colors = get_colors_for_graph(graph)

	color_graph_first_available_slightly_faster(graph, graph_colors)

	assert validate_graph_colors(graph)


def test_color_graph_small():
	a = GraphNode('a')
	b = GraphNode('b')
	c = GraphNode('c')
	d = GraphNode('d')

	a.neighbors.add(b)
	b.neighbors.add(a)
	b.neighbors.add(c)
	c.neighbors.add(b)
	c.neighbors.add(d)
	d.neighbors.add(c)

	graph = [a, b, c, d]

	graph_colors = get_colors_for_graph(graph)

	color_graph_first_available_slightly_faster(graph, graph_colors)

	assert validate_graph_colors(graph)


def test_color_graph_isolated_nodes():
	a = GraphNode('a')
	b = GraphNode('b')
	c = GraphNode('c')
	d = GraphNode('d')
	e = GraphNode('e')

	a.neighbors.add(b)
	b.neighbors.add(a)
	c.neighbors.add(d)
	d.neighbors.add(c)

	graph = [a, b, c, d, e]

	graph_colors = get_colors_for_graph(graph)

	color_graph_first_available_slightly_faster(graph, graph_colors)

	assert validate_graph_colors(graph)


def test_color_graph_node_loops():
	a = GraphNode('a')
	b = GraphNode('b')

	a.neighbors.add(b)
	b.neighbors.add(a)
	b.neighbors.add(b)

	graph = [a, b]

	graph_colors = get_colors_for_graph(graph)

	with pytest.raises(ValueError) as e:
		color_graph_first_available_slightly_faster(graph, graph_colors)
