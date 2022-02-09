"""
https://leetcode.com/problems/zigzag-conversion/

Runtime: 76 ms, faster than 58.23% of Python3 online submissions for Zigzag Conversion.
Memory Usage: 14.1 MB, less than 91.05% of Python3 online submissions for Zigzag Conversion.
"""
from math import ceil


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s

        items_per_zig = 2 * numRows - 2
        num_zigs = ceil(len(s) / items_per_zig)

        result = ""
        for row in range(numRows):
            for zig in range(num_zigs):
                # first item in zig
                idx = zig * items_per_zig + row
                if idx < len(s):
                    result += s[idx]

                # middle rows have a second item per zig. idx of second item
                # is (row number) spaces before start of next zig
                if 0 < row < numRows - 1:
                    next_zig_start_idx = (zig + 1) * items_per_zig
                    idx = next_zig_start_idx - row
                    if idx < len(s):
                        result += s[idx]

        return result
