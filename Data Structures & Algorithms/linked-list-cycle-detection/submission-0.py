# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        fast_ptr = head
        slow_ptr = head

        while True:
            # Move the pointers
            if not fast_ptr:
                return False
            if not slow_ptr:
                return False

            fast_ptr = fast_ptr.next
            
            if not fast_ptr:
                return False

            fast_ptr = fast_ptr.next
            slow_ptr = slow_ptr.next

            if fast_ptr == slow_ptr:
                return True