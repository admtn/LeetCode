from typing import List
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        S,T = len(s),len(t)
        cache = {}
        # dfs returns the num of subsequences of t[tI:] in s[sI:]
        def dfs(si,ti):
            if ti == T:
                return 1
            if si == S:
                return 0
            if (si,ti) in cache:
                return cache[(si,ti)]
            
            if s[si] == t[ti]:
                cache[(si,ti)] = dfs(si+1,ti+1) + dfs(si+1,ti)
            else:
                cache[(si,ti)] = dfs(si+1,ti)
            return cache[(si,ti)]
        
        return dfs(0,0)

print(Solution().numDistinct("babgbag","bag"))