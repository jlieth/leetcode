"""
https://leetcode.com/problems/longest-palindromic-substring/

Runtime: 2985 ms, faster than 22.48% of Python3 online submissions for Longest Palindromic Substring.
Memory Usage: 14.1 MB, less than 29.29% of Python3 online submissions for Longest Palindromic Substring.
"""
from collections import deque


class Solution:
    def longestPalindrome(self, s: str) -> str:
        length = len(s)

        # fill queue with seeds:
        # each letter in s is a seed
        q = deque((x, x) for x in range(length))

        # two of the same letters are a seed
        for idx in range(length - 1):
            char1 = s[idx]
            char2 = s[idx + 1]
            if char1 == char2:
                q.append((idx, idx + 1))

        longest = 0
        palindrome = ""
        while len(q):
            (start, end) = q.popleft()
            seed_length = end - start + 1

            # update longest if current seed is longer
            if seed_length > longest:
                longest = seed_length
                palindrome = s[start : end + 1]

            # if we're on the edges of the string, we can't add more letters
            if start == 0 or end == length - 1:
                continue

            # check of the letters on both sides of the seed are the same
            char1 = s[start - 1]
            char2 = s[end + 1]
            if char1 == char2:
                q.append((start - 1, end + 1))

        return palindrome
