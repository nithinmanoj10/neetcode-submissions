class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Find the pivot, which is the index of the minimum number

        left = 0
        right = len(nums) - 1
        pivot_idx = 0
        min_val = nums[0]

        while left <= right:
            mid = left + int((right - left) / 2)
            if nums[mid] < min_val:
                min_val = nums[mid]
                pivot_idx = mid

            if nums[right] <= nums[mid]:
                left = mid + 1
            else:
                right = mid - 1

        # do binary search on either sides
        left_1 = pivot_idx
        right_1 = len(nums) - 1

        while left_1 <= right_1:
            mid_1 = left_1 + int((right_1 - left_1) / 2)
            if nums[mid_1] == target:
                return mid_1
            elif target > nums[mid_1]:
                left_1 = mid_1 + 1
            else:
                right_1 = mid_1 - 1

        left_2 = 0
        right_2 = pivot_idx - 1

        while left_2 <= right_2:
            mid_2 = left_2 + int((right_2 - left_2) / 2)
            if nums[mid_2] == target:
                return mid_2
            elif target > nums[mid_2]:
                left_2 = mid_2 + 1
            else:
                right_2 = mid_2 - 1

        return -1