class Solution:
    def numDecodings(self, s: str) -> int:

        if s[0] == "0":
            return 0

        n = len(s)
        dp = [0] * (n+1)
        dp[-1] = 1

        def is_valid(sub_string: str) -> int:
            num = int(sub_string)
            if num >= 1 and num <= 26:
                return 1
            else:
                return 0

        for i in range(n-1, -1, -1):
            if i == n-1:
                dp[i] = is_valid(s[i])
            elif s[i] == "0":
                dp[i] = 0
            else:
                dp[i] = (is_valid(s[i:i+1]) * dp[i+1]) + (is_valid(s[i:i+2]) * dp[i+2])

        return dp[0]