class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xFFFFFFFF
        while b:
            # a is sum of 1 and 0, b is carry bits
            a,b = (a^b) & mask, ((a & b) << 1) & mask
            # a,b = (a^b) , ((a & b) << 1)
        return a if a <= 0x7FFFFFFF else ~(a ^ mask)

s = Solution()
print(s.getSum(-1,1))