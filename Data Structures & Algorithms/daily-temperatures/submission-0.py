class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        temp_stack: list[tuple(int, int)] = []
        result: list[int] = [0] * len(temperatures)

        for idx, temp in enumerate(temperatures):
            if len(temp_stack) == 0:
                temp_stack.append(tuple([temp, idx]))
            else:
                while len(temp_stack) != 0 and temp_stack[-1][0] < temp:
                    result[temp_stack[-1][1]] = idx - temp_stack[-1][1]
                    temp_stack.pop()
                temp_stack.append(tuple([temp, idx]))

        return result