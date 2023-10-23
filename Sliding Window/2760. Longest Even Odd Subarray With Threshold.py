from typing import List
class Solution:
    def longestAlternatingSubarray(self, nums: List[int], threshold: int) -> int:
        # first num is even
        # alternate between even and odd
        # all nums less than threshold
        l = 0
        r = 0
        res = 0
        def valid(l,r):
            return nums[r]%2 != nums[r-1]%2 and nums[r] <= threshold if r != l else nums[r] <= threshold
            
        while r < len(nums) and l < len(nums):
            while l < len(nums) and (nums[l]%2 == 1 or nums[l] > threshold):
                l += 1
                r = l
            while r < len(nums) and valid(l,r):
                res = max(res,r-l+1)
                r += 1
            l += 1
        return res