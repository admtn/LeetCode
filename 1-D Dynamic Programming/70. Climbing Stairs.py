from typing import List
class Solution:
    def climbStairs(self, n: int) -> int:
        
        if n == 1 or n == 0: return 1
        var1,var2 = 1 , 1
        for i in range(2,n+1):
            temp = var1 + var2
            var1 = var2
            var2 = temp
        
        return temp




    
s = Solution()
for i in range(1,11):
    print(f"{i} : {s.climbStairs(i)}")

