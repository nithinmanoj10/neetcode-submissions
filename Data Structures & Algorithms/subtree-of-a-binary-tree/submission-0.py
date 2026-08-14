# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        def isSameTree(tree1, tree2):
            if tree1 is None and tree2 is not None:
                return False
            if tree1 is not None and tree2 is None:
                return False
            if tree1 is None and tree2 is None:
                return True

            print(f'({tree1.val}, {tree2.val})')

            return (tree1.val == tree2.val) and isSameTree(tree1.left, tree2.left) and isSameTree(tree1.right, tree2.right)

        self.is_same_tree = False

        def dfs(root):
            if root is None:
                return

            if isSameTree(root, subRoot):
                self.is_same_tree = True
                return

            dfs(root.left)
            dfs(root.right)

        dfs(root)
        return self.is_same_tree