from typing import List
class dpSolution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = {}
        # returns the max profit given at index i, and whether have stock
        def dfs(i,stock):
            if i == len(prices):
                return 0
            if (i,stock) in dp:
                return dp[(i,stock)]
            if stock:
                res = max(
                    dfs(i+1,False) + prices[i], # sell
                    dfs(i+1,stock) # don't sell
                    ) 
            else:
                res = max(
                    dfs(i+1,True) - prices[i], # buy
                    dfs(i+1,stock) # don't buy
                )
            dp[(i,stock)] = res
            return res
        return dfs(0,False)
class greedySolution:
    def maxProfit(self, prices: List[int]) -> int:
        money = 0
        stock = False
        for i,p in enumerate(prices):
            if i == len(prices)-1:
                money += prices[i] if stock else 0
                break
            if stock and p > prices[i+1]: # i have stock and its price is gonna drop tmr, sell now
                money += prices[i]
                stock = False
            if not stock and p < prices[i+1]: # i have no stock but its price is gonna rise tmr, buy now
                money -= prices[i]
                stock = True
        return money

class neetCode:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        for i in range(len(prices)-1):
            res += prices[i+1] - prices[i] if prices[i+1] > prices[i] else 0
        return res
print(neetCode().maxProfit([1,2,3,4,5]))