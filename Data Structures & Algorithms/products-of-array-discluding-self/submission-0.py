class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left_prod = []
        right_prod = []
        result = []

        left_prod_cumm = 1
        right_prod_cumm = 1

        for num in nums:
            left_prod_cumm *= num
            left_prod.append(left_prod_cumm)

        for num in reversed(nums):
            right_prod_cumm *= num
            right_prod.append(right_prod_cumm)

        left_prod.insert(0, 1)
        left_prod.append(1)

        right_prod.insert(0, 1)
        right_prod.append(1)
        right_prod.reverse()

        for i in range(1, len(left_prod) - 1):
            result.append(left_prod[i-1] * right_prod[i+1])

        return result

