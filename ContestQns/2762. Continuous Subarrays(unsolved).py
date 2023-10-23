from typing import List
class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        
        def valid(l,r):
            for i in range(l,r+1):
                for j in range(i+1,r+1):
                    if abs(nums[i] - nums[j]) > 2:
                        return False
            return True
        res = len(nums)
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if valid(i,j):
                    res += 1
        return res