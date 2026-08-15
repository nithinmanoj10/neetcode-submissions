# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        nums = []
        heapq.heapify(nums)
        result_head = None
        result_tail = None
        counter = 0

        for head_node in lists:
            heapq.heappush(nums, (head_node.val, counter, head_node))
            counter += 1

        while len(nums) > 0:
            _, _, top_node = heapq.heappop(nums)
            next_node = top_node.next
            top_node.next = None

            if next_node is not None:
                heapq.heappush(nums, (next_node.val, counter, next_node))
                counter += 1

            if result_head is None and result_tail is None:
                result_head = top_node
                result_tail = top_node
            else:
                result_tail.next = top_node
                result_tail = top_node

        return result_head