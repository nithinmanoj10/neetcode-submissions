class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        max_val = max(piles)
        
        k_low = 1
        k_high = max_val
        min_k = k_high

        def compute_eat_time(k):
            time = 0
            for pile in piles:
                time += math.ceil(pile / k)

            return time

        while k_low <= k_high:
            k_mid = k_low + int((k_high - k_low) / 2)
            eat_hrs = compute_eat_time(k_mid)

            if eat_hrs <= h:
                min_k = min(min_k, k_mid)
                k_high = k_mid - 1
            else:
                k_low = k_mid + 1

        return min_k