class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        groups = [[] for _ in range(len(nums) + 1)]
        num_group_dict = {}
        result = []

        for num in nums:
            if num not in num_group_dict:
                num_group_dict[num] = 1
            else:
                num_group_dict[num] += 1

        for num, freq in num_group_dict.items():
            groups[freq].append(num)

        for group in reversed(groups):
            while len(group) != 0 and k > 0:
                result.append(group.pop())
                k -= 1

        return result