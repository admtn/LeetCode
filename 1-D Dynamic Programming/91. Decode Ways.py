from typing import List
class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        dpList = [int(s[i]) for i in range(n)]
        dpSoln = [0] * n
        dpSoln.extend([1,1])
        dpList.extend([99,99])
        for i in range(n-1,-1,-1):
            if dpList[i] == 0: # 0
                dpSoln[i] = 0
            elif dpList[i] in range(3,10): # 3 to 9
                dpSoln[i] = dpSoln[i+1]
            else: # 1 or 2
                dpSoln[i] += dpSoln[i+1]
                
                if( dpList[i] == 1 and dpList[i+1] in range(10) ) or (dpList[i] == 2 and dpList[i+1] in range(7)):
                    dpSoln[i] += dpSoln[i+2]
        
        return dpSoln[0]
    
s = Solution()
ans = s.numDecodings("1224151") 
print(ans)


