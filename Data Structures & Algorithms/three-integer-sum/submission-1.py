class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        result = []
        nums.sort()

        for i, a in enumerate(nums):

            if i + 2 > len(nums):
                break

            if i > 0 and nums[i-1] == nums[i]:
                continue

            req_sum = -1 * (a)
            left = i + 1
            right = len(nums) - 1

            while left < right:
                curr_sum = nums[left] + nums[right]

                if curr_sum < req_sum:
                    left += 1
                elif curr_sum > req_sum:
                    right -= 1
                elif curr_sum == req_sum:
                    result.append([a, nums[left], nums[right]])

                    left += 1
                     
                    while left < right and nums[left-1] == nums[left]:
                        left += 1

        return result
