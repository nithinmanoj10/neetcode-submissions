class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        num_rows = len(board)
        num_cols = len(board[0])
        visited_cells: List[List[bool]] = [[False for j in range(num_cols)] for i in range(num_rows)]

        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

        def backtrack(row_idx, col_idx, curr_string) -> bool:
            if curr_string == word:
                return True

            visited_cells[row_idx][col_idx] = True

            for dx, dy in directions:
                new_row_idx = row_idx + dy
                new_col_idx = col_idx + dx
                if new_row_idx in range(num_rows) and new_col_idx in range(num_cols) and not visited_cells[new_row_idx][new_col_idx]:
                    result = backtrack(new_row_idx, new_col_idx, curr_string + board[new_row_idx][new_col_idx])

                    if result:
                        return True

            visited_cells[row_idx][col_idx] = False

            return False


        for row in range(num_rows):
            for col in range(num_cols):
                if backtrack(row, col, "" + board[row][col]):
                    return True

        return False
        