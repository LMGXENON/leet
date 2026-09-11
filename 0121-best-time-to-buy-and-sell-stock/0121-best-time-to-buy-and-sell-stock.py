class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_profit = 0
        max_profit = 0

        for i in range(1, len(prices)):
            if prices[i] < prices[min_profit]:
                min_profit = i
            else:
                profit = prices[i] - prices[min_profit]
                max_profit = max(max_profit, profit)

        return max_profit