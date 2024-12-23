class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        hold = -prices[0]
        cash = 0

        for i in range(1, len(prices)):
            hold = max(hold, cash - prices[i])
            cash = max(cash, hold + prices[i] - fee)

        return cash