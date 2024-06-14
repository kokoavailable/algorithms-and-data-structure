def dfs_stack(graph, start):
  """
  스택을 이용한 dfs
  """
  visited = set()
  stack = [start]
  result = []

  while stack:
    vertex = stack.pop()
    if vertex not in visited:
      visited.add(vertex)
      result.append(vertex)
      stack.extend([neighbour for neighbour in graph[vertex] if neighbour not in visited]) # 인접리스트가 어떤 순서로 정렬돼 있냐에 따라서 순회 순서가 달라진다.
      # stack.extend(reversed([neighbour for neighbour in graph[vertex] if neighbour not in visited]))

  return result

def dfs_recursive(graph, start, visited=None, result=None)
  if visited is None:
      visited = set()  # 방문한 노드를 저장할 집합을 초기화합니다.
  if result is None:
      result = []  # 방문 순서를 저장할 리스트를 초기화합니다.

  visited.add(start)
  result.append(start)

  for neighbour in graph[start]:
    if neighbour not in visited:
      dfs_recursive(graph, neighbour, visited, result)

  return result
  
