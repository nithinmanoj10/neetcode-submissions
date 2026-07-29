class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sum_dict = dict()

        for idx in range(len(nums)):
            num = nums[idx]

            if num in sum_dict:
                return [sum_dict[num], idx]

            else:
                reference = target - num
                if reference not in sum_dict:
                    sum_dict[reference] = idx