from typing import List
class Solution:
    def maxNonDecreasingLength(self, nums1: List[int], nums2: List[int]) -> int:
        N = len(nums1)
        if N == 1:
            return 1
        dp1,dp2 = [1]*N,[1]*N
        for i in range(1,N):
            if nums1[i] >= nums1[i-1]:
                dp1[i] = dp1[i-1]+1
            if nums1[i] >= nums2[i-1]:
                dp1[i] = max(dp1[i],dp2[i-1]+1)
            if nums2[i] >= nums1[i-1]:
                dp2[i] = dp1[i-1] + 1
            if nums2[i] >= nums2[i-1]:
                dp2[i] = max(dp2[i],dp2[i-1]+1)
        return max(max(dp1),max(dp2))

print(Solution().maxNonDecreasingLength([10,6,13],[19,17,11]))

class dfs:
    def maxNonDecreasingLength(self, nums1: List[int], nums2: List[int]) -> int:
        N = len(nums1)
        if N == 1:
            return 1
        
        # returns max length starting from index i
        def dfs(i):

            # start with number from nums1
            a = max(
                dfs(i+1) + 1 if nums1[i+1] >= nums1[i] else dfs(i+1),
                dfs(i+1) + 1 if nums2[i+1] >= nums1[i] else dfs(i+1)
            )
            # start with number from nums2
            b = max(
                dfs(i+1) + 1 if nums1[i+1] >= nums2[i] else dfs(i+1),
                dfs(i+1) + 1 if nums2[i+1] >= nums2[i] else dfs(i+1)
            )
            return max(a,b)