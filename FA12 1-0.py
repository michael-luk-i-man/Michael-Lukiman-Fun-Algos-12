# We want to maximize the product, recalling that the sum of logs is equal to the log of the two terms multiplied. 


# Consider a graph with nodes A B C D.
# And reliabilities between AB 0.5 AC 0.4 BD 0.3 CD 0.5
# The right path is AC CD. 


for weight in w:
	weight = 1/log(weight)




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