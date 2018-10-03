from .get_graph_node_distance_array import solution


def test_1():
	items = [9, 1, 4, 9, 0, 4, 8, 9, 0, 1]
	assert solution(items) == [1, 3, 2, 3, 0, 0, 0, 0, 0]
