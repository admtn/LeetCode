from typing import List
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        if len(word1) < len(word2): # word1 is always longer
            word1,word2 = word2,word1
        dp = {}
        def dfs(i,j):
            if i == len(word1) and j == len(word2): # if all matched
                return 0
            if j == len(word2): # if match all and still have chars left, delete all of them
                return len(word1) - i
            if i == len(word1):
                return len(word2) - j
            if (i,j) in dp:
                return dp[(i,j)]
            
            if word1[i] == word2[j]:
                dp[(i,j)] = dfs(i+1,j+1)
                return dp[(i,j)]
            dp[(i,j)] = 1 + min(dfs(i+1,j+1),dfs(i+1,j),dfs(i,j+1))
            return dp[(i,j)]
        return dfs(0,0)
            
print(Solution().minDistance("prosperity","properties"))