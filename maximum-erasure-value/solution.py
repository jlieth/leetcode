"""
https://leetcode.com/problems/maximum-erasure-value/

Runtime: 1287 ms, faster than 92.34% of Python3 online submissions for Maximum Erasure Value.
Memory Usage: 28.1 MB, less than 38.51% of Python3 online submissions for Maximum Erasure Value.
"""
from itertools import accumulate
from typing import List


class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        hashtable = {}
        running_sums = list(accumulate(nums))

        max_sum = 0
        start_idx = 0
        for end_idx, n in enumerate(nums):
            last_seen = hashtable.get(n, -1)

            # number was already seen in current subarray (i.e. is not unique)
            if last_seen >= start_idx:
                # pull up start_idx to after last_seen
                start_idx = last_seen + 1

            if start_idx == 0:
                cur_sum = running_sums[end_idx]
            else:
                cur_sum = running_sums[end_idx] - running_sums[start_idx - 1]
            max_sum = max(max_sum, cur_sum)

            # update last_seen hashtable
            hashtable[n] = end_idx

        return max_sum
