class Solution:
    def jump(self, nums: List[int]) -> int:
        i = 0
        result = 0

        if len(nums) == 1:
            return 0

        while i < len(nums):
            if i + nums[i] >= len(nums) - 1:
                return result + 1

            max_cov_val = -1
            max_cov_val_idx = -1

            for j in range(1, nums[i] + 1):
                if i + j + nums[i+j] > max_cov_val:
                    max_cov_val = i + j + nums[i+j]
                    max_cov_val_idx = i + j

            i = max_cov_val_idx
            result += 1

        return result