class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []

        candidates.sort()

        def backtrack(i: int, curr_result: List[int], total: int):
            if total == target:
                result.append(curr_result.copy())
                return

            if total > target or i >= len(candidates):
                return

            top_val = candidates[i]

            # Option 1 - Include the top_val in the sum
            curr_result.append(top_val)
            backtrack(i + 1, curr_result, total + top_val)

            # Option 2 - Don't include the top_val in the sum
            curr_result.pop()
            while i < len(candidates) - 1 and candidates[i] == candidates[i+1]:
                i += 1
            backtrack(i + 1, curr_result, total)

            return

        backtrack(0, [], 0)

        return result