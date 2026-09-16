class Solution:
    def reverseBits(self, n: int) -> int:
        result = 0

        for i in range(32):
            ith_bit = (n >> i) & 1
            result |= (ith_bit << (31-i))

        return result