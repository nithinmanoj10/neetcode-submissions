class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        result = 0
        num_rows = len(grid)
        num_cols = len(grid[0])

        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

        # returns the size of the island starting from grid[row][col]
        def bfs(row: int, col: int) -> int:
            size = 0

            queue = collections.deque()
            size += 1
            grid[row][col] = 0
            queue.append((row, col))

            while queue:
                curr_row, curr_col = queue.popleft()
                
                for dr, dc in directions:
                    new_row = curr_row + dr
                    new_col = curr_col + dc

                    if 0 <= new_row < num_rows and 0 <= new_col < num_cols and grid[new_row][new_col] == 1:
                        size += 1
                        grid[new_row][new_col] = 0
                        queue.append((new_row, new_col))

            return size


        for row in range(num_rows):
            for col in range(num_cols):
                if grid[row][col] == 1:
                    size = bfs(row, col)
                    result = max(result, size)

        return result
        