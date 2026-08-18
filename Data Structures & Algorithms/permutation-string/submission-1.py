class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        k = len(s1)
        left = 0
        right = left + k - 1

        s1_char_count = defaultdict(int)
        window_char_count = defaultdict(int)

        for char in s1:
            s1_char_count[char] += 1

        for i in range(left + k):
            window_char_count[s2[i]] += 1

        while right < len(s2):
            # Check if they are permute strings
            # if yes return true
            # if not slide the fixed window by one

            is_window_match = True
            for char, count in s1_char_count.items():
                if window_char_count[char] != count:
                    is_window_match = False
                    break

            if is_window_match:
                return True

            window_char_count[s2[left]] -= 1
            left += 1
            right += 1
            if right < len(s2):
                window_char_count[s2[right]] += 1

        return False