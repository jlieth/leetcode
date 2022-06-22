"""
https://leetcode.com/problems/next-permutation/

Runtime: 48 ms, faster than 75.72% of Python3 online submissions for Next Permutation.
Memory Usage: 13.9 MB, less than 79.00% of Python3 online submissions for Next Permutation.
"""
from typing import List


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        if len(nums) == 1:
            return

        # search for the right-most digit that is followed by a larger digit
        swap_idx = None
        for idx1 in range(len(nums) - 1, -1, -1):
            # find the smallest number that is larger than nums[idx1]
            smallest_larger = float("inf")
            smallest_larger_idx = None
            for idx2 in range(idx1 + 1, len(nums)):
                if nums[idx2] <= nums[idx1] or nums[idx2] > smallest_larger:
                    continue
                smallest_larger = nums[idx2]
                smallest_larger_idx = idx2

            # if a digit was found, swap and break
            if smallest_larger_idx is not None:
                swap_idx = idx1
                nums[idx1], nums[smallest_larger_idx] = (
                    nums[smallest_larger_idx],
                    nums[idx1],
                )
                break

        # if a swap was made, do a stupid sort (bubble) of the rest of the array
        if swap_idx is not None:
            while True:
                swapped = False
                for idx in range(swap_idx + 2, len(nums)):
                    if nums[idx - 1] > nums[idx]:
                        nums[idx - 1], nums[idx] = nums[idx], nums[idx - 1]
                        swapped = True
                if not swapped:
                    break

        # if no digit for swapping was found, we should return the lowest
        # possible permutation (which is just the array sorted)
        else:
            nums.sort()
