from typing import List
from collections import defaultdict
class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:

        champs = set([i for i in range(n)])
        for u,v in edges:
            champs.discard(v)
        champs = list(champs)
        return -1 if len(champs) > 1 else champs[0]

print(Solution().findChampion(4,[[0,2],[1,3],[1,2]]))