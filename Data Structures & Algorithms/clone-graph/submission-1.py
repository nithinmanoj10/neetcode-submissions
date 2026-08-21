"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:

        if node is None:
            return None

        og_queue = collections.deque()
        clone_queue = collections.deque()

        visited = set()

        og_queue.append(node)
        visited.add(node.val)

        new_clone_node = Node(node.val)
        clone_queue.append(new_clone_node)

        cloned_nodes = {}

        cloned_nodes[new_clone_node.val] = new_clone_node

        while og_queue:
            og_node = og_queue.popleft()
            clone_node = clone_queue.popleft()

            for neighbors in og_node.neighbors:
                if neighbors.val in cloned_nodes:
                    clone_neighbor = cloned_nodes[neighbors.val]
                else:
                    clone_neighbor = Node(neighbors.val)
                    cloned_nodes[neighbors.val] = clone_neighbor

                clone_node.neighbors.append(clone_neighbor)

                if neighbors.val not in visited:
                    og_queue.append(neighbors)
                    visited.add(neighbors.val)
                    clone_queue.append(clone_neighbor)

        print(new_clone_node.neighbors)

        return new_clone_node