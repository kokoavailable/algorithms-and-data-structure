# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        depth_sum = defaultdict(int)
        
        def dfs(node, depth):
            if not node:
                return
            
            depth_sum[depth] += node.val

            dfs(node.left, depth + 1)
            dfs(node.right, depth + 1)
            
        dfs(root, 1)
        
        
        return  max(depth_sum, key=depth_sum.get)
            
            
        