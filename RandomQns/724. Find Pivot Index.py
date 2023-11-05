from typing import List
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        N = len(nums)
        lsum,rsum = [0]*N, [0]*N

        for i in range(1,N):
            lsum[i] = lsum[i-1] + nums[i-1]
        for i in range(N-2,-1,-1):
            rsum[i] = rsum[i+1] + nums[i+1]
        for i in range(N):
            if lsum[i] == rsum[i]:
                return i
        return -1
class SSolution:
    def pivotIndex(self, nums: List[int]) -> int:
        N = len(nums)
        lsum,rsum = 0, sum(nums)
        for i in range(N):
            rsum -= nums[i]
            if lsum == rsum:
                return i
            lsum += nums[i]
        return -1



print(SSolution().pivotIndex([1,7,3,6,5,6]))