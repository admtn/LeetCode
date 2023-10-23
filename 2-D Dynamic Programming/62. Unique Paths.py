from typing import List
class topDownSolution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [ [None]*n for i in range(m)]

        # dfs returns the num.of ways to reach the goal from (row,col)
        def dfs(row,col):
            if row == m-1 and col == n-1:
                return 1
            if dp[row][col] != None :
                return dp[row][col]
            
            ways = 0
            if row + 1 <= m-1:
                ways += dfs(row+1,col)
            if col + 1 <= n-1:
                ways += dfs(row,col+1)
            dp[row][col] = ways
            return ways
        
        return dfs(0,0)
            

class bottomUpSolution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [ [None]*n for i in range(m)]
        for r in range(m): dp[r][n-1] = 1
        for c in range(n): dp[m-1][c] = 1
        # value at square is v(right) + v(down)
        for row in range(m-2,-1,-1):
            for col in range(n-2,-1,-1):
                dp[row][col] = dp[row+1][col] + dp[row][col+1]
        
        return dp[0][0]


# s = Solution()
# print(s.uniquePaths(3,7))