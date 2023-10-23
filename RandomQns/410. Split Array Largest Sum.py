from typing import List
class Ssolution:
    def splitArray(self, nums: List[int], k: int) -> int:
        L = len(nums)
        dp = {}
        # dfs returns the max subarray starting from index i (inclusive) segmented into m partitions
        def dfs(i,m):
            if m == 1:
                return sum(nums[i:])
            if (i,m) in dp:
                return dp[(i,m)]
            res = float('inf')
            curSum = 0
            for j in range(i+1,L-m+2):
                curSum += nums[j-1]
                res = min(res, max(dfs(j,m-1), sum(nums[i:j])) )
                if curSum > res:
                    break
            dp[(i,m)] = res
            return res 
        return dfs(0,k)
class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        
        def canSplit(val):
            cnt, curSum = 0,0
            for n in nums:
                curSum += n
                if curSum > val:
                    curSum = n
                    cnt += 1
                    if cnt + 1 > m:
                        return False
            return True

        l,r = max(nums),sum(nums) # res lies in the range between l and r inclusive
        res = r
        while l <= r:
            mid = l + (r-l)//2
            if canSplit(mid):
                res = mid
                r = mid - 1
            else:
                l = mid + 1
        return res
        


        

print(Solution().splitArray([1,2,3,4,5],2))