class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []

        def backtrack(nums: List[int], curr_target: int, curr_result: List[int]):
            if curr_target == 0:
                result.append(curr_result)
                return

            if len(nums) == 0:
                return

            top_val = nums[0]

            if top_val <= curr_target:
                backtrack(nums, curr_target - top_val, curr_result + [top_val])
            
            backtrack(nums[1:], curr_target, curr_result)

            return

        backtrack(nums, target, [])

        return result