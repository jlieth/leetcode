"""
https://leetcode.com/problems/decode-string/

Runtime: 29 ms, faster than 94.46% of Python3 online submissions for Decode String.
Memory Usage: 13.8 MB, less than 71.25% of Python3 online submissions for Decode String.
"""


class Solution:
    def decodeString(self, s: str) -> str:
        if s == "" or s.isalpha():
            return s

        # find all alphabetic chars at the beginning of the string
        for char_idx, char in enumerate(s):
            if not char.isalpha():
                break

        result = s[:char_idx]

        # find all numeric chars
        for num_idx, char in enumerate(s[char_idx:]):
            if not char.isnumeric():
                break

        num_start = char_idx
        num_end = num_start + num_idx
        num_str = s[num_start:num_end]
        num = int(num_str)

        # find the closing bracket
        brackets = 1
        bracket_start = num_end
        bracket_end = bracket_start + 1
        while brackets > 0:
            if s[bracket_end] == "[":
                brackets += 1
            elif s[bracket_end] == "]":
                brackets -= 1
            bracket_end += 1

        result += num * self.decodeString(s[bracket_start + 1 : bracket_end - 1])
        result += self.decodeString(s[bracket_end:])
        return result
