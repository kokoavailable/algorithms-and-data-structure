# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        
        uni_num = root.val
        
        def dfs(node):
            if not node:
                return True
            
            if node.val != uni_num:
                return False
            

            return dfs(node.left) and dfs(node.right)
            
        return dfs(root)
        
        