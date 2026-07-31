class Solution:

    def encode(self, strs: List[str]) -> str:

        encoded_string = ""

        for string in strs:
            str_len = len(string)
            encoded_string += f'{str_len}#{string}'

        return encoded_string

    def decode(self, s: str) -> List[str]:
        curr_len_str: str = ""
        curr_len: int
        idx = 0
        result : List[str] = []

        while idx < len(s):
            char = s[idx]

            if char == "#":
                curr_len = int(curr_len_str)
                curr_str = s[idx + 1 : idx + 1 + curr_len]
                result.append(curr_str)
                idx = idx + 1 + curr_len
                curr_len_str = ""
            else:
                curr_len_str += char
                idx += 1

        return result