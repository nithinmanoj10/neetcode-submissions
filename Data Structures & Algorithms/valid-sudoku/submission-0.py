class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def containsDuplicateNumber(nums: List[str]) -> bool:
            nums_set = set()
            for num in nums:
                if num == ".": continue
                if num in nums_set: return True
                else: nums_set.add(num)

        # Check every row for duplicates
        for row in board:
            if containsDuplicateNumber(row):
                return False

        # Check every column for duplicates
        for col_idx in range(9):
            col = []
            for row_idx in range(9):
                col.append(board[row_idx][col_idx])

            if containsDuplicateNumber(col):
                return False

        # Check every sub-box for duplicates
        subBox_center_coords = [
            (1,1), (1,4), (1,7),
            (4,1), (4,4), (4,7),
            (7,1), (7,4), (7,7)
        ]

        for cx, cy in subBox_center_coords:
            subbox = []
            for dx in [-1, 0, 1]:
                for dy in [-1, 0, 1]:
                    subbox.append(board[cx + dx][cy + dy])

            if containsDuplicateNumber(subbox):
                return False

        return True


