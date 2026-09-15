class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        char_last_idx = {char : idx for idx, char in enumerate(s)}

        result = []
        start = 0
        end = 0

        for i, char in enumerate(s):
            end = max(end, char_last_idx[char])

            if i == end:
                result.append(end - start + 1)
                start = end + 1

        return result