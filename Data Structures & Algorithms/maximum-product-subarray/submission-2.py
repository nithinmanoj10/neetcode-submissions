class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        result = nums[0]
        curr_max = 1
        curr_min = 1

        for num in nums:
            temp_max = curr_max
            curr_max = max(num, max(num * curr_max, num * curr_min))
            curr_min = min(num, min(num * temp_max, num * curr_min))

            result = max(result, curr_max)

        return result 