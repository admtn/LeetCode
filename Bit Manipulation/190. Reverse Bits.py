class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        for i in range(31,-1,-1):
            if n&1:
                n = n >> 1
                res += 2**i
            else:
                n = n >> 1
        return bin(n)

s = Solution()
print(s.reverseBits(0b0001))