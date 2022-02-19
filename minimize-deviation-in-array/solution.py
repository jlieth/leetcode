"""
https://leetcode.com/problems/minimize-deviation-in-array/

Runtime: 3549 ms, faster than 5.82% of Python3 online submissions for Minimize Deviation in Array.
Memory Usage: 29.9 MB, less than 41.75% of Python3 online submissions for Minimize Deviation in Array.
"""
from queue import PriorityQueue
from typing import List


class Solution:
    def minimumDeviation(self, nums: List[int]) -> int:
        # multiply odd numbers so we only have even numbers
        for idx, n in enumerate(nums):
            if not n % 2 == 0:
                nums[idx] = n * 2

        nums = sorted(list(set(nums)))
        if len(nums) == 1:
            return 0

        return self.minimize(nums)

    def minimize(self, nums: List[int]) -> int:
        max_n = nums[-1]
        min_n = nums[0]
        min_diff = max_n - min_n

        pq = PriorityQueue()
        for n in nums:
            pq.put(-n)

        while True:
            max_n = -pq.get()
            min_diff = min(min_diff, max_n - min_n)

            # if the highest value is odd, we're done
            if not max_n % 2 == 0:
                break

            # put half the highest value back in queue and update min_n
            pq.put(-max_n // 2)
            min_n = min(min_n, max_n // 2)

        return min_diff
