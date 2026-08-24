class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # 1. Form an adj list
        adj_list = {src : [] for src in range(n)}
        for src, dst in edges:
            adj_list[src].append(dst)
            adj_list[dst].append(src)

        # 2. Apply DFS starting from any node. Keep a Visited nodes set. If we encounter any node that
        # is already visited, that means we have encountered a cycle

        visited = set()
        self.has_no_cycle = True

        def dfs(root, parent):
            # print(f"dfs({root}, {parent})")
            for dst in adj_list[root]:
                # print(f"({root}, {dst})")
                if dst == parent: 
                    continue
                
                if dst in visited:
                    # print(f"{dst} in visited from {root}")
                    self.has_no_cycle = False
                    return

                visited.add(dst)
                dfs(dst, root)

            return

        visited.add(0)
        dfs(0, -1)

        # For a tree, it should not have cycles and it should be all connected
        is_connected = True if len(visited) == n else False

        return self.has_no_cycle and is_connected