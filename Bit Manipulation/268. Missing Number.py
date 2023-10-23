from typing import List
class sSolution:
    def missingNumber(self,nums: List[int]) -> int:
        n = len(nums)
        res = 0
        for num in nums:
            res = res ^ num
        
        for i in range(n+1):
            res = res ^ i
        
        return res

class Solution:
    def missingNumber(self,nums: List[int]) -> int:
        n = len(nums)
        res = n
        for i in range(n):
            res += (i-nums[i])
        return res

s= Solution()
print(s.missingNumber([9,6,4,2,3,5,7,0,1]))
