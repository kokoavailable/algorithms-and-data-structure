# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # 내가 알고 있어야 하는정보. 왼쪽 노드가 몇개인가, 오른쪽 노드는 몇개인가?
        result = None

        def inorder(node):
            nonlocal result, k
            if not node or result is not None:
                return

            inorder(node.left)
            
            k -= 1
            if k == 0:
                result = node.val
                return
            
            inorder(node.right)


        inorder(root)
        return result