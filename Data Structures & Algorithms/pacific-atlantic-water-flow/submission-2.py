class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        result = []
        num_rows = len(heights)
        num_cols = len(heights[0])

        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

        reachable_pacific = [[False for col in range(num_cols)] for row in range(num_rows)]
        reachable_atlantic = [[False for col in range(num_cols)] for row in range(num_rows)]

        # multi-source BFS from pacific
        pacific_queue = collections.deque()
        for col in range(num_cols):
            pacific_queue.append((0, col))
            reachable_pacific[0][col] = True
        
        for row in range(num_rows):
            pacific_queue.append((row, 0))
            reachable_pacific[row][0] = True

        while pacific_queue:
            curr_row, curr_col = pacific_queue.popleft()

            for dr, dc in directions:
                new_row, new_col = curr_row + dr, curr_col + dc

                # boundary condition check
                if not (0 <= new_row < num_rows and 0 <= new_col < num_cols):
                    continue

                # if already visited, skip
                if reachable_pacific[new_row][new_col]:
                    continue

                # if water can traverse upwards
                if heights[new_row][new_col] >= heights[curr_row][curr_col]:
                    pacific_queue.append((new_row, new_col))
                    reachable_pacific[new_row][new_col] = True
                
        

        # multi-source BFS from atlantic

        atlantic_queue = collections.deque()
        for col in range(num_cols):
            atlantic_queue.append((num_rows-1, col))
            reachable_atlantic[num_rows-1][col] = True
        
        for row in range(num_rows):
            atlantic_queue.append((row, num_cols-1))
            reachable_atlantic[row][num_cols-1] = True

        while atlantic_queue:
            curr_row, curr_col = atlantic_queue.popleft()

            for dr, dc in directions:
                new_row, new_col = curr_row + dr, curr_col + dc

                # boundary condition check
                if not (0 <= new_row < num_rows and 0 <= new_col < num_cols):
                    continue

                # if already visited, skip
                if reachable_atlantic[new_row][new_col]:
                    continue

                # if water can traverse upwards
                if heights[new_row][new_col] >= heights[curr_row][curr_col]:
                    atlantic_queue.append((new_row, new_col))
                    reachable_atlantic[new_row][new_col] = True

        # check cells reachable from both
        for row in range(num_rows):
            for col in range(num_cols):
                if reachable_pacific[row][col] and reachable_atlantic[row][col]:
                    result.append((row, col))

        return result
                

                



