class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()

        def backtrack(idx: int, curr_subset: List[int]):
            if idx == len(nums):
                result.append(curr_subset.copy())
                return

            # Choices to make - either include or not include

            # Choice 1 - include
            curr_subset.append(nums[idx])
            backtrack(idx + 1, curr_subset)

            # Choice 2 - exclude and make sure to skip all duplicates
            curr_subset.pop()
            while idx < len(nums) - 1 and nums[idx] == nums[idx+1]:
                idx += 1

            backtrack(idx + 1, curr_subset)

            return
            

        backtrack(0, [])

        return result