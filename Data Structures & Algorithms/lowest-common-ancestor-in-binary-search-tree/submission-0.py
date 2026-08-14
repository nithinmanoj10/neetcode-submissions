# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        
        # if either of them is the root
        if root.val == p.val:
            return root
        if root.val == q.val:
            return root

        # p and q on either sides of the root
        if (p.val < root.val and root.val < q.val) or (q.val < root.val and root.val < p.val):
            return root

        # if p and q are on the left
        if p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        
        # if p and q are on the right
        if p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right, p, q)
            