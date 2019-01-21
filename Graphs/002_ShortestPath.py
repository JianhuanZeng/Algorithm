################################################
# Dijkstra's algorithm
## non-negative weight, greedy algorithm
## from a s to all t
## - v1:O(n*(n+sum(degree(u))))
## - v2:O(n*(n+m))
## - v3:O(log(n)*(n+m)), binary min-heap

# from https://dev.to/mxl/dijkstras-algorithm-in-python-algorithms-for-beginners-dkc
from collections import deque,namedtuple
inf = float('inf')
edge = namedtuple('edge', 'start, end, cost')

def make_edge(start, end, cost=1):
  return edge(start, end, cost)

Class Graph:
  def __init__(self,edges):
    wrong_edges = [i for i in edges if len(i) not in [2, 3]]
    if wrong_edges:
      raise ValueError('Wrong edges data: {}'.format(wrong_edges))
    self.edges = [make_edge(*edge) for edge in edges]
    
   @property
   def vertices(self):
      return set(sum(([edge.start, edge.end] for edge in self.edges), []))
    
  def get_node_pairs(self, n1, n2, both_ends=True):
      if both_ends:
          node_pairs = [[n1, n2], [n2, n1]]
      else:
          node_pairs = [[n1, n2]]
      return node_pairs    
    
  def remove_edge(self, n1, n2, both_ends=True):
      node_pairs = self.get_node_pairs(n1, n2, both_ends)
      edges = self.edges[:]
      for edge in edges:
          if [edge.start, edge.end] in node_pairs:
              self.edges.remove(edge)    
              
  def Dijkstra(self,s,t):
    assert s in self.vertices, 'Such source node doesn\'t exist'
    distance = {vertex: inf for vertex in self.vertices}
    previous_vertices = {vertex: None for vertex in self.vertices}
    distances[s] = 0
    vertices = self.vertices.copy()

    while vertices:
      current_vertex = min(vertices, key=lambda vertex: distances[vertex])
      if distances[current_vertex] == inf:
        break

      for neighbour, cost in self.neighbours[current_vertex]:
        alternative_route = distances[current_vertex] + cost
        if alternative_route < distances[neighbour]:
          distances[neighbour] = alternative_route
          previous_vertices[neighbour] = current_vertex

        vertices.remove(current_vertex)

    path, current_vertex = deque(), dest
    while previous_vertices[current_vertex] is not None:
      path.appendleft(current_vertex)
      current_vertex = previous_vertices[current_vertex]
    if path:
        path.appendleft(current_vertex)
    return path
  
  graph = Graph([("a", "b", 7), ("a", "c", 9), ("a", "f", 14), 
                 ("b", "c", 10), ("b", "d", 15), ("c", "d", 11), 
                 ("c", "f", 2),  ("d", "e", 6), ("e", "f", 9)])
  
  print(graph.Dijkstra("a", "e"))
  
  
# from https://startupnextdoor.com/dijkstras-algorithm-in-python-3/
import queue  
from collections import namedtuple
Edge = namedtuple('Edge', ['vertex', 'weight'])

class GraphUndirectedWeighted(object):  
  def __init__(self, vertex_count):
    self.vertex_count = vertex_count
    self.adjacency_list = [[] for _ in range(vertex_count)]
        def add_edge(self, source, dest, weight):
        assert source < self.vertex_count
        assert dest < self.vertex_count
        self.adjacency_list[source].append(Edge(dest, weight))
        self.adjacency_list[dest].append(Edge(source, weight))

  def get_edge(self, vertex):
      for e in self.adjacency_list[vertex]:
          yield e

  def get_vertex(self):
      for v in range(self.vertex_count):
          yield v

def Dijkstra(graph, source, dest):
    q = queue.PriorityQueue()
    parents = {}
    distances = {}
    start_weight = float('inf')
  
     for i in graph.get_vertex():
        weight = start_weight
        if source == i:
            weight = 0
        distances.append(weight)
        parents.append(None)  
        
      q.put(([0, source]))
      
      while not q.empty():
        v_tuple = q.get()
        v = v_tuple[1]
        
        for e in graph.get_edge(v):
          alternative_route = distances[v] + e.weight
          if distances[e.vertex] > alternative_route:
              distances[e.vertex] = candidate_distance
              parents[e.vertex] = v
              if candidate_distance < -1000:
                 raise Exception("Negative cycle detected")  
              q.put(([distances[e.vertex], e.vertex]))
              
    shortest_path = []
    end = dest
    while end is not None:
        shortest_path.append(end)
        end = parents[end]
    shortest_path.reverse()
    return shortest_path, distances[dest]
  
  def main():
    g = GraphUndirectedWeighted(9)
    g.add_edge(0, 1, 4)
    g.add_edge(1, 7, 6)
    g.add_edge(1, 2, 1)
    g.add_edge(2, 3, 3)
    g.add_edge(3, 7, 1)
    g.add_edge(3, 4, 2)
    g.add_edge(3, 5, 1)
    g.add_edge(4, 5, 1)
    g.add_edge(5, 6, 1)
    g.add_edge(6, 7, 2)
    g.add_edge(6, 8, 2)
    g.add_edge(7, 8, 2)
    
    print(Dijkstra(g, 0, 1))
################################################
## Bellman-Ford algorithm </br>
################################################
## Floyd-Warshall algorithm </br>
