class Solution:
    def hammingWeight(self, n: int) -> int:
        result = 0

        # Keep clearing the set one bit till it becomes zero
        while n > 0:
            n = n & (n-1)
            result += 1

        return result