from typing import List
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        R,C = len(grid), len(grid[0])
        cache = {}
        # dfs returns the min cost from current node to goal node
        def dfs(r,c):
            if r == R-1 and c == C-1:
                return grid[R-1][C-1]
            if r not in range(R) or c not in range(C):
                return float('inf')
            if (r,c) in cache:
                return cache[(r,c)]
            cache[(r,c)] = grid[r][c] + min(dfs(r+1,c),dfs(r,c+1))
            return cache[(r,c)]
        return dfs(0,0)
    
grid = [[1,2],[1,1]]
print(Solution().minPathSum(grid))