for weight in w:
	weight = log(1/weight)



# _____________________________________-

def reliable_path(G, w, s, t): # Finds the path that optimizes for max reliability given a reliability of each edge. 
	initialize_single_source(G,s) # Refer to subfunc
	S = [] # To hold the path. 
	Q = G.v # The max priority queue comprised of vertices.
	while Q != []:
		u = extract_max(Q) # Extracts the element with the most reliability, AKA a max-queue sorted by reliability. 
		S.append(u) # Add that vertex to the path list. 
		for v in G.adj[u]: # For all adjacent nodes to that vertex...
			relax(u,v,w) # Relax the edge between the two nodes. 
                if v_max = t: # If we've reached t, the destination...
                        return S # ...Return the path. Since reliability is always 1 or below, any further nodes will just make more unreliable.

def initialize_single_source_reliably(G,s):
	for v in G.v: 
		v.p = -inf # Initialize so all other reliabilities will register as higher. 
		v.pi = NIL # Initialize with no parent node.
	reliability[s] = 1.0 # Start with 1.0 for the sake of probability multiplication.  

def relax_reliably(u,v,w):
	if reliability[v] < reliability[u] * w(u,v): # If v's current reliability value is less reliable than with the tested edge (reliability of u * weighted edge reliability)...
		reliability[v] = reliability[u] * w(u,v) # ...Set the reliability as taking the path with the tested edge.
		v.pi = u # u is the parent of that edge's v. 
                global v_max = v # Holder value to check v outside of the loop.



# _____________________________

def reliable_path(G, w, s):
	initialize_single_source(G,s)
	S = []
	Q = G.v
	while Q != []:
		u = extract_max(Q)
		S.append(u)
		for v in G.adj[u]
			relax(u,v,w)


def initialize_single_source_reliably(G,s):
	for v in G.v:
		v.d = -inf
		v.pi = NIL
	probability[s] = 1

def relax_reliably(u,v,w):
	if probability[v] < probability[u] * w(u,v):
		probability[v] = probability[u] * w(u,v)
		v.pi = u

# __________________________

def dijkstra(G, w, s):
	initialize_single_source(G,s) # Make every vertex far and parentless.
	# The distance of s is 0. 

	S = [] # This is the decided path, I guess. 
	Q = G.v # The queue is the set of vertices in G. 
	while Q != []: # While the queue is not empty...
		u = extract_min(Q) # Extract the next vertex? with the smallest distance?
		S.append(u) # Add the vertex to the group.
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