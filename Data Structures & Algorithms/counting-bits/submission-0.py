class Solution:
    def countBits(self, n: int) -> List[int]:
        def count1Bits(n: int):
            result = 0
            while n > 0:
                result += 1
                n = n & (n-1)
            return result

        result = []
        for i in range(n+1):
            result.append(count1Bits(i))

        return result