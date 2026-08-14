# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def validate(root, small, large) -> bool:
            if root is None:
                return True

            if root.val <= small or root.val >= large:
                return False

            return validate(root.left, small, root.val) and validate(root.right, root.val, large)

        return validate(root, float("-inf"), float("inf"))