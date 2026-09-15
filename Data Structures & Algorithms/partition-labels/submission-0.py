class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        curr_substring_chars = set()
        curr_substring_len = 0
        req_substring_len = 0
        result = []
        i = 0

        char_count = collections.Counter(s)

        while i < len(s):
            char = s[i]

            # forming a new substring
            if curr_substring_len == 0:
                curr_substring_chars.add(char)
                curr_substring_len += 1
                req_substring_len += char_count[char]
                i += 1
                continue

            # if we have made the appropriate substring
            if req_substring_len == curr_substring_len:
                result.append(curr_substring_len)

                curr_substring_chars.clear()
                curr_substring_len = 0
                req_substring_len = 0
            else:
                if char not in curr_substring_chars:
                    curr_substring_chars.add(char)
                    req_substring_len += char_count[char]
                curr_substring_len += 1
                i += 1

        if curr_substring_len > 0:
            result.append(curr_substring_len)

        return result
