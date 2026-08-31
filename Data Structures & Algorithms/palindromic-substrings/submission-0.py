class Solution:
    def countSubstrings(self, s: str) -> int:
        
        def countPalindromes(left: int, right: int) -> int:
            result = 0

            while left >= 0 and right < len(s) and s[left] == s[right]:
                result += 1
                left -= 1
                right += 1

            return result

        count = 0

        for i in range(len(s)):

            # form odd length palindromes
            left, right = i, i
            count += countPalindromes(left, right)

            # form even length palindromes
            left, right = i, i+1
            count += countPalindromes(left, right)

        return count