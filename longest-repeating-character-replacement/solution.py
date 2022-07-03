"""
https://leetcode.com/problems/longest-repeating-character-replacement/

Runtime: 131 ms, faster than 88.85% of Python3 online submissions for Longest Repeating Character Replacement.
Memory Usage: 13.9 MB, less than 93.18% of Python3 online submissions for Longest Repeating Character Replacement.
"""
from collections import defaultdict


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        letters = defaultdict(lambda: 0)
        start = 0
        longest = 0
        for end, char in enumerate(s):
            # add current char
            letters[char] += 1

            # update longest count if current substring is viable
            length = end - start + 1
            if length - max(letters.values()) <= k:
                longest = max(longest, length)

            # if the substring is not viable, remove the first char
            else:
                first_char = s[start]
                letters[first_char] -= 1
                if letters[first_char] == 0:
                    del letters[first_char]
                start += 1

        return longest
