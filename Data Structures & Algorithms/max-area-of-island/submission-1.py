class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        result = 0
        num_rows = len(grid)
        num_cols = len(grid[0])

        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

        # returns the size of the island starting from grid[row][col]
        def dfs(row: int, col: int) -> int:
            if (row < 0 or row == num_rows) or (col < 0 or col == num_cols) or grid[row][col] == 0:
                return 0

            grid[row][col] = 0

            return 1 + dfs(row-1,col) + dfs(row, col+1) + dfs(row+1, col) + dfs(row, col-1)

        for row in range(num_rows):
            for col in range(num_cols):
                if grid[row][col] == 1:
                    size = dfs(row, col)
                    result = max(result, size)

        return result
        