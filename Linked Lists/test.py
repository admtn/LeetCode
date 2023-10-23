from typing import List
class Solution:
    def maximumJumps(self, nums: List[int], target: int) -> int:
        
        cache = {}
        # dfs gives the max num of jumps from i to reach n-1
        def dfs(i):
            if i == len(nums)-1:
                return 0
            if i in cache:
                return cache[i]

            res = float('-inf')
            for n in range(i+1,len(nums)):
                if abs(nums[n] - nums[i]) <= target:
                    res = max(res,1+dfs(n))
            cache[i] = res
            return cache[i]
        sol = dfs(0)
        return sol if sol != float('-inf') else -1

s = Solution()
print(s.maximumJumps([1,3,6,4,1,2],0))