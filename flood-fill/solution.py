"""
https://leetcode.com/problems/flood-fill/

Runtime: 124 ms, faster than 36.55% of Python3 online submissions for Flood Fill.
Memory Usage: 14 MB, less than 89.68% of Python3 online submissions for Flood Fill.
"""
from collections import deque
from typing import List


class Solution:
    def floodFill(
        self, image: List[List[int]], sr: int, sc: int, color: int
    ) -> List[List[int]]:
        m = len(image)
        n = len(image[0])

        visited = {(sr, sc): True}
        q = deque([(sr, sc)])
        while len(q) > 0:
            row, col = q.popleft()
            pixel = image[row][col]

            # find neighbors
            neighbors = [
                (row - 1, col),  # north
                (row + 1, col),  # south
                (row, col + 1),  # east
                (row, col - 1),  # west
            ]
            for nrow, ncol in neighbors:
                # check boundaries
                if not 0 <= nrow < m:
                    continue
                if not 0 <= ncol < n:
                    continue

                # check color
                if not image[nrow][ncol] == pixel:
                    continue

                # check visited
                if visited.get((nrow, ncol), False):
                    continue

                # add to queue
                q.append((nrow, ncol))

                # mark as visited
                visited[(nrow, ncol)] = True

            # change color
            image[row][col] = color

        return image
