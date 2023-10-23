from typing import List
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        cache = {}
        def dfs(i,j):
            if i >= len(s) and j >= len(p):
                return True
            if j >= len(p):
                return False
            if i > len(s):
                return False
            if (i,j) in cache:
                return cache[(i,j)]
            
            match = i < len(s) and (s[i] == p[j] or p[j] == '.')
            if j+1 < len(p) and p[j+1] == '*':
                cache[(i,j)] = (
                    # don't use the star, go next
                    dfs(i,j+2) or
                    # using the star to match, can only use if character is matching
                    (match and dfs(i+1,j))
                )
                return cache[(i,j)]
            else:
                if match:
                    cache[(i,j)] = dfs(i+1,j+1)
                    return cache[(i,j)]
                else:
                    cache[(i,j)] = False
                    return False
        return dfs(0,0)

s = Solution()
print(s.isMatch("mississippi","mis*is*p*."))



