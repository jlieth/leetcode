"""
https://leetcode.com/problems/4sum-ii/

Runtime: 825 ms, faster than 64.36% of Python3 online submissions for 4Sum II.
Memory Usage: 14.1 MB, less than 99.75% of Python3 online submissions for 4Sum II.
"""
from typing import List


class Solution:
    def fourSumCount(
        self,
        nums1: List[int],
        nums2: List[int],
        nums3: List[int],
        nums4: List[int],
    ) -> int:
        result = 0

        # build a hashmap with sums of first two lists as key and
        # number of occurrence of given key as value
        hashmap = {}
        for i in nums1:
            for j in nums2:
                sum_ = i + j
                try:
                    hashmap[sum_] += 1
                except KeyError:
                    hashmap[sum_] = 1

        # iterate other two lists, summing items in pairs and
        # check whether the negative of the sum is in the hashmap
        for k in nums3:
            for l in nums4:
                sum_ = k + l
                result += hashmap.get(-sum_, 0)

        return result
