class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []

        def backtrack(curr_permutation: List[int], non_visited_idx: set):
            if len(curr_permutation) == len(nums):
                result.append(curr_permutation.copy())
                return
            
            # branch off into our decisions
            for idx in list(non_visited_idx):
                non_visited_idx.remove(idx)
                curr_val = nums[idx]
                curr_permutation.append(curr_val)

                backtrack(curr_permutation, non_visited_idx)

                curr_permutation.pop()
                non_visited_idx.add(idx)

            return

        non_visited_idx = set()
        for i in range(len(nums)):
            non_visited_idx.add(i)

        backtrack([], non_visited_idx)

        return result