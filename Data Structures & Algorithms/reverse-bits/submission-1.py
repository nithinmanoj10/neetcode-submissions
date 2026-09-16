class Solution:
    def reverseBits(self, n: int) -> int:
        def get_last_bit(n: int):
            return n & 1

        bits = []
        result = 0

        for i in range(32):
            bits.append(get_last_bit(n))
            n = n >> 1

        power = 0
        for bit in bits[::-1]:
            result += (bit * (2 ** power))
            power += 1

        return result