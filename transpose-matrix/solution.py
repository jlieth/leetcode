"""
https://leetcode.com/problems/transpose-matrix/

Runtime: 84 ms, faster than 68.17% of Python3 online submissions for Transpose Matrix.
Memory Usage: 14.8 MB, less than 55.33% of Python3 online submissions for Transpose Matrix.
"""
from typing import List


class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        m = len(matrix)
        n = len(matrix[0])

        return [[matrix[row][col] for row in range(m)] for col in range(n)]
