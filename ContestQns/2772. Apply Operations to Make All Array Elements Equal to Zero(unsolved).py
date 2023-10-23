from typing import List
class Solution:
    def checkArray(self, nums: List[int], k: int) -> bool:
        
        for i in range(len(nums)-k+1):
            res = float('inf')
            for j in range(i,i+k):
                res = min(res,nums[j])
            for j in range(i,i+k):
                nums[j] -= res
                if nums[j] == 0 and j > 0 and nums[j-1] > 0:
                    return False

        return sum(nums) == 0