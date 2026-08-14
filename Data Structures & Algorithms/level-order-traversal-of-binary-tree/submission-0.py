# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        
        level_order_list = []
        curr_level = []
        level_order_stack = deque()

        level_order_stack.append(root)
        level_order_stack.append(None)

        while len(level_order_stack) > 0:
            curr_node = level_order_stack.popleft()

            if curr_node is None:
                level_order_list.append(curr_level)
                curr_level = []
                if len(level_order_stack) > 0:
                    level_order_stack.append(None)
            else:
                curr_level.append(curr_node.val)

                if curr_node.left is not None:
                    level_order_stack.append(curr_node.left)
                if curr_node.right is not None:
                    level_order_stack.append(curr_node.right)
        
        return level_order_list