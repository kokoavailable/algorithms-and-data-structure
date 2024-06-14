from collections import deque

def bfs(graph,start):
  visited = set() 
  queue = dequeue([start])
  result = []

  while queue:
    vertex = queue.popleft()
    if vertex not in visited:
      visited.add(vertex)
      result.append(vertex)
      queue.extend([neighbour for neighbour in graph[vertex] if neighbour not in visited])

  return result

