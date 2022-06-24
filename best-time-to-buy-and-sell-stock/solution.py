"""
https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

Runtime: 1428 ms, faster than 54.43% of Python3 online submissions for Best Time to Buy and Sell Stock.
Memory Usage: 25.1 MB, less than 37.57% of Python3 online submissions for Best Time to Buy and Sell Stock.
"""
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = 10**4
        max_profit = 0
        for price in prices:
            profit = price - min_price
            min_price = min(min_price, price)
            max_profit = max(max_profit, profit)
        return max_profit
