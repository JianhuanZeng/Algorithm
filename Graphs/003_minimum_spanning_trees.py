################################################
# motivation: find the cheapest comummication network over a set of locations.
# unequal edge assimption

################################################
# Prim's algorithm </br>
## cut property, bipatition
## O(n*n)

## from http://interactivepython.org/runestone/static/pythonds/Graphs/PrimsSpanningTreeAlgorithm.html
from pythonds.graphs import PriorityQueue, Graph, Vertex

def prim(Graph, s):
    pq = PriorityQueue()
    for v in Graph:
      v.setDistance(sys.maxsize)
      v.setPred(None)
    s.setDistance(0)
    pq.buildHeap([(v.getDistance(),v) for v in Graph]
    while not pq.isEmpty():
       currentVert = pq.delMin()
       for neighboor in currentVert.getConnections(): 
          newCost = currentVert.getWeight(neighboor)
          if neighboor in pq and newCost <  neighboor.getDistance():
            neighboor.setDistance(newCost)
            neighboor.setPred(currentVert)
            pq.decreaseKey(neighboor,newCost)
                 
## from https://codereview.stackexchange.com/questions/174946/prims-algorithm-using-heapq-module-in-python
from heapq import heappush, heappop

def prim(graph):
   tiebreak = count().__next__              
   total = 0
   explored = set()
   source_vertex = next(iter(graph))
   unexplored = [(0,tiebreak(), source_vertex)]   
   while unexplored:
       cost, _, cur_vertex = heappop(unexplored)
       if cur_vertex not in explored:
            explored.add(cur_vertex)
            total += cost
            for neighbour, cost in graph[cur_vertex]:
                 if neighbour not in explored:
                    heappush(unexplored, (cost, tiebreak(), neighbour))
   return total              
################################################
# Kruskal's algorithm </br>
## O(m*log(n))                 
                 
## from https://gist.github.com/hayderimran7/09960ca438a65a9bd10d0254b792f48f
parent = dict()
rank = dict()

def make_set(vertice):
    parent[vertice] = vertice
    rank[vertice] = 0

def find(vertice):
    if parent[vertice] != vertice:
        parent[vertice] = find(parent[vertice])
    return parent[vertice]

def union(vertice1, vertice2):
    root1 = find(vertice1)
    root2 = find(vertice2)
    if root1 != root2:
        if rank[root1] > rank[root2]:
            parent[root2] = root1
	else:
	    parent[root1] = root2
	if rank[root1] == rank[root2]: rank[root2] += 1

def kruskal(graph):
    for vertice in graph['vertices']:
	make_set(vertice)
	minimum_spanning_tree = set()
	edges = list(graph['edges'])
	edges.sort()
	#print edges
    for edge in edges:
	weight, vertice1, vertice2 = edge
	if find(vertice1) != find(vertice2):
	    union(vertice1, vertice2)
	    minimum_spanning_tree.add(edge)
	    
    return sorted(minimum_spanning_tree)
                 
graph = {
'vertices': ['A', 'B', 'C', 'D', 'E', 'F', 'G'],
'edges': set([
(7, 'A', 'B'),
(5, 'A', 'D'),
(7, 'B', 'A'),
(8, 'B', 'C'),
(9, 'B', 'D'),
(7, 'B', 'E'),
(8, 'C', 'B'),
(5, 'C', 'E'),
(5, 'D', 'A'),
(9, 'D', 'B'),
(7, 'D', 'E'),
(6, 'D', 'F'),
(7, 'E', 'B'),
(5, 'E', 'C'),
(15, 'E', 'D'),
(8, 'E', 'F'),
(9, 'E', 'G'),
(6, 'F', 'D'),
(8, 'F', 'E'),
(11, 'F', 'G'),
(9, 'G', 'E'),
(11, 'G', 'F'),
])
}

print kruskal(graph)                
################################################
# more
## reverse-delete
## unequal edge assimption: perturbations, tie-breakers                 
