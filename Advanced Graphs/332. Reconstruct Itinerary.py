from typing import List
from collections import defaultdict
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        # goal is to travel along all the edges once
        # for each city, travel its dests in lexical order.
        # if i have unused tickets, and am stuck in a city, backtrack and travel
        # to a different dest.
        # if all paths of that city is invalid, backtrack
        # note: tickets are not unique, there can be duplicates. so we cannot use a set for tixCnt
        adj = defaultdict(list)
        tixCnt = defaultdict(int)
        tickets.sort()
        for u,v in tickets:
            adj[u].append(v)
            tixCnt[(u,v)] += 1

        res = []
        usedTix = 0
        def dfs(city):
            nonlocal usedTix
            res.append(city)
            if usedTix == len(tickets):
                return True
            for dest in adj[city]:
                if tixCnt[(city,dest)] > 0:
                    usedTix += 1
                    tixCnt[(city,dest)] -= 1
                    if dfs(dest):
                        return res
                    usedTix -= 1
                    tixCnt[(city,dest)] += 1
            res.pop()
        dfs("JFK")
        return res


class beast:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = defaultdict(list)
        for a,b in sorted(tickets)[::-1]:
            graph[a].append(b)

        path = []
        def dfs(cur):
            while graph[cur]:
                dfs(graph[cur].pop())
                
            path.append(cur)
        
        dfs("JFK")
        return path[::-1]
        

# HierHolzers algorithm
# Greedy DFS, build route backwards when retreating
# Good video: https://www.youtube.com/watch?v=8MpoO2zA2l4&t=644s&ab_channel=WilliamFiset
# Time O(v)
s = Solution()
a = [["EZE","AXA"],["TIA","ANU"],["ANU","JFK"],["JFK","ANU"],["ANU","EZE"],["TIA","ANU"],["AXA","TIA"],["TIA","JFK"],["ANU","TIA"],["JFK","TIA"]]
print(s.findItinerary(a))
