from typing import List
class Solution:
    def partitionString(self, s: str) -> int:
        # if char already inside set, clear set, res += 1, l = r,
        res = 0
        vis = set()
        for c in s:
            if c in vis:
                res += 1
                vis.clear()
            vis.add(c)
        return res+1

print(Solution().partitionString("abacaba"))