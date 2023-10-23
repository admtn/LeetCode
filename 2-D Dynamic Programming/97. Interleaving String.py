class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False
        cache = {}
        def dfs(one,two):
            if (one,two) in cache:
                return cache[(one,two)]
            tr = one + two
            if one == len(s1) and two == len(s2) and tr == len(s3):
                return True
            
            if one < len(s1) and s1[one] == s3[tr] and dfs(one+1,two):
                return True
            if two < len(s2) and s2[two] == s3[tr] and dfs(one,two+1):
                return True
            
            # we only need to cache False results.
            # if True, just straight away return it, no need to cache.
            cache[(one,two)] = False
            return False
                
        return dfs(0,0)
class BottomUp:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False
        dp = [[False] * (len(s2)+1) for i in range(len(s1)+1)]
        dp[len(s1)][len(s2)] = True

        for row in range(len(s1),-1,-1):
            for col in range(len(s2),-1,-1):
                if row < len(s1) and s1[row] == s3[row+col] and dp[row+1][col]:
                    dp[row][col] = True
                if col < len(s2) and s2[col] == s3[row+col] and dp[row][col+1]:
                    dp[row][col] = True
                    
        return dp[0][0]



                
s = BottomUp()
print(s.isInterleave("aabcc","dbbca","aadbbcbcac"))   