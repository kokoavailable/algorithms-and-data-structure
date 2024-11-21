# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        total = 0
        
        
        def dfs(node, parent):
            nonlocal total
            
            if not node:
                return
            
            dfs(node.left, node)
            dfs(node.right, node)
            
            if parent.left == node and not node.left and not node.right:
                total += node.val
                
        dfs(root, root)
                
        return total
            
                
                
            
            