from typing import List
class wrongCache:
    # this caching doesnt work because im caching the profit, not the revenue. This is a problem because the cache
    # doesn't know the price which I bought the stocks, so if I buy at 0 then dfs to have stock(true), not on cooldown(false) and 
    # i == 2, it will return 4 which is wrong , because 4 was cached when I bought at 1 and sold at 5. But this time I bought at 0 and sold at 
    # 5 which should give me 5, not 4.
    def maxProfit(self, prices: List[int]) -> int:
        
        cache = {}
        # dfs returns the max profit i can gain given the index, presence of stock, and whether i sold ytd
        def dfs(i,stock,bank,soldYtd):

            if i == len(prices):
                return bank
            # if soldYtd , can only cd
            # if stock is true, cd or sell
            # if stock is false, cd or buy
            if (i,stock,soldYtd) in cache:
                return cache[(i,stock,soldYtd)]

            if soldYtd:
                # cd
                res = dfs(i+1,False,bank,False)
            else:
                # have stock 
                if stock:
                    res = max(
                        # cd
                        dfs(i+1,True,bank,False),
                        # sell
                        dfs(i+1,False,bank+prices[i],True)
                    )
                
                if not stock:
                    res = max(
                        # cd
                        dfs(i+1,False,bank,False),
                        # buy
                        dfs(i+1,True,bank-prices[i],False)
                    )

            cache[(i,stock,soldYtd)] = res
            return res
        
        ans = dfs(0,False,0,False)
        return ans
    

class rightCache:
    # this cache is correct because it 'remembers' the price at which i bought my stock via the -price[i] THEN storing the result into the cahce
    def maxProfit(self, prices: List[int]) -> int:
        
        cache = {}
        # dfs returns the max profit i can gain given the index, presence of stock, and whether i sold ytd
        def dfs(i,stock,soldYtd):

            if i == len(prices):
                return 0
            # if soldYtd , can only cd
            # if stock is true, cd or sell
            # if stock is false, cd or buy
            if (i,stock,soldYtd) in cache:
                return cache[(i,stock,soldYtd)]

            if soldYtd:
                # 
                res = dfs(i+1,False,False)
            else:
                # have stock 
                if stock:
                    res = max(
                        # cd
                        dfs(i+1,True,False),
                        # sell
                        dfs(i+1,False,True)+prices[i]
                    )
                
                if not stock:
                    res = max(
                        # cd
                        dfs(i+1,False,False),
                        # buy
                        dfs(i+1,True,False)-prices[i]
                    )

            cache[(i,stock,soldYtd)] = res
            return res

        ans = dfs(0,False,0)
        return ans
class recursion:
    def maxProfit(self, prices: List[int]) -> int:
        
        cache = {}
        # dfs returns the max profit i can gain given the index, presence of stock, and whether i sold ytd
        def dfs(i,stock,bank,soldYtd):

            if i == len(prices):
                return bank
            # if soldYtd , can only cd
            # if stock is true, cd or sell
            # if stock is false, cd or buy

            if soldYtd:
                return dfs(i+1,False,bank,False)

            # have stock 
            if stock:
                return max(
                    # cd
                    dfs(i+1,True,bank,False),
                    # sell
                    dfs(i+1,False,bank+prices[i],True)
                )
            
            if not stock:
                return max(
                    # cd
                    dfs(i+1,False,bank,False),
                    # buy
                    dfs(i+1,True,bank-prices[i],False)
                )
        
        return dfs(0,False,0,False)
    
s = rightCache()
print(s.maxProfit([0,1,5]))

# r = recursion()
# print(r.maxProfit([0,1,5]))