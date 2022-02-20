"""
https://leetcode.com/problems/remove-covered-intervals/

Runtime: 121 ms, faster than 60.52% of Python3 online submissions for Remove Covered Intervals.
Memory Usage: 14.5 MB, less than 74.29% of Python3 online submissions for Remove Covered Intervals.
"""
from typing import List


class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        count = len(intervals)

        # sort the intervals so that the highest l_i is first
        intervals = sorted(intervals, key=lambda x: x[0], reverse=True)

        # iterate all intervals
        for idx, x in enumerate(intervals):
            l1, r1 = x
            # compare it to all the intervals after it
            # since we sorted the intervals by descending l_i, only later intervals
            # could contain this one since the l_i of the "outside" interval has to
            # be lesser or equal
            for y in intervals[idx + 1 :]:
                l2, r2 = y
                if x == y:
                    continue
                if l2 <= l1 and r2 >= r1:
                    count -= 1
                    break

        return count
