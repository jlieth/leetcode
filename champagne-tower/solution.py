"""
https://leetcode.com/problems/champagne-tower/

Runtime: 193 ms, faster than 43.69% of Python3 online submissions for Champagne Tower.
Memory Usage: 14.4 MB, less than 29.61% of Python3 online submissions for Champagne Tower.
"""


class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        glasses = []
        for row_idx in range(query_row + 1):
            row = []
            glasses.append(row)
            for glass_idx in range(row_idx + 1):
                filled = 0
                excess = 0

                # first glass in pyramid has no parents and is directly filled
                if row_idx == 0:
                    filled = poured

                # only glasses with index > 0 have a left parent in the row above
                if glass_idx > 0:
                    left_parent = glasses[row_idx - 1][glass_idx - 1]
                    # add half parent's excess to filled
                    filled += left_parent[1] / 2

                # only glasses with index < row_idx + 1 (i.e. not the last glass)
                # have a right parent
                if glass_idx < row_idx:
                    right_parent = glasses[row_idx - 1][glass_idx]
                    # add half parent's excess to filled
                    filled += right_parent[1] / 2

                if filled > 1:
                    excess = filled - 1
                    filled = 1

                row.append((filled, excess))

        return glasses[query_row][query_glass][0]
