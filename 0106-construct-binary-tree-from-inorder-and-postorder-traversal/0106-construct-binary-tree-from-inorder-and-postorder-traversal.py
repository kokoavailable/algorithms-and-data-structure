# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not inorder or not postorder:
            return None
        
        in_map = {v: i for i, v in enumerate(inorder)}
        
        def build(in_start, post_start, post_end):
            if post_start > post_end:
                return None
            
            root_val = postorder[post_end]
            root = TreeNode(root_val)
            in_idx = in_map[root_val]
            left_size = in_idx - in_start
            
            root.left = build(in_start, post_start, post_start + left_size - 1)
            root.right = build(in_idx + 1, post_start + left_size, post_end - 1)
            
            return root
        
        return build(0, 0, len(postorder) - 1)
            