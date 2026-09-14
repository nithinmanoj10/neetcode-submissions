class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        heapq.heapify(heap)

        for num in nums:
            heapq.heappush(heap, num)

            # The size of the heap is always <= k
            if len(heap) == k + 1:
                heapq.heappop(heap)

        return heap[0]