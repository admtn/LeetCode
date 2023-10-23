from typing import List
from collections import defaultdict
class usingSort:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums : return 0
        nums.sort()
        cur = 1
        res = 1
        for i in range(len(nums)-1):
            if nums[i] + 1 == nums[i+1]:
                cur += 1
            elif nums[i] == nums[i+1]:
                continue
            else:
                res = max(res,cur)
                cur = 1
        res = max(res,cur)
        return res

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        def getLength(x):
            length = 1
            while x+1 in nums:
                x += 1
                length += 1
            return length
        
        nums = set(nums)
        res = 0
        for n in nums:
            if n-1 not in nums:
                # n is the start of a seq
                res = max(res,getLength(n))
        
        return res
        



        


s = Solution()
print(s.longestConsecutive([1,2,0,1]))