class Solution:
    def isHappy(self, n: int) -> bool:

        vis = set()
        while True:
            res = 0
            while n:
                res += (n%10)**2
                n //= 10
            if res == 1:
                return True
            if res in vis:
                return False
            vis.add(res)
            n = res