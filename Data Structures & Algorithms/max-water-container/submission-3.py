class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_level = 0
        left = 0
        right = len(heights) - 1
        curr_water_level = 0

        def get_water_level(left, right):
            return min(heights[left], heights[right]) * (right - left)

        while left < right:
            # compute current water level
            curr_water_level = get_water_level(left, right)
            max_level = max(max_level, curr_water_level)

            # movement of left and right level
            if heights[left] < heights[right]:
                left += 1
            elif heights[right] < heights[left]:
                right -= 1
            else:
                if heights[left+1] <= heights[right-1]:
                    right -= 1
                elif heights[right-1] < heights[left+1]:
                    left += 1

        return max_level