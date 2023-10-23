from typing import List
from math import ceil
class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        cache = {}
        # dfs returns the max alice can get given that both alice and bob are playing optimally
        def dfs(l,r):
            if l > r:
                return 0
            if (l,r) in cache:
                return cache[(l,r)]
            As_turn = (r-l+1)%2 == 0
            if As_turn:
                cache[(l,r)] = max( piles[l] + dfs(l+1,r),
                                    piles[r] + dfs(l,r-1))
            else:
                cache[(l,r)] = min( dfs(l+1,r),dfs(l,r-1))
            return cache[(l,r)]
        return dfs(0,len(piles)-1) >= ceil(sum(piles)/2)
    
class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        return True
    # because alice can always decide to take all even index or all odd index
    # since sum(piles) is ODD, alice can choose to take which ever sum is higher : sum(even) or sum(odd)
    # imagine 0 1 2 3 4 5
    #         e o e o e o   e = even, o = odd
    # if alice wants to take all even, she takes idx 0, bob is forced to take idx 1 or 5 (both odd), then alice can choose even again.
    # similarly if she wants all odd, she can take idx 5, bob is forced to take idx 0 or 4 (both even), then alice can choose odd again. 
