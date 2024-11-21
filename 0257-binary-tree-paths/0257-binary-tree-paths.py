# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        
        result = []
        path = []
        
        def dfs(node):
            if not node:
                return
            
            path.append(str(node.val))
            dfs(node.left)
            dfs(node.right)
            
            
            if not node.left and not node.right:
                result.append("->".join(path[:]))
            
            path.pop()
            
            
        dfs(root)
            
            
        return result