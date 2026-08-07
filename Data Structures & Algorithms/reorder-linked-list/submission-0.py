# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        # 1. Find the center and divide into two separate list
        slow_ptr = head
        fast_ptr = head

        while fast_ptr and fast_ptr.next:
            fast_ptr = fast_ptr.next.next
            
            if not fast_ptr:
                continue
            else:
                slow_ptr = slow_ptr.next

        L1 = head
        L2 = slow_ptr.next
        slow_ptr.next = None

        # 2. Reverse the second list L2

        prev = None
        curr = L2

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        L2 = prev

        # 3. Combine the two lists sequentially

        new_head = ListNode()
        trav_ptr = new_head

        while L2:
            temp1 = L1.next
            temp2 = L2.next
            trav_ptr.next = L1
            trav_ptr = trav_ptr.next
            trav_ptr.next = L2
            trav_ptr = trav_ptr.next

            L1 = temp1
            L2 = temp2

        trav_ptr.next = L1

        head = new_head.next




