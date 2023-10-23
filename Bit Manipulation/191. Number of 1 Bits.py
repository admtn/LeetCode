class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        while n:
            res += n%2
            n = n >> 1
        return res

class sSolution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        while n:
            n = n & (n-1)
            res += 1
        return res

class sSolution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        while n:
            res += n & 1
            n = n >> 1
        return res
s = sSolution()
print(s.hammingWeight(128))