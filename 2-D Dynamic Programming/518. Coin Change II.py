from typing import List
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        
        dp = [[0]*(amount+1) for i in range(len(coins))]

        # initialise first column (amt 0)
        for i in range(len(coins)):
            dp[i][0] = 1

        # initialise first row (first coin)
        for amt in range(amount+1):
            if amt >= coins[0]:
                dp[0][amt] = dp[0][amt-coins[0]]
            
        for row in range(1,len(coins)):
            for amt in range(amount+1):
                if amt >= coins[row]:
                    dp[row][amt] = dp[row][amt-coins[row]] + dp[row-1][amt]
                else:
                    dp[row][amt] = dp[row-1][amt]
        
        return dp[len(coins)-1][amount]

class TopDown: # literally same as combination sum
    def change(self, amount: int, coins: List[int]) -> int:
        
        # dfs returns the number of combinations to reach the amount given 
        # the coins starting from i
        cache = {}
        def dfs(i,sum):
            if i == len(coins):
                return 0
            if sum == amount:
                return 1
            if sum > amount:
                return 0
            
            if (i,sum) not in cache:
                cache[(i,sum)] = dfs(i,sum+coins[i]) + dfs(i+1,sum)
            
            return cache[(i,sum)]
        
        return dfs(0,0)


