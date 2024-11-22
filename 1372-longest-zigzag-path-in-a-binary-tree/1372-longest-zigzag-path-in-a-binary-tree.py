# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        max_depth = 0
        
        def dfs(node, prev, depth):
            nonlocal max_depth
            if not node:
                return
            
            max_depth = max(depth, max_depth)
            
            if prev == "left":
                dfs(node.right, "right", depth + 1)
                dfs(node.left, "left", 1)
            if prev == "right":
                dfs(node.left, "left", depth + 1)
                dfs(node.right, "right", 1)
                
        dfs(root, "left", 0)
        dfs(root, "right", 0)
        
        return max_depth
                