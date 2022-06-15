"""
https://leetcode.com/problems/longest-string-chain/

Runtime: 381 ms, faster than 29.50% of Python3 online submissions for Longest String Chain.
Memory Usage: 14.4 MB, less than 48.74% of Python3 online submissions for Longest String Chain.
"""
from collections import defaultdict
from typing import List


class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        min_length = 16

        # create a dictionary with word length as key and list of words
        # with that length as value
        by_length = defaultdict(list)
        for word in words:
            length = len(word)
            by_length[length].append(word)
            min_length = min(min_length, length)

        # build a dictionary that has the words as keys and their
        # respective maximum chain length as value
        longest_chain = 1
        chain_length = {}
        # iterate available word lengths from smallest to largest
        for length in sorted(by_length.keys()):
            words = by_length[length]
            # iterate all words of this length
            for word in words:
                # if the words have minimum length, their maximum chain length is 1
                if length == min_length:
                    chain_length[word] = 1
                    continue

                # iterate all words that have a length of one character less
                # these are the possible chain predecessors
                longest_predecessor_chain = 0
                for candidate in by_length[length - 1]:
                    if self.is_predecessor(word, candidate):
                        chain = chain_length[candidate]
                        longest_predecessor_chain = max(
                            longest_predecessor_chain, chain
                        )
                # maxiumum chain length for this word is maximum chain length of all
                # predecessors plus one
                chain_length[word] = longest_predecessor_chain + 1
                longest_chain = max(longest_chain, chain_length[word])

        return longest_chain

    @staticmethod
    def is_predecessor(word: str, candidate: str) -> bool:
        for idx, (char1, char2) in enumerate(zip(word, candidate)):
            # find the first char that is different between both words
            if char1 == char2:
                continue

            # if a different char was found, compare the rest of both words
            return word[idx + 1 :] == candidate[idx:]

        return True
