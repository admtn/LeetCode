from typing import List
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        res = 0
        visited = set()

        def dfs(r,c):
            # up down left right
            # not 1, out of range, visited : return 0
            # if not return 1 + dfs udlr
            cur = 0
            if (
                r not in range(len(grid)) or 
                c not in range(len(grid[0])) or 
                grid[r][c] == 0 or 
                (r,c) in visited
                ):
                    return 0
            
            visited.add((r,c))
            directions = [[-1,0],[1,0],[0,-1],[0,1]]
            for i,j in directions:
                cur += dfs(r+i,c+j)
            
            return cur+1
                

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1 and (row,col) not in visited:
                    res = max(dfs(row,col),res)
        return res

s = Solution()
ans = s.maxAreaOfIsland([[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]])
print(ans)