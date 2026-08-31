class Solution:
    def longestPalindrome(self, s: str) -> str:
        def getLongestPalindrome(left: int, right: int) -> str:
            result = ""
            while left >= 0 and right < len(s) and s[left] == s[right]:
                result = s[left : right + 1]
                left -= 1
                right += 1

            return result

        result = ""
        result_len = 0

        for i in range(len(s)):
            # checking odd length palindrome
            left, right = i, i
            possible_palindrome = getLongestPalindrome(left, right)

            if len(possible_palindrome) > result_len:
                result_len = len(possible_palindrome)
                result = possible_palindrome

            # checking even length palindrome
            left, right = i, i+1
            possible_palindrome = getLongestPalindrome(left, right)

            if len(possible_palindrome) > result_len:
                result_len = len(possible_palindrome)
                result = possible_palindrome

        return result