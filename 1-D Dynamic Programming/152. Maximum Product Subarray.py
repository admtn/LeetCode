
from typing import List
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if len(nums) == 1: return nums[0]
        curMin, curMax = 1,1
        res = float('-inf')
        for num in nums:
            prevMin = curMin
            curMin = min(num,curMax*num,curMin*num)
            curMax = max(num,curMax*num,prevMin*num)
            res = max(res,curMax)
        
        return res


s = Solution()
ans = s.maxProduct([2,4,-4,6,-1,-3,-2,3])
print(ans)