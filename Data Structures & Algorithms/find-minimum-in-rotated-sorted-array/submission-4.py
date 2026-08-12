class Solution:
    def findMin(self, nums: List[int]) -> int:
        min_val = nums[0]
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = left + int((right - left) / 2)
            min_val = min(min_val, nums[mid])

            if nums[right] >= nums[mid]:
                right = mid - 1
            else:
                left = mid + 1

        return min_val