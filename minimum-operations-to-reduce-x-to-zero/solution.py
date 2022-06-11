"""
https://leetcode.com/problems/minimum-operations-to-reduce-x-to-zero/

Runtime: 1276 ms, faster than 81.46% of Python3 online submissions for Minimum Operations to Reduce X to Zero.
Memory Usage: 35.8 MB, less than 29.58% of Python3 online submissions for Minimum Operations to Reduce X to Zero.
"""
from typing import List


class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        # create a hashtable mapping prefix sum from the back to index
        prefix_sum_hashtable = {}
        prefix_sum = 0
        for idx in range(len(nums) - 1, -1, -1):
            n = nums[idx]
            prefix_sum += n
            if prefix_sum > x:
                break
            prefix_sum_hashtable[prefix_sum] = idx

        # initialize min operations: if a prefix sum of x is found,
        # len(nums) - idx operations need to be made to reach it
        idx = prefix_sum_hashtable.get(x, None)
        if idx is None:
            min_operations = float("inf")
        else:
            min_operations = len(nums) - idx

        # build prefix sum from the front
        prefix_sum = 0
        for idx, n in enumerate(nums):
            prefix_sum += n

            # break loop if prefix sum is greater than target
            if prefix_sum > x:
                break

            # update operations if prefix sum equals target
            if prefix_sum == x:
                operations = idx + 1
                min_operations = min(min_operations, operations)
                continue

            # find required value on the other end
            m = x - prefix_sum
            idx_m = prefix_sum_hashtable.get(m, None)
            if idx_m is None:
                continue
            if idx_m <= idx:
                continue
            operations = idx + 1 + (len(nums) - idx_m)
            min_operations = min(min_operations, operations)

        if min_operations == float("inf"):
            min_operations = -1

        return min_operations
