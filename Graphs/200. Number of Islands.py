from typing import List
from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        islands = 0
        numRows = len(grid)
        numCols = len(grid[0])
        visited = set()
        q = deque()

        def bfs(row,col):
            q.append((row,col))
            while q:
                (r,c) = q.popleft()
                udlr = [[-1,0],[1,0],[0,-1],[0,1]] # Up Down Left Right
                for vertical,horizontal in udlr:

                    (adjR,adjC) = (r+vertical,c+horizontal)
                    if (                            # if new calcualted node is in the grid
                        adjR in range(numRows) 
                        and adjC in range(numCols)
                        and grid[adjR][adjC] == "1"
                        and (adjR,adjC) not in visited
                        ): 
                        q.append((adjR,adjC))
                        visited.add((adjR,adjC))

        for row in range(numRows):
            for col in range(numCols):
                if grid[row][col] == "1" and (row,col) not in visited:
                    visited.add((row,col))
                    islands += 1
                    bfs(row,col)
                    


        return islands
o = Solution()
ans = o.numIslands([
["1","1","1"],
["0","1","0"],
["1","1","1"]
])

print(ans)