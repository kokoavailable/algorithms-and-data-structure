# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        
        def getLeafValues(root):
            
            leaf_values = []

            def dfs(node):
                if node:
                    if not node.left and not node.right:
                        leaf_values.append(node.val)
                    dfs(node.left)
                    dfs(node.right)
                    
            dfs(root)
            return leaf_values
                
        leaf_values1 = getLeafValues(root1)
        leaf_values2 = getLeafValues(root2)
        
        return leaf_values1 == leaf_values2
        
        