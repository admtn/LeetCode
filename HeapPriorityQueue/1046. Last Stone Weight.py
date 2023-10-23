from typing import List
import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [ -s for s in stones ]
        heapq.heapify(stones)

        while len(stones) > 1:
            heavy1 = heapq.heappop(stones)
            heavy2 = heapq.heappop(stones)
            newStone = -abs(heavy1-heavy2)
            if newStone != 0 :
                heapq.heappush(stones,newStone)
        
        return -stones[0] if len(stones) else 0

s = Solution()
print(s.lastStoneWeight([2,2]))
