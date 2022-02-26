"""
https://leetcode.com/problems/shortest-path-visiting-all-nodes/

Runtime: 693 ms, faster than 31.00% of Python3 online submissions for Shortest Path Visiting All Nodes.
Memory Usage: 23.9 MB, less than 21.58% of Python3 online submissions for Shortest Path Visiting All Nodes.
"""
from collections import deque
from typing import List


class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        num_nodes = len(graph)

        # shortest path is zero if we only have one node
        if num_nodes == 1:
            return 0

        queue = deque()
        seen = set()

        # add all nodes as starting nodes to queue
        for idx in range(num_nodes):
            queue.append((idx, {idx}, 0))
            seen.add((idx, tuple({idx})))

        while len(queue):
            current, visited, path_len = queue.popleft()

            for neighbor in graph[current]:
                next_visited = visited.union({neighbor})
                next_path_len = path_len + 1

                # termination: after next step, all nodes have been visited
                if len(next_visited) == num_nodes:
                    return next_path_len

                if (neighbor, tuple(next_visited)) in seen:
                    continue

                queue.append((neighbor, next_visited, next_path_len))
                seen.add((neighbor, tuple(next_visited)))
