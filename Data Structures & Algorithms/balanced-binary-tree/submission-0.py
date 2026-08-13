# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.is_height_balanced = True

        # returns the height of the tree rooted at root and
        # checks the height balancing as well
        def dfs(root) -> int:
            if root is None:
                return 0

            left_height = dfs(root.left)
            right_height = dfs(root.right)

            if abs(left_height - right_height) > 1:
                self.is_height_balanced = False

            return 1 + max(left_height, right_height)

        dfs(root)

        return self.is_height_balanced