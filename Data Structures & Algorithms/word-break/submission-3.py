class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        
        # memo[i] : Can the substring s[i:] be segmented properly?
        memo = {}
        t = max([len(word) for word in wordDict])
        print(f"t: {t}")
        word_set = set(wordDict)

        # dfs(i) : Can the substring s[i:] be segmented properly?
        def dfs(i: int) -> bool:
            # print(f"dfs({i})")
            if i in memo:
                return memo[i]

            if i == len(s):
                return True

            result = False

            for offset in range(i, min(len(s), i + t) + 1):
                # print(f"{i}:{offset} {s[i:offset]}")
                if s[i : offset] in word_set:
                    # print(f"Found: {s[i:offset]}")
                    result = result or dfs(offset)

            memo[i] = result
            return result

        return dfs(0)

        