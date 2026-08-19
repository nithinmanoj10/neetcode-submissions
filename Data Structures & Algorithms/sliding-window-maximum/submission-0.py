class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        result = []
        left = right = 0

        # stores indices
        q = collections.deque()
        
        while right < len(nums):

            # add the new element to the monotonically dec. queue
            while q and nums[q[-1]] < nums[right]:
                q.pop()
            q.append(right)

            # remove elements from the start that are no longer part of the window
            while q and q[0] < left:
                q.popleft()

            if right < k-1:
                right += 1
                continue

            result.append(nums[q[0]])

            right += 1
            left += 1

        return result
        
        
