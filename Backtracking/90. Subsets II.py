from typing import List
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        subset = []
        def backtrack(i:int):
            if i == len(nums):
                res.append(subset.copy())
                return

            subset.append(nums[i])
            backtrack(i+1)
            subset.pop()

            while i+1 < len(nums) and nums[i+1] == nums[i]:
                i += 1
            
            backtrack(i+1)
            return
        
        backtrack(0)
        return res

s = Solution()
ans = s.subsetsWithDup([1,2,2,3])
ans.sort()
print(ans)

