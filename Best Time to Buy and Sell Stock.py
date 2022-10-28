from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        day_to_buy = 0
        day_to_sell = 1
        res_profit = 0

        while day_to_sell < len(prices):
            if prices[day_to_buy] < prices[day_to_sell]:
                profit = prices[day_to_sell] - prices[day_to_buy]
                if res_profit < profit:
                    res_profit = profit
            else:
                day_to_buy = day_to_sell
            day_to_sell += 1
        return res_profit