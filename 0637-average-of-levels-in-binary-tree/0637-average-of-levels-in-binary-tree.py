# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        record = defaultdict(list)
        
        def dfs(node, depth):
            if not node:
                return
            record[depth].append(node.val)
            
            dfs(node.left, depth + 1)
            dfs(node.right, depth + 1)
            
        
        dfs(root, 0)
            
        result = [sum(ls) / len(ls) for ls in record.values()]
        
        return result
