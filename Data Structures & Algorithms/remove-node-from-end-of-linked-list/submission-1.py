# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Step 1 - Find length of the linked list
        length = 0
        trav_ptr = head

        while trav_ptr:
            length += 1
            trav_ptr = trav_ptr.next

        if length == 1:
            return None

        # Step 2 - Traverse to the nth node from the end accordingly
        node_to_del = length - n

        if node_to_del == 0:
            return head.next

        del_node_trav = head
        prev = None
        
        while node_to_del > 0:
            prev = del_node_trav
            del_node_trav = del_node_trav.next
            node_to_del -= 1

        # Step 3 - Remove it
        prev.next = del_node_trav.next
        del_node_trav.next = None

        return head