from typing import List
from collections import deque
class dpSolution:
    def checkValidString(self, s: str) -> bool:
        cache = {(len(s),0):True}
        def dfs(i,left):
            if i == len(s):
                return left == 0
            if (i,left) in cache:
                return cache[(i,left)]
            if left < 0:
                return False
            
            if s[i] == '(':
                cache[(i,left)] = dfs(i+1,left+1)
            elif s[i] == ')':
                cache[(i,left)] = dfs(i+1,left-1)
            else:
                cache[(i,left)] = dfs(i+1,left-1) or dfs(i+1,left+1) or dfs(i+1,left)
            
            return cache[(i,left)]
        
        return dfs(0,0)

class Solution:
    def checkValidString(self, s: str) -> bool:
        leftMin = 0 # take )
        leftMax = 0 # take (
        i = 0
        for c in s:
            if c == "(":
                leftMin += 1
                leftMax += 1
            elif c == ")":
                leftMin -= 1
                leftMax -= 1
                if leftMax < 0:
                    return False
                if leftMin < 0: # reset because if we don't, we would be using INVALID leftMin values, which might lead to negative True. if leftmin negative, we wrongly assumed ).
                    leftMin = 0
            else:
                leftMin -= 1
                leftMax += 1
                if leftMin < 0: # reset because if we don't, we would be using INVALID leftMin values, which might lead to negative True. if leftmin negative, we wrongly assumed ).
                    leftMin = 0
        return leftMin <= 0 <= leftMax

s = Solution()
print(s.checkValidString("*)("))

