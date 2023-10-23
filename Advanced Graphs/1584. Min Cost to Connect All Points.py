from typing import List
import heapq
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # Kruskal's algo
        parent = [i for i in range(len(points))]

        # O(logn)
        def find(x):
            while parent[x] != x:
                x = parent[x]
            return x
        # O(logn)
        def union(x,y):
            parent[find(y)] = find(x)
        
        # O(n^2)
        dist = []
        for i in range(len(points)):
            for j in range(i+1,len(points)):
                p1 = points[i]
                p2 = points[j]
                d = abs(p1[0] - p2[0]) + abs(p1[1]-p2[1])
                dist.append([d,i,j])

        heapq.heapify(dist)
        cost = 0
        edges = 0
        # O(n^2 * logn)
        while edges != len(points)-1:
            d = heapq.heappop(dist)
            if find(d[1]) != find(d[2]):
                union(d[1],d[2])
                cost += d[0]
                edges += 1
        # Overall n^2 log n
        return cost
    
        # dist.sort()
        # cost = 0
        # edges = 0
        # # O(n^2 * logn)
        # for d in dist:
        #     if find(d[1]) != find(d[2]):
        #         union(d[1],d[2])
        #         cost += d[0]
        #         edges += 1
        #         if edges == len(points) - 1:
        #             return cost
        # # Overall n^2 log n
        # return cost

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # Prim's algo
        adj = {i:[] for i in range(len(points))}
        for i in range(len(points)): # O(n^2)
            for j in range(i+1,len(points)):
                d = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                adj[i].append([d,j])
                adj[j].append([d,i])
        
        vis = set()
        minH = []
        vis.add(0)
        for d in adj[0]:
            heapq.heappush(minH,d) # d = [distance to node , node] wrt og

        cost = 0
        # Overall  O( n^2 * logn ) because possible size of minheap == n^2 and pop is logn
        while len(vis) != len(points):
            while minH and minH[0][1] in vis:
                heapq.heappop(minH)

            val = heapq.heappop(minH)
            vis.add(val[1])
            cost += val[0]
            for d in adj[val[1]]:
                if val[1] not in vis:
                    heapq.heappush(minH,d)
        return cost




    
s = Solution()
print(s.minCostConnectPoints([[0,0],[2,2],[3,10],[5,2],[7,0]]))