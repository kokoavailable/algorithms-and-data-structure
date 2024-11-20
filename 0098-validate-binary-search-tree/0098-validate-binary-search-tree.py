# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        prev = None
        
        def inorder(node):
            nonlocal prev
            if not node:  # 현재 노드가 None이면 True 반환
                return True
            
            if not inorder(node.left):
                return False
            if prev is not None and node.val <= prev:
                return False
            prev = node.val
            if not inorder(node.right):
                return False
            
            return True     
            
        return inorder(root)