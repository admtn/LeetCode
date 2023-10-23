from typing import List
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre = [1] * len(nums)
        post = [1] * len(nums)
        for i in range(len(nums)):
            if i == 0: pre[i] = nums[i]
            else: pre[i] = nums[i] * pre[i-1]
        for i in range(len(nums)-1,-1,-1):
            if i == len(nums) - 1 : post[i] = nums[i]
            else: post[i] = nums[i] * post[i+1]
        
        # res = [pre[i-1]*post[i+1] for i in range(len(nums))]
        res = [1] * len(nums)
        for i in range(len(nums)):
            if i == 0: res[i] = post[i+1]
            elif i == len(nums)-1: res[i] = pre[i-1]
            else:res[i] = pre[i-1]*post[i+1]
        return res

s = Solution()
print(s.productExceptSelf([-1,1,0,-3,3]))