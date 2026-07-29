class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        num_edges = len(edges)
        if num_edges != n - 1:
            return False

        edge_list = defaultdict(list)
        for src, dst in edges:
            edge_list[src].append(dst)
            edge_list[dst].append(src)

        WHITE = 0
        GRAY = 1
        BLACK = 2

        dfs_res = []
        colours = [WHITE for _ in range(n)]
        is_tree = [True]

        def dfs(source, dfs_res, colours, parent, is_tree):
            # print(f'Inside {source} from {parent}')
            if colours[source] == BLACK:
                return
    
            dfs_res.append(source)
            colours[source] = GRAY

            # print(f'At {source}: {colours}')
            for neigh in edge_list[source]:
                # print(f'Inspecting {neigh} from {source}')
                if colours[neigh] == GRAY and neigh != parent:
                    # print(f'Not a tree source: {source}, neigh: {neigh}, parent:{parent}')
                    is_tree[0] = False
                if colours[neigh] == WHITE:
                    dfs(neigh, dfs_res, colours, source, is_tree)

            colours[source] = BLACK
                

        dfs(0, dfs_res, colours, -1, is_tree)
        print(dfs_res)

        # print(f'Final: {is_tree}')
        return is_tree[0]