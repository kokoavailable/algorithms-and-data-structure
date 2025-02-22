# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        def flatten_tree(node):
            if not node:
                return None
            
            # 왼쪽 및 오른쪽 서브트리를 평탄화하고 각각의 꼬리 노드를 가져옴
            left_tail = flatten_tree(node.left)
            right_tail = flatten_tree(node.right)
            
            # 왼쪽 서브트리를 오른쪽으로 이동
            if node.left:
                left_tail.right = node.right  # 왼쪽 서브트리의 꼬리를 원래 오른쪽 서브트리에 연결
                node.right = node.left        # 현재 노드의 오른쪽을 왼쪽 서브트리로 변경
                node.left = None              # 왼쪽 포인터 제거
            
            # 오른쪽 꼬리가 존재하면 반환, 그렇지 않으면 왼쪽 꼬리 또는 현재 노드 반환
            return right_tail or left_tail or node
        
        flatten_tree(root)