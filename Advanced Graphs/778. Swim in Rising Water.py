from typing import List
import heapq
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        minH = [(grid[0][0],0,0)] # each item in the heap is (val,r,c)
        vis = set() # includes nodes visited and frontiers
        vis.add((0,0))
        dir = [[0,1],[0,-1],[1,0],[-1,0]]
        while minH:
            val = heapq.heappop(minH)
            for i,j in dir:
                r,c = val[1]+i,val[2]+j
                if r not in range(len(grid)) or c not in range(len(grid[0])) or (r,c) in vis:
                    continue
                if r == len(grid)-1 and c == len(grid[0])-1:
                    return max(val[0],grid[r][c])
                
                heapq.heappush(minH,(max(val[0],grid[r][c]),r,c))
                vis.add((r,c))
        return grid[0][0]        

class dfs:
    def swimInWater(self, grid: List[List[int]]) -> int:
        # find min val of t so that there exists a path where all vals
        # in the path is less than or equal to t
        # caching doesn't work here because we wont cache the optimal path/

        vis = set()

        def dfs(i,j):
            if i == len(grid)-1 and j == len(grid[0])-1:
                return grid[i][j]
            if i not in range(len(grid)) or j not in range(len(grid[0])) or (i,j) in vis:
                return float('inf')
            vis.add((i,j))
            ans = min(
                dfs(i+1,j),
                dfs(i-1,j),
                dfs(i,j+1),
                dfs(i,j-1)
            )
            vis.remove((i,j))
            return max(ans,grid[i][j])
        return dfs(0,0)
class updatePath:
    def swimInWater(self, grid: List[List[int]]) -> int:
        # find min val of t so that there exists a path where all vals
        # in the path is less than or equal to t
        # caching doesn't work here because we wont cache the optimal path/
        path = [[False]*len(grid[0]) for i in range(len(grid))]
        vis = set()
        def dfs(i,j):
            if i not in range(len(path)) or j not in range(len(path[0])) or (i,j) in vis or not path[i][j]:
                return False
            if i == len(path)-1 and j == len(path[0])-1:
                return True
            
            vis.add((i,j))
            canReach = dfs(i+1,j) or dfs(i-1,j) or dfs(i,j+1) or dfs(i,j-1)
            vis.remove((i,j))
            return canReach

        items = []
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                items.append((grid[i][j],(i,j))) # each items in val is (height, (coordinates i,j))
        heapq.heapify(items)
        while not dfs(0,0):
            val = heapq.heappop(items)
            path[val[1][0]][val[1][1]] = True
        return val[0]


s = Solution()
g = [[0]]
print(s.swimInWater(g))