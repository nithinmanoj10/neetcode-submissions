class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        
        num_rows = len(grid)
        num_cols = len(grid[0])
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        queue = collections.deque()

        # stores the source it's closest to if visited, else -1
        visited = [[-1 for c in range(num_cols)] for r in range(num_rows)]

        # def bfs(row: int, col: int):
        #     visited = set()

        #     queue.append((row, col))
        #     visited.add((row, col))

        #     while queue:
        #         c_row, c_col = queue.popleft()

        #         for dr, dc in directions:
        #             n_row = c_row + dr
        #             n_col = c_col + dc

        #             if 0 <= n_row < num_rows and 0 <= n_col < num_cols and (n_row, n_col) not in visited and grid[n_row][n_col] not in [0, -1]:

        #                 if grid[c_row][c_col] + 1 < grid[n_row][n_col]:
        #                     grid[n_row][n_col] = grid[c_row][c_col] + 1
        #                     queue.append((n_row, n_col))
        #                     visited.add((n_row, n_col))
                        

        
        source_count = 0

        for row in range(num_rows):
            for col in range(num_cols):
                if grid[row][col] == 0:
                    queue.append((source_count, row, col))
                    visited[row][col] = source_count
                    source_count += 1

        while queue:
            source, curr_row, curr_col = queue.popleft()

            for dr, dc in directions:
                new_row = curr_row + dr
                new_col = curr_col + dc

                # boundary check
                if not (0 <= new_row < num_rows and 0 <= new_col < num_cols):
                    continue

                # traversal feasibility
                if grid[new_row][new_col] in [-1, 0]:
                    continue

                # if it's part of the current source, update nothing
                if visited[new_row][new_col] == source:
                    continue

                if grid[curr_row][curr_col] + 1 < grid[new_row][new_col]:
                    grid[new_row][new_col] = grid[curr_row][curr_col] + 1
                    queue.append((source, new_row, new_col))
                    visited[new_row][new_col] = source

                






