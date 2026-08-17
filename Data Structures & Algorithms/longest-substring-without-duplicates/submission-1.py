class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charIdx = {}
        startIdx, endIdx = 0, 0
        longestLength = 0

        while endIdx < len(s):
            next_char = s[endIdx]

            if next_char in charIdx:
                repeatCharIdx = charIdx[next_char]
                while startIdx < repeatCharIdx + 1:
                    del charIdx[s[startIdx]]
                    startIdx += 1
                
            charIdx[next_char] = endIdx
            longestLength = max(longestLength, endIdx - startIdx + 1)

            endIdx += 1

        return longestLength