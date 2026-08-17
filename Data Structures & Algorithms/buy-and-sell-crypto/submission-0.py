class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buyidx, sellidx = 0, 0
        best_price = 0

        for idx in range(len(prices)):
            sellidx = idx
            best_price = max(best_price, prices[sellidx] - prices[buyidx])

            if prices[idx] < prices[buyidx]:
                buyidx = idx

        return best_price