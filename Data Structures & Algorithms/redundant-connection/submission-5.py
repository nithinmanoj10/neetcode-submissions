class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        num_nodes = len(edges)

        # Create Union-Find data structure and helper functions
        self.parent = [n for n in range(num_nodes+1)]
        self.rank = [1] * (num_nodes + 1)

        def find(x: int) -> int:
            if self.parent[x] != x:
                self.parent[x] = find(self.parent[x])
            
            return self.parent[x]

        # Return False if part of same group, else union and return True
        def union(x: int, y: int) -> bool:
            root_x = find(x)
            root_y = find(y)

            if root_x == root_y:
                return False

            if self.rank[root_x] > self.rank[root_y]:
                self.parent[root_y] = root_x
            elif self.rank[root_y] > self.rank[root_x]:
                self.parent[root_x] = root_y
            else:
                self.parent[root_y] = root_x
                self.rank[root_x] += 1
            
            return True

        # Use the edges to form groups
        for x, y in edges:
            if not union(x, y):
                return [x, y]



