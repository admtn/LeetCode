from typing import List
from collections import defaultdict
import heapq
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:

        adj = defaultdict(list)
        for u,v,w in times:
            adj[u].append([v,w])
        
        vis = set()
        minH = [(0,k)] # (time,node)
        t = 0
        while minH:
            val = heapq.heappop(minH)
            if val[1] in vis:
                continue
            vis.add(val[1]) # val = [time, node]
            t = max(t,val[0])
            for v,w in adj[val[1]]:
                if v not in vis:
                    heapq.heappush(minH,[w+val[0],v])
        
        return t if len(vis) == n else -1

s = Solution()
print(s.networkDelayTime([[2,1,1],[2,3,1],[3,4,1]],4,2))