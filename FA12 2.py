def supermarket_paths(G, B, h, w):
	"""
		Find the shortest distance from h to each supermarket b in B. 
	"""
	initialize_single_source(G,s) # Make every vertex far and parentless.
	# The distance of h is 0. 

	P = [] # This list to hold the path. 
	Q = G.v # The queue is the set of vertices in G. 
	while Q != []: # While the queue is not empty...
		u = extract_min(Q) # Extract the vertex with the smallest distance in queue (and unqueue it).
		P.append(u) # Add the vertex to the path.
		for v in G.adj[u]
			relax(u,v,w)


def initialize_single_source(G,s):
	for v in G.v:
		v.d = inf
		v.pi = NIL
	distance[s] = 0

def relax(u,v,w):
	if distance[v] > distance[u] + w(u,v):
		distance[v] = distance[u] + w(u,v)
		v.pi = u