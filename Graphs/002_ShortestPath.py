# Dijkstra's algorithm
## non-negative weight, greedy algorithm
## from a s to all t
## - v1:O(n*(n+sum(degree(u))))
## - v2:O(n*(n+m))
## - v3:O(log(n)*(n+m)), binary min-heap
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
  
