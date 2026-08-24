class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # 1. Form the adj. list of the graph
        adj_list = {src: [] for src in range(n)}
        for src, dst in edges:
            adj_list[src].append(dst)
            adj_list[dst].append(src)

        # 2. Run DFS, multiple times to cover the entire graph.
        # The total number of times DFS was run, will be the number of connected components
        result = 0
        visited = set()

        def dfs(root):
            for dst in adj_list[root]:
                if dst not in visited:
                    visited.add(dst)
                    dfs(dst)

        for node in range(n):
            if node not in visited:
                visited.add(node)
                dfs(node)
                result += 1

        return result