from typing import List
class topDown:
    def minDistance(self, word1: str, word2: str) -> int:
        # if same char go next
        # if diff
        # insert -> return 1 + (i,j+1)
        # del -> return 1 + (i+1,j)
        # replace -> return 1 + (i+1,j+1)
        cache = {}
        def td(i,j):
            if i == len(word1) and j == len(word2):
                return 0
            if i == len(word1):
                return len(word2)-j
            if j == len(word2):
                return len(word1)-i
            
            if (i,j) in cache:
                return cache[(i,j)]
            
            if word1[i] == word2[j]:
                cache[(i,j)] = td(i+1,j+1)
                return cache[(i,j)]
            
            soln = 1 + min(
                td(i,j+1),
                td(i+1,j),
                td(i+1,j+1)
            )
            cache[(i,j)] = soln
            return soln
        
        return td(0,0)
            
class bottomUp:
    def minDistance(self, word1: str, word2: str) -> int:
        # if same char go next
        # if diff
        # insert -> return 1 + (i,j+1)
        # del -> return 1 + (i+1,j)
        # replace -> return 1 + (i+1,j+1)
        dp = [[None]*(len(word1)+1) for i in range(len(word2)+1)]

        for i in range(len(word1)+1):
            dp[len(word2)][i] = len(word1) - i
        
        for j in range(len(word2)+1):
            dp[j][len(word1)] = len(word2) - j

        for i in range(len(word2)-1,-1,-1):
            for j in range(len(word1)-1,-1,-1):
                if word1[j] == word2[i]:
                    dp[i][j] = dp[i+1][j+1]
                else:
                    dp[i][j] = 1 + min(
                        dp[i+1][j],
                        dp[i][j+1],
                        dp[i+1][j+1]
                    )
        return dp[0][0]
                


s = bottomUp()
print(s.minDistance("horse","ros"))

