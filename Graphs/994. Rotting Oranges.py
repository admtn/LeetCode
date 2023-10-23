from collections import deque
from typing import List
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        rows,cols = len(grid),len(grid[0])
        fresh = 0
        q = deque()
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 2: q.append((i,j))
                if grid[i][j] == 1: fresh += 1
            
        # if no fresh oranges at all, the condition is immediately satisfied, so return 0 time taken.
        if fresh == 0: return 0
        def bfs():
            n = len(q)
            for i in range(n):
                (r,c) = q.popleft()
                
                directions = [[1,0],[-1,0],[0,1],[0,-1]]
                for u,d in directions:
                    newR = r+u
                    newC = c+d
                    if (
                        newR in range(rows) and
                        newC in range(cols) and
                        grid[newR][newC] == 1
                        ):
                        grid[newR][newC] = 2
                        q.append((newR,newC))
        
        time = 0
        while(q):
            time += 1
            bfs()
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    return -1
        return time-1 # minus 1 because when all oranges have been rottened, 
                        # the frontier rottened oranges are still in the queue and would need +1 time to be popped.
                
s = Solution()
thegrid = [[0,2]]
ans = s.orangesRotting(thegrid)
print(ans)