from typing import List
from collections import defaultdict
import heapq
class Solution:
    # djikstra's algorithm with k stops condition
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj = defaultdict(list)
        for u,v,w in flights:
            adj[u].append((w,v)) # (cost,destination)
        
        frontiers = [(0,src,0)] # (cost,destination,steps)
        vis = set()
        while frontiers:
            val = heapq.heappop(frontiers)
            if val[1] == dst:
                return val[0]
            vis.add(val[1])
            for c,d in adj[val[1]]:
                if val[2] + 1 > k+1:
                    continue
                heapq.heappush(frontiers,(val[0]+c, d, val[2]+1))
        
        return -1
    
class Solution:
    # bellman's ford
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int: 
        prices = {n:float('inf') for n in range(n)}
        prices[src] = 0
        temp = {n:float('inf') for n in range(n)}
        temp[src] = 0
        k += 1
        while k:
            for u,v,w in flights:
                temp[v] = min(prices[u] + w , temp[v])
                # source dist + weight = new dist (update in temp)
            prices = temp.copy()
            k -= 1
        
        return -1 if prices[dst] == float('inf') else prices[dst]

        

s = Solution()
print(s.findCheapestPrice(4,[[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]],0,3,1))