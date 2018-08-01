#
# Problem: Write a function to find the shortest route from one phone to another in a messaging app.
#
from collections import deque
from typing import Dict, List


def bfs(network: Dict, node_start, node_end) -> str:
	if not network or not node_start or not node_end:
		raise ValueError('network, node_start and node_end must contain values')

	if node_start not in network or node_end not in network:
		raise ValueError('start and end nodes must be in the network')

	nodes_to_visit = deque()
	nodes_to_visit.append(node_start)

	nodes_visited = set()

	while len(nodes_to_visit) > 0:
		current_node = nodes_to_visit.popleft()

		if current_node == node_end:
			return current_node

		nodes_visited.add(current_node)
		for neighbor in network[current_node]:
			if neighbor not in nodes_visited:
				nodes_to_visit.append(neighbor)

	raise ValueError('node not found')


def find_shortest_route(network: Dict, node_start: str, node_end: str):
	"""
	Solution:
	Complexity:
		Time: O(X) -
		Space: O(X) -
	"""
	if not network or not node_start or not node_end:
		raise ValueError('network, node_start and node_end must contain values')

	if node_start not in network or node_end not in network:
		raise ValueError('start and end nodes must be in the network')

	nodes_to_visit = deque()
	nodes_to_visit.append(node_start)

	# Keep track of what nodes we've already seen
	# so we don't process them twice
	nodes_already_seen = {node_start}

	nodes_how_reached = {node_start: None}

	while len(nodes_to_visit) > 0:
		current_node = nodes_to_visit.popleft()

		# Stop when we reach the end node
		if current_node == node_end:
			# Found it!
			break

		for neighbor in network[current_node]:
			if neighbor not in nodes_already_seen:
				nodes_already_seen.add(neighbor)
				nodes_to_visit.append(neighbor)
				nodes_how_reached[neighbor] = current_node

	stuff = reconstruct_path(node_start, node_end, nodes_how_reached)
	return stuff


def reconstruct_path(node_start, node_end, nodes_how_reached):
	if node_end not in nodes_how_reached:
		return None

	path = []
	current_node = node_end
	while current_node:
		path.append(current_node)
		current_node = nodes_how_reached[current_node]
	path.reverse()
	return path
