from typing import List
class Solution:
    def countBits(self, n: int) -> List[int]:
        res = [0] * (n+1)
        offset = 1
        for i in range(1,len(res)):
            if i == offset*2:
                offset *= 2
            res[i] = 1 + res[i-offset]
        return res

s = Solution()
print(s.countBits(5))