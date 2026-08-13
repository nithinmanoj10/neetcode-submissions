# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return None

        bfs_stack = deque()
        bfs_stack.append(root)

        while len(bfs_stack) != 0:
            curr_node = bfs_stack.popleft()

            if curr_node is None:
                continue

            temp = curr_node.left
            curr_node.left = curr_node.right
            curr_node.right = temp

            bfs_stack.append(curr_node.left)
            bfs_stack.append(curr_node.right)

        return root