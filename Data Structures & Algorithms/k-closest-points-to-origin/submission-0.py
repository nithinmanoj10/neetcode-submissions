class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        points_dist = []
        result = []

        def compute_dist(x, y):
            return math.sqrt((x**2) + (y**2))

        for point in points:
            x, y = point[0], point[1]
            points_dist.append((compute_dist(x,y), x, y))

        heapq.heapify(points_dist)

        count = 0
        while count < k:
            point = heapq.heappop(points_dist)
            result.append([point[1], point[2]])
            count += 1

        return result