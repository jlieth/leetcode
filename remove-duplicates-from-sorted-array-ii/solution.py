"""
https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii

Runtime: 48 ms, faster than 97.23% of Python3 online submissions for Remove Duplicates from Sorted Array II.
Memory Usage: 13.9 MB, less than 96.82% of Python3 online submissions for Remove Duplicates from Sorted Array II.

Note: This is probably a bad solution because I pop elements from the middle
of the list which is not technically an in-place operation (the problem
requires modifying the array in-place).
"""
from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # start at index 2 because the first two items are always valid
        idx = 2
        while True:
            # get number at idx or break if at end of list
            try:
                n = nums[idx]
            except IndexError:
                break

            # remove n from list if it's the same value as previous two
            if n == nums[idx - 1] and n == nums[idx - 2]:
                nums.pop(idx)
                continue

            idx += 1

        return len(nums)
