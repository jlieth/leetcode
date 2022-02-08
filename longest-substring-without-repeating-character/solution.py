"""
https://leetcode.com/problems/longest-substring-without-repeating-characters/

Runtime: 68 ms, faster than 74.80% of Python3 online submissions for Longest Substring Without Repeating Characters.
Memory Usage: 14.1 MB, less than 90.72% of Python3 online submissions for Longest Substring Without Repeating Characters.
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        result = 0

        hashtable = {}
        start_idx = 0
        for end_idx in range(len(s)):
            char = s[end_idx]
            last_seen = hashtable.get(char, -1)
            if last_seen >= start_idx:
                start_idx = last_seen + 1
            hashtable[char] = end_idx

            length = end_idx - start_idx + 1
            result = max(result, length)

        return result
