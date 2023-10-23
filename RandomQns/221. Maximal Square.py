from typing import List
class bruteForce:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        def getSize(r,c):
            size = 1 # the length of the current square
            newR,newC = r+1,c+1 # the corners of the new square to be checked
            while newR in range(len(matrix)) and newC in range(len(matrix[0])):
                if matrix[newR][newC] == '0':
                    return size*size
                for i in range(size):
                    if matrix[newR][c+i] == '0':
                        return size*size
                    if matrix[r+i][newC] == '0':
                        return size*size
                size += 1
                newR = r + size # bottom left
                newC = c + size # top right
            return (size)*(size)
        
        res = 0
        ROW,COL = len(matrix),len(matrix[0])
        for r in range(ROW):
            for c in range(COL):
                if matrix[r][c] == '1':
                    res = max(res,getSize(r,c))
        return res
class td:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        cache = {}
        ROW,COL = len(matrix), len(matrix[0])
        def dfs(r,c):
            if (
                r not in range(ROW) or
                c not in range(COL)
                ):
                return 0 # do we want to cache this?
            if (r,c) in cache:
                return cache[(r,c)]
            cache[(r,c)] = 0
            right = dfs(r,c+1)
            down = dfs(r+1,c)
            diag = dfs(r+1,c+1)
            if matrix[r][c] == '1':
                cache[(r,c)] = 1 + min(right,down,diag)
            return cache[(r,c)]
        dfs(0,0)
        return max(cache.values())**2
class Solution: # bottom up
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        ROW,COL = len(matrix), len(matrix[0])
        dp = [[0]*(COL+1) for i in range(ROW+1)]
        for i in range(COL+1):
            dp[ROW][i] = 0
        for i in range(ROW+1):
            dp[i][COL] = 0
        res = 0
        for r in range(ROW-1,-1,-1):
            for c in range(COL-1,-1,-1):
                dp[r][c] = min(dp[r+1][c],dp[r][c+1],dp[r+1][c+1]) + 1 if matrix[r][c] == '1' else 0
                res = max(res,dp[r][c])
        return res ** 2
        


print(Solution().maximalSquare([["0"],["1"]]))

