from typing import List
from collections import defaultdict
class Solution:
    def distinctNames(self, ideas: List[str]) -> int:
        names = defaultdict(set)
        for n in ideas:
            names[n[0]].add(n[1:])
        res = 0
        for c1 in names:
            for c2 in names:
                if c1 == c2:
                    continue
                intersect = self.same(names[c1],names[c2])
                res += (len(names[c1])-intersect)*(len(names[c2])-intersect)
        return res

    def same(self,s1,s2):
        same = 0
        for suffix in s1:
            same += 1 if suffix in s2 else 0
        return same



ideas = ["coffee","donuts","time","toffee"]
print(Solution().distinctNames(ideas))