class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        result = []
        can_be_reached = set()
        cannot_be_reached = set()

        num_rows = len(heights)
        num_cols = len(heights[0])

        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

        def is_pacific(row: int, col: int):
            return row == 0 or col == 0

        def is_atlantic(row: int, col: int):
            return row == num_rows-1 or col == num_cols-1

        def bfs(row: int, col: int):
            visited = set()
            queue = collections.deque()
            queue.append((row, col))
            visited.add((row, col))

            reached_pacific = False
            reached_atlantic = False

            while queue:
                curr_row, curr_col = queue.popleft()

                # Checking if we can reach both oceans
                if is_pacific(curr_row, curr_col):
                    reached_pacific = True
                if is_atlantic(curr_row, curr_col):
                    reached_atlantic = True

                if reached_pacific and reached_atlantic:
                    return True

                for dr, dc in directions:
                    new_row = curr_row + dr
                    new_col = curr_col + dc
                    
                    # Already visited or not
                    if (new_row, new_col) in visited:
                        continue

                    # Boundary check
                    if not (0 <= new_row < num_rows and 0 <= new_col < num_cols):
                        continue
                    
                    # Only explore if we can move
                    if heights[new_row][new_col] > heights[curr_row][curr_col]:
                        continue
                    
                    # We can explore and it is a point that reaches both ocean
                    if (new_row, new_col) in can_be_reached:
                        return True

                    queue.append((new_row, new_col))
                    visited.add((new_row, new_col))

            return False

        for row in range(num_rows):
            for col in range(num_cols):

                if (row, col) in can_be_reached or (row, col) in cannot_be_reached:
                    continue 

                reached = bfs(row, col)

                if reached:
                    # print(f"Reached from source: ({row}, {col})")
                    result.append((row, col))
                    can_be_reached.add((row, col))

                for dr, dc in directions:
                    new_row = row + dr
                    new_col = col + dc

                    # boundary condition check
                    if not (0 <= new_row < num_rows and 0 <= new_col < num_cols):
                        continue

                    if (new_row, new_col) in can_be_reached or (new_row, new_col) in cannot_be_reached:
                        continue

                    if reached and heights[new_row][new_col] >= heights[row][col]:
                        # print(f"Reached ({new_row}, {new_col}) from neighbor: ({row}, {col})")
                        result.append((new_row, new_col))
                        can_be_reached.add((new_row, new_col))

                    if not reached and heights[new_row][new_col] < heights[row][col]:
                        cannot_be_reached.add((new_row, new_col))



        return result
                

                



