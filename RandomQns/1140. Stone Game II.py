from typing import List
class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        
        cache = {}
        # dfs returns the most num that alice can get starting from index L
        def dfs(l,m,alice):
            if l >= len(piles):
                return 0
            if (l,m,alice) in cache:
                return cache[(l,m,alice)]
            if alice:
                res = 0
                for i in range(1,2*m+1):
                    res = max(res, sum(piles[l:l+i])+dfs(l+i,max(i,m),False) )
            else:
                res = float('inf')
                for i in range(1,2*m+1):
                    res = min(res, dfs(l+i,max(i,m),True) )
            cache[(l,m,alice)] = res
            return res
        return dfs(0,1,True)

print(Solution().stoneGameII([1,2,3,4,5,100]))