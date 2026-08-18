class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""

        left = 0
        right = left + len(t) - 1

        t_char_count = defaultdict(int)
        window_char_count = defaultdict(int)

        min_window_length = len(s) + 1
        result = ""

        for char in t:
            t_char_count[char] += 1
        
        for i in range(right + 1):
            window_char_count[s[i]] += 1

        while right < len(s) and left <= right:
            # check window equality
            is_all_present = True

            for char, count in t_char_count.items():
                if window_char_count[char] < count:
                    is_all_present = False
                    break


            if is_all_present:
                window_length = right - left + 1
                if window_length < min_window_length:
                    min_window_length = window_length
                    result = s[left:right+1]
                window_char_count[s[left]] -= 1
                left += 1
            else:
                right += 1
                if right < len(s):
                    window_char_count[s[right]] += 1

        return result
