"""
https://leetcode.com/problems/number-of-islands/

Runtime: 313 ms, faster than 91.40% of Python3 online submissions for Number of Islands.
Memory Usage: 16.1 MB, less than 97.31% of Python3 online submissions for Number of Islands.
"""
from collections import deque
from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        self.grid = grid
        self.m = len(grid)
        self.n = len(grid[0])

        count = 0
        for row_idx, row in enumerate(grid):
            for col_idx, col in enumerate(row):
                if col == "0":
                    continue
                count += 1
                self.floodfill(row_idx, col_idx)

        return count

    def floodfill(self, start_row: int, start_col: int):
        self.grid[start_row][start_col] = "0"
        q = deque([(start_row, start_col)])
        while len(q) > 0:
            row, col = q.popleft()
            neighbors = [
                (row - 1, col),  # north
                (row + 1, col),  # south
                (row, col + 1),  # east
                (row, col - 1),  # west
            ]
            for nrow, ncol in neighbors:
                # check boundaries
                if not 0 <= nrow < self.m:
                    continue
                if not 0 <= ncol < self.n:
                    continue

                # check land or water
                if self.grid[nrow][ncol] == "0":
                    continue

                # set to water
                self.grid[nrow][ncol] = "0"

                # add neighbor to queue
                q.append((nrow, ncol))
