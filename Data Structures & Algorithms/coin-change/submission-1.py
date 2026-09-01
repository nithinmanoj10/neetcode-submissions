class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        self.sub_probs = {}
        MAX = 1000001

        if amount == 0:
            return 0

        def dfs(value: int) -> int:
            if value in self.sub_probs:
                return self.sub_probs[value]

            res = MAX
            for coin in coins:
                if coin > value:
                    continue
                elif coin == value:
                    return 1
                else:
                    res = min(res, dfs(value-coin))

            self.sub_probs[value] = res + 1
            return res + 1

        result = dfs(amount)

        if result >= MAX:
            return -1

        return result