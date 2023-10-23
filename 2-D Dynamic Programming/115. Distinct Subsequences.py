from typing import List
class mySolution:
    def numDistinct(self, s: str, t: str) -> int:

        # returns the number of subsequences of t[j:] in s[i:]
        cache = {}
        def dfs(i,j):
            if j == len(t):
                return 1
            if (i,j) in cache:
                return cache[(i,j)]
            count = 0
            for k in range(i,len(s)):
                if s[k] == t[j]:
                    count += dfs(k+1,j+1)
            cache[(i,j)] = count
            return count
        return dfs(0,0)
    
class Solution:
    def numDistinct(self, s: str, t: str) -> int:

        # returns the number of subsequences of t[j:] in s[i:]
        cache = {}
        def dfs(i,j):
            if j == len(t):
                return 1
            if i == len(s):
                return 0
            if (i,j) in cache:
                return cache[(i,j)]
            
            if s[i] == t[j]:
                cache[(i,j)] = dfs(i+1,j+1) + dfs(i+1,j)
            else:
                cache[(i,j)] = dfs(i+1,j)
            return cache[(i,j)]
        return dfs(0,0)


s = Solution()
print(s.numDistinct("rabbbit","rabbit"))