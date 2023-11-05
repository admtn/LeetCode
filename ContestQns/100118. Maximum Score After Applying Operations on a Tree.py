from typing import List
from collections import defaultdict
class Solution:
    def maximumScoreAfterOperations(self, edges: List[List[int]], values: List[int]) -> int:
        # to get healthy(best) from current node, we
        # either take cur node and get healthy result from its child nodes
        # or dont take cur ndoe and get total result from child nodes

        adjList = defaultdict(list)
        for u,v in edges:
            adjList[u].append(v)
            adjList[v].append(u)

        cache_total = {}
        vis_total = set()
        def total(n):
            if n in vis_total:
                return 0
            if n in cache_total:
                return cache_total[n]
            vis_total.add(n)
            cur = 0
            for c in adjList[n]:
                cur += total(c)
            vis_total.discard(n)
            cache_total[n] = cur + values[n]
            return cache_total[n]
        total(0)

        cache_best = {}
        vis_best = set()
        def getBest(n):
            if n in vis_best or (len(adjList[n]) == 1 and adjList[n][0] in vis_best):
                return 0
            if n in cache_best:
                return cache_best[n]

            vis_best.add(n)
            cur, child_total = 0,0
            for c in adjList[n]:
                cur += getBest(c)
                child_total += cache_total[c] if c not in vis_best else 0
            vis_best.discard(n)
            cache_best[n] = max(cur + values[n], child_total)
            return cache_best[n]
        return getBest(0)

            

        
edges = [[7,0],[3,1],[6,2],[4,3],[4,5],[4,6],[4,7]]
values =  [2,16,23,17,22,21,8,6]
# edges = [[0,1],[0,2],[0,3],[2,4],[4,5]]
# values = [5,2,5,2,1,1]
print(Solution().maximumScoreAfterOperations(edges,values))