class Solution:
    def canJump(self, nums: List[int]) -> bool:
        i = 0

        while i < len(nums):

            if nums[i] == 0:
                break

            if i + nums[i] >= len(nums) - 1:
                i = len(nums) - 1
                break

            max_jump_cov = -1
            max_jump_cov_idx = -1
            for j in range(1, nums[i] + 1):
                if i+j < len(nums) and (i + j + nums[i+j]) > max_jump_cov:
                    max_jump_cov = i + j + nums[i+j]
                    max_jump_cov_idx = i+j

            i = max_jump_cov_idx

        return i == (len(nums) - 1)
