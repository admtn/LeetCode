from typing import List
from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        q = deque()
        l = 0
        r = k-1
        for i in range(k):
            while q and nums[i] > nums[q[-1]]:
                q.pop()
            q.append(i)
        res.append(nums[q[0]])
        l += 1
        r += 1

        while r < len(nums):
            if q and q[0] < l:
                q.popleft()
            while q and nums[r] >= nums[q[-1]]:
                q.pop()
            q.append(r)
            res.append(nums[q[0]])
            r += 1
            l += 1
        return res



class NeetCode:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        q = deque()  # index
        l = r = 0
        # O(n) O(n)
        while r < len(nums):
            while q and nums[r] > nums[q[-1]]:
                q.pop()
            q.append(r)
            
            if l > q[0]:
                q.popleft()
            
            if r >= k-1:
                res.append(nums[q[0]])
                l += 1
            r += 1
        return res
            
s = NeetCode()
nums = [1,3,-1,-3,5,3,6,7,5,1,6,12,51]
k = 3
print(s.maxSlidingWindow(nums,k))