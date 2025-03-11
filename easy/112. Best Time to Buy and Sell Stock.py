class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = prices[0]
        profit = 0
        for i in range(1, len(prices)):
            if prices[i] < buy:
                buy = prices[i]
            # the "buy" is always the smallest one, 
            # but if the latter smaller buy does not have larger profit, we do not update the profit
            elif prices[i] - buy > profit:
                profit = prices[i] - buy
        return profit





