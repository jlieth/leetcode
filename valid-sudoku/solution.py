"""
https://leetcode.com/problems/valid-sudoku/

Runtime: 107 ms, faster than 66.24% of Python3 online submissions for Valid Sudoku.
Memory Usage: 13.9 MB, less than 95.73% of Python3 online submissions for Valid Sudoku.
"""
from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in range(9):
            cells = board[row]
            if not self.isUnique(cells):
                return False

        for col in range(9):
            cells = [row[col] for row in board]
            if not self.isUnique(cells):
                return False

        for box in range(9):
            first_row = (box // 3) * 3
            first_col = (box % 3) * 3
            cells = []
            for i in range(3):
                cells += board[first_row + i][first_col : first_col + 3]
            if not self.isUnique(cells):
                return False

        return True

    def isUnique(self, cells: List[str]) -> bool:
        # filter out empty cells
        cells = list(filter(lambda x: x != ".", cells))

        # cells are unique if length of list is length of set
        return len(cells) == len(set(cells))
