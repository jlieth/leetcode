"""
https://leetcode.com/problems/k-diff-pairs-in-an-array/

Runtime: 92 ms, faster than 61.13% of Python3 online submissions for K-diff Pairs in an Array.
Memory Usage: 18.5 MB, less than 5.01% of Python3 online submissions for K-diff Pairs in an Array.
"""
from typing import List


class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        result = 0
        hashtable = {}
        for x in nums:
            y1 = x - k
            y2 = x + k

            found = hashtable.get(y1)
            # candidate found and no such combination counted
            if found and not hashtable.get((x, y1)) and not hashtable.get((y1, x)):
                result += 1
                hashtable[(x, y1)] = True
                hashtable[(y1, x)] = True

            found = hashtable.get(y2)
            # candidate found and no such combination counted
            if found and not hashtable.get((x, y2)) and not hashtable.get((y2, x)):
                result += 1
                hashtable[(x, y2)] = True
                hashtable[(y2, x)] = True

            hashtable[x] = True

        return result
