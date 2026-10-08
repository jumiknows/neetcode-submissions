class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # smallest value
        cheapest_price = prices[0]
        # highest profit
        profit = 0

        for price in prices:
            cheapest_price = min(cheapest_price, price)

            # take the difference greatest and smallest
            earnings = price - cheapest_price
            profit = max(profit, earnings)

        return profit