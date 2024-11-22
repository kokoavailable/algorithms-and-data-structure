# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        
        def postorder(node):
            if not node:
                return
            
            left = postorder(node.left)
            right = postorder(node.right)
            
            if not node.left and not node.right:
                if node.val == 0:
                    return False
                elif node.val == 1:
                    return True
                
            if node.val == 2:
                return left or right
            elif node.val == 3:
                return left and right
            
        return postorder(root)