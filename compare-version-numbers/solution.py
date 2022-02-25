"""
https://leetcode.com/problems/compare-version-numbers/

Runtime: 39 ms, faster than 60.20% of Python3 online submissions for Compare Version Numbers.
Memory Usage: 13.9 MB, less than 68.52% of Python3 online submissions for Compare Version Numbers.
"""


class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1 = [int(x) for x in version1.split(".")]
        v2 = [int(x) for x in version2.split(".")]

        # add trailing zeroes to shorter array
        missing = abs(len(v2) - len(v1))
        if len(v1) < len(v2):
            v1 += [0] * missing
        elif len(v2) < len(v1):
            v2 += [0] * missing

        if v1 < v2:
            return -1
        elif v1 > v2:
            return 1
        else:
            return 0
