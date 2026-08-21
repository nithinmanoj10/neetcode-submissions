class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        result = 0
        num_rows = len(grid)
        num_cols = len(grid[0])

        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        
        def bfs(row_idx: int, col_idx: int):
            visited = collections.deque()
            grid[row_idx][col_idx] = "0"
            visited.append((row_idx, col_idx))

            while len(visited) > 0:
                row, col = visited.popleft()

                for dx, dy in directions:
                    if row + dy in range(num_rows) and col + dx in range(num_cols) and grid[row+dy][col+dx] == "1":
                        grid[row+dy][col+dx] = "0"
                        visited.append((row+dy, col+dx))

            return

        for row in range(num_rows):
            for col in range(num_cols):
                if grid[row][col] == "1":
                    result += 1
                    bfs(row, col)

        return result