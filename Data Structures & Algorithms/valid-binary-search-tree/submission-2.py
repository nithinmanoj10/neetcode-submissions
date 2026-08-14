# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True

        if root.left is not None and root.left.val >= root.val:
            return False

        if root.right is not None and root.right.val <= root.val:
            return False

        # get the smallest element from the right subtree
        smallest = root.right
        if smallest is not None:
            while smallest.left:
                smallest = smallest.left

            if root.val >= smallest.val:
                return False

        # get the largest element from the left subtree

        largest = root.left
        if largest is not None:
            while largest.right:
                largest = largest.right

            if root.val <= largest.val:
                return False

        return self.isValidBST(root.left) and self.isValidBST(root.right)