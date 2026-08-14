# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []

        result = []
        node_stack = deque()

        node_stack.append(root)

        while len(node_stack) > 0:
            result.append(node_stack[-1].val)

            for _ in range(len(node_stack)):
                curr_node = node_stack.popleft()

                if curr_node.left is not None:
                    node_stack.append(curr_node.left)
                if curr_node.right is not None:
                    node_stack.append(curr_node.right)
        
        return result