class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Find the pivot, which is the index of the minimum number

        if len(nums) == 1:
            return 0 if nums[0] == target else -1

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

        if pivot_idx == 0:
            low = 0
            high = len(nums) - 1
        elif target >= nums[0] and target <= nums[pivot_idx - 1]:
            low = 0
            high = pivot_idx - 1
        elif target >= nums[pivot_idx] and target <= nums[-1]:
            low = pivot_idx
            high = len(nums) - 1
        else:
            return -1

        while low <= high:
            mid = low + int((high - low) / 2)
            if nums[mid] == target:
                return mid
            elif target > nums[mid]:
                low = mid + 1
            else:
                high = mid - 1

        return -1