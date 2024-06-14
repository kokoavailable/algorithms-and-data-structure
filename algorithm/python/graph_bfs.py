from collections import deque

def bfs(graph,start):
  """
  그래프에서 레벨이란 루트로드로부터 해당 노드까지의 간선의 수.
  트리의 bfs와 비슷하게, 같은 레벨부터 순차적으로 탐색한다.
  """
  visited = set() # set을 사용하면 중복 처리가 필요가 없고 요소의 존재 여부를 확인하는 연산이 O(1)의 시간 복잡도를 가진다.
  queue = dequeue([start])
  result = []

  while queue:
    vertex = queue.popleft()
    if vertex not in visited:
      visited.add(vertex)
      result.append(vertex)
      queue.extend([neighbour for neighbour in graph[vertex] if neighbour not in visited])

  return result

