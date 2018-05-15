""" Djikstra's Algorithm (Uniform Cost)
	O(|E| + |V|log|V|)

	Max E = V*(V-1) in a directed graph or V*(V-1)/2 in an undirected graph
"""
from heapq import *

INF = float('inf')


class Node():
	"""
	Args:
		self.name = str
		self.connections = {'name': edge_val, ...}
		self.val = int value to get to this node from start
		self.prev = node that hopped to this spot
	"""
	def __init__(self, name):
		self.name = name
		self.connections = {}#connections are edges
		self.val = INF
		self.prev = None

#

def construct_graph(nodes):
	"""
	Args:
		nodes (dict of keys as node names and
		vals as a dict with {'adjacent_node': edge_val_to_node})
	Returns:
		dictionary of all nodes with key as node name and val as Node instance
	"""
	graph = {}
	for node, connections in nodes:
		new_node = Node(node)
		new_node.connections.update(connections)
		graph[node] = new_node
	return graph


def Djikstra(start, end, graph):
	"""
	Returns:
		list of node names in the graph which 
		make up the shortest path from start to end
	"""

	# Initialize Values 
	live_nodes = []				# Python heapq/Priority Queue for O(1) min pop
	dead_nodes = set()			# O(1) lookups
	end_node = graph[end]
	curr_node = graph[start]
	curr_node.val = 0
	heappush(live_nodes, (curr_node.val, curr_node))

	while curr_node != end_node:
		curr_node = heappop(live_nodes)[1]
		dead_nodes.add(curr_node.name)

		# For every node adjacent to current_node
		for name, val in min_node.connections:
			if name not in dead_nodes:
				new_cost = val + curr_node.val
				if graph[name].prev is None:		# Never Visited
					graph[name].prev = curr_node.name
					graph[name].val = new_cost
					heappush(live_nodes, (graph[name].val, graph[name]))
				else:								# Previously Visited
					if graph[name].val > new_cost:
						graph[name].prev = curr_node.name
						graph[name].val = new_cost

		# Dead End Scenario
		if len(live_nodes) == 0:
			return []

	# Backtrack to get path
	# Can call Djikstra(end, start, graph) to avoid backtrack and reverse
	path = [end_node]
	curr_node = end_node
	while curr_node != start_node:
		path.append(graph[curr_node.prev])
		curr_node = graph[curr_node.prev]

	return path[::-1]
