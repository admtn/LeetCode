from typing import List
from math import ceil
class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        reach = [ ceil(dist[i]/speed[i]) for i in range(len(dist))] # t = ? to reach base
        reach.sort(reverse=True)
        cnt,t = 0,0
        while len(reach) > 0:
            if reach[-1] <= t:
                return cnt
            reach.pop()
            cnt += 1
            t += 1
        return cnt