from typing import List
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1: return nums[0]
        if len(nums) == 2: return max(nums[0],nums[1])
        newarr = nums.copy()
        newarr.pop(0)
        n = len(newarr)
        ndp = [0] * (n)
        ndp[0] , ndp[1] = newarr[0], max(newarr[0],newarr[1])
        for i in range(2,n):
            ndp[i] = max(ndp[i-1],ndp[i-2]+newarr[i])
        
        ndp.insert(0,0)

        ogdp = [0] * len(nums)
        ogdp[0] = nums[0]
        ogdp[1] = max(nums[0],nums[1])
        for i in range(2,len(nums)):
            ogdp[i] = max(ogdp[i-1],ogdp[i-2]+nums[i])

        res = [0] * len(nums)
        # initialise 0 1 and 2 index
        res[0],res[1] = nums[0],max(nums[0],nums[1])
        for i in range(2,len(nums)):
            res[i] = max(ogdp[i-1],nums[i]+ndp[i-2])
        
        return res[len(nums)-1]

s = Solution()
ans = s.rob([2,3,2])
print(ans)