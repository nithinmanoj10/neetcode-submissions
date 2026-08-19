class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []

        def backtrack(avail_open_count: int, total_open_count: int, curr_parans: str):
            if len(curr_parans) == 2 * n:
                result.append(curr_parans)
                return

            # Two choices to make - whether to add an open or close

            # Choice 1 - add open paranthesis if it allows
            if total_open_count < n:
                backtrack(avail_open_count + 1, total_open_count + 1, curr_parans + "(")

            # Choice 2 - add close paranthesis if it allows
            if avail_open_count > 0:
                backtrack(avail_open_count - 1, total_open_count, curr_parans + ")")

            return

        backtrack(0, 0, "")

        return result