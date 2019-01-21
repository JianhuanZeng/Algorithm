################################################
# BFS: O(m+n)
## app: shortest path

# https://codereview.stackexchange.com/questions/135156/bfs-implementation-in-python-3
def BFS(G,s): 
  seen, queue = set([s]), collections.deque([s])
  while queue:
    vertex = queue.popleft()
    print(vertex)
    for node in G[vertex]:
      if node not in seen:
        seen.add(node)
        queue.append(node)
   return seen
   
if __name__ == '__main__':
  G = {'A': set(['B', 'C']),
           'B': set(['A', 'D', 'E']),
           'C': set(['A', 'F']),
           'D': set(['B']),
           'E': set(['B', 'F']),
           'F': set(['C', 'E'])}
  BFS(G, 'D')
  
# from https://eddmann.com/posts/depth-first-search-and-breadth-first-search-in-python/
def BFS(G, s):
  seen, queue = set(), [s]
  while queue:
      vertex = queue.pop(0)
      if vertex not in seen:
          seen.add(vertex)
          queue.extend(G[vertex] - seen)
  return seen
    
def bfs_paths(G, s, t):
  queue = [(s,[s])]
  while queue:
    (vertex,path) = queue.pop(0)
    for next in G[vertex]-set(path):
      if next == goal:
        yield path+[next]
      else:
        queue.append((next,path+[next]))        
  
  # shortest path
  def shortest_path():
    try:
      return next(bfs_paths(G, 'A', 'F'))
    except StopIteration:
      return None
################################################
# DFS, O(m+n)
def DFS(G, s):
  seen, stack = set(), [s]
  while stack:
      vertex = stack.pop()
      if vertex not in seen:
          seen.add(vertex)
          stack.extend(G[vertex] - seen)
  return seen


def DFS(G,s,seen=[s]):
    for next in G[vertex]-seen:
      DFS(G,s,seen)
    return seen  
    
################################################
# Connected Component 
## initailize all vertices as unvisited, recursively run DFS
## -app: study spread of disease  
## -app: particle detection

## Strrongly Connected Component 
## - run G and G^r
## - meta-graph: make super vertexes for SCC, O(m+n)
################################################
# Graph Challenge
# bipartitle
# find a cycle
# Eulerian cycle: find a cycle that uses every edge exactly once?
# NP Hamilton cycle/Travel city: find a cycle that uses every vertex exactly once?
# NP are they identical graphs?
# lay out on a plane without edge crossing: DFS


