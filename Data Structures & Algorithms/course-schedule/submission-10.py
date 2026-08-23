class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj_list = {node : [] for node in range(numCourses)}

        in_degree_counter = [0] * numCourses
        total_nodes = numCourses
        zero_nodes = collections.deque()

        # Creating the Adj. List and In-degree counter
        # Required - O(n)
        for edge in prerequisites:
            to_node = edge[0]
            from_node = edge[1]
            in_degree_counter[to_node] += 1

            adj_list[from_node].append(to_node)

        # Keep track of zero in-degree nodes
        for node in range(numCourses):
            if in_degree_counter[node] == 0:
                zero_nodes.append(node)

        # Find node with in-degree 0, if none in this iteration return zero
        while total_nodes > 0:
            if len(zero_nodes) == 0:
                return False

            in_deg_zero_node = zero_nodes.popleft()

            # Node with in-degree 0 found, remove it from the graph
            # Required
            for to_node in adj_list[in_deg_zero_node]:
                in_degree_counter[to_node] -= 1
                if in_degree_counter[to_node] == 0:
                    zero_nodes.append(to_node)

            del adj_list[in_deg_zero_node]
            total_nodes -= 1

        return True