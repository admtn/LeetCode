from typing import List
from math import ceil,floor
class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        half = sum(stones)/2
        C = floor(half)+1 # num cols
        R = len(stones)+1 # num rows
        dp = [[0]*C for i in range(R)]
        for r in range(1,R):
            for c in range(1,C):
                cur = stones[r-1]
                if c >= stones[r-1]:
                    dp[r][c] = max(dp[r-1][c], cur + dp[r-1][c-cur])
                else:
                    dp[r][c] = dp[r-1][c]
        for r in dp:
            print(r)
        return sum(stones) - 2 * dp[R-1][C-1]
class sSolution:
    def lastStoneWeightII(self, stones: List[int]) -> int:

        # dfs returns the max value given a capacity and the stones available
        total = sum(stones)
        half = total/2
        cap = floor(half)
        L = len(stones)
        dp = {}
        def dfs(i,c):
            if c < 0 or i == -1:
                return 0
            if (i,c) in dp:
                return dp[(i,c)]
            
            dp[(i,c)] = max(stones[i]+dfs(i-1,c-stones[i]),dfs(i-1,c)) if c >= stones[i] else dfs(i-1,c)
            return dp[(i,c)]
        
        return total- 2*dfs(L-1,cap)
        

print(sSolution().lastStoneWeightII([31,26,33,21,40]))