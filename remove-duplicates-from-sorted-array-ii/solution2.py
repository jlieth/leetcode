"""
https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii

Runtime: 48 ms, faster than 97.24% of Python3 online submissions for Remove Duplicates from Sorted Array II.
Memory Usage: 13.9 MB, less than 87.87% of Python3 online submissions for Remove Duplicates from Sorted Array II.
"""
from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        """
        algorithm (two-pointer):
        - initialize var idx as 2 (or smaller if the length of the array is
          smaller, but then the loop won't run at all) since the first two
          values in the array are always valid
        - for-loop with var pointer over range(2, length of array)
        - find a value at num[pointer] that is different from the value
          at num[idx - 2]. since pointer and idx are the same at the start
          of the loop, this will find the first value that is different
          from the current streak of identical numbers.
        - if the value at nums[pointer] is the same, continue the for-loop
        - if the value is different, write it to nums[idx] and increase idx
        """
        length = len(nums)
        idx = min(length, 2)
        for pointer in range(2, length):
            if not nums[idx - 2] == nums[pointer]:
                nums[idx] = nums[pointer]
                idx += 1

        return idx
