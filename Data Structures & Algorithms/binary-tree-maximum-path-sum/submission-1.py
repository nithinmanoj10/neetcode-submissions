# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.max_path_sum = root.val

        def dfs(root):
            if root is None:
                return 0

            left_val = dfs(root.left)
            right_val = dfs(root.right)

            A = root.val + left_val
            B = root.val + right_val
            C = root.val + left_val + right_val

            self.max_path_sum = max([A, B, C, self.max_path_sum])

            if A < 0 and B < 0:
                return 0

            return max(A, B)

        dfs(root)

        return self.max_path_sum

