class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # Find the row that the target could possible be inside
        # If no such row, return False

        nums = None

        for row in matrix:
            if target >= row[0] and target <= row[-1]:
                nums = row
                break

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
