"""
https://leetcode.com/problems/count-and-say/

Runtime: 58 ms, faster than 57.18% of Python3 online submissions for Count and Say.
Memory Usage: 14.6 MB, less than 7.18% of Python3 online submissions for Count and Say.
"""


class Solution:
    def countAndSay(self, n: int) -> str:
        said = "1"
        for _ in range(n - 1):
            said = self.say(said)
        return said

    def say(self, s: str) -> str:
        counter = [{"char": s[0], "count": 0}]
        for char in s:
            prev_char = counter[-1]["char"]
            if char == prev_char:
                counter[-1]["count"] += 1
            else:
                counter.append({"char": char, "count": 1})

        result = "".join(f"{x['count']}{x['char']}" for x in counter)
        return result
