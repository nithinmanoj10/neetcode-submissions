# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        level_stack = deque()
        level_stack.append(root)
        level_stack.append(None)

        max_depth = 0

        while len(level_stack) != 0:
            top_node = level_stack.popleft()

            if top_node is None:
                max_depth += 1
                if len(level_stack) == 0:
                    continue
                level_stack.append(None)
            else:
                if top_node.left is not None:
                    level_stack.append(top_node.left)
                if top_node.right is not None:
                    level_stack.append(top_node.right)

        return max_depth

            

            