class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 1:
            return x
        if n > 0:
            if n%2 == 0:
                return self.myPow(x*x,n//2)
            else:
                n -= 1
                return x * self.myPow(x*x,n//2)
        elif n < 0:
            n = -n
            if n%2 == 0:
                return 1/self.myPow(x*x,n//2)
            else:
                n -= 1
                return 1/(x * self.myPow(x*x,n//2))
        else:
            return 1
        
class Cleaner:
    def myPow(self, x: float, n: int) -> float:
        def helper(x,n):
            if x == 0:
                return 0
            if n == 0:
                return 1
            if n == 1:
                return x
            return helper(x*x,n/2) if n%2 == 0 else x*helper(x*x,(n-1)/2)
        
        return helper(x,n) if n >= 0 else 1/helper(x,-n)