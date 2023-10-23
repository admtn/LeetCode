from typing import List,Counter
import heapq
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand)%groupSize != 0:
            return False
        
        count = Counter(hand)
        minH = list(count.keys())
        heapq.heapify(minH)
        while len(minH):
            cur = minH[0]
            for i in range(groupSize):
                if cur not in count or count[cur] <= 0:
                    return False
                
                count[cur] -= 1
                if count[cur] == 0:
                    if minH[0] != cur:
                        return False
                    heapq.heappop(minH)

                cur += 1
        return True
s = Solution()
print(s.isNStraightHand([1,2,3,6,2,3,4,7,8],3))