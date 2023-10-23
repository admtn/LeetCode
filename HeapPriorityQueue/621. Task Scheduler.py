from typing import List
from collections import defaultdict,Counter,deque
import heapq
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # each c has its own count and cd
        # among all c's that are not on cd i.e cd false, select the c that has the biggest count among them

        hash = Counter(tasks)
        off_cd = [-hash[i] for i in hash]
        on_cd = deque()
        heapq.heapify(off_cd)
        t = 0
        while off_cd or on_cd:
            if off_cd:
                num = heapq.heappop(off_cd)
                num += 1
                if num:
                    on_cd.append([num,t+n])
            if on_cd and on_cd[0][1] == t:
                heapq.heappush(off_cd,on_cd.popleft()[0])
            t += 1
        return t
            

s = Solution()

print(s.leastInterval(["A","A","A","B","B","B"],2))
        