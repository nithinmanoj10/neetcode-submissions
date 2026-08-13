# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p is None and q is None:
            return True
        if p is None and q is not None:
            return False
        if p is not None and q is None:
            return False

        p_level_nodes = deque()
        q_level_nodes = deque()

        p_level_nodes.append(p)
        q_level_nodes.append(q)

        while len(p_level_nodes) > 0 and len(q_level_nodes) > 0:
            p_top = p_level_nodes.popleft()
            q_top = q_level_nodes.popleft()

            if p_top is None and q_top is not None:
                return False
            if p_top is not None and q_top is None:
                return False
            if p_top is None and q_top is None:
                continue

            if p_top.val != q_top.val:
                return False

            p_level_nodes.append(p_top.left)
            p_level_nodes.append(p_top.right)

            q_level_nodes.append(q_top.left)
            q_level_nodes.append(q_top.right)

        if len(p_level_nodes) != len(q_level_nodes):
            return False

        return True