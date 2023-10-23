from typing import List
from collections import deque
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        S = len(s)
        res = ""
        for r in range(numRows):
            idx = r
            if r == 0 or r == numRows-1:
                while idx < S:
                    res += s[idx]
                    idx += (numRows-1)*2
            else:
                while idx < S:
                    res += s[idx]
                    if idx + (numRows-1)*2-r*2 < S:
                        res += s[idx + (numRows-1)*2-r*2]
                    idx += (numRows-1)*2
        return res
print(Solution().convert("PAYPALISHIRING",4))