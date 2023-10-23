from typing import List
class rec:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        cache = {}
        res = [0]
        def dfs(i,total):
            if i == len(nums):
                if total == target: 
                    res[0] += 1
                return
            
            # plus
            dfs(i+1,total+nums[i])
            # minus
            dfs(i+1,total-nums[i])

        dfs(0,0)
        return res[0]
class nonCached:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        cache = {}
        # dfs returns the num of ways to reach the target starting from index i
        def dfs(i,curTarget):
            if i == len(nums):
                if curTarget == 0:
                    return 1
                else:
                    return 0 
            # plus 
            return dfs(i+1,curTarget-nums[i]) + dfs(i+1,curTarget+nums[i])
            # minus
            
        return dfs(0,target)

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        cache = {}
        # dfs returns the num of ways to reach the curTarget starting from index i
        def dfs(i,curTarget):
            if i == len(nums):
                return 1 if curTarget == 0 else 0
            
            if (i,curTarget) in cache: return cache[(i,curTarget)]

            cache[(i,curTarget)] = dfs(i+1,curTarget-nums[i]) + dfs(i+1,curTarget+nums[i])
            return cache[(i,curTarget)]
            
        return dfs(0,target)

s = Solution()
print(s.findTargetSumWays([1,2,3],0))