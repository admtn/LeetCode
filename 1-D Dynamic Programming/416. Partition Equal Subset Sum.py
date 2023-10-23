from typing import List
class dfsSolution:
    def canPartition(self, nums: List[int]) -> bool:
        total = 0
        for num in nums:
            total += num
        
        if total%2 != 0: return False
        half = total/2

        def dfs(i,cursum):
            if i == len(nums): return False
            if cursum == half: return True
            if cursum > half: return False
            if dfs(i+1,cursum + nums[i]):return True
            if dfs(i+1,cursum):return True
            return False
        return dfs(0,0)
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = 0
        nums.insert(0,0)
        for num in nums:
            total += num
        
        if total%2 != 0: return False
        half = total//2

        dp = [[0]*(half+1) for i in range(len(nums))]
        for i in range(1,len(nums)):
            for c in range(half+1):
                if c >= nums[i]:
                    dp[i][c] = max(dp[i-1][c],dp[i-1][c-nums[i]]+nums[i])
                else:
                    dp[i][c] = dp[i-1][c]
        
        if dp[len(nums)-1][half] == half:return True
        else: return False
class neetCodeSolution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total%2: return False # if odd
        target = total//2

        res = set()
        res.add(0)
        for num in nums:
            newRes = res.copy() # make a copy of the target set
            for results in res:
                if results + num == target:
                    return True
                newRes.add(results+num)
            res = newRes
        return False


s = neetCodeSolution()
print(s.canPartition([1,5,11,5]))


