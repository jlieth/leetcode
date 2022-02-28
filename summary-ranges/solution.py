"""
https://leetcode.com/problems/summary-ranges/

Runtime: 38 ms, faster than 63.96% of Python3 online submissions for Summary Ranges.
Memory Usage: 13.7 MB, less than 99.05% of Python3 online submissions for Summary Ranges.
"""
from typing import List


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        # hack: append infinity so list is never empty
        nums.append(float("inf"))
        length = len(nums)

        # algorithm: keep track of start and end of ranges.
        # iterate all elements in num[1:], comparing element
        # to previous value. if difference between elements
        # is one, increase end index by one. otherwise, add
        # current range to range array. set start and end
        # indices of new range to current index.
        ranges = []
        start = 0
        end = 0
        for idx in range(1, length):
            current = nums[idx]
            prev = nums[idx - 1]

            # range continues if current value is one greater than previous
            if current == prev + 1:
                end += 1
                continue

            # end of range: add to array
            if start == end:
                ranges.append(str(nums[start]))
            else:
                ranges.append(f"{nums[start]}->{nums[end]}")

            # reset range indices to current index
            start = end = idx

        return ranges
