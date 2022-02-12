"""
https://leetcode.com/problems/word-ladder/

Runtime: 3213 ms, faster than 5.00% of Python3 online submissions for Word Ladder.
Memory Usage: 22.6 MB, less than 5.33% of Python3 online submissions for Word Ladder.
"""
from collections import defaultdict, deque
from typing import List


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordList.append(beginWord)
        length = len(beginWord)

        siblings = defaultdict(list)
        for word in wordList:
            for idx in range(length):
                placeholder = word[:idx] + "_" + word[idx + 1 :]
                siblings[placeholder].append(word)

        # breadth-first search for a ladder
        visited = {}
        queue = deque([(beginWord, 1)])
        while len(queue) > 0:
            word, depth = queue.popleft()

            # if word is endWord, we found the ladder
            if word == endWord:
                return depth

            # add all adjacent words that haven't been visited yet to queue
            for idx in range(length):
                placeholder = word[:idx] + "_" + word[idx + 1 :]
                for x in siblings[placeholder]:
                    if not visited.get(x):
                        queue.append((x, depth + 1))

            # mark current word as visited
            visited[word] = True

        return 0
