"""
https://leetcode.com/problems/isomorphic-strings/

Runtime: 55 ms, faster than 63.54% of Python3 online submissions for Isomorphic Strings.
Memory Usage: 14.2 MB, less than 44.50% of Python3 online submissions for Isomorphic Strings.
"""


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        mapping = {}
        for char1, char2 in zip(s, t):
            previous_mapping = mapping.get(char1, None)
            if previous_mapping is None:
                mapping[char1] = char2
                continue

            if not previous_mapping == char2:
                return False

        # No two characters may map to the same character
        return len(mapping.values()) == len(set(mapping.values()))
