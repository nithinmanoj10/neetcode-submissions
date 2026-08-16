# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        self.result = ""

        def dfs_serialize(root):
            if root is None:
                self.result += "N#"
                return

            self.result += f"{root.val}#"
            dfs_serialize(root.left)
            dfs_serialize(root.right)

        dfs_serialize(root)
        print(self.result)

        return self.result

    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if data == "":
            return None

        preorder_list = deque()
        curr_num = ""

        for char in data:
            if char == "#":
                if curr_num == "N":
                    preorder_list.append(None)
                else:
                    preorder_list.append(int(curr_num))
                curr_num = ""
                continue
            
            curr_num += char

        # print(preorder_list)
        
        def dfs_deserialize():
            curr_val = preorder_list.popleft()
            if curr_val == None:
                return None

            curr_node = TreeNode(curr_val)
            curr_node.left = dfs_deserialize()
            curr_node.right = dfs_deserialize()

            return curr_node

        return dfs_deserialize()
            






