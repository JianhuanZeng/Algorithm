# motivation: find the cheapest comummication network over a set of locations.
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
################################################
# more
