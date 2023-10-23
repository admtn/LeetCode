from typing import List
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        N = len(nums)
        for i,n in enumerate(nums):
            if n <= 0:
                nums[i] = N+1
        for i,n in enumerate(nums):
            if abs(n)-1 in range(N) and nums[abs(n)-1] > 0:
                nums[abs(n)-1] = -nums[abs(n)-1]
        
        for i in range(1,N+1):
            if nums[i-1] >= 0: # if does not exist
                return i
        return N+1
    


print(Solution().firstMissingPositive([1]))