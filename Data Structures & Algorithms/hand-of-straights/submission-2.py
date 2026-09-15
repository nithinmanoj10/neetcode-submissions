class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False

        # bin count array and min-heap
        hand_count = [0] * (max(hand) + 1)
        min_heap = []

        # O(n)
        for num in hand:
            hand_count[num] += 1
            min_heap.append(num)

        # O(n)
        heapq.heapify(min_heap)

        req_group_count = len(hand) // groupSize
        curr_group_count = 0

        while curr_group_count < req_group_count:
            smallest_hand_num = heapq.heappop(min_heap)
            while hand_count[smallest_hand_num] == 0:
                smallest_hand_num = heapq.heappop(min_heap)

            # create the group
            curr_group_size = 0
            for i in range(groupSize):
                if smallest_hand_num + i >= len(hand_count):
                    break
                if hand_count[smallest_hand_num + i] == 0:
                    return False
                
                hand_count[smallest_hand_num + i] -= 1
                curr_group_size += 1

            if curr_group_size != groupSize:
                return False

            curr_group_count += 1

        return True