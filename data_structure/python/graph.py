# 그래프는 정점 (Vertex, 노드)와 간선(Edge)로 구성된 자료구조이다.

# 방향과 간선의 가중치 유무에 따라 각 종류들이 나뉜다.

# 그래프 표현 방법.

# 인접 리스트 표현 방식
class Graph:
  def __init__(self):
    self.graph = {}

  def add_edge(self, u, v):
    if u not in self.graph:
      self.graph[u] = []
    self.graph[u].append(v)
    if v not in self.graph:
      self.graph[v] = []

  def __str__(self):
    return str(self.graph)

# {'A': ['B', 'C'], 'B': ['D'], 'C': ['D'], 'D': []}

# 인접 행렬 표현방식 
class GraphMatrix:
  def __init__(self, size):
    # 고정된 크기의 인접 행렬을 사용하여 구현된 그래프로, 초기화시 지정된 정점 수 이상을 추가할 수 없다.
    self.size = size
    self.graph = [[0 for _ in range(size) for _ in range(size)]
    self.vertex_map = {}

  # 인덱스 할당 {'A': 0, 'B': 1, 'C': 2, 'D': 3}
  def add_vertex(self, v):
    self.vertex_map[v] = len(self.vertex_map)

  def add_edge(self, u, v):
    if u in self.vertex_map and v in self.vertex_map:
      self.graph[self.vertex_map[u]][self.vertex_map[v]] = 1
