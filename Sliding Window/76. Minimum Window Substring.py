from typing import List
from collections import Counter
class SolutionONM:
    def minWindow(self, s: str, t: str) -> str:
        # O(nm) soln
        def invalidWindow(dict):
            for c in dict:
                if dict[c] > 0:
                    return True
            return False

        counter = Counter(t)
        l,r,resl,resr = 0,0,0,float("inf")
        solvable = False
        if s[0] in counter: counter[s[0]] -= 1
        while r < len(s):

            if invalidWindow(counter):
                r += 1
                if r < len(s) and s[r] in counter: counter[s[r]] -= 1
            else:
                solvable = True
                if resr - resl + 1 > r-l+1:
                    resl = l
                    resr = r
                if l < len(s) and s[l] in counter: counter[s[l]] += 1
                l += 1

        return s[resl:resr+1] if solvable else ""

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # O(n) soln
        counter = Counter(t)
        have = 0
        l,r,resl,resr = 0,-1,0,float("inf")
        solvable = False
        # if s[0] in counter: counter[s[0]] -= 1
        while r < len(s):
            
            # if invalid window
            if have < len(counter):
                r += 1
                if r < len(s) and s[r] in counter:
                    counter[s[r]] -= 1
                    if counter[s[r]] == 0:
                        have += 1
            else:
                solvable = True
                if resr - resl + 1 > r-l+1:
                    resl = l
                    resr = r
                if s[l] in counter:
                    counter[s[l]] += 1
                    if counter[s[l]] == 1:
                        have -= 1
                l += 1

        return s[resl:resr+1] if solvable else ""
a = Solution()
s = "ADOBECODEBANC"
t = "ABC"
print(a.minWindow(s,t))