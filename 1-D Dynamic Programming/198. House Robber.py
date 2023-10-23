from typing import List
class Solution:
    def rob(self, nums: List[int]) -> int:

        v1,v2 = 0,0

        for i in range(len(nums)):
            temp = max(v1+nums[i],v2)
            v1 = v2
            v2 = temp
        
        return v2
        
