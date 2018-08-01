import pytest

from .ic_mesh_message import bfs, find_shortest_route


def lists_equal(l1, l2):
	return len(l1) == len(l2) and sorted(l1) == sorted(l2)


def test_bfs():
	network = {
		'Min': ['William', 'Jayden', 'Omar'],
		'William': ['Min', 'Noam'],
		'Jayden': ['Min', 'Amelia', 'Ren', 'Noam'],
		'Ren': ['Jayden', 'Omar'],
		'Amelia': ['Jayden', 'Adam', 'Miguel'],
		'Adam': ['Amelia', 'Miguel'],
		'Miguel': ['Amelia', 'Adam'],
		'Noam': ['Jayden', 'William'],
		'Omar': ['Ren', 'Min']
	}
	node_start = 'Ren'
	node_end = 'William'
	assert bfs(network, node_start, node_end) == 'William'


def test_bfs_not_found():
	network = {
		'Min': ['William', 'Jayden', 'Omar'],
		'William': ['Min', 'Noam'],
		'Jayden': ['Min', 'Amelia', 'Ren', 'Noam'],
		'Ren': ['Jayden', 'Omar'],
		'Amelia': ['Jayden', 'Adam', 'Miguel'],
		'Adam': ['Amelia', 'Miguel'],
		'Miguel': ['Amelia', 'Adam'],
		'Noam': ['Jayden', 'William'],
		'Omar': ['Ren', 'Min']
	}
	node_start = 'Ren'
	node_end = 'Bart'
	with pytest.raises(ValueError):
		bfs(network, node_start, node_end)


def test_find_shortest_route_validate_inputs():
	network = {}
	node_start = 'Jayden'
	node_end = 'Adam'
	with pytest.raises(ValueError):
		find_shortest_route(network, node_start, node_end)

	network = {'Min': ['William', 'Jayden', 'Omar']}
	node_start = ''
	node_end = 'Adam'
	with pytest.raises(ValueError):
		find_shortest_route(network, node_start, node_end)

	network = {'Min': ['William', 'Jayden', 'Omar']}
	node_start = 'Jayden'
	node_end = ''
	with pytest.raises(ValueError):
		find_shortest_route(network, node_start, node_end)

	network = {'Min': ['NOT-IN-NETWORK', 'Jayden', 'Omar']}
	node_start = 'Jayden'
	node_end = ''
	with pytest.raises(ValueError):
		find_shortest_route(network, node_start, node_end)

	network = {'Min': ['William', 'NOT-IN-NETWORK', 'Omar']}
	node_start = 'Jayden'
	node_end = ''
	with pytest.raises(ValueError):
		find_shortest_route(network, node_start, node_end)


def test_find_shortest_route():
	expected = ['Jayden', 'Amelia', 'Adam']
	network = {
		'Min': ['William', 'Jayden', 'Omar'],
		'William': ['Min', 'Noam'],
		'Jayden': ['Min', 'Amelia', 'Ren', 'Noam'],
		'Ren': ['Jayden', 'Omar'],
		'Amelia': ['Jayden', 'Adam', 'Miguel'],
		'Adam': ['Amelia', 'Miguel'],
		'Miguel': ['Amelia', 'Adam'],
		'Noam': ['Jayden', 'William'],
		'Omar': ['Ren', 'Min']
	}
	node_start = 'Jayden'
	node_end = 'Adam'
	actual = find_shortest_route(network, node_start, node_end)
	assert lists_equal(actual, expected)


def test_find_shortest_route_no_path():
	network = {
		'Min': ['William'],
		'William': ['Min'],
		'Jayden': ['Amelia'],
		'Amelia': ['Jayden']
	}
	node_start = 'Min'
	node_end = 'Jayden'
	assert find_shortest_route(network, node_start, node_end) is None
