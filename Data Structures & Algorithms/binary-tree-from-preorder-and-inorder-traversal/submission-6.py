# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        self.idx_map = {num : idx for idx, num in enumerate(inorder)}
        self.preorder_idx = 0

        def dfs(left, right):
            # TODO: Add base case
            if right < left:
                return None

            root_val = preorder[self.preorder_idx]
            root_node = TreeNode(root_val)
            self.preorder_idx += 1

            idx = self.idx_map[root_val]

            root_node.left = dfs(left, idx-1)
            root_node.right = dfs(idx+1, right)

            return root_node
              

        return dfs(0, len(inorder) - 1)    
