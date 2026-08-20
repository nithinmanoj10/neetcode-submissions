class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        result = []

        if len(digits) == 0:
            return result

        digit_letter = {
            "2" : ["a", "b", "c"],
            "3" : ["d", "e", "f"],
            "4" : ["g", "h", "i"],
            "5" : ["j", "k", "l"],
            "6" : ["m", "n", "o"],
            "7" : ["p", "q", "r", "s"],
            "8" : ["t", "u", "v"],
            "9" : ["w", "x", "y", "z"]
        }

        def backtrack(idx: int, curr_string: str):
            if len(curr_string) == len(digits):
                result.append(curr_string)
                return

            for letters in digit_letter[digits[idx]]:
                backtrack(idx + 1, curr_string + letters)

            return

        backtrack(0, "")

        return result