from typing import List
class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        cache = {}
        L = len(stoneValue)
        # dfs returns the most value that Alice can get starting from idx i (inclusive)
        def dfs(i,alice):
            if i >= L:
                return 0
            if (i,alice) in cache:
                return cache[(i,alice)]
            
            if alice:
                res = float('-inf')
                stone = 0
                for s in range(3):
                    stone += stoneValue[i+s] if i+s < L else 0
                    res = max(res, stone + dfs(i+s+1,False))
            else:
                res = float('inf')
                for s in range(3):
                    res = min(res,dfs(i+s+1,True))
            cache[(i,alice)] = res
            return res
        
        Alice,half = dfs(0,True), sum(stoneValue)/2
        if Alice > half:
            return "Alice"
        elif Alice < half:
            return "Bob"
        else:
            return "Tie"
class Ssolution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:

        # dfs returns the max amount one can win the other if he starts at index i (inclusive)
        # dfs returns the most optimal value one can get starting from index i
        dp = {}
        L = len(stoneValue)
        def dfs(i):
            if i >= L:
                return 0
            if i in dp:
                return dp[i]
            res = float("-inf")

            for j in range(i,min(i+3,L)):
                res = max(res, sum(stoneValue[i:j+1]) - dfs(j+1) )
            dp[i] = res
            return res
        z = dfs(0)
        return dfs(0)


print(Ssolution().stoneGameIII([0,1,2,3,4,5,6,7]))
