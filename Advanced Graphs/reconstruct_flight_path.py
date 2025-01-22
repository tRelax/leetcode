from typing import List
from collections import defaultdict


class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        edges = defaultdict(list)

        for u, v in tickets:
            edges[u].append(v)

        for u in edges:
            edges[u].sort(reverse=True)

        stack = ["JFK"]
        res = []
        while stack:
            curr = stack[-1]
            if edges[curr]:
                stack.append(edges[curr].pop())
            else:
                res.append(stack.pop())

        return res[::-1]


tickets = [["BUF", "HOU"], ["HOU", "SEA"], ["JFK", "BUF"]]
tickets = [["HOU", "JFK"], ["SEA", "JFK"], ["JFK", "SEA"], ["JFK", "HOU"]]
tickets = [["JFK", "KUL"], ["JFK", "NRT"], ["NRT", "JFK"]]

print(Solution().findItinerary(tickets))  # ["JFK", "BUF", "HOU", "SEA"]
