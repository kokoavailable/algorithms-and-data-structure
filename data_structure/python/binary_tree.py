

class TreeNode:
  """
  계층적 데이터 구조로, 루트 노드와 자식 노드로 구성된다, 각 노드는 자식 노드를 가지며, 자식 노드가 없는 노드는 리프노드 라고 한다.
  이진트리는 루트가 두개의 자식을 가질 수 있다.
  """
  def __init__(self, key):
    self.left = None
    self.right = None
    self.val = key



  """
  이진 탐색 트리. 최악의 경우엔 한쪽으로 치우친 비대칭 트리가 된다. 이렇게 되면 사실상 연결리스트와 유사한 형태가 되어 O(n)의 시간복잡도를 지닌다.
  """
def insert(root, key):
  if root is None:
    return TreeNode(key)
  else:
    if root.val < key:
      root.right = insert(root.right, key)
    else:
      root.left = insert(root.left, key)
  return root

#     50
#    /  \
#   30   70
#  / \   / \
# 20 40 60 80

# inorder(50) 호출
#   inorder(30) 호출
#     inorder(20) 호출
#       왼쪽 자식 None, 아무 일도 안 함
#       print(20), 출력: 20
#       오른쪽 자식 None, 아무 일도 안 함
#     print(30), 출력: 20 30
#     inorder(40) 호출
#       왼쪽 자식 None, 아무 일도 안 함
#       print(40), 출력: 20 30 40
#       오른쪽 자식 None, 아무 일도 안 함
#   print(50), 출력: 20 30 40 50
#   inorder(70) 호출
#     inorder(60) 호출
#       왼쪽 자식 None, 아무 일도 안 함
#       print(60), 출력: 20 30 40 50 60
#       오른쪽 자식 None, 아무 일도 안 함
#     print(70), 출력: 20 30 40 50 60 70
#     inorder(80) 호출
#       왼쪽 자식 None, 아무 일도 안 함
#       print(80), 출력: 20 30 40 50 60 70 80
#       오른쪽 자식 None, 아무 일도 안 함

# 이진트리의 중위 순회
def inorder(root):
  if root:
    inorder(root.left)
    print(root.val, end=' ')
    inorder(root.right)
    
