"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # 1. Create the linked list deep copy without the random pointer
        # 2. Maintain a map of old_node : new_node
        # 3. Map accordingly

        trav_ptr = head
        new_head = None
        new_trav_ptr = new_head

        old_new_map = {}

        while trav_ptr:
            new_node = Node(trav_ptr.val, trav_ptr.next, None)
            if not new_head:
                new_head = new_node
                new_trav_ptr = new_node
            else:
                new_trav_ptr.next = new_node
                new_trav_ptr = new_node
            
            old_new_map[trav_ptr] = new_node
            trav_ptr = trav_ptr.next

        trav_ptr = head
        while trav_ptr:
            if trav_ptr.random == None:
                old_new_map[trav_ptr].random = None
            else:
                old_new_map[trav_ptr].random = old_new_map[trav_ptr.random]
            trav_ptr = trav_ptr.next

        return new_head

        



