class Solution:
    def solve(self, board: List[List[str]]) -> None:
        
        num_rows = len(board)
        num_cols = len(board[0])

        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

        # True if not captured. False if captured by surrounding X
        non_region = [[False for c in range(num_cols)] for r in range(num_rows)]

        # Apply multi-source BFS from border cells
        queue = collections.deque()

        for row in range(num_rows):
            for col in [0, num_cols-1]:
                if board[row][col] == "O":
                    print(f"Updating ({row}, ({col}))")
                    non_region[row][col] = True
                    queue.append((row, col))

        for col in range(num_cols):
            for row in [0, num_rows-1]:
                if board[row][col] == "O" and not non_region[row][col]:
                    print(f"Updating ({row}, ({col}))")
                    non_region[row][col] = True
                    queue.append((row, col))

        while queue:
            curr_row, curr_col = queue.popleft()

            for dr, dc in directions:
                new_row, new_col = curr_row+dr, curr_col+dc

                # boundary check
                if not (0 <= new_row < num_rows and 0 <= new_col < num_cols):
                    continue

                # already visited
                if non_region[new_row][new_col]:
                    continue

                # traverse through Os
                if board[new_row][new_col] == "O":
                    queue.append((new_row, new_col))
                    print(f"Updating ({new_row}, ({new_col}))")
                    non_region[new_row][new_col] = True

        # print non-regions
        # for row in range(num_rows):
        #     for col in range(num_cols):
        #         print(board[row][col], end=" ")
        #     print("")

        # Update the board using non_regions found
        for row in range(num_rows):
            for col in range(num_cols):
                if board[row][col] == "O" and not non_region[row][col]:
                    board[row][col] = "X"

        