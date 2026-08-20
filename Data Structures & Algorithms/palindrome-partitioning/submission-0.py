class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result = []

        def is_palindrome(s: str) -> bool:
            return s == s[::-1]

        def backtrack(curr_string: str, substrings: List[str]):
            if len(curr_string) == 0:
                result.append(substrings.copy())
                return

            for idx in range(1, len(curr_string) + 1):
                substring = curr_string[:idx]

                if is_palindrome(substring):
                    substrings.append(substring)
                    backtrack(curr_string[idx:], substrings)
                    substrings.pop()

            return


        backtrack(s, [])

        return result