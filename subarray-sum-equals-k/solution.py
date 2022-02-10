"""
https://leetcode.com/problems/subarray-sum-equals-k/

Runtime: 276 ms, faster than 63.16% of Python3 online submissions for Subarray Sum Equals K.
Memory Usage: 16.6 MB, less than 76.55% of Python3 online submissions for Subarray Sum Equals K.
"""
from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        result = 0
        hashtable = {0: 1}
        sum_ = 0
        for n in nums:
            sum_ += n

            diff = sum_ - k
            result += hashtable.get(diff, 0)

            try:
                hashtable[sum_] += 1
            except KeyError:
                hashtable[sum_] = 1

        return result
