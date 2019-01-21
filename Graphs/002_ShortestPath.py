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
    
if __name__ == "__main__":  
    main()    
################################################
# Bellman-Ford algorithm
## negative edges, DP algorithm(no negative cycle)
## from a s to all v
## DP: OPT(i,v) = cost of a shortest s-v path with at most i edges
## DP: OPT(i,v) = min(OPT(i-1,v), min(OPT(i-1,x)+w(x,v)))
## O(nm)

# from https://www.sanfoundry.com/python-program-implement-bellman-ford-algorithm/
class Vertex:
    def __init__(self, key):
        self.key = key
        self.points_to = {}
 
    def get_key(self):
        """Return key corresponding to this vertex object."""
        return self.key
 
    def add_neighbour(self, dest, weight):
        """Make this vertex point to dest with given edge weight."""
        self.points_to[dest] = weight
 
    def get_neighbours(self):
        """Return all vertices pointed to by this vertex."""
        return self.points_to.keys()
 
    def get_weight(self, dest):
        """Get weight of edge from this vertex to dest."""
        return self.points_to[dest]
 
    def does_it_point_to(self, dest):
        """Return True if this vertex points to dest."""
        return dest in self.points_to
      
class Graph:
    def __init__(self):
        # dictionary containing keys that map to the corresponding vertex object
        self.vertices = {}
        
    def add_vertex(self, key):
        """Add a vertex with the given key to the graph."""
        vertex = Vertex(key)
        self.vertices[key] = vertex
 
    def get_vertex(self, key):
        """Return vertex object with the corresponding key."""
        return self.vertices[key]
 
    def __contains__(self, key):
        return key in self.vertices
 
    def add_edge(self, src_key, dest_key, weight=1):
        """Add edge from src_key to dest_key with given weight."""
        self.vertices[src_key].add_neighbour(self.vertices[dest_key], weight)
 
    def does_edge_exist(self, src_key, dest_key):
        """Return True if there is an edge from src_key to dest_key."""
        return self.vertices[src_key].does_it_point_to(self.vertices[dest_key])
 
    def __len__(self):
        return len(self.vertices)
 
    def __iter__(self):
        return iter(self.vertices.values())

def bellman_ford(graph, s):
    distance[s] = 0
    for _ in range(len(g) - 1):
      for v in graph:
        for n in v.get_neighbours():
            distance[n] = min(distance[n], distance[v] + v.get_weight(n))
     return distance       
 
g = Graph()

# from https://gist.github.com/joninvski/701720

################################################
## Floyd-Warshall algorithm </br>
## negative edges, DP algorithm(negative cycle)
## all s to all t: O(n*n*m) for run n time Bellman-Ford algorithm
## O(n*n*n)

# from https://github.com/cy94/floyd-warshall/blob/master/FloydWarshall.py
