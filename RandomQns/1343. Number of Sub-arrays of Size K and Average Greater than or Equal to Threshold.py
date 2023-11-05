from typing import List
class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        if len(arr) < k:
            return 0
        res,curSum = 0, sum(arr[0:k-1])
        l,r = 0,k-1
        while r < len(arr):
            curSum += arr[r]
            if curSum/k >= threshold:
                res += 1
            curSum -= arr[l]
            l += 1
            r += 1
        return res

arr = [2,2,2,2,5,5,5,8]
k = 3
threshold = 4
print(Solution().numOfSubarrays(arr,k,threshold))