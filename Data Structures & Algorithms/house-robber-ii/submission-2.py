class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        if len(nums) == 2:
            return max(nums[0], nums[1])

        # scenario of not including the first house
        result_1 = [0] * len(nums)
        result_1[1] = nums[1]

        # scenario of including the first house
        result_2 = [0] * len(nums)
        result_2[0] = nums[0]
        result_2[1] = max(nums[0], nums[1])
        
        for i in range(2, len(nums)):
            result_1[i] = max(result_1[i-1], nums[i] + result_1[i-2])
            result_2[i] = max(result_2[i-1], nums[i] + result_2[i-2])

        return max(result_1[-1], result_2[-2])