# 너비 우선 탐색

# 루트노드에서 시작해 인접 노드를 모두 탐색한 후, 다음 레벨로 이동해 그 다음 인접한 노드를 탐색하는 방식으로 진행된다.

class TreeNode:
  def __init__(self, value=0, left=None, right=None):
    self.value = value
    self.left = left
    self.right = right

def bfs(root):
  """
  현재 노드를 큐에 추가한뒤, 그 노드의 자식 노드를 큐에 추가하며, 순차적으로 탐색을 수행한다.
  트리의 레벨에 따라 수평적으로 탐색을 수행하게 된다.
  """
  if root is None:
    return

  queue = deque([root])

  while queue:
    current_node = queue.popleft()
    print(current_node.value, end=' ')

    if current_node.left:
      queue.append(current_node.left)
    if current_node.right:
      queue.append(current_node.right)

if current
