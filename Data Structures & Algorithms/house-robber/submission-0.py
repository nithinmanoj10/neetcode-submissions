class Solution:
    def rob(self, nums: List[int]) -> int:
        yes_rob = [0] * len(nums)
        no_rob = [0] * len(nums)

        yes_rob[0] = nums[0]
    
        for i in range(1, len(nums)):
            yes_rob[i] = nums[i] + no_rob[i-1]
            no_rob[i] = max(yes_rob[i-1], no_rob[i-1])

        return max(yes_rob[-1], no_rob[-1]) 