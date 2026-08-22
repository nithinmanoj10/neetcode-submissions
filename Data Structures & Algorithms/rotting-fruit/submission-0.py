class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        num_rows = len(grid)
        num_cols = len(grid[0])

        queue = collections.deque()
        visited = [[False for c in range(num_cols)] for r in range(num_rows)]
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

        result = 0

        # initialize the rotten oranges sources - minute 0
        for row in range(num_rows):
            for col in range(num_cols):
                if grid[row][col] == 2:
                    queue.append((0, row, col))
                    visited[row][col] = True

        while queue:
            minute, curr_row, curr_col = queue.popleft()
            result = max(result, minute)

            for dr, dc in directions:
                new_row = curr_row + dr
                new_col = curr_col + dc

                # boundary check
                if not (0 <= new_row < num_rows and 0 <= new_col < num_cols):
                    continue

                # non-feasible traversal
                if grid[new_row][new_col] in [0, 2] or visited[new_row][new_col]:
                    continue

                # Make traversal
                grid[new_row][new_col] = 2
                queue.append((minute + 1, new_row, new_col))
                visited[new_row][new_col] = True
                
        for r in range(num_rows):
            for c in range(num_cols):
                if grid[r][c] == 1:
                    return -1

        return result

        