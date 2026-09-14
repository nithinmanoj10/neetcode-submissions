class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        result = nums[0]
        curr_subarray_sum = nums[0]

        for num in nums[1:]:
            curr_subarray_sum = max(curr_subarray_sum + num, num)
            result = max(result, curr_subarray_sum)

        return result