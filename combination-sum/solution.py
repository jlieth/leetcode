"""
https://leetcode.com/problems/combination-sum/

Runtime: 62 ms, faster than 91.28% of Python3 online submissions for Combination Sum.
Memory Usage: 13.9 MB, less than 97.98% of Python3 online submissions for Combination Sum.
"""
from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.candidates = sorted(candidates, reverse=True)
        self.results = []
        for i, num in enumerate(self.candidates):
            self.comb(i, num, target, [])

        return self.results

    def comb(self, idx: int, num: int, target: int, path: List[int]):
        rest = target - num

        if rest < 0:
            return

        path = path + [num]

        if rest == 0:
            self.results.append(path)
            return

        for i, num in enumerate(self.candidates[idx:]):
            self.comb(idx + i, num, rest, path)
