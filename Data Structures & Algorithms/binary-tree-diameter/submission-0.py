# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        self.diameter = 0

        # Returns the height of the binary tree rooted at root 
        def dfs(root) -> int:
            if root is None:
                return 0

            left_height = dfs(root.left)
            right_height = dfs(root.right)

            self.diameter = max(self.diameter, left_height + right_height)

            return 1 + max(left_height, right_height)

        height = dfs(root)

        return self.diameter