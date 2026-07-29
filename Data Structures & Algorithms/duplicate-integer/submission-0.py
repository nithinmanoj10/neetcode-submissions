class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        num_tracker = set()
        for num in nums:
            if num in num_tracker:
                return True
            num_tracker.add(num)

        return False