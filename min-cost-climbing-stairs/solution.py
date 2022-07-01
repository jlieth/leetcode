"""
https://leetcode.com/problems/min-cost-climbing-stairs/

Runtime: 63 ms, faster than 90.38% of Python3 online submissions for Min Cost Climbing Stairs.
Memory Usage: 13.9 MB, less than 97.20% of Python3 online submissions for Min Cost Climbing Stairs.
"""
from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        for i in range(2, len(cost)):
            cost[i] = min(cost[i - 1], cost[i - 2]) + cost[i]
        return min(cost[-2:])
