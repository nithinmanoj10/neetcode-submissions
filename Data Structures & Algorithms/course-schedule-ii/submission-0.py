class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        # 1. Traverse the entire edge list to create the adj. list and in-degree node counts
        adj_list = {src : [] for src in range(numCourses)}
        in_deg = [0] * numCourses

        for dst, src in prerequisites:
            adj_list[src].append(dst)
            in_deg[dst] += 1

        # 2. Create a queue of nodes with in-deg zero
        queue = collections.deque()
        for course in range(numCourses):
            if in_deg[course] == 0:
                queue.append(course)

        # 3. Pop each of the zero in-deg nodes, add to result and remove it from the graph
        result = []

        while queue:
            node = queue.popleft()
            result.append(node)

            for dst in adj_list[node]:
                in_deg[dst] -= 1
                if in_deg[dst] == 0:
                    queue.append(dst)

        # 4. Return result accordingly

        if len(result) != numCourses:
            return []

        return result
