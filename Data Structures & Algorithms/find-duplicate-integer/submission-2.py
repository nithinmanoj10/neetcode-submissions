class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        nums = sorted(nums)
        for i in range(len(nums) - 1):
            curr_num = nums[i]
            next_num = nums[i+1]

            if curr_num == next_num:
                return curr_num