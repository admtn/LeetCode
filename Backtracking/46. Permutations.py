from typing import List
import copy
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        # base case
        if len(nums) == 1:
            return [copy.deepcopy(nums)]
        for i in range(len(nums)):
            firstElement = nums.pop(0)
            perms = self.permute(nums)
            for permutation in perms:
                permutation.append(firstElement)
            
            res.extend(perms)
            nums.append(firstElement)
        return res
        

nums = [1,2,3]
sol = Solution()
dd = sol.permute(nums)
print(dd)