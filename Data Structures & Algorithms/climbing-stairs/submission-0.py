class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1

        i = 1
        res, s1, s2 = 0, 1, 1

        while i != n:
            res = s1 + s2
            s1 = s2
            s2 = res
            i += 1

        return res