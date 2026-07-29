class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        edge_list = defaultdict(list)
        for src, dst in edges:
            edge_list[src].append(dst)
            edge_list[dst].append(src)
        
        visited = [False for _ in range(n)]
        num_cc = 0

        def dfs(source, visited):
            if visited[source]:
                return

            visited[source] = True

            for neigh in edge_list[source]:
                if not visited[neigh]:
                    dfs(neigh, visited)

        for node in range(n):
            if not visited[node]:
                dfs(node, visited)
                num_cc += 1

        return num_cc