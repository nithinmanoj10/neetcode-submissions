class Solution:
    def reverseBits(self, n: int) -> int:
        
        def get_ith_bit(n, i):
            return (n >> i) & 1

        result = 0

        for i in range(32):
            # get the ith bit (0-31)
            ith_bit = get_ith_bit(n, i)
            result |= (ith_bit << (31-i))

        return result