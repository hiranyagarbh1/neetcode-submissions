class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        maxprofit = 0
        min_price_so_far = prices[0]

        for price in prices:
            if price < min_price_so_far:
                min_price_so_far = price
            elif price - min_price_so_far > maxprofit:
                maxprofit = price - min_price_so_far

        return maxprofit
