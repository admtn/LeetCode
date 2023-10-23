from typing import List
class RecursiveSolution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        # lcs finds the lcs given of 2 strings (via starting indexes to end)
        # if not same max(lcs(i+1,j),lcs(i,j+1))
        # if same then it is 1 + lcs(i+1,j+1)
        
        def lcs(i,j):
            if i == len(text1) or j == len(text2):
                return 0
            if text1[i] == text2[j]:
                return lcs(i+1,j+1) + 1
            else:
                return max(lcs(i+1,j),lcs(i,j+1))
        
        return lcs(0,0)
    
class TopDown:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        # lcs finds the lcs given of 2 strings (via starting indexes to end)
        # if not same max(lcs(i+1,j),lcs(i,j+1))
        # if same then it is 1 + lcs(i+1,j+1)
        cache = {}
        def lcs(i,j):
            if i == len(text1) or j == len(text2):
                return 0
            if text1[i] == text2[j]:
                if (i+1,j+1) not in cache: cache[(i+1,j+1)] = lcs(i+1,j+1)
                return cache[(i+1,j+1)] + 1
            else:
                if (i+1,j) not in cache: cache[(i+1,j)] = lcs(i+1,j)
                if (i,j+1) not in cache: cache[(i,j+1)] = lcs(i,j+1)
                return max(cache[(i+1,j)],cache[(i,j+1)])
        
        return lcs(0,0)
class BottomUp:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [ [0]*(len(text1)+1) for i in range(len(text2)+1)]
        for row in range(len(text2)-1,-1,-1):
            for col in range(len(text1)-1,-1,-1):
                if text1[col] == text2[row]:
                    dp[row][col] = 1 + dp[row+1][col+1]
                else:
                    dp[row][col] = max(dp[row+1][col],dp[row][col+1])
        return dp[0][0]

s = BottomUp()
print(s.longestCommonSubsequence("pmjghexybyrgzczy","hafcdqbgncrcbihkd"))