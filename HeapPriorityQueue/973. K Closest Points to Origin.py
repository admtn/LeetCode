from typing import List
import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dist = [ ( p[0]*p[0]+p[1]*p[1], p) for p in points] # O(n)
        # e.g [ 20,[2,4] , 40,[2,6] ]
        heapq.heapify(dist) # O(n)
        res = [ heapq.heappop(dist)[1] for i in range(k)] # O(k * log n )
        return res

