class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        leftIdx = 0
        rightIdx = len(numbers) - 1

        while leftIdx < rightIdx:
            num_sum = numbers[leftIdx] + numbers[rightIdx]
            if num_sum == target:
                return [leftIdx+1, rightIdx+1]
            elif num_sum > target:
                rightIdx -= 1
            elif num_sum < target:
                leftIdx += 1