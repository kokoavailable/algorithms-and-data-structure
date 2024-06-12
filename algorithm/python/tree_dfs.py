# 트리 - 깊이 우선 탐색 방식
# 왜 DFS인가? 자식 노드들을 방문하기 전에, 다른 형제노드들을 방문하지 않는다.
# 
class TreeNode:
  def __init__(self, value=0, left=None, right=None):
    self.value = value
    self.left = left
    self.right = right



def preorder_traversal(root):
  """
  전위 순회
  각 노드를 만나자마자 방문하기 떄문에, 새로운 트리에 같은 구조로 노드를 추가할 수 있다. 따라서 복사등의 작업에 적합
  """
  if root:
    print(root.value, end=' ') # 현재노드 방문
    preorder_traversal(root.left) # 왼쪽 자식 방문
    preorder_traversal(root.right) # 오른쪾 자식 방문

# 중위 순회
def inorder_traversal(root):
  """
  중위 순회
  중위 순회의 경우, 이진 탐색트리에서 각 노드가 오름 차순으로 방문되게 된다.

  이는 BST의
  1. 모든 왼쪽 자식 노드의 값이 부모 노드보다 작고,
  2. 모든 오른쪽 자식 노드의 값이 부모 노드의 값보다 크다.
  와 같은 특징 때문이다.
  """
    if root:
        inorder_traversal(root.left)
        print(root.value, end=' ')
        inorder_traversal(root.right)

# 후위 순회
def postorder_traversal(root):
  """
  파일 시스템의 디렉토리와 같은 구조에서, 디렉토의 내부 파일과 서브 디렉토리를 모드 삭제한후 해당 디렉토리를 삭제해야 하는 등의 작업에 유용하다.
  """
    if root:
        postorder_traversal(root.left)
        postorder_traversal(root.right)
        print(root.value, end=' ')
