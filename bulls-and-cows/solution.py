"""
https://leetcode.com/problems/bulls-and-cows/

Runtime: 41 ms, faster than 93.48% of Python3 online submissions for Bulls and Cows.
Memory Usage: 13.8 MB, less than 78.80% of Python3 online submissions for Bulls and Cows.
"""
from collections import defaultdict


class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        guesses = defaultdict(lambda: 0)

        bulls = 0
        for x, y in zip(secret, guess):
            if x == y:
                bulls += 1
            else:
                guesses[y] += 1

        cows = 0
        for x, y in zip(secret, guess):
            if x == y:
                continue
            if guesses[x] > 0:
                cows += 1
                guesses[x] -= 1

        return f"{bulls}A{cows}B"
