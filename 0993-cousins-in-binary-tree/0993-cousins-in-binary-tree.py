# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        def dfs(node, parent, depth, target, info):
            if not node:
                return 0

            if node.val == target:
                info["depth"] = depth
                info["parent"] = parent
                return

            dfs(node.left, node, depth + 1, target, info)
            dfs(node.right, node, depth + 1, target, info)

        x_info = {}
        y_info = {}

        dfs(root, None, 0, x, x_info)
        dfs(root, None, 0, y, y_info)

        return x_info["depth"] == y_info["depth"] and x_info["parent"] != y_info["parent"]