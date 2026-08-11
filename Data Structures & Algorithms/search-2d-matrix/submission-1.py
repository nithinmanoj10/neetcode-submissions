class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # Find the row that the target could possible be inside
        # If no such row, return False

        nums = None
        row_low = 0
        row_high = len(matrix) - 1

        while row_low <= row_high:
            row_mid = row_low + int((row_high - row_low) / 2)

            if target >= matrix[row_mid][0] and target <= matrix[row_mid][-1]:
                nums = matrix[row_mid]
                break
            elif target < matrix[row_mid][0]:
                row_high = row_mid - 1
            elif target > matrix[row_mid][-1]:
                row_low = row_mid + 1

        if nums is None:
            return False

        # Now apply binary search on the row we just found
        low = 0
        high = len(nums) - 1

        while low <= high:
            mid = low + int((high - low) / 2)

            if nums[mid] == target:
                return True
            elif target > nums[mid]:
                low = mid + 1
            else:
                high = mid - 1

        return False
