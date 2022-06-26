"""
https://leetcode.com/problems/first-bad-version/

Runtime: 33 ms, faster than 85.80% of Python3 online submissions for First Bad Version.
Memory Usage: 13.8 MB, less than 60.47% of Python3 online submissions for First Bad Version.
"""


# The isBadVersion API is already defined for you.
def isBadVersion(version: int) -> bool:
    pass


class Solution:
    def firstBadVersion(self, n: int) -> int:
        start = 0
        end = n

        while not start == end:
            middle = start + (end - start) // 2
            if isBadVersion(middle):
                end = middle
            else:
                start = middle + 1

        return start
