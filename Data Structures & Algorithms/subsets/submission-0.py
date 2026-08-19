class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []

        def dfs(nums, curr_set):
            if len(nums) == 0:
                result.append(curr_set)
                return
            top_val = nums[0]
            dfs(nums[1:], curr_set + [top_val])
            dfs(nums[1:], curr_set)

            return

        dfs(nums, [])

        return result