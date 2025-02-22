class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
# 중위순회
def morris_traversal(root):
    node = root
    result = []

    while node:
        # 왼쪽 자식이 없는 경우 → 바로 방문하고 오른쪽으로 이동
        if not node.left:
            result.append(node.val)
            node = node.right
        else:
            # 왼쪽 서브트리에서 가장 오른쪽(Tail) 노드를 찾음 (Predecessor)
            predecessor = node.left
            while predecessor.right and predecessor.right != node:
                predecessor = predecessor.right

            # "임시 링크가 없는 경우" → Threading 설정 (임시 링크 생성)
            if predecessor.right is None:
                predecessor.right = node  # 임시 링크 설정
                node = node.left  # 왼쪽으로 이동
            else:
                # "임시 링크를 다시 만난 경우" → 백트래킹 (Threading 해제)
                predecessor.right = None  # 임시 링크 제거 (원래대로 복구)
                result.append(node.val)  # 현재 노드 방문
                node = node.right  # 오른쪽 서브트리로 이동

    return result

def morris_preorder(root):
    node = root
    result = []
    
    while node:
        if not node.left:
            result.append(node.val)  # 왼쪽 자식이 없을 때 방문 (Pre-order)
            node = node.right
        else:
            predecessor = node.left
            while predecessor.right and predecessor.right != node:
                predecessor = predecessor.right
                
            if predecessor.right is None:
                result.append(node.val)  # 스레드 생성할 때 방문 (Pre-order)
                predecessor.right = node
                node = node.left
            else:
                predecessor.right = None
                node = node.right
                
    return result
