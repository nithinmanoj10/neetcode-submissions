class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        if k == len(s):
            return len(s)

        left = 0
        right = 0
        char_count = defaultdict(int)
        char_count[s[0]] = 1
        result = 0
        curr_substring_len = 1

        while right < len(s) and left <= right:
            curr_char = s[right]

            max_occurrence = 0
            for char, count in char_count.items():
                max_occurrence = max(max_occurrence, count)

            if curr_substring_len - max_occurrence <= k:
                result = max(result, curr_substring_len)
                right += 1
                if right < len(s):
                    char_count[s[right]] += 1
                curr_substring_len += 1
            else:
                char_count[s[left]] -= 1
                left += 1
                curr_substring_len -= 1
                

        return result
        