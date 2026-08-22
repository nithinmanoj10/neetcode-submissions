class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        
        num_rows = len(grid)
        num_cols = len(grid[0])
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        queue = collections.deque()

        def bfs(row: int, col: int):
            visited = set()

            queue.append((row, col))
            visited.add((row, col))

            while queue:
                c_row, c_col = queue.popleft()

                for dr, dc in directions:
                    n_row = c_row + dr
                    n_col = c_col + dc

                    if 0 <= n_row < num_rows and 0 <= n_col < num_cols and (n_row, n_col) not in visited and grid[n_row][n_col] not in [0, -1]:

                        if grid[c_row][c_col] + 1 < grid[n_row][n_col]:
                            grid[n_row][n_col] = grid[c_row][c_col] + 1
                            queue.append((n_row, n_col))
                            visited.add((n_row, n_col))
                        


        for row in range(num_rows):
            for col in range(num_cols):
                if grid[row][col] == 0:
                    bfs(row, col)