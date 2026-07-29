class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        char_count = dict()

        for char in s:
            if char not in char_count:
                char_count[char] = 1
            else:
                char_count[char] += 1

        for char in t:
            if char not in char_count:
                return False
            else:
                char_count[char] -= 1

        for char, count in char_count.items():
            if count != 0:
                return False

        return True