from math import fmod
class sSolution:
    def reverse(self, x: int) -> int:
        x = str(x)
        if x[0] == '-':
            res = int('-'+x[-1:-len(x):-1])
        else:
            res = int(x[::-1])
        
        return res if res in range(-1*(2**31),2**31) else 0

class Solution:
    def reverse(self, x: int) -> int:
        MIN = -2147483648  # -2^31,
        MAX = 2147483647  #  2^31 - 1
        
        res = 0
        while x:
            if (
                res > MAX//10 or
                res < int(MIN/10) or
                (res == MAX//10 and fmod(x,10) > fmod(MAX,10)) or
                (res == int(MIN/10) and fmod(x,10) < fmod(MIN,10) )
                ):
                return 0

            res = res*10 + int(fmod(x,10))
            x = int(x/10)
        return res
        

s = Solution() 
print(s.reverse(-123))