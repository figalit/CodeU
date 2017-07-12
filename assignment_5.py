def find_language_characters(ordered_list):
	# use a dict to represent a graph
	# key: item, value: neighbors
	graph = {}
	graph = fill_graph(False, graph, ordered_list)
	graph = fill_graph(True, graph, ordered_list)
	
	# map all nodes to visited or not flag
	node_visited = {}
	for item in graph.keys():
		if item not in node_visited.keys():
			node_visited[item] = False
			
		for val in graph[item]:
			if val not in node_visited.keys():
				node_visited[val] = False
				
	# find predecessors of each node, then sort topollogically
	predecessors_graph = find_predecessors(graph, node_visited)	
	return topological_sort(graph, node_visited, predecessors_graph)

def topological_sort(graph, node_visited, predecessors_graph):
	stack = []
	final_list = []

	for v in node_visited.keys():
		if v not in predecessors_graph.keys():
			stack.append(v)
			node_visited[v] = True
	while(len(stack) != 0):
		v = stack.pop()
		stack.append(v) # we dont want to remove it yet

		# find out if they're all visited
		all_vis = True
		if v in graph.keys() and graph[v] != None:
			for nv in graph[v]:
				if node_visited[nv] == False:
					all_vis = False # no, they're not all visited

		if(all_vis):
			final_list.append(stack.pop())
		else:
			for nv in graph[v]:
				if node_visited[nv] == False:
					stack.append(nv)
					node_visited[nv] = True
	return final_list[::-1]

def fill_graph(fill, graph, ordered_list):
	# traverse through the words in sorted order two by two
	for i in range(1, len(ordered_list)):
		w1 = ordered_list[i-1]
		w2 = ordered_list[i]
		# keep two pointers in each of the words
		p1 = 0
		p2 = 0

		# init neighbors
		while w1[p1] == w2[p2] and p1 < len(w1) and p2 < len(w2): 
			p1 += 1
			p2 += 1
		if fill == False:
			graph[w1[p1]] = [] # initialize
		else:
			graph[w1[p1]].append(w2[p2]) # fill
	return graph

def find_predecessors(graph, node_visited):
	predecessors_graph = {}
	for item in graph.keys():	
		for value_item in graph[item]:
			predecessors_graph[value_item] = []

	for item in graph.keys():
		for value_item in graph[item]:
			predecessors_graph[value_item].append(item)
	return predecessors_graph

print(find_language_characters(['ART', 'RAT', 'CAT', 'CAR','art', 'rat', 'cat', 'car']))



