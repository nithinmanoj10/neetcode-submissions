# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        # 1. Find length of the two lists, and pad the smallest with 
        #    zero from the left - O(n)
        # 2. Apply the sum, mod, carry operation left to right
        # 3. Store result in an array

        l1_len = 1
        l2_len = 1
        l1_trav = l1
        l2_trav = l2

        while l1_trav.next:
            l1_len += 1
            l1_trav = l1_trav.next

        while l2_trav.next:
            l2_len += 1
            l2_trav = l2_trav.next

        if l1_len < l2_len:
            len_diff = l2_len - l1_len
            while len_diff > 0:
                new_zero_node = ListNode(0)
                l1_trav.next = new_zero_node
                l1_trav = l1_trav.next
                len_diff -= 1
        elif l2_len < l1_len:
            len_diff = l1_len - l2_len
            while len_diff > 0:
                new_zero_node = ListNode(0)
                l2_trav.next = new_zero_node
                l2_trav = l2_trav.next
                len_diff -= 1

        result = []
        carry = 0

        while l1 and l2:
            curr_sum = l1.val + l2.val + carry
            result.append(curr_sum % 10)
            carry = int(curr_sum / 10)

            l1 = l1.next
            l2 = l2.next

        if carry != 0:
            result.append(carry)

        new_number_head = None
        new_number_trav = new_number_head

        for num in result:
            new_node = ListNode(num)

            if not new_number_head:
                new_number_head = new_node
                new_number_trav = new_node
            else:
                new_number_trav.next = new_node
                new_number_trav = new_node

        return new_number_head
