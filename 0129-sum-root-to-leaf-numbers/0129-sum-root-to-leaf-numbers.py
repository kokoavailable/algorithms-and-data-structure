# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        total = 0

        def preorder(node, current):
            nonlocal total
            if not node:
                return

            current = current * 10 + node.val

            if not node.left and not node.right:
                total += current
                return
            preorder(node.left, current)
            preorder(node.right, current)

        preorder(root, 0)
        return total
