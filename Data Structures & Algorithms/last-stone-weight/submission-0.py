class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        neg_stones = [-stone for stone in stones]
        heapq.heapify(neg_stones)

        while len(neg_stones) > 1:
            first_heavy = -1 * heapq.heappop(neg_stones)
            second_heavy = -1 * heapq.heappop(neg_stones)

            if first_heavy == second_heavy:
                continue
            
            heapq.heappush(neg_stones, -1 * abs(first_heavy - second_heavy))

        if len(neg_stones) == 1:
            return -1 * neg_stones[0]

        return 0